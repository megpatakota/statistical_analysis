# Hotels.com Customer Churn Analysis
## Presentation for Leadership Team

**Duration:** 20 minutes  
**Audience:** Senior Executives  
**Date:** [Insert Date]

---

## Slide 1: Title Slide

### Content
- **Title:** Understanding & Reducing Customer Churn at Hotels.com
- **Subtitle:** Data-Driven Insights for Customer Retention Strategy
- **Presenter:** [Name]
- **Date:** [Date]
- **Logo:** Hotels.com

### Speaker Notes
> "Good morning/afternoon. Thank you for the opportunity to present our findings on customer churn analysis. Today, I'll walk you through our data-driven approach to understanding why customers leave and, more importantly, what we can do to retain them. This 20-minute presentation will cover our key findings, the predictive model we've built, and actionable recommendations to reduce our churn rate."

---

## Slide 2: Executive Summary

### Content
**The Challenge:**
- High customer churn rate observed (customers not rebooking within 6 months)
- Need to understand key drivers and predict at-risk customers

**Our Approach:**
- Analysed 689,744 booking records
- Built predictive models to identify churn factors
- Developed customer risk scoring system

**Key Finding:**
- **Customer type, loyalty tier, and cancellation behaviour** are the strongest predictors of churn

### Speaker Notes
> "Let me start with the big picture. We've conducted a comprehensive analysis of nearly 700,000 booking records to understand churn behaviour. Our analysis reveals that the strongest predictors of whether a customer will churn are their customer type—whether they're new or existing—their loyalty tier status, and whether they've previously cancelled a booking. These three factors alone explain a significant portion of churn behaviour, and they form the foundation of our recommendations."

---

## Slide 3: Data Overview

### Content
**Dataset Characteristics:**
| Metric | Value |
|--------|-------|
| Total Bookings | 689,744 |
| Unique Customers | ~XXX,XXX |
| Time Period | Aug 2018 - Jul 2019 |
| Churn Rate | XX.X% |

**Data Sources:**
- Booking transactions
- Customer profiles
- Website engagement metrics
- Marketing attribution

### Speaker Notes
> "Our analysis is based on a robust dataset covering nearly 700,000 bookings over approximately one year. The data includes customer profiles, booking behaviour, website engagement metrics, and marketing channel information. This comprehensive view allows us to understand churn from multiple angles—not just whether someone booked again, but how they engaged with our platform leading up to that decision."

---

## Slide 4: Overall Churn Distribution

### Content
**Visual:** Pie chart showing Churned vs Retained split

**Key Statistics:**
- Retained customers: XX.X%
- Churned customers: XX.X%

**What this means:**
- Significant portion of customers not returning
- Represents substantial revenue at risk
- Opportunity for improvement through targeted retention

### Speaker Notes
> "This chart shows our current churn situation. As you can see, a significant proportion of our customers do not return for another booking within six months. When we translate this into revenue terms, we're talking about substantial lifetime value at risk. However, the good news is that our analysis has identified clear patterns in who churns and why—which means we have an opportunity to intervene proactively."

---

## Slide 5: Key Finding #1 - Customer Type Impact

### Content
**Visual:** Bar chart comparing churn rates
- New Customers: ~XX% churn rate
- Existing Customers: ~XX% churn rate
- Difference: ~XX percentage points

**Insight:** New customers are significantly more likely to churn than existing customers

**Implication:** First booking experience is critical for long-term retention

### Speaker Notes
> "Our first major finding relates to customer type. New customers—those making their first booking with us—have a dramatically higher churn rate compared to existing customers. This tells us that the first booking experience is absolutely critical. If we can successfully convert a new customer to a second booking, they're much more likely to become a loyal, repeat customer. This 'second booking barrier' should be a primary focus of our retention efforts."

---

## Slide 6: Key Finding #2 - Loyalty Tier Effect

### Content
**Visual:** Bar chart showing churn rate by loyalty tier
- Non-members (Tier 0): ~XX% churn
- Base members (Tier 1): ~XX% churn
- Silver/Gold (Tier 2): ~XX% churn

**Insight:** Higher loyalty tiers have progressively lower churn rates

**Implication:** Loyalty programme is effective—need to increase enrolment and progression

### Speaker Notes
> "The second key finding involves our loyalty programme. There's a clear inverse relationship between loyalty tier and churn rate. Non-members have the highest churn, while our Silver and Gold members—our most engaged customers—rarely leave us. This validates that our loyalty programme works. The strategic question becomes: how do we move more customers up the loyalty ladder faster? Every customer we can convert from non-member to Base, or from Base to Silver, represents a significant reduction in churn risk."

---

## Slide 7: Key Finding #3 - Cancellation as a Predictor

### Content
**Visual:** Comparison showing
- Customers who cancelled: ~XX% churn
- Customers who didn't cancel: ~XX% churn

**Insight:** Booking cancellation is a strong early warning signal for churn

**Implication:** Post-cancellation is a critical intervention point

### Speaker Notes
> "Our third finding is perhaps the most actionable in the short term. Customers who cancel a booking are significantly more likely to churn completely. This makes intuitive sense—cancellation often indicates dissatisfaction or a shift in preference to a competitor. The good news is that this gives us a clear trigger for intervention. When a customer cancels, we know they're at elevated risk, and we can proactively reach out with retention offers or to understand their concerns."

---

## Slide 8: Key Finding #4 - Engagement Matters

### Content
**Visual:** Chart showing engagement metrics vs churn

**Low Engagement = Higher Churn:**
- Fewer pages viewed
- Less time on site
- Fewer destinations searched

**High Engagement = Lower Churn:**
- More property pages viewed
- Longer visit duration
- More search activity

### Speaker Notes
> "Beyond these primary factors, we also found that website engagement correlates with retention. Customers who spend more time on our site, view more property pages, and search more destinations are less likely to churn. This suggests that helping customers find the right property—through better UX, personalised recommendations, or guided search—could have retention benefits. It also implies that customers who book quickly without much exploration may not be fully committed to Hotels.com as their go-to platform."

---

## Slide 9: Platform & Channel Insights

### Content
**Platform Analysis:**
- App users show lower churn rates
- Desktop and MWeb similar churn patterns

**Marketing Channel Analysis:**
- Direct traffic: Lower churn
- Paid channels: Variable churn
- Meta/Affiliates: Higher churn

**Implication:** Channel mix affects customer quality and retention

### Speaker Notes
> "We also examined platform and channel effects. Customers who book via our app tend to have lower churn—likely because app installation represents a higher level of commitment. On the channel side, customers who come to us directly have better retention than those acquired through paid or affiliate channels. This doesn't mean we should stop paid acquisition, but it does suggest we should factor retention likelihood into our customer acquisition cost calculations and potentially differentiate our onboarding based on acquisition channel."

---

## Slide 10: Our Predictive Model

### Content
**Model Comparison:**
| Model | ROC-AUC | Accuracy |
|-------|---------|----------|
| Logistic Regression | ~0.70 | ~65% |
| **Random Forest** | **~0.76** | **~70%** |
| Gradient Boosting | ~0.75 | ~69% |

**Selected Model:** Random Forest
- Best balance of performance and interpretability
- Can score customers in real-time
- Identifies high-risk customers for intervention

### Speaker Notes
> "To operationalise these insights, we built a predictive model that can score customers based on their likelihood to churn. We tested three different approaches and found that the Random Forest model performed best, with an ROC-AUC score of approximately 0.76. In practical terms, this means the model can distinguish between customers who will churn and those who won't with reasonable accuracy. More importantly, it can identify high-risk customers before they leave, giving us a window for intervention."

---

## Slide 11: Feature Importance Ranking

### Content
**Visual:** Horizontal bar chart showing top 10 features

**Top Factors (in order of importance):**
1. Customer Type (New vs Existing)
2. Loyalty Tier
3. Cancellation Rate
4. Total Bookings
5. Website Engagement
6. Platform
7. Pay Now Rate
8. Marketing Channel
9. Property Page Ratio
10. Search Behaviour

### Speaker Notes
> "This chart shows the relative importance of each factor in predicting churn, as determined by our model. Customer type and loyalty tier are by far the most important, followed by cancellation behaviour and booking history. These top factors should drive our prioritisation of retention initiatives. Website engagement and platform choice are also meaningful, while factors like star rating preference have less predictive power for churn specifically."

---

## Slide 12: Customer Risk Segmentation

### Content
**Visual:** Customer distribution by risk category

| Risk Category | % of Customers | Actual Churn Rate |
|---------------|----------------|-------------------|
| Low Risk | XX% | ~XX% |
| Medium Risk | XX% | ~XX% |
| High Risk | XX% | ~XX% |
| Critical Risk | XX% | ~XX% |

**Application:** Target High/Critical risk customers for retention campaigns

### Speaker Notes
> "Using our model, we've segmented our entire customer base into four risk categories. As you can see, the model is quite effective—customers in the Critical Risk category have a much higher actual churn rate than those in Low Risk. This segmentation enables us to focus our retention budget where it will have the greatest impact. Rather than treating all customers the same, we can allocate resources proportionally to risk level."

---

## Slide 13: Recommendation #1 - First-Booking Programme

### Content
**Initiative:** First-Booking Experience Programme

**Target:** All new customers

**Actions:**
- Personalised welcome email series
- Incentive for second booking within 30 days (e.g., 10% discount)
- Post-stay feedback collection
- Loyalty programme introduction

**Expected Impact:** HIGH - Addresses #1 churn driver

### Speaker Notes
> "Our first recommendation targets the biggest churn driver: new customer attrition. We propose a comprehensive 'First-Booking Experience Programme' that nurtures new customers through to their second booking. This would include a welcome email series, a time-limited incentive for rebooking, proactive post-stay feedback collection, and clear communication about loyalty programme benefits. The goal is to convert one-time bookers into repeat customers before they even consider going elsewhere."

---

## Slide 14: Recommendation #2 - Loyalty Enhancement

### Content
**Initiative:** Loyalty Programme Enhancement

**Target:** Non-members and Base tier members

**Actions:**
- Prominent loyalty promotion at booking
- Lower barrier to Base tier entry
- Milestone rewards for tier progression
- Exclusive member-only deals

**Expected Impact:** HIGH - Drives customers to protective loyalty tiers

### Speaker Notes
> "Second, we recommend enhancing our loyalty programme strategy. Given how strongly loyalty tier correlates with retention, we should make it easier for customers to join and progress. This could include more prominent promotion of benefits at the booking stage, reducing the threshold to reach Base tier, introducing milestone rewards to celebrate progression, and ensuring members feel the value through exclusive deals. Every customer we move up a tier becomes significantly less likely to churn."

---

## Slide 15: Recommendation #3 - Cancellation Recovery

### Content
**Initiative:** Cancellation Recovery Campaign

**Target:** Customers who cancel bookings

**Actions:**
- Immediate post-cancellation outreach
- Rebooking incentive within 48 hours
- Cancellation reason survey
- Flexible rebooking policies

**Expected Impact:** MEDIUM-HIGH - Prevents imminent churn

### Speaker Notes
> "Third, we should implement a structured cancellation recovery programme. When a customer cancels, we have a narrow window to understand why and potentially recover the booking or relationship. This should include automated outreach within 48 hours offering a rebooking incentive, a brief survey to understand the cancellation reason, and clear communication about our flexible policies. This is a high-intent intervention—these customers were literally about to travel with us."

---

## Slide 16: Recommendation #4 - Engagement Optimisation

### Content
**Initiative:** Engagement-Based Interventions

**Target:** Low-engagement website visitors

**Actions:**
- UX improvements for easier discovery
- Personalised property recommendations
- Re-engagement email campaigns
- Push notifications for searched destinations

**Expected Impact:** MEDIUM - Addresses engagement gap

### Speaker Notes
> "Fourth, we should address the engagement gap. Customers who engage more deeply with our site are more likely to return. We can improve engagement through UX optimisation, better personalised recommendations, and re-engagement campaigns for customers who searched but didn't fully explore. The goal is to help customers find their perfect property and build a stronger connection with our platform."

---

## Slide 17: Recommendation #5 - Predictive Scoring System

### Content
**Initiative:** Real-Time Churn Risk Scoring

**Implementation:**
- Deploy model into CRM/marketing systems
- Automated risk score calculation
- Trigger-based campaigns by risk level
- Monthly model performance monitoring

**Expected Impact:** HIGH - Enables proactive, targeted retention

### Speaker Notes
> "Finally, and perhaps most importantly for long-term value, we recommend deploying our predictive model as a real-time scoring system. This would integrate with our CRM and marketing automation to calculate churn risk for every customer and trigger appropriate interventions automatically. High-risk customers could receive retention offers before they even think about leaving. This transforms our retention approach from reactive to proactive."

---

## Slide 18: Implementation Roadmap

### Content
**Phase 1 (0-3 months):**
- Launch cancellation recovery campaign
- Implement first-booking email series
- Develop risk scoring infrastructure

**Phase 2 (3-6 months):**
- Deploy predictive scoring system
- Roll out loyalty programme enhancements
- A/B test retention incentives

**Phase 3 (6-12 months):**
- Full personalisation based on risk
- Expand to additional channels
- Measure and optimise

### Speaker Notes
> "Here's our proposed timeline. In the first three months, we focus on quick wins—the cancellation recovery campaign and first-booking programme can be implemented relatively quickly with existing tools. In parallel, we build the infrastructure for risk scoring. In months three to six, we deploy the scoring system and roll out loyalty enhancements, testing our approach through A/B experiments. By month twelve, we should have a fully personalised, risk-based retention system operating across all channels."

---

## Slide 19: Expected Business Impact

### Content
**Projected Outcomes (12-month horizon):**

| Metric | Current | Target | Improvement |
|--------|---------|--------|-------------|
| Overall Churn Rate | XX% | XX% | -X pp |
| New Customer Retention | XX% | XX% | +X pp |
| Loyalty Enrolment | XX% | XX% | +X pp |

**Revenue Impact:**
- Estimated incremental revenue from retained customers: $X.XM
- Programme investment: $XXX,XXX
- Expected ROI: X:1

### Speaker Notes
> "What does this mean for the business? Based on our model and industry benchmarks for retention programme effectiveness, we project that these initiatives could reduce our overall churn rate by X percentage points within twelve months. Given our customer lifetime values, this translates to an estimated $X million in incremental revenue from retained customers. Against the investment required for these programmes, we're looking at a compelling ROI of X to 1."

---

## Slide 20: Summary & Call to Action

### Content
**Key Takeaways:**
1. New customers and non-loyalty members are highest risk
2. Cancellation is a critical early warning signal
3. Our predictive model can identify at-risk customers
4. Five targeted initiatives to reduce churn

**Immediate Next Steps:**
1. ✅ Approve Phase 1 initiatives
2. 📊 Allocate budget for implementation
3. 👥 Assign cross-functional project team
4. 📅 Schedule monthly progress reviews

**Questions?**

### Speaker Notes
> "To summarise: we've identified clear drivers of churn—customer newness, lack of loyalty membership, and cancellation behaviour are the key factors. We've built a model that can predict which customers are at risk. And we've developed five targeted initiatives to address these drivers. My ask today is to approve Phase 1 implementation, allocate the necessary budget, assign a cross-functional team to execute, and schedule monthly reviews to track progress. I'm confident that with executive support, we can meaningfully reduce our churn rate and strengthen customer lifetime value. I'm happy to take any questions."

---

## Appendix Slides

### A1: Methodology Details
- Data preprocessing steps
- Feature engineering approach
- Model selection criteria
- Validation methodology

### A2: Detailed Model Performance
- Full classification reports
- ROC curves
- Confusion matrices
- Cross-validation results

### A3: Statistical Significance Tests
- Chi-square test results
- T-test results
- Effect sizes (Cramér's V)

### A4: Data Dictionary
- Complete field descriptions
- Value definitions
- Data quality notes

---

## Backup Q&A Responses

**Q: How confident are we in the model's predictions?**
> "Our model has an ROC-AUC of approximately 0.76, which means it performs significantly better than random chance. In practical terms, if we select a customer the model flags as high-risk and a customer it flags as low-risk, it will correctly identify which one actually churns about 76% of the time. This is strong enough to drive meaningful business value while acknowledging that no model is perfect."

**Q: How often should we retrain the model?**
> "We recommend quarterly retraining to ensure the model stays current with evolving customer behaviour. We should also monitor key metrics monthly—if we see model performance degrading, we can trigger an earlier refresh."

**Q: What's the risk of over-contacting customers with retention offers?**
> "Great question. We need to balance retention efforts with customer experience. Our recommendation is to set frequency caps on retention communications and to use the risk score to prioritise rather than blanket-contact everyone. We should also A/B test to ensure our retention efforts don't have a negative effect."

**Q: How does this interact with our existing marketing campaigns?**
> "The churn model should be integrated with our existing marketing stack. Risk scores can be used to exclude high-risk customers from acquisition-focused campaigns and instead route them to retention workflows. This ensures consistent, appropriate messaging across the customer journey."

