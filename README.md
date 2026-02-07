# AI Freelance Rate Calculator
## Cenoa Value-Add Product - Phase 1

*Started: February 6, 2026*

---

## Overview

A free web tool that helps freelancers understand their market value. Viral acquisition engine for Cenoa.

**Core value prop:** "Find out if you're undercharging" → shareable results → leads to Cenoa banking.

## User Flow

```
1. Input Form
   - Skill/profession (dropdown + free text)
   - Years of experience
   - Location (country/city)
   - Project type (hourly, fixed, retainer)
   - Current rate (optional - for comparison)

2. AI Analysis
   - Scrape/analyze Upwork, Fiverr, Toptal job postings
   - Adjust for cost-of-living in user's location
   - Compare to historical rate data
   - Factor in demand trends for the skill

3. Results Page
   - Market rate range (e.g., $50-85/hr)
   - Personalized recommendation
   - Percentile ranking ("You're in the top 30%")
   - "You're undercharging by X%" callout if applicable
   - Shareable card for social media

4. Conversion Points
   - Email capture: "Track your rate over time"
   - CTA: "Get paid faster with Cenoa"
   - Blog content on rate negotiation
```

## Technical Architecture

### Data Sources
- [ ] Upwork job postings (scraping or API)
- [ ] Fiverr gig data
- [ ] Toptal rate ranges (they publish some)
- [ ] LinkedIn salary insights
- [ ] Cost of living indices (Numbeo, etc.)
- [ ] Historical data from Cenoa users (future)

### Backend
- Rate analysis API
- AI prompt engineering for personalized insights
- Data storage for benchmarks
- User tracking (anonymous → authenticated)

### Frontend
- Simple, fast-loading form
- Beautiful shareable result cards
- Mobile-responsive
- Social sharing integration (Twitter, LinkedIn)

## MVP Scope (Week 1-2)

### Must Have
- [ ] Input form with key fields
- [ ] Basic rate calculation logic
- [ ] Results page with market range
- [ ] Shareable image/card generation
- [ ] Email capture

### Nice to Have
- [ ] Real-time Upwork data integration
- [ ] Location-adjusted recommendations
- [ ] Rate history tracking
- [ ] Comparison to similar professionals

## Research Needed

1. **Upwork scraping feasibility** - Can we get job posting data?
2. **Rate data sources** - What public data exists?
3. **Competitor analysis** - Who else does this?
4. **Viral mechanics** - What makes rate content shareable?

## Next Steps

1. Research existing rate calculators/tools
2. Prototype the calculation logic
3. Design the shareable card format
4. Build MVP landing page

---

## Notes

*Space for ongoing notes and decisions*

