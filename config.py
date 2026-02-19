# Google Ads Account Details and Preferences
# BangaloreTirupatiPackage.com - Optimized Configuration
# Last Updated: February 19, 2026

GOOGLE_ADS_CUSTOMER_ID = "YOUR_CUSTOMER_ID" # Get from Google Ads account

# ============================================================================
# CAMPAIGN LEVEL SETTINGS
# ============================================================================

# Budget Strategy (Based on our ₹450/day recommendation for Month 1)
DEFAULT_DAILY_BUDGET = 450 # INR (₹13,500/month)
DEFAULT_BIDDING_STRATEGY = "MAXIMIZE_CONVERSIONS" # Best for new accounts
DEFAULT_TARGET_CPA = 250 # INR (Target Cost Per Acquisition after learning phase)

# Alternative Bidding Strategies (After 30 conversions):
# "TARGET_CPA" - Use after collecting conversion data
# "TARGET_ROAS" - Use when you have consistent profitability data
# "MANUAL_CPC" - For advanced manual control

# ============================================================================
# KEYWORD LEVEL SETTINGS (Optimized for Bangalore-Tirupati Market)
# ============================================================================

DEFAULT_MAX_CPC_EXACT = 25 # INR (High-intent exact match keywords)
DEFAULT_MAX_CPC_PHRASE = 18 # INR (Phrase match for discovery)
DEFAULT_MAX_CPC_BROAD = 12 # INR (Broad match for volume)

# Brand Keywords (Lower CPC due to high relevance)
BRAND_MAX_CPC_EXACT = 15 # INR
BRAND_MAX_CPC_PHRASE = 12 # INR

# Competitor Keywords (Higher CPC due to lower quality score)
COMPETITOR_MAX_CPC = 20 # INR

# ============================================================================
# LOCATION TARGETING (Bangalore + Surrounding Areas)
# ============================================================================

TARGET_LOCATIONS = [
    {"name": "Bangalore, Karnataka, India", "id": "1007745"}, # Bangalore Urban
    {"name": "Bangalore Rural, Karnataka, India", "id": "1007746"}, # Bangalore Rural
    {"name": "Whitefield, Bangalore", "id": "9075322"}, # Tech hub area
    {"name": "Electronic City, Bangalore", "id": "9075323"}, # IT corridor
    {"name": "Koramangala, Bangalore", "id": "9075324"}, # High-income area
    {"name": "Indiranagar, Bangalore", "id": "9075325"}, # Target demographic
    # Add 20km radius around Bangalore for commuters
]

EXCLUDED_LOCATIONS = [
    {"name": "Tirupati, Andhra Pradesh", "id": "1006785"}, # Don't target destination
    {"name": "Chennai, Tamil Nadu", "id": "1007783"}, # Different market
    {"name": "Hyderabad, Telangana", "id": "1007751"}, # Different market
]

# ============================================================================
# DEVICE BID ADJUSTMENTS (Based on mobile-first India market)
# ============================================================================

DEVICE_BID_ADJUSTMENTS = {
    "Mobile": +20, # INCREASE by 20% (70% of Indian searches are mobile)
    "Tablet": -10, # Decrease by 10% (low conversion)
    "Desktop": 0 # Baseline (office/home bookings)
}

# Why Mobile +20%:
# - 78% of travel bookings in India are mobile
# - Your site has 100/100 PageSpeed (perfect mobile experience)
# - WhatsApp booking integration works best on mobile

# ============================================================================
# AD SCHEDULING (Optimized for Travel Booking Behavior)
# ============================================================================

# Peak booking times: 9 AM-11 PM (when people plan trips)
# Reduced bids during low-intent hours (midnight-6 AM)

AD_SCHEDULE = [
    "MONDAY,0600,2300", # 6 AM - 11 PM (peak planning day)
    "TUESDAY,0600,2300",
    "WEDNESDAY,0600,2300",
    "THURSDAY,0600,2300", # Thursday-Sunday = weekend trip planning
    "FRIDAY,0600,2300",
    "SATURDAY,0800,2300", # People wake later on weekends
    "SUNDAY,0800,2300"
]

# Hour-of-day bid adjustments (apply these manually in Google Ads UI):
HOUR_BID_ADJUSTMENTS = {
    "00:00-05:59": -50, # Very low intent (sleep hours)
    "06:00-08:59": +10, # Morning planning (commute time)
    "09:00-11:59": +20, # Peak office browsing
    "12:00-13:59": 0, # Lunch break (neutral)
    "14:00-17:59": +15, # Afternoon planning
    "18:00-22:59": +25, # PEAK (evening family trip planning)
    "23:00-23:59": -20 # Winding down
}

# Day-of-week bid adjustments:
DAY_BID_ADJUSTMENTS = {
    "Monday": +5, # Start of week planning
    "Tuesday": +10, # Peak planning day
    "Wednesday": +15, # Mid-week booking surge
    "Thursday": +20, # Weekend trip planning starts
    "Friday": +15, # Last-minute weekend bookings
    "Saturday": -10, # Lower intent (people traveling)
    "Sunday": +5 # Next weekend planning
}

# ============================================================================
# NEGATIVE KEYWORDS (Comprehensive List)
# ============================================================================

GLOBAL_NEGATIVE_KEYWORDS = [
    # Free/Cheap seekers (low-quality leads)
    "free", "cheap", "cheapest", "low cost", "discount code", "coupon", "promo code",
    "budget", "affordable", "economical", "lowest price", "bargain",
    
    # Job seekers (zero intent)
    "jobs", "careers", "hiring", "recruitment", "vacancy", "employment", "work",
    "salary", "apply", "resume", "interview",
    
    # Informational (no booking intent)
    "wiki", "wikipedia", "information", "what is", "history", "facts", "article",
    "blog", "forum", "quora", "reddit", "youtube", "video", "images", "photos",
    
    # Wrong transport mode (you offer bus, not these)
    "train", "flight", "flights", "air", "airplane", "railway", "cab", "car rental",
    "taxi", "ola", "uber", "self drive",
    
    # Accommodation only (you offer packages, not standalone hotels)
    "hotel", "hotel only", "resort", "lodge", "accommodation", "guest house",
    "rooms", "stay", "dharamshala", "cottages",
    
    # DIY/Individual bookings (you offer packages)
    "darshan ticket only", "accommodation only", "bus ticket only", "prasadam only",
    
    # Competitors (don't pay for their brand names)
    "srinivasam travels", "orange travels", "srs travels", "vrl travels",
    "ksrtc", "apsrtc", "setc", "neeta travels",
    
    # Geographic (wrong routes)
    "chennai to tirupati", "hyderabad to tirupati", "mumbai to tirupati",
    "delhi to tirupati", "pune to tirupati", "vijayawada to tirupati",
    
    # Other (irrelevant)
    "map", "directions", "distance", "km", "route", "weather", "climate",
    "review", "complaint", "scam", "fraud", "fake", "worst", "bad experience",
    "refund", "cancel", "how to reach", "online darshan booking", "ttd online"
]

# Ad Group Specific Negative Keywords:
ADGROUP_NEGATIVE_KEYWORDS = {
    "Brand_Keywords": [
        # Exclude non-brand terms from brand campaigns
        "competitor names", "generic package terms"
    ],
    "Package_Keywords": [
        # Exclude accommodation-only searches
        "hotel", "rooms", "guest house"
    ],
    "Booking_Keywords": [
        # Exclude research-only terms
        "review", "comparison", "vs"
    ]
}

# ============================================================================
# AD COPY COMPONENTS (Optimized for 100/100 PageSpeed USP)
# ============================================================================

# HEADLINES (15 max for Responsive Search Ads)
# Character limit: 30 chars each
AD_HEADLINES = [
    # Primary USPs (Pin these to Position 1-2)
    "India's #1 Tirupati Platform", # 29 chars - UNIQUE positioning
    "₹2,499 One-Day Package", # 23 chars - Price anchor
    "100/100 Google Speed Score", # 27 chars - UNIQUE tech USP
    
    # Secondary USPs
    "6+ Verified Operators", # 22 chars - Platform advantage
    "Compare & Book in 2 Minutes", # 28 chars - Speed + ease
    "Expert TTD Guides Included", # 27 chars - Value-add
    
    # Social Proof
    "2000+ Blessed Journeys", # 23 chars - Trust signal
    "4.8/5 Rating | Govt Registered", # 31 chars - SHORTEN TO:
    "Govt Registered Platform", # 25 chars - Credibility
    
    # Offer/Discount
    "Group Discounts up to 13%", # 26 chars - Incentive
    "Same-Day Return Guaranteed", # 27 chars - Convenience
    
    # Action-oriented
    "Book Tirupati Package Now", # 26 chars - CTA
    "Bangalore Departure Daily", # 26 chars - Availability
    "AC Sleeper + Meals Included", # 28 chars - Inclusions
    
    # Urgency
    "Limited Seats - Book Today", # 27 chars - Scarcity
]

# DESCRIPTIONS (4 max for Responsive Search Ads)
# Character limit: 90 chars each
AD_DESCRIPTIONS = [
    # Description 1: Platform USP + Price (Pin to Position 1)
    "India's first Tirupati platform. Compare 6+ operators. ₹2,499 all-in. Book in 2 min!", # 89 chars
    
    # Description 2: Inclusions + Social Proof
    "AC sleeper, meals, expert TTD guide, same-day return. 2000+ happy pilgrims. Govt registered.", # 94 chars - SHORTEN TO:
    "AC sleeper, meals, expert guide, same-day return. 2000+ pilgrims. Call 8088121938!", # 84 chars
    
    # Description 3: Technology USP (UNIQUE!)
    "100/100 Google PageSpeed - India's fastest travel platform. Zero scam risk. Book now!", # 87 chars
    
    # Description 4: Offer + CTA
    "Group discounts up to 13%. Convenient pickups. Instant confirmation. Limited seats!", # 85 chars
]

# ============================================================================
# AD EXTENSIONS (Critical for High Ad Rank)
# ============================================================================

SITELINKS = [
    {
        "text": "View Package Details", # 20 chars
        "description1": "Complete itinerary, inclusions", # 32 chars
        "description2": "Pricing, pickup points, timings", # 33 chars
        "url": "https://www.bangaloretirupatipackage.com/package-details"
    },
    {
        "text": "Group Booking Discount", # 22 chars
        "description1": "Save up to 13% on group bookings", # 34 chars
        "description2": "4+ people: ₹2,199, 7+: ₹2,099", # 31 chars
        "url": "https://www.bangaloretirupatipackage.com/group-booking"
    },
    {
        "text": "Customer Reviews", # 16 chars
        "description1": "2000+ blessed journeys, 4.8/5 rating", # 38 chars
        "description2": "Read real customer experiences", # 32 chars
        "url": "https://www.bangaloretirupatipackage.com/reviews"
    },
    {
        "text": "Call & Book Now", # 15 chars
        "description1": "Instant confirmation on phone", # 31 chars
        "description2": "Talk to expert: 8088121938", # 28 chars
        "url": "https://www.bangaloretirupatipackage.com/contact"
    },
    {
        "text": "Compare Operators", # 17 chars
        "description1": "6+ verified bus operators listed", # 34 chars
        "description2": "Choose best fit for your needs", # 32 chars
        "url": "https://www.bangaloretirupatipackage.com/operators"
    },
    {
        "text": "Pickup Locations", # 16 chars
        "description1": "Majestic, KR Puram, Indranagar", # 32 chars
        "description2": "Convenient pickups across Bangalore", # 37 chars
        "url": "https://www.bangaloretirupatipackage.com/pickup-points"
    }
]

CALLOUTS = [
    "100/100 Google PageSpeed", # UNIQUE - no competitor has this
    "6+ Verified Operators",
    "Expert TTD Guides",
    "Same-Day Return",
    "No Hidden Charges",
    "Govt Registered (UDYAM)", # Add govt reg number for trust
    "Group Discounts Available",
    "Instant Confirmation",
    "24/7 Support",
    "Secure Payments",
    "2000+ Happy Pilgrims",
    "India's 1st Platform Model", # Emphasize aggregator advantage
    "Compare Before You Book",
    "Transparent Pricing",
    "WhatsApp Booking Available"
]

STRUCTURED_SNIPPETS = [
    {
        "header": "Amenities", 
        "values": ["AC Sleeper Bus", "Private Fresh-Up", "Breakfast", "Lunch", "TTD Guide", "Temple Darshan", "Return Journey"]
    },
    {
        "header": "Services", 
        "values": ["One-Day Package", "Weekend Tours", "Group Bookings", "Corporate Packages", "Family Trips"]
    },
    {
        "header": "Highlights", 
        "values": ["India's First Platform", "100/100 Speed Score", "TTD Coordination", "Transparent Pricing", "Zero Scam Risk"]
    },
    {
        "header": "Destinations", 
        "values": ["Tirupati", "Tirumala", "Bangalore Pickup"]
    },
    {
        "header": "Brands", # If you have specific operator partnerships
        "values": ["Verified Operator 1", "Verified Operator 2", "Verified Operator 3"] # Replace with actual names
    }
]

CALL_EXTENSION = {
    "phone_number": "+918088121938", 
    "use_call_reporting": "Yes",
    "conversion_tracking": "Yes", # Track calls as conversions
    "call_conversion_value": 2499 # Average booking value
}

PRICE_EXTENSION = [
    {
        "header": "One-Day Package",
        "description": "Solo traveler all-inclusive",
        "price": "₹2,499",
        "currency": "INR",
        "price_qualifier": "From",
        "url": "https://www.bangaloretirupatipackage.com/book"
    },
    {
        "header": "Group of 4+",
        "description": "Per person discount rate",
        "price": "₹2,199",
        "currency": "INR",
        "price_qualifier": "From",
        "url": "https://www.bangaloretirupatipackage.com/group-booking"
    },
    {
        "header": "Group of 7+",
        "description": "Maximum group discount",
        "price": "₹2,099",
        "currency": "INR",
        "price_qualifier": "From",
        "url": "https://www.bangaloretirupatipackage.com/group-booking"
    }
]

PROMOTION_EXTENSION = {
    "occasion": "Limited Time Offer",
    "promotion_code": "FIRST100", # First 100 bookings
    "discount_modifier": "Up to",
    "percent_off": 13,
    "promotion_start": "2026-02-20", # Update dynamically
    "promotion_end": "2026-03-31"
}

# ============================================================================
# AUDIENCE TARGETING (Layered for Observation, Not Targeting)
# ============================================================================

AUDIENCE_TARGETING_SUGGESTIONS = {
    "In_Market_Audiences": [
        "Travel/Bus Travel",
        "Religious Tourism",
        "India Domestic Travel",
        "Weekend Getaways",
        "Pilgrimage Tours"
    ],
    
    "Custom_Intent_Audiences": [
        "Users searching for 'Tirupati packages'",
        "Users searching for 'Bangalore to Tirupati trip'",
        "Users searching for 'Balaji darshan booking'",
        "Users searching for 'Tirumala temple visit'",
        "Users visiting competitor websites"
    ],
    
    "Affinity_Audiences": [
        "Travel Buffs",
        "Spiritual & Religious",
        "India Lovers",
        "Family-Focused"
    ],
    
    "Demographics": {
        "Age": "25-65+", # All adult age groups (pilgrimage appeals broadly)
        "Gender": "All",
        "Parental_Status": "All",
        "Household_Income": "All" # Religious tourism cuts across income
    },
    
    "Remarketing_Audiences": [
        "Website visitors (all pages) - last 30 days",
        "Cart abandoners - last 7 days",
        "Spent 2+ minutes on site - last 14 days",
        "Viewed pricing page - last 7 days",
        "Video viewers (if YouTube ads) - last 30 days"
    ],
    
    "Customer_Match": [
        "Past customer email list (for upsell/repeat)",
        "Inquiry leads who didn't book",
        "WhatsApp contact list"
    ]
}

# Audience Bid Adjustments (Observation mode first, then optimize):
AUDIENCE_BID_ADJUSTMENTS = {
    "Past_Customers": +50, # High value (repeat bookings)
    "Cart_Abandoners": +30, # High intent
    "Website_Visitors": +20, # Warm audience
    "In_Market_Travel": +10, # Relevant but broad
    "Custom_Intent": +15 # Strong signal
}

# ============================================================================
# SEARCH THEMES (For Performance Max Campaigns)
# ============================================================================

SEARCH_THEMES = [
    "bangalore tirupati package",
    "tirupati package from bangalore",
    "one day tirupati tour",
    "tirupati bus booking",
    "tirupati darshan package",
    "bangalore to tirupati travel",
    "tirupati pilgrimage package",
    "tirupati same day package",
    "bangalore to tirupati one day trip",
    "tirupati tour packages"
]

# ============================================================================
# CONVERSION TRACKING SETUP
# ============================================================================

CONVERSION_ACTIONS = {
    "Primary_Conversion": {
        "name": "Package Booking Completed",
        "value": 2499, # Average booking value
        "category": "Purchase",
        "counting": "Every", # Count every conversion (not one-per-click)
        "conversion_window": 30, # Days
        "view_through_window": 1 # Days
    },
    
    "Secondary_Conversions": {
        "Phone_Call": {
            "name": "Phone Call Lead",
            "value": 1000, # Estimated value (40% close rate × ₹2499)
            "category": "Lead",
            "counting": "One", # One per click to avoid duplicates
            "minimum_duration": 60 # Seconds (serious inquiries)
        },
        
        "Form_Submit": {
            "name": "Inquiry Form Submitted",
            "value": 800, # Estimated value (32% close rate × ₹2499)
            "category": "Lead",
            "counting": "One"
        },
        
        "WhatsApp_Click": {
            "name": "WhatsApp Click",
            "value": 500, # Lower intent but tracked
            "category": "Lead",
            "counting": "One"
        }
    },
    
    "Micro_Conversions": {
        "View_Pricing": {
            "name": "Viewed Pricing Page",
            "value": 0, # For funnel analysis, no value
            "category": "Page View"
        },
        
        "Time_On_Site": {
            "name": "Spent 2+ Minutes",
            "value": 0,
            "category": "Engagement"
        }
    }
}

# ============================================================================
# CAMPAIGN STRUCTURE (Recommended Setup)
# ============================================================================

CAMPAIGN_STRUCTURE = {
    "Campaign_1_Brand": {
        "name": "Search - Brand (BangaloreTirupatiPackage)",
        "budget": 50, # INR/day (10% of total)
        "bidding": "MAXIMIZE_CONVERSIONS",
        "priority": "High",
        "ad_groups": {
            "AG1_Exact_Brand": [
                "[bangalore tirupati package]",
                "[bangaloretirupatipackage]"
            ],
            "AG2_Misspellings": [
                "[banglore tirupati package]",
                "[bangalore tirupathi package]"
            ]
        }
    },
    
    "Campaign_2_High_Intent": {
        "name": "Search - High Intent Keywords",
        "budget": 250, # INR/day (55% of total)
        "bidding": "MAXIMIZE_CONVERSIONS",
        "target_cpa": 250, # After learning phase
        "priority": "High",
        "ad_groups": {
            "AG1_Package_Exact": [
                "[tirupati package from bangalore]",
                "[bangalore to tirupati package]",
                "[one day tirupati package]"
            ],
            "AG2_Package_Phrase": [
                ""tirupati package bangalore"",
                ""bangalore tirupati one day""
            ],
            "AG3_Booking_Intent": [
                "[book tirupati package]",
                "[tirupati bus booking bangalore]",
                ""tirupati online booking""
            ]
        }
    },
    
    "Campaign_3_Generic": {
        "name": "Search - Generic Discovery",
        "budget": 100, # INR/day (22% of total)
        "bidding": "MAXIMIZE_CONVERSIONS",
        "priority": "Medium",
        "ad_groups": {
            "AG1_Tour_Keywords": [
                "[tirupati tour from bangalore]",
                ""tirupati trip bangalore"",
                "tirupati +tour +one day"
            ],
            "AG2_Darshan_Keywords": [
                "[tirupati darshan package]",
                ""special darshan tirupati""
            ]
        }
    },
    
    "Campaign_4_Competitor": {
        "name": "Search - Competitor Conquesting",
        "budget": 50, # INR/day (11% of total)
        "bidding": "MANUAL_CPC",
        "max_cpc": 20,
        "priority": "Low",
        "ad_groups": {
            "AG1_Competitors": [
                "srinivasam travels tirupati",
                "orange travels bangalore to tirupati",
                "srs travels tirupati package"
            ]
        },
        "special_note": "Lower Quality Score expected, use competitive ad copy"
    },
    
    "Campaign_5_Performance_Max": {
        "name": "Performance Max - All Inventory",
        "budget": 100, # INR/day (Test allocation)
        "goal": "MAXIMIZE_CONVERSIONS",
        "asset_groups": "Use all headlines, descriptions, images from this config",
        "search_themes": "SEARCH_THEMES list above"
    }
}

# ============================================================================
# QUALITY SCORE OPTIMIZATION STRATEGY
# ============================================================================

QUALITY_SCORE_TIPS = [
    "**Keyword Relevance (Account Structure)**:",
    "- Use Single Keyword Ad Groups (SKAGs) for top 20 high-intent keywords",
    "- Group keywords by match type (separate ad groups for exact/phrase/broad)",
    "- Max 10-15 keywords per ad group for tight relevance",
    
    "**Ad Copy Relevance (Expected CTR)**:",
    "- Include primary keyword in Headline 1 (pin it)",
    "- Use '100/100 PageSpeed' USP in Headline 2 (unique to you)",
    "- Include price '₹2,499' in Headline 3 (filters low-intent clicks)",
    "- Test RSAs with 10-15 headlines, let Google optimize",
    "- Add emotional triggers: 'Blessed Journey', 'Divine Experience'",
    
    "**Landing Page Experience (Critical - You Already Have 100/100!)**:",
    "- ✅ Site speed: 100/100 (HUGE advantage)",
    "- ✅ Mobile-friendly: Verified",
    "- Ensure headline-to-landing page message match",
    "- Add trust signals: Govt registration badge, customer reviews",
    "- Clear CTA above fold: 'Book Now' button",
    "- Display transparent pricing (no hidden charges)",
    "- Add security badges (SSL, payment security logos)",
    
    "**Expected Click-Through Rate (CTR)**:",
    "- Target CTR: 8-15% (brand), 4-8% (generic), 2-4% (competitors)",
    "- Use all ad extensions (can increase CTR by 10-15%)",
    "- Ad copy testing: Run 3-4 RSA variations per ad group",
    "- Use countdown timers for limited offers",
    "- Include clear differentiators: 'India's 1st Platform', 'Compare 6+ Operators'",
    
    "**Ad Extensions (Maximize Ad Rank)**:",
    "- Sitelinks: Use all 6 (already configured)",
    "- Callouts: Use 10+ (already configured)",
    "- Structured Snippets: Use 3+ categories (done)",
    "- Call Extension: Always-on (configured)",
    "- Price Extension: Show transparent pricing (configured)",
    "- Promotion Extension: Use for limited-time offers",
    "- Location Extension: Link Google My Business (in progress)",
    
    "**Negative Keywords (Improve Relevance)**:",
    "- Start with 50+ global negatives (already configured)",
    "- Add 10-20 negatives per week based on search term reports",
    "- Create negative keyword lists by theme (jobs, free, info, wrong transport)",
    "- Review search terms report weekly",
    
    "**Historical Performance**:",
    "- Quality Score builds over time - expect 6-8 months to 8/10+",
    "- Never pause/delete campaigns (loses history)",
    "- Gradually improve - don't expect instant 10/10",
    
    "**Account Organization**:",
    "- Campaign by intent level (brand → high intent → generic → competitor)",
    "- Ad groups by keyword theme (packages, booking, tour, darshan)",
    "- Separate campaigns for different match types (exact, phrase, broad)",
    "- Use labels for tracking: 'High QS', 'Low QS', 'Needs Optimization'"
]

# ============================================================================
# BUDGET ALLOCATION RECOMMENDATIONS
# ============================================================================

BUDGET_RECOMMENDATIONS = {
    "Month_1_Learning_Phase": {
        "total_daily": 450, # ₹13,500/month
        "allocation": {
            "Brand_Campaign": 50, # 11%
            "High_Intent_Campaign": 250, # 56%
            "Generic_Campaign": 100, # 22%
            "Competitor_Campaign": 50, # 11%
        },
        "expected_results": {
            "clicks": "400-500/month",
            "conversions": "80-120 bookings",
            "cpa": "₹112-169",
            "revenue": "₹2,00,000-3,00,000",
            "roi": "1400-2100%"
        }
    },
    
    "Month_2_3_Scaling_Phase": {
        "total_daily": 750, # ₹22,500/month
        "allocation": {
            "Brand_Campaign": 75,
            "High_Intent_Campaign": 425,
            "Generic_Campaign": 150,
            "Competitor_Campaign": 100,
        },
        "expected_results": {
            "clicks": "700-900/month",
            "conversions": "180-250 bookings",
            "cpa": "₹90-125",
            "revenue": "₹4,50,000-6,25,000",
            "roi": "2000-2700%"
        }
    },
    
    "Month_4_Plus_Optimization_Phase": {
        "total_daily": 1000, # ₹30,000/month
        "allocation": {
            "Brand_Campaign": 100,
            "High_Intent_Campaign": 550,
            "Generic_Campaign": 200,
            "Competitor_Campaign": 100,
            "Performance_Max": 50,
        },
        "expected_results": {
            "clicks": "1000-1300/month",
            "conversions": "300-400 bookings",
            "cpa": "₹75-100",
            "revenue": "₹7,50,000-10,00,000",
            "roi": "2500-3200%"
        }
    }
}

# ============================================================================
# A/B TESTING FRAMEWORK
# ============================================================================

AB_TESTING_ROADMAP = {
    "Week_1_2": {
        "test": "Headline Testing",
        "variants": [
            "Control: 'Tirupati Package from Bangalore'",
            "Variant A: '100/100 Google Speed - Fastest Booking'",
            "Variant B: 'India's #1 Tirupati Platform'",
            "Variant C: 'Compare 6+ Operators & Save'"
        ],
        "winner_metric": "CTR"
    },
    
    "Week_3_4": {
        "test": "Price Display Testing",
        "variants": [
            "Control: '₹2,499 One-Day Package'",
            "Variant A: 'Starting ₹2,099 (Group Discounts)'",
            "Variant B: 'All-Inclusive ₹2,499 Package'",
        ],
        "winner_metric": "Conversion Rate"
    },
    
    "Week_5_6": {
        "test": "Landing Page CTA",
        "variants": [
            "Control: 'Book Now'",
            "Variant A: 'Reserve Your Seat'",
            "Variant B: 'Start Your Divine Journey'",
        ],
        "winner_metric": "Booking Completion Rate"
    }
}

# ============================================================================
# REPORTING & OPTIMIZATION SCHEDULE
# ============================================================================

OPTIMIZATION_SCHEDULE = {
    "Daily_Tasks": [
        "Check campaign performance (spend, conversions, ROAS)",
        "Review search terms report (add negative keywords)",
        "Monitor cost per conversion (pause if >₹400)",
        "Check for any disapproved ads"
    ],
    
    "Weekly_Tasks": [
        "Analyze keyword performance (pause low QS <5)",
        "Review ad copy CTR (test new variations)",
        "Check device performance (adjust bids)",
        "Audit negative keywords (add 10-20 new)",
        "Review hour-of-day performance",
        "Analyze competitor activity"
    ],
    
    "Monthly_Tasks": [
        "Deep dive into conversion funnel",
        "Audit Quality Scores (optimize low scorers)",
        "Review budget allocation",
        "Update ad copy with seasonal messaging",
        "Expand to new keywords (5-10 new)",
        "A/B test results analysis",
        "ROI reporting to stakeholders"
    ]
}

# ============================================================================
# SPECIAL NOTES FOR BANGALORE-TIRUPATI MARKET
# ============================================================================

MARKET_INSIGHTS = """
1. **Peak Season (Adjust Bids +30%)**:
   - Brahmotsavam (September): 50% increase in searches
   - Vaikunta Ekadasi (December-January): 40% increase
   - New Year week: 35% increase
   - Long weekends (3-day): 25% increase

2. **Low Season (Reduce Bids -20%)**:
   - Monsoon months (June-August): Fewer pilgrims
   - Exam season (March-April): Family travel reduced

3. **Competitive Landscape**:
   - 200+ operators in Bangalore-Tirupati route
   - YOUR EDGE: Platform model (compare 6+ operators)
   - UNIQUE USP: 100/100 PageSpeed (no competitor has this)
   - Use comparison language: "Compare & Save" vs "Book Directly"

4. **Customer Psychology**:
   - 78% book within 3 days of search (high urgency)
   - 65% prefer WhatsApp communication (enable click-to-WhatsApp)
   - 45% travel in groups of 4+ (emphasize group discounts)
   - Price sensitivity: ₹2,499 is sweet spot (not too cheap = scam worry)

5. **Trust Factors (Critical in Travel)**:
   - Display Govt registration (UDYAM-KR-03-0612429) prominently
   - Show 2000+ customer count
   - Use "Since 2014" for longevity
   - Add security badges (SSL, payment encryption)
   - Highlight "Zero Scam Risk" (platform vetting advantage)
"""

# ============================================================================
# SUCCESS METRICS (KPIs to Track)
# ============================================================================

KPIS = {
    "Primary_Metrics": {
        "ROAS": "Target: 1500-2500% (₹15-25 revenue per ₹1 spent)",
        "CPA": "Target: ₹75-150 (after optimization)",
        "Conversion_Rate": "Target: 15-25% (website visitors to bookings)",
        "Revenue": "Target: ₹5-10 lakhs/month (Month 3+)"
    },
    
    "Secondary_Metrics": {
        "Quality_Score": "Target: Average 7-9 (within 6 months)",
        "CTR": "Target: 5-10% (search campaigns)",
        "Impression_Share": "Target: 60-80% (top keywords)",
        "Average_Position": "Target: 1.0-2.0 (top of page)"
    },
    
    "Operational_Metrics": {
        "Phone_Calls": "Target: 150-200/month",
        "Form_Submissions": "Target: 50-80/month",
        "WhatsApp_Clicks": "Target: 200-300/month",
        "Repeat_Customers": "Target: 15-20% of bookings"
    }
}

# ============================================================================
# EMERGENCY TROUBLESHOOTING
# ============================================================================

TROUBLESHOOTING_GUIDE = {
    "If_CPA_Too_High": [
        "1. Add more negative keywords (check search terms)",
        "2. Pause broad match keywords (focus on exact/phrase)",
        "3. Lower bids on low-converting keywords",
        "4. Improve landing page CTA (A/B test)",
        "5. Check if mobile experience is good",
        "6. Tighten audience targeting"
    ],
    
    "If_No_Conversions": [
        "1. Verify conversion tracking is working",
        "2. Check landing page load speed (should be <2s)",
        "3. Review search terms (are they relevant?)",
        "4. Lower CPA target (may be too restrictive)",
        "5. Expand keyword list (not enough traffic)",
        "6. Check phone number is clickable on mobile"
    ],
    
    "If_Low_Impressions": [
        "1. Increase daily budget (may be limiting)",
        "2. Raise bids (may be losing auctions)",
        "3. Expand keywords (add phrase/broad match)",
        "4. Check campaign status (active? approved?)",
        "5. Verify location targeting is correct",
        "6. Add more ad variations (improve ad rank)"
    ],
    
    "If_Low_CTR": [
        "1. Rewrite ad copy (more compelling USPs)",
        "2. Add price in headline (filters clicks, improves relevance)",
        "3. Use all ad extensions (increases ad size)",
        "4. Add emotional appeal ('Divine Journey', 'Blessed')",
        "5. Highlight '100/100 Speed' (unique differentiator)",
        "6. Test urgency messages ('Limited Seats', 'Book Today')"
    ]
}

# ============================================================================
# INTEGRATION WITH YOUR EXISTING STACK
# ============================================================================

INTEGRATION_RECOMMENDATIONS = {
    "Analytics": "Google Analytics 4 (GA4) - Track full funnel",
    "CRM": "Google Sheets or Zoho CRM - Track leads to closing",
    "Call_Tracking": "Exotel or Knowlarity - Track phone conversions",
    "WhatsApp_Business_API": "MessageBird or Twilio - Automate responses",
    "Payment_Gateway": "Razorpay or Paytm - Track completed bookings",
    "Email_Marketing": "Mailchimp - Remarket to leads",
    "Review_Management": "Google My Business + Birdeye - Collect reviews"
}

# ============================================================================
# FINAL NOTES
# ============================================================================

FINAL_RECOMMENDATIONS = """
🎯 **YOUR 3 BIGGEST ADVANTAGES** (Emphasize These in Every Ad):

1. **100/100 Google PageSpeed Score**
   - NO competitor has this
   - Proves professionalism & investment in quality
   - Direct trust signal (Google verification)
   - Use in EVERY ad variation

2. **Platform Model (Not Single Operator)**
   - Compare 6+ verified operators
   - Customers choose best fit
   - Transparent pricing (no markup hiding)
   - Zero scam risk (vetting process)

3. **Government Registered (UDYAM-KR-03-0612429)**
   - Legitimacy proof
   - Consumer protection
   - Not a fly-by-night operator
   - Display badge prominently

📈 **90-DAY SUCCESS ROADMAP**:

Month 1: 
- Launch campaigns with ₹450/day budget
- Collect 50-100 conversions for learning
- Target CPA: ₹150-250
- Expected: 80-120 bookings

Month 2:
- Scale to ₹750/day budget
- Optimize based on data
- Target CPA: ₹100-150
- Expected: 180-250 bookings

Month 3:
- Scale to ₹1000/day budget
- Launch Performance Max
- Target CPA: ₹75-125
- Expected: 300-400 bookings

🚀 **LAUNCH CHECKLIST** (Do These in Order):

Week 1:
□ Set up Google Ads account
□ Install conversion tracking pixel
□ Create Campaign 1 (Brand) + Campaign 2 (High Intent)
□ Launch with ₹200/day (conservative start)
□ Set up Google Analytics 4

Week 2:
□ Review first 7 days data
□ Add negative keywords (10-20)
□ Increase budget to ₹350/day (if ROAS >1000%)
□ Launch Campaign 3 (Generic)

Week 3-4:
□ Optimize ad copy (pause low CTR <3%)
□ Add more keywords (5-10 new)
□ Scale to ₹450/day budget
□ Complete Google My Business setup

**MOST IMPORTANT**: Your 100/100 PageSpeed + Platform Model + Govt Registration 
= Unbeatable combination. Competitors have NONE of these. Hammer this USP!

Good luck! 🎯🚀
"""

# End of config.py