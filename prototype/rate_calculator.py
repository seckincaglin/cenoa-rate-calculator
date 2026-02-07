#!/usr/bin/env python3
"""
AI Freelance Rate Calculator - Prototype
Cenoa Value-Add Product Phase 1

This is a simple prototype to demonstrate the calculation logic.
Production version would include:
- Real-time job posting data from Upwork/Fiverr
- More granular location adjustments
- AI-powered personalized recommendations
"""

# Rate data based on 2025 research
BASE_RATES = {
    # (min, mid, max) in USD/hr
    "software_developer": (50, 80, 160),
    "frontend_developer": (40, 65, 120),
    "backend_developer": (50, 85, 140),
    "fullstack_developer": (55, 95, 160),
    "mobile_developer": (45, 75, 140),
    "ai_ml_engineer": (80, 130, 250),
    "devops_engineer": (55, 85, 150),
    "data_scientist": (60, 100, 180),
    "ui_ux_designer": (35, 55, 90),
    "graphic_designer": (25, 40, 60),
    "web_designer": (30, 50, 80),
    "content_writer": (20, 40, 80),
    "copywriter": (30, 55, 100),
    "video_editor": (25, 45, 80),
    "social_media_manager": (20, 40, 70),
    "virtual_assistant": (15, 25, 45),
    "project_manager": (45, 75, 130),
    "product_manager": (60, 100, 180),
}

# Experience multipliers
EXPERIENCE_MULTIPLIERS = {
    "junior": 0.6,      # 0-2 years
    "mid": 1.0,         # 3-5 years
    "senior": 1.5,      # 6-9 years
    "expert": 2.0,      # 10+ years
}

# Location adjustments (cost of living + market factors)
# Values relative to US baseline (1.0)
LOCATION_ADJUSTMENTS = {
    # North America
    "us": 1.0,
    "canada": 0.9,
    # Western Europe
    "uk": 0.85,
    "germany": 0.8,
    "france": 0.75,
    "switzerland": 1.1,
    # Eastern Europe
    "poland": 0.45,
    "ukraine": 0.35,
    "romania": 0.4,
    # Turkey & Middle East
    "turkey": 0.4,
    "israel": 0.75,
    "uae": 0.7,
    # Asia
    "india": 0.35,
    "philippines": 0.3,
    "vietnam": 0.3,
    "singapore": 0.7,
    "japan": 0.75,
    # Latin America
    "brazil": 0.4,
    "mexico": 0.4,
    "argentina": 0.35,
    "colombia": 0.35,
    # Africa
    "south_africa": 0.35,
    "nigeria": 0.3,
    "kenya": 0.3,
}

# Client location premium (targeting clients in higher-paying markets)
CLIENT_MARKET_PREMIUM = {
    "us": 1.0,
    "uk": 0.9,
    "eu": 0.85,
    "global": 0.7,
    "local": 0.5,
}


def calculate_rate(
    skill: str,
    experience: str,
    location: str,
    client_market: str = "global"
) -> dict:
    """
    Calculate recommended freelance rate.
    
    Args:
        skill: Job category (e.g., "software_developer")
        experience: "junior", "mid", "senior", or "expert"
        location: Freelancer's country
        client_market: Target client market ("us", "uk", "eu", "global", "local")
    
    Returns:
        Dict with rate range, recommendation, and insights
    """
    # Get base rates
    if skill not in BASE_RATES:
        return {"error": f"Unknown skill: {skill}"}
    
    base_min, base_mid, base_max = BASE_RATES[skill]
    
    # Apply experience multiplier
    exp_mult = EXPERIENCE_MULTIPLIERS.get(experience, 1.0)
    
    # Apply location adjustment
    loc_adj = LOCATION_ADJUSTMENTS.get(location, 0.5)
    
    # Apply client market premium
    client_premium = CLIENT_MARKET_PREMIUM.get(client_market, 0.7)
    
    # Calculate adjusted rates
    # Formula: base_rate * experience * max(location, client_premium)
    # The max() reflects that you can charge based on your market OR your client's market
    market_factor = max(loc_adj, client_premium)
    
    rate_min = round(base_min * exp_mult * market_factor)
    rate_mid = round(base_mid * exp_mult * market_factor)
    rate_max = round(base_max * exp_mult * market_factor)
    
    # Calculate local rate (if not targeting international)
    local_rate_mid = round(base_mid * exp_mult * loc_adj)
    
    # Calculate potential uplift from targeting international clients
    if client_market != "local" and loc_adj < client_premium:
        uplift_pct = round((client_premium / loc_adj - 1) * 100)
        international_opportunity = f"Targeting {client_market.upper()} clients could earn you {uplift_pct}% more than local rates"
    else:
        international_opportunity = None
    
    return {
        "skill": skill.replace("_", " ").title(),
        "experience": experience.title(),
        "location": location.upper(),
        "client_market": client_market.upper(),
        "rate_range": {
            "min": rate_min,
            "mid": rate_mid,
            "max": rate_max,
            "currency": "USD",
        },
        "recommendation": f"${rate_mid}/hr",
        "local_comparison": {
            "rate": local_rate_mid,
            "note": f"Local market rate: ${local_rate_mid}/hr",
        } if loc_adj < client_premium else None,
        "international_opportunity": international_opportunity,
        "percentile_note": f"At ${rate_mid}/hr, you'd be competitive with {experience} {skill.replace('_', ' ')}s targeting {client_market} clients",
    }


def compare_to_current(current_rate: float, calculated: dict) -> dict:
    """Compare user's current rate to market rate."""
    market_mid = calculated["rate_range"]["mid"]
    
    if current_rate < market_mid * 0.8:
        diff_pct = round((market_mid / current_rate - 1) * 100)
        status = "undercharging"
        message = f"You're undercharging by ~{diff_pct}%! 🚨"
    elif current_rate > market_mid * 1.2:
        diff_pct = round((current_rate / market_mid - 1) * 100)
        status = "premium"
        message = f"You're charging {diff_pct}% above market - nice if you can get it! 💪"
    else:
        status = "competitive"
        message = "You're pricing competitively with the market ✓"
    
    return {
        "current_rate": current_rate,
        "market_rate": market_mid,
        "status": status,
        "message": message,
        "shareable": f"According to Cenoa, {calculated['experience']} {calculated['skill']}s earn ${calculated['rate_range']['min']}-${calculated['rate_range']['max']}/hr. I'm at ${current_rate}/hr. {message}"
    }


# Example usage
if __name__ == "__main__":
    # Example: Turkish mid-level software developer targeting US clients
    result = calculate_rate(
        skill="software_developer",
        experience="mid",
        location="turkey",
        client_market="us"
    )
    
    print("=== Rate Calculation ===")
    for key, value in result.items():
        if value:
            print(f"{key}: {value}")
    
    print("\n=== Comparison ===")
    comparison = compare_to_current(40, result)
    print(comparison["message"])
    print(f"\nShareable: {comparison['shareable']}")
