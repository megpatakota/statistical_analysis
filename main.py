"""
Hotels.com Customer Churn Analysis - Main Script
================================================

This script orchestrates the complete churn analysis pipeline:
1. Data loading and preprocessing
2. Exploratory data analysis with visualizations
3. Statistical significance testing
4. Model training and evaluation
5. Customer risk scoring

Run this script to execute the full analysis.

Usage:
    python main.py
"""

import warnings
warnings.filterwarnings('ignore')

# Import configuration and setup
from config import (setup_plot_style, CATEGORICAL_COLS, NUMERICAL_COLS, 
                    BINARY_FLAGS, COLORS, CHURN_COLORS)

# Import custom modules
from data_loader import load_data, preprocess_data, aggregate_to_customer_level, get_data_summary
from visualizations import (plot_churn_distribution, plot_churn_by_category, plot_binary_flags,
                            plot_numerical_distributions, plot_correlation_heatmap,
                            plot_model_comparison, plot_confusion_matrices,
                            plot_feature_importance, plot_risk_segmentation)
from statistical_tests import perform_ttest, perform_chi_square_tests, calculate_mean_comparison
from models import (prepare_features, split_and_scale_data, 
                    train_logistic_regression, train_random_forest, train_gradient_boosting,
                    get_logistic_regression_odds_ratios, score_customers)


def print_header(title):
    """Print a formatted header."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70 + "\n")


def run_analysis():
    """Run the complete churn analysis pipeline."""
    
    # Setup
    print_header("HOTELS.COM CUSTOMER CHURN ANALYSIS")
    print("Setting up plot style and configuration...")
    setup_plot_style()
    print("✓ Configuration loaded\n")
    
    # =========================================================================
    # STEP 1: DATA LOADING AND PREPROCESSING
    # =========================================================================
    print_header("STEP 1: DATA LOADING AND PREPROCESSING")
    
    # Load raw data
    df = load_data()
    
    # Get data summary
    get_data_summary(df)
    
    # Preprocess data
    df_processed = preprocess_data(df)
    
    # =========================================================================
    # STEP 2: EXPLORATORY DATA ANALYSIS
    # =========================================================================
    print_header("STEP 2: EXPLORATORY DATA ANALYSIS")
    
    # 2.1 Churn distribution
    print("\n--- 2.1 Overall Churn Distribution ---")
    plot_churn_distribution(df_processed)
    
    # 2.2 Churn by categorical variables
    print("\n--- 2.2 Churn by Categorical Variables ---")
    
    print("\n📌 Customer Type:")
    plot_churn_by_category(df_processed, 'customer_type', 'Customer Type')
    
    print("\n📌 Loyalty Tier:")
    print("  0 = Not a member, 1 = Base member, 2 = Silver/Gold member")
    plot_churn_by_category(df_processed, 'loyalty_tier', 'Loyalty Tier')
    
    print("\n📌 Platform:")
    plot_churn_by_category(df_processed, 'platform', 'Platform')
    
    print("\n📌 Marketing Channel:")
    plot_churn_by_category(df_processed, 'marketing_channel', 'Marketing Channel', figsize=(12, 6))
    
    # 2.3 Binary flags
    print("\n--- 2.3 Churn by Binary Flags ---")
    plot_binary_flags(df_processed, BINARY_FLAGS)
    
    # 2.4 Numerical distributions
    print("\n--- 2.4 Numerical Feature Analysis ---")
    calculate_mean_comparison(df_processed, NUMERICAL_COLS)
    plot_numerical_distributions(df_processed, NUMERICAL_COLS)
    
    # 2.5 Correlation analysis
    print("\n--- 2.5 Correlation Analysis ---")
    plot_correlation_heatmap(df_processed)
    
    # =========================================================================
    # STEP 3: STATISTICAL SIGNIFICANCE TESTING
    # =========================================================================
    print_header("STEP 3: STATISTICAL SIGNIFICANCE TESTING")
    
    # T-tests for numerical variables
    ttest_results = perform_ttest(df_processed, NUMERICAL_COLS)
    
    # Chi-square tests for categorical variables
    chi_square_cols = ['customer_type', 'loyalty_tier', 'platform', 'marketing_channel',
                       'coupon_flag', 'pay_now_flag', 'cancel_flag']
    chi_square_results = perform_chi_square_tests(df_processed, chi_square_cols)
    
    # =========================================================================
    # STEP 4: CUSTOMER-LEVEL AGGREGATION
    # =========================================================================
    print_header("STEP 4: CUSTOMER-LEVEL AGGREGATION")
    
    customer_df = aggregate_to_customer_level(df_processed)
    
    # =========================================================================
    # STEP 5: MODEL TRAINING AND EVALUATION
    # =========================================================================
    print_header("STEP 5: MODEL TRAINING AND EVALUATION")
    
    # Prepare features
    X, y, feature_cols, model_df_dummies = prepare_features(customer_df)
    
    # Split and scale data
    (X_train, X_test, y_train, y_test, 
     X_train_scaled, X_test_scaled, scaler) = split_and_scale_data(X, y)
    
    # Train models
    print("\n--- Training Models ---\n")
    
    # Logistic Regression
    lr_model, y_pred_lr, y_prob_lr = train_logistic_regression(
        X_train_scaled, y_train, X_test_scaled, y_test
    )
    
    # Get odds ratios
    odds_ratios = get_logistic_regression_odds_ratios(lr_model, feature_cols)
    
    # Random Forest
    rf_model, y_pred_rf, y_prob_rf = train_random_forest(
        X_train, y_train, X_test, y_test
    )
    
    # Feature importance
    print("\n--- Random Forest Feature Importance ---")
    rf_importance = plot_feature_importance(
        feature_cols, rf_model.feature_importances_,
        title='Random Forest: Top 15 Feature Importance'
    )
    
    # Gradient Boosting
    gb_model, y_pred_gb, y_prob_gb = train_gradient_boosting(
        X_train, y_train, X_test, y_test
    )
    
    # =========================================================================
    # STEP 6: MODEL COMPARISON
    # =========================================================================
    print_header("STEP 6: MODEL COMPARISON")
    
    # ROC curves and metrics comparison
    metrics_comparison = plot_model_comparison(
        y_test, y_prob_lr, y_prob_rf, y_prob_gb,
        y_pred_lr, y_pred_rf, y_pred_gb
    )
    
    # Confusion matrices
    print("\n--- Confusion Matrices ---")
    plot_confusion_matrices(y_test, y_pred_lr, y_pred_rf, y_pred_gb)
    
    # =========================================================================
    # STEP 7: CUSTOMER RISK SCORING
    # =========================================================================
    print_header("STEP 7: CUSTOMER RISK SCORING")
    
    # Score customers using Random Forest (best model)
    customer_scores = score_customers(rf_model, X, model_df_dummies)
    plot_risk_segmentation(customer_scores)
    
    # =========================================================================
    # FINAL SUMMARY
    # =========================================================================
    print_header("ANALYSIS COMPLETE")
    
    print(f"""
    ┌─────────────────────────────────────────────────────────────────────┐
    │                        ANALYSIS SUMMARY                              │
    ├─────────────────────────────────────────────────────────────────────┤
    │  Total Bookings Analysed:         {len(df):>10,}                          │
    │  Unique Customers:                {len(customer_df):>10,}                          │
    │  Overall Churn Rate:              {df['churn_flag'].mean()*100:>10.2f}%                        │
    ├─────────────────────────────────────────────────────────────────────┤
    │                        BEST MODEL: RANDOM FOREST                     │
    │  ROC-AUC Score:                   {metrics_comparison.loc[metrics_comparison['Model'] == 'Random Forest', 'ROC-AUC'].values[0]:>10.4f}                        │
    │  Accuracy:                        {metrics_comparison.loc[metrics_comparison['Model'] == 'Random Forest', 'Accuracy'].values[0]:>10.4f}                        │
    ├─────────────────────────────────────────────────────────────────────┤
    │                        KEY DRIVERS OF CHURN                          │
    │  1. Customer Type (New vs Existing)                                  │
    │  2. Loyalty Tier (Non-member vs Member)                              │
    │  3. Cancellation Behaviour                                           │
    │  4. Website Engagement (Visit duration, pages viewed)                │
    │  5. Number of Previous Bookings                                      │
    └─────────────────────────────────────────────────────────────────────┘
    """)
    
    print("✅ All visualizations generated successfully!")
    print("✅ Analysis ready for presentation to leadership team\n")
    
    # Return key objects for further analysis if needed
    return {
        'df': df,
        'df_processed': df_processed,
        'customer_df': customer_df,
        'models': {
            'logistic_regression': lr_model,
            'random_forest': rf_model,
            'gradient_boosting': gb_model
        },
        'metrics': metrics_comparison,
        'customer_scores': customer_scores
    }


if __name__ == "__main__":
    results = run_analysis()

