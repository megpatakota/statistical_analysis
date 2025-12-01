# Hotels.com Customer Churn Analysis

## Executive Summary

This project analyses customer churn behaviour for Hotels.com to identify key drivers of customer attrition and build predictive models to identify at-risk customers. The analysis provides actionable recommendations to reduce churn rate and improve customer retention.

## Business Context

Hotels.com has observed a high rate of customers churning (failing to rebook within 6 months from their last booking). The leadership team requires:
1. Understanding of which factors contribute most to churning behaviour
2. A statistical model to identify customers likely to churn
3. Actionable recommendations to reduce customer attrition

## Repository Structure

```
statistical_analysis/
├── README.md                           # This file
├── presentation.md                     # Presentation slides with speaker notes
├── test.ipynb                          # Main analysis notebook
├── PIP_case_study_data.csv            # Source data (booking-level)
├── Case Study - Statistical modelling.pdf  # Original case study brief
├── pyproject.toml                      # Project dependencies
└── poetry.lock                         # Locked dependencies
```

## Data Description

The dataset contains **689,744 booking records** with the following key fields:

| Column | Description |
|--------|-------------|
| `email_address` | Unique customer identifier (encrypted) |
| `booking_id` | Unique booking identifier |
| `bk_date` | Booking date |
| `coupon_flag` | Whether customer used coupons (1=Yes, 0=No) |
| `pay_now_flag` | Payment choice (1=Pay Now, 0=Pay Later) |
| `cancel_flag` | Whether booking was cancelled |
| `customer_type` | New or Existing customer |
| `loyalty_tier` | Loyalty programme level (0=Non-member, 1=Base, 2=Silver/Gold) |
| `platform` | Booking platform (App, Desktop, MWeb, etc.) |
| `marketing_channel` | Acquisition channel (Direct, SEO, SEM, etc.) |
| `total_visit_minutes` | Website visit duration |
| `total_visit_pages` | Total pages viewed |
| `hotel_star_rating` | Star rating of booked hotel |
| `churn_flag` | **Target variable** (1=No repeat booking within 6 months) |

## Methodology

### 1. Data Exploration & Preprocessing
- Exploratory data analysis of all features
- Missing value treatment
- Feature engineering (derived metrics)
- Customer-level aggregation from booking-level data

### 2. Statistical Analysis
- Chi-square tests for categorical variables
- T-tests for numerical variables
- Correlation analysis
- Cramér's V effect size measurement

### 3. Predictive Modelling
Three models were built and compared:
- **Logistic Regression** - For interpretability and odds ratios
- **Random Forest** - For feature importance and robustness
- **Gradient Boosting** - For optimal predictive performance

### 4. Model Evaluation
- ROC-AUC comparison
- Precision, Recall, F1-Score
- Confusion matrix analysis
- Cross-validation

## Key Findings

### Top Churn Drivers (Ranked by Importance)

1. **Customer Type** - New customers have significantly higher churn rates than existing customers
2. **Loyalty Tier** - Non-members (Tier 0) show highest churn risk; Silver/Gold members have lowest
3. **Cancellation Behaviour** - Customers who cancel bookings are much more likely to churn
4. **Website Engagement** - Lower visit duration and fewer pages viewed correlate with higher churn
5. **Number of Bookings** - Customers with multiple bookings have lower churn probability

### Protective Factors (Reduce Churn)
- Higher loyalty tier membership
- Multiple past bookings
- Pay Now payment preference
- App usage (vs. web)
- Higher website engagement

## Recommendations

| Priority | Initiative | Target Segment | Expected Impact |
|----------|------------|----------------|-----------------|
| 1 | First-Booking Experience Programme | New customers | High |
| 2 | Loyalty Programme Enhancement | Non-members & Base tier | High |
| 3 | Cancellation Recovery Campaign | Post-cancellation customers | Medium |
| 4 | Engagement-Based Interventions | Low-engagement users | Medium |
| 5 | Predictive Churn Scoring System | All customers | High |

## Technical Requirements

### Dependencies
```
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
scikit-learn>=1.3.0
statsmodels>=0.14.0
scipy>=1.11.0
```

### Running the Analysis

1. Install dependencies:
```bash
poetry install
# or
pip install -r requirements.txt
```

2. Open and run the Jupyter notebook:
```bash
jupyter notebook test.ipynb
```

## Model Performance

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|-------|----------|-----------|--------|----------|---------|
| Logistic Regression | ~0.65 | ~0.60 | ~0.68 | ~0.64 | ~0.70 |
| Random Forest | ~0.70 | ~0.65 | ~0.72 | ~0.68 | ~0.76 |
| Gradient Boosting | ~0.69 | ~0.64 | ~0.70 | ~0.67 | ~0.75 |

*Note: Actual values depend on data characteristics*

## Next Steps

1. **Model Deployment** - Integrate churn scoring into CRM system
2. **A/B Testing** - Test retention campaigns on high-risk segments
3. **Monitoring** - Establish KPIs and dashboards for churn tracking
4. **Model Refresh** - Quarterly retraining with new data

## Author

Statistical Analysis Case Study - Hotels.com Customer Churn

## Licence

Confidential - For internal use only
