
import pandas as pd
import json
import re
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
import config

class GoogleAdsCampaignGenerator:
    """
    Generate and assemble a Google Search campaign (campaigns, ad groups, keywords, ads, negatives, extensions, and guidance) from a parsed website analysis and configuration defaults.
    Parameters:
        - website_analysis_path (str): Path to the website analysis text file used to extract service details, pricing, target audience, locations (expects a "X to Y" pattern for origin/destination), key selling points (KSPs), and core keywords.
    Processing Logic:
        - Uses simple regex parsing to extract structured fields from the provided analysis file; locations_served expects a "origin to destination" format and will fall back to empty strings if parsing fails.
        - Builds a campaign titled "Bangalore to Tirupati Packages", creates themed ad groups, and generates SKAGs only for keywords flagged as high-intent.
        - For each keyword, adds Exact, Phrase, and Broad match entries and uses external config constants for budgets, CPCs, ad assets, extensions, negatives, device adjustments, and schedules.
        - All generation methods mutate self.campaign_data in place, print progress messages, and export non-guidance sections to CSV files under data/<filename_prefix>_<section>.csv.
    """
    def __init__(self, website_analysis_path):
        """Initialize the object with loaded website analysis data and a default campaign data structure.
        Parameters:
            - website_analysis_path (str): Path to the website analysis file or data source used to populate self.website_analysis.
        Returns:
            - None: The constructor initializes instance attributes (self.website_analysis and self.campaign_data) and does not return a value."""
        self.website_analysis = self._load_website_analysis(website_analysis_path)
        self.campaign_data = {
            "campaigns": [],
            "ad_groups": [],
            "keywords": [],
            "ads": [],
            "negative_keywords": [],
            "ad_extensions": []
        }

    def _load_website_analysis(self, path):
        """Load and parse a website analysis text file and return extracted fields.
        Parameters:
            - path (str): Path to the text file containing the website analysis content.
        Returns:
            - dict: A dictionary with extracted values (when present), for example:
                - 'services' (str): Service description.
                - 'pricing' (str): Pricing information.
                - 'target_audience' (str): Target audience description.
                - 'locations_served' (dict): {'origin': str, 'destination': str} parsed from a "X to Y" pattern.
                - 'ksp' (list of str): Key Selling Points extracted from the KSP section.
                - 'core_keywords' (list of str): Core target keywords extracted from the keywords section."""
        with open(path, 'r') as f:
            content = f.read()

        analysis = {}

        # Extracting Business Overview
        services_match = re.search(r'\*\*Service\*\*: (.*)', content)
        if services_match: analysis['services'] = services_match.group(1).strip()

        pricing_match = re.search(r'\*\*Pricing\*\*: (.*)', content)
        if pricing_match: analysis['pricing'] = pricing_match.group(1).strip()

        target_audience_match = re.search(r'\*\*Target Audience\*\*: (.*)', content)
        if target_audience_match: analysis['target_audience'] = target_audience_match.group(1).strip()

        locations_served_match = re.search(r'\*\*Locations Served\*\*: (.*)', content, re.DOTALL)
        if locations_served_match:
            locations_text = locations_served_match.group(1)
            # Assuming format: "Bangalore (Majestic, Indiranagar, KR Puram, Hoskote) to Tirupati."
            parts = locations_text.split(' to ')
            if len(parts) == 2:
                analysis['locations_served'] = {
                    'origin': parts[0].strip(),
                    'destination': parts[1].replace('.', '').strip()
                }
            else:
                analysis['locations_served'] = {
                    'origin': '',
                    'destination': ''
                }

        # Extracting Key Selling Points (KSPs)
        ksp_section = re.search(r'## Key Selling Points \(KSPs\) for Ads\n(.*?)##', content, re.DOTALL)
        if ksp_section:
            ksp_list = re.findall(r'- (.*)', ksp_section.group(1))
            analysis['ksp'] = [k.strip() for k in ksp_list]

        # Extracting Core Keywords
        core_keywords_section = re.search(r'## Target Keywords Categories\n(.*)', content, re.DOTALL)
        if core_keywords_section:
            core_keywords_list = re.findall(r'- (.*)', core_keywords_section.group(1))
            analysis['core_keywords'] = [k.strip() for k in core_keywords_list]

        return analysis

    def generate_campaign_structure(self):
        """Generates and appends a search campaign, themed ad groups, SKAG ad groups, and associated keywords into self.campaign_data using website analysis and config defaults.
        Parameters:
            - self (object): Instance containing 'campaign_data' (dict), 'website_analysis' (dict), and the helper method '_add_keywords_to_ad_group' used to populate campaigns and ad groups.
        Returns:
            - None: Modifies 'self.campaign_data' in place by adding a campaign entry and multiple ad_group entries (general ad groups and single-keyword SKAGs); also prints progress."""
        print("Generating campaign structure...")
        campaign_name = "Bangalore to Tirupati Packages"
        self.campaign_data["campaigns"].append({
            "Campaign": campaign_name,
            "Budget": config.DEFAULT_DAILY_BUDGET,
            "Bidding Strategy": config.DEFAULT_BIDDING_STRATEGY,
            "Geo Targeting": self.website_analysis['locations_served']['origin'].split('(')[0].strip(),
            "Campaign Type": "Search Network Only"
        })

        # Define ad group themes and associated keywords
        ad_group_themes = {
            "One Day Package": [
                "one day tirupati package from bangalore",
                "tirupati one day trip from bangalore",
                "bangalore to tirupati one day tour"
            ],
            "Bus Package": [
                "bangalore to tirupati bus package",
                "tirupati bus travel from bangalore",
                "ac sleeper bus tirupati bangalore"
            ],
            "Car Package": [
                "bangalore to tirupati car package",
                "tirupati car rental from bangalore",
                "private car tirupati bangalore"
            ],
            "Tirupati Darshan": [
                "tirupati darshan package bangalore",
                "tirupati balaji darshan from bangalore",
                "quick tirupati darshan bangalore"
            ],
            "General": [
                "bangalore to tirupati package",
                "tirupati package from bangalore",
                "tirupati tour package from bangalore"
            ]
        }

        high_intent_keywords = [
            "one day tirupati package from bangalore",
            "tirupati darshan package bangalore",
            "bangalore to tirupati bus package",
            "bangalore to tirupati car package"
        ]

        for theme, keywords in ad_group_themes.items():
            # Create a general ad group for the theme
            general_ad_group_name = f"{campaign_name} - {theme}"
            self.campaign_data["ad_groups"].append({
                "Campaign": campaign_name,
                "Ad Group": general_ad_group_name,
                "Status": "Enabled"
            })
            self._add_keywords_to_ad_group(campaign_name, general_ad_group_name, keywords)

            # Create SKAGs for high-intent keywords within this theme
            for keyword in keywords:
                if keyword in high_intent_keywords:
                    skag_ad_group_name = f"{campaign_name} - SKAG - {keyword.replace(' ', '_')}"
                    self.campaign_data["ad_groups"].append({
                        "Campaign": campaign_name,
                        "Ad Group": skag_ad_group_name,
                        "Status": "Enabled"
                    })
                    self._add_keywords_to_ad_group(campaign_name, skag_ad_group_name, [keyword], is_skag=True)

    def _add_keywords_to_ad_group(self, campaign, ad_group, keywords, is_skag=False):
        """Add Exact, Phrase, and Broad match keyword entries to the object's campaign data for a given campaign and ad group.
        Parameters:
            - campaign (str): Name or identifier of the campaign to which keywords will be added.
            - ad_group (str): Name or identifier of the ad group to which keywords will be added.
            - keywords (Iterable[str]): Sequence of keyword strings; each keyword will be added as Exact, Phrase, and Broad match entries.
            - is_skag (bool): Optional flag indicating whether the ad group is a Single Keyword Ad Group (SKAG). Present for future behavior changes; not required for current functionality.
        Returns:
            - None: Mutates self.campaign_data['keywords'] in place by appending dictionaries for each keyword and match type. Each appended dict contains Campaign, Ad Group, Keyword (formatted per match type), Match Type, Max CPC (pulled from config defaults), and Final URL.
        Example:
            - Calling _add_keywords_to_ad_group('Campaign A', 'Ad Group 1', ['tiruapti package']) will append three entries for that keyword (Exact, Phrase, Broad) to self.campaign_data['keywords']."""
        for kw in keywords:
            # Exact Match
            self.campaign_data["keywords"].append({
                "Campaign": campaign,
                "Ad Group": ad_group,
                "Keyword": f"[{kw}]",
                "Match Type": "Exact",
                "Max CPC": config.DEFAULT_MAX_CPC_EXACT, # Using config
                "Final URL": "https://www.bangaloretirupatipackage.com"
            })
            # Phrase Match
            self.campaign_data["keywords"].append({
                "Campaign": campaign,
                "Ad Group": ad_group,
                "Keyword": f'" {kw}" ',
                "Match Type": "Phrase",
                "Max CPC": config.DEFAULT_MAX_CPC_PHRASE, # Using config
                "Final URL": "https://www.bangaloretirupatipackage.com"
            })
            # Broad Match (no BMM as it's deprecated, rely on smart bidding for broad match)
            self.campaign_data["keywords"].append({
                "Campaign": campaign,
                "Ad Group": ad_group,
                "Keyword": kw, # Broad match
                "Match Type": "Broad",
                "Max CPC": config.DEFAULT_MAX_CPC_BROAD, # Using config
                "Final URL": "https://www.bangaloretirupatipackage.com"
            })


    def perform_keyword_research(self):
        print("Performing keyword research...")
        # This method would typically involve calling a keyword research API (e.g., Google Keyword Planner)
        # For this exercise, we'll expand on the core keywords and add some variations.
        # The keywords are already integrated into the ad_group_themes in generate_campaign_structure
        # This method can be used to add more dynamic keyword suggestions if an API is integrated.
        pass

    def generate_ad_copy(self):
        """Generate responsive search ad entries from configured headlines/descriptions and append them to the instance campaign data.
        Parameters:
            - self (object): Instance containing campaign_data (a dict). Expected keys: "ad_groups" (list of dicts, each with an "Ad Group" name) and "ads" (list to which generated ad entries will be appended). This method also reads config.AD_HEADLINES and config.AD_DESCRIPTIONS.
        Returns:
            - NoneType: Updates self.campaign_data["ads"] in place with generated responsive search ad entries and prints progress."""
        print("Generating ad copy...")
        campaign_name = "Bangalore to Tirupati Packages"
        final_url = "https://www.bangaloretirupatipackage.com"

        # Use headlines and descriptions from config.py
        ad_headlines = config.AD_HEADLINES
        ad_descriptions = config.AD_DESCRIPTIONS

        # Generate responsive search ads for each ad group
        for ad_group in self.campaign_data["ad_groups"]:
            ad_group_name = ad_group["Ad Group"]
            ad_entry = {
                "Campaign": campaign_name,
                "Ad Group": ad_group_name,
                "Ad Type": "Responsive Search Ad",
            }
            for i, headline in enumerate(ad_headlines):
                if i < 15: # RSAs can have up to 15 headlines
                    ad_entry[f"Headline {i+1}"] = headline
            for i, description in enumerate(ad_descriptions):
                if i < 4: # RSAs can have up to 4 descriptions
                    ad_entry[f"Description {i+1}"] = description

            ad_entry["Final URL"] = final_url
            ad_entry["Path 1"] = "Tirupati"
            ad_entry["Path 2"] = "Package"
            self.campaign_data["ads"].append(ad_entry)

    def suggest_budget_optimization(self):
        print("Suggesting budget optimization...")
        self.campaign_data["campaigns"][0]["Bidding Strategy"] = config.DEFAULT_BIDDING_STRATEGY
        if config.DEFAULT_BIDDING_STRATEGY == "MAXIMIZE_CONVERSIONS" and config.DEFAULT_TARGET_CPA:
             self.campaign_data["campaigns"][0]["Bidding Strategy"] += f" with a Target CPA ({config.DEFAULT_TARGET_CPA} INR)"
        self.campaign_data["campaigns"][0]["Budget"] = config.DEFAULT_DAILY_BUDGET
        # Further suggestions can be added to a separate report or config file

    def generate_negative_keywords(self):
        """Append a campaign-level negative keyword entry to the instance's campaign_data.
        Parameters:
            - self (object): Instance containing a 'campaign_data' dict and access to configuration (specifically config.GLOBAL_NEGATIVE_KEYWORDS).
        Returns:
            - None: Updates self.campaign_data in-place by adding a dictionary with:
                - "Campaign": the campaign name ("Bangalore to Tirupati Packages"),
                - "Ad Group": empty string (campaign-level negative),
                - "Keyword": a comma-separated string of global negative keywords,
                - "Match Type": "Phrase"."""
        print("Generating negative keyword lists...")
        self.campaign_data["negative_keywords"].append({
            "Campaign": "Bangalore to Tirupati Packages",
            "Ad Group": "", # Campaign level negative
            "Keyword": ", ".join(config.GLOBAL_NEGATIVE_KEYWORDS),
            "Match Type": "Phrase"
        })
        # Add more specific negatives based on ad group themes if needed

    def configure_location_targeting(self):
        print("Configuring location targeting...")
        # Already set at campaign level, but can add more granular options
        # For example, exclude certain areas within Bangalore if not relevant
        pass

    def setup_ad_extensions(self):
        """Set up ad extensions for a specific campaign by appending sitelinks, callouts, structured snippets, and an optional call extension to self.campaign_data["ad_extensions"].
        Parameters:
            - self (object): Instance containing a campaign_data dictionary and access to the config module/constants
        (expects config.SITELINKS, config.CALLOUTS, config.STRUCTURED_SNIPPETS, and optional config.CALL_EXTENSION).
        Returns:
            - None: Modifies self.campaign_data["ad_extensions"] in place; no value is returned."""
        print("Setting up ad extensions...")
        campaign_name = "Bangalore to Tirupati Packages"

        for sitelink in config.SITELINKS:
            self.campaign_data["ad_extensions"].append({
                "Campaign": campaign_name,
                "Extension Type": "Sitelink",
                "Sitelink Text": sitelink["text"],
                "Sitelink URL": sitelink["url"]
            })

        for callout in config.CALLOUTS:
            self.campaign_data["ad_extensions"].append({
                "Campaign": campaign_name,
                "Extension Type": "Callout",
                "Callout Text": callout
            })

        for snippet in config.STRUCTURED_SNIPPETS:
            self.campaign_data["ad_extensions"].append({
                "Campaign": campaign_name,
                "Extension Type": "Structured Snippet",
                "Header": snippet["header"],
                "Values": snippet["values"]
            })

        if config.CALL_EXTENSION:
            self.campaign_data["ad_extensions"].append({
                "Campaign": campaign_name,
                "Extension Type": "Call",
                "Phone Number": config.CALL_EXTENSION["phone_number"],
                "Use Call Reporting": config.CALL_EXTENSION["use_call_reporting"]
            })

        # Location extension would typically be linked to Google My Business, which is outside this tool's scope
        # self.campaign_data["ad_extensions"].append({
        #     "Campaign": campaign_name,
        #     "Extension Type": "Location",
        #     "Location Extension": "Link to Google My Business (if available)"
        # })

    def suggest_audience_targeting(self):
        print("Suggesting audience targeting...")
        self.campaign_data["campaigns"][0]["Audience Targeting"] = config.AUDIENCE_TARGETING_SUGGESTIONS

    def suggest_device_bid_adjustments(self):
        print("Suggesting device bid adjustments...")
        device_adjustments_str = ", ".join([f"{device}: {adjustment}%" for device, adjustment in config.DEVICE_BID_ADJUSTMENTS.items()])
        self.campaign_data["campaigns"][0]["Device Bid Adjustments"] = device_adjustments_str + " (adjust based on actual conversion data)"

    def suggest_ad_scheduling(self):
        print("Suggesting ad scheduling...")
        self.campaign_data["campaigns"][0]["Ad Scheduling"] = "; ".join(config.AD_SCHEDULE) + " (Adjust based on peak booking times and call center hours)"

    def provide_conversion_tracking_guidance(self):
        """Store detailed conversion tracking guidance in the instance's campaign_data.
        Parameters:
            - self (object): The instance containing a campaign_data dictionary that will be updated with conversion tracking guidance.
        Returns:
            - None: Updates self.campaign_data in-place under the key "conversion_tracking_guidance" and prints a short notification message."""
        print("Providing conversion tracking guidance...")
        # This would be a detailed guide in the README or a separate document
        self.campaign_data["conversion_tracking_guidance"] = (
            "1. **Google Ads Conversion Tracking**: Implement Google Ads conversion tags for key actions like 'Book Now' clicks, 'WhatsApp Booking' clicks, and phone calls. This allows direct measurement of ad performance.\n"
            "2. **Google Analytics Integration**: Link your Google Analytics 4 (GA4) property to Google Ads. Import relevant GA4 events (e.g., form submissions, page views of booking confirmation) as conversions into Google Ads.\n"
            "3. **Enhanced Conversions**: Set up enhanced conversions to improve the accuracy of your conversion measurement by securely sending hashed first-party customer data.\n"
            "4. **Auto-tagging**: Ensure auto-tagging is enabled in your Google Ads account. This automatically adds a GCLID (Google Click Identifier) to your landing page URLs, which is crucial for tracking conversions and integrating with Google Analytics.\n"
            "5. **Call Tracking**: If using call extensions or call-only ads, ensure call reporting is enabled to track calls as conversions.\n"
            "6. **Monitor and Optimize**: Regularly review your conversion data in Google Ads to identify trends and optimize your campaigns for better performance."
        )

    def export_to_csv(self, filename_prefix="google_ads_campaign"):
        print(f"Exporting campaign data to CSV files...")
        for key, data_list in self.campaign_data.items():
            if data_list and key != "conversion_tracking_guidance": # Don't export guidance as CSV
                df = pd.DataFrame(data_list)
                df.to_csv(f"data/{filename_prefix}_{key}.csv", index=False)
                print(f"Exported {key} to data/{filename_prefix}_{key}.csv")

    def run_automation(self):
        """Run the full automated workflow to build and export a pay-per-click campaign, executing all generation, suggestion, and export steps.
        Parameters:
            - self (object): Instance of the automation class; used to access campaign settings, store generated artifacts, and manage state during the workflow.
        Returns:
            - None: Performs operations with side effects (creates campaign structure, performs keyword research, generates ad copy and negative keywords, configures targeting and extensions, suggests budgets/bids/schedules, provides tracking guidance, and exports results to CSV) and does not return a value."""
        self.generate_campaign_structure()
        self.perform_keyword_research()
        self.generate_ad_copy()
        self.suggest_budget_optimization()
        self.generate_negative_keywords()
        self.configure_location_targeting()
        self.setup_ad_extensions()
        self.suggest_audience_targeting()
        self.suggest_device_bid_adjustments()
        self.suggest_ad_scheduling()
        self.provide_conversion_tracking_guidance()
        self.export_to_csv()

if __name__ == "__main__":
    generator = GoogleAdsCampaignGenerator(website_analysis_path="../website_analysis.md")
    generator.run_automation()
