# Google Ads Campaign Automation Tool for BangaloreTirupatiPackage.com

This tool automates the generation of a comprehensive Google Ads campaign structure tailored for the website [bangaloretirupatipackage.com](https://www.bangaloretirupatipackage.com). It is designed with best practices from PPC experts to create an efficient and effective campaign.

## Features

- **Campaign Structure Generator**: Creates a logical campaign structure with themed ad groups, including Single Keyword Ad Groups (SKAGs) for high-intent keywords.
- **Keyword Research**: Generates relevant keywords for Bangalore to Tirupati travel packages with appropriate match types (Exact, Phrase, Broad).
- **Ad Copy Generator**: Produces multiple variations of responsive search ads (RSAs) incorporating compelling headlines, descriptions, strong calls-to-action (CTAs), unique selling propositions (USPs), and urgency triggers.
- **Budget Optimization Suggestions**: Provides recommendations for daily budgets and smart bidding strategies (e.g., Maximize Conversions with Target CPA).
- **Negative Keyword Lists**: Generates a comprehensive list of negative keywords to prevent irrelevant ad impressions and clicks.
- **Location Targeting Configuration**: Sets up precise location targeting for Bangalore and Tirupati.
- **Ad Extensions Setup**: Configures various ad extensions, including Sitelinks, Callouts, Structured Snippets, and Call Extensions, to enhance ad visibility and provide more information.
- **Audience Targeting Suggestions**: Offers recommendations for in-market and custom intent audiences.
- **Device Bid Adjustments**: Suggests bid adjustments for different devices (mobile, tablet, desktop) based on typical performance.
- **Ad Scheduling Recommendations**: Provides optimal ad scheduling based on potential peak booking times.
- **Conversion Tracking Setup Guidance**: Offers detailed guidance on setting up Google Ads conversion tracking, Google Analytics integration, enhanced conversions, and auto-tagging.
- **CSV Export**: Exports all generated campaign components into CSV files, ready for bulk upload to Google Ads.

## Getting Started

### Prerequisites

- Python 3.x
- `pandas` library (`pip install pandas`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/google_ads_automation.git
   cd google_ads_automation
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Edit the `config.py` file to set your Google Ads account details and preferences:

- `GOOGLE_ADS_CUSTOMER_ID`: Your Google Ads customer ID.
- `DEFAULT_DAILY_BUDGET`: Your desired daily budget for the campaign.
- `DEFAULT_BIDDING_STRATEGY`: Choose your preferred bidding strategy (e.g., `MAXIMIZE_CONVERSIONS`, `TARGET_CPA`).
- `DEFAULT_TARGET_CPA`: Set a target CPA if using the `TARGET_CPA` bidding strategy.
- `DEFAULT_MAX_CPC_EXACT`, `DEFAULT_MAX_CPC_PHRASE`, `DEFAULT_MAX_CPC_BROAD`: Maximum CPC bids for different keyword match types.
- `TARGET_LOCATIONS`, `EXCLUDED_LOCATIONS`: Define your geographical targeting.
- `DEVICE_BID_ADJUSTMENTS`: Adjust bids for mobile, tablet, and desktop devices.
- `AD_SCHEDULE`: Set the days and times for your ads to run.
- `GLOBAL_NEGATIVE_KEYWORDS`: Add any global negative keywords.
- `AD_HEADLINES`, `AD_DESCRIPTIONS`: Customize your ad copy.
- `SITELINKS`, `CALLOUTS`, `STRUCTURED_SNIPPETS`, `CALL_EXTENSION`: Configure your ad extensions.
- `AUDIENCE_TARGETING_SUGGESTIONS`: Review and apply audience targeting suggestions.

### Usage

Run the main script:

```bash
python src/main.py
```

This will generate CSV files in the `data/` directory, which can be used for bulk upload to Google Ads.

## Output Files

The `data/` directory will contain the following CSV files:

- `google_ads_campaign_campaigns.csv`: Campaign-level settings.
- `google_ads_campaign_ad_groups.csv`: Ad group definitions.
- `google_ads_campaign_keywords.csv`: Keywords with match types and bids.
- `google_ads_campaign_ads.csv`: Responsive Search Ads copy.
- `google_ads_campaign_negative_keywords.csv`: Negative keyword lists.
- `google_ads_campaign_ad_extensions.csv`: Ad extension details.

## Quality Score Optimization Tips

Google Ads Quality Score is a diagnostic tool that gives you a holistic view of the quality of your ads. A higher Quality Score can lead to lower costs and better ad positions. Here are key factors and tips for optimization:

- **Keyword Relevance**: Ensure keywords are tightly grouped into themed ad groups. Use SKAGs (Single Keyword Ad Groups) where it makes sense for high-intent keywords to maximize relevance between the keyword, ad copy, and landing page.
- **Ad Copy Relevance**: Create highly relevant ad copy that directly addresses the keywords in each ad group. Include keywords naturally in headlines and descriptions. Highlight unique selling propositions (USPs) and strong calls-to-action (CTAs).
- **Landing Page Experience**: Ensure your landing page ([bangaloretirupatipackage.com](https://www.bangaloretirupatipackage.com)) is fast, mobile-friendly, transparent, and provides a clear call to action relevant to the ad copy and keywords. The content should be easy to navigate and provide the information a user expects after clicking your ad.
- **Expected Click-Through Rate (CTR)**: Write compelling ad copy with strong CTAs and USPs to encourage clicks. Use ad extensions to increase ad visibility and relevance, making your ad stand out and more appealing to users.
- **Ad Extensions**: Implement all relevant ad extensions (sitelinks, callouts, structured snippets, call extensions) to provide more information, increase ad real estate, and improve ad rank. This helps users find what they need quickly and improves the overall ad experience.
- **Negative Keywords**: Continuously refine your negative keyword lists to prevent irrelevant clicks and improve ad group focus. Regularly review search terms reports to identify new negative keyword opportunities.
- **Account Structure**: Maintain a logical and organized campaign and ad group structure for better control and optimization. A well-structured account allows for easier management, reporting, and targeted bidding.

## Conversion Tracking Guidance

Effective conversion tracking is crucial for optimizing your Google Ads campaigns. Follow these steps to ensure accurate measurement:

1.  **Google Ads Conversion Tracking**: Implement Google Ads conversion tags for key actions like \'Book Now\' clicks, \'WhatsApp Booking\' clicks, and phone calls. This allows direct measurement of ad performance.
2.  **Google Analytics Integration**: Link your Google Analytics 4 (GA4) property to Google Ads. Import relevant GA4 events (e.g., form submissions, page views of booking confirmation) as conversions into Google Ads.
3.  **Enhanced Conversions**: Set up enhanced conversions to improve the accuracy of your conversion measurement by securely sending hashed first-party customer data.
4.  **Auto-tagging**: Ensure auto-tagging is enabled in your Google Ads account. This automatically adds a GCLID (Google Click Identifier) to your landing page URLs, which is crucial for tracking conversions and integrating with Google Analytics.
5.  **Call Tracking**: If using call extensions or call-only ads, ensure call reporting is enabled to track calls as conversions.
6.  **Monitor and Optimize**: Regularly review your conversion data in Google Ads to identify trends and optimize your campaigns for better performance.

## License

This project is licensed under the MIT License - see the LICENSE file for details. (Note: A LICENSE file will be added later.)
