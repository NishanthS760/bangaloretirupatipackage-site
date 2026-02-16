
# Google Ads Account Details and Preferences

# This file will hold sensitive information or user-specific preferences.
# It should be excluded from version control in a real-world scenario.

GOOGLE_ADS_CUSTOMER_ID = "YOUR_CUSTOMER_ID" # Example: 123-456-7890

# Campaign Level Settings
DEFAULT_DAILY_BUDGET = 500 # INR
DEFAULT_BIDDING_STRATEGY = "MAXIMIZE_CONVERSIONS" # Other options: TARGET_CPA, MANUAL_CPC
DEFAULT_TARGET_CPA = 500 # INR (only if using TARGET_CPA)

# Keyword Level Settings
DEFAULT_MAX_CPC_EXACT = 20 # INR
DEFAULT_MAX_CPC_PHRASE = 15 # INR
DEFAULT_MAX_CPC_BROAD = 10 # INR

# Location Targeting
TARGET_LOCATIONS = [
    {"name": "Bangalore, Karnataka, India", "id": "20079"}, # Example Location ID
    # Add other specific locations if needed
]
EXCLUDED_LOCATIONS = [
    # Example: {"name": "Some irrelevant city", "id": "12345"}
]

# Device Bid Adjustments (as percentages, e.g., -20 for -20%)
DEVICE_BID_ADJUSTMENTS = {
    "Mobile": -20,
    "Tablet": -10,
    "Desktop": 10
}

# Ad Scheduling (24-hour format, e.g., ["MONDAY,0600,2200", "TUESDAY,0600,2200"])
AD_SCHEDULE = [
    "MONDAY,0600,2200",
    "TUESDAY,0600,2200",
    "WEDNESDAY,0600,2200",
    "THURSDAY,0600,2200",
    "FRIDAY,0600,2200",
    "SATURDAY,0600,2200",
    "SUNDAY,0600,2200"
]

# Negative Keywords (Campaign Level)
GLOBAL_NEGATIVE_KEYWORDS = [
    "free", "cheap", "low cost", "jobs", "careers", "wiki", "wikipedia",
    "train", "flight", "hotel", "resort", "lodge", "accommodation", "rent", "hire",
    "images", "photos", "map", "directions", "reviews", "forum", "blog"
]

# Ad Copy Components (for Responsive Search Ads)
# Provide a good number of diverse headlines and descriptions
AD_HEADLINES = [
    "Tirupati Package from Bangalore",
    "One Day Tirupati Trip ₹2499",
    "50% Faster Darshan Guaranteed",
    "Book Your Tirupati Tour Now",
    "Verified Operators & 24/7 Support",
    "Group Discounts Up To 13% Off",
    "Hassle-Free Pilgrimage",
    "AC Sleeper Bus & Meals Included",
    "Expert TTD Guide Service",
    "Bangalore Pickup & Drop",
    "Divine Journey to Tirupati",
    "Stress-Free Pilgrimage Packages",
    "Best Tirupati Tour Deals",
    "Experience Spiritual Bliss"
]

AD_DESCRIPTIONS = [
    "Experience a seamless Bangalore to Tirupati pilgrimage. All-inclusive package at just ₹2499.",
    "Save 50% time on Darshan with our Expert TTD Guide. Book your one-day trip today!",
    "Enjoy comfortable AC sleeper bus, private fresh-up, and authentic meals. Limited seats available!",
    "Choose from 6+ verified operators. Get scam protection & 24/7 support. Book now!",
    "Group discounts up to 13% available. Call us for custom pricing and a divine journey.",
    "Don\\'t miss out! Secure your spot for a spiritual journey. Limited time offer.",
    "Your complete one-day Tirupati experience. Book with confidence and peace of mind.",
    "Trusted platform for Tirupati packages. Read our 2000+ happy pilgrim reviews."
]

# Ad Extensions
SITELINKS = [
    {"text": "Book Now", "url": "https://www.bangaloretirupatipackage.com/book"},
    {"text": "Group Discounts", "url": "https://www.bangaloretirupatipackage.com/group-discounts"},
    {"text": "Testimonials", "url": "https://www.bangaloretirupatipackage.com/#testimonials"},
    {"text": "Contact Us", "url": "https://www.bangaloretirupatipackage.com/#contact"}
]

CALLOUTS = [
    "50% Faster Darshan",
    "Verified Operators",
    "24/7 Support",
    "All-Inclusive Package",
    "Expert TTD Guide",
    "Scam Protection"
]

STRUCTURED_SNIPPETS = [
    {"header": "Service offerings", "values": "AC Bus, Fresh-up, Meals, Expert Guide"},
    {"header": "Destinations", "values": "Tirupati, Tirumala, Bangalore"}
]

CALL_EXTENSION = {"phone_number": "+918088121938", "use_call_reporting": "Yes"}

# Audience Targeting Suggestions
AUDIENCE_TARGETING_SUGGESTIONS = (
    "In-market: Travel/Bus Travel, Religious Travel, India Travel; "
    "Custom Intent: Users searching for \\'Tirupati packages\\', \\'Bangalore to Tirupati trip\\', \\'Balaji darshan\\'; "
    "Demographics: Age 25-65, Income (Upper 50%)"
)

# Quality Score Optimization Tips (for README)
QUALITY_SCORE_TIPS = [
    "**Keyword Relevance**: Ensure keywords are tightly grouped into themed ad groups. Use SKAGs for high-intent keywords.",
    "**Ad Copy Relevance**: Create highly relevant ad copy that directly addresses the keywords in each ad group. Include keywords in headlines and descriptions.",
    "**Landing Page Experience**: Ensure your landing page (bangaloretirupatipackage.com) is fast, mobile-friendly, transparent, and provides a clear call to action relevant to the ad copy and keywords.",
    "**Expected Click-Through Rate (CTR)**: Write compelling ad copy with strong CTAs and USPs to encourage clicks. Use ad extensions to increase ad visibility and relevance.",
    "**Ad Extensions**: Implement all relevant ad extensions (sitelinks, callouts, structured snippets, call extensions) to provide more information and improve ad rank.",
    "**Negative Keywords**: Continuously refine your negative keyword lists to prevent irrelevant clicks and improve ad group focus.",
    "**Account Structure**: Maintain a logical and organized campaign and ad group structure for better control and optimization."
]
