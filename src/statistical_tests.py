"""
Statistical Testing module for Hotels.com Churn Analysis
Contains functions for significance testing
"""

import pandas as pd
import numpy as np
from scipy import stats


def perform_ttest(df_processed, numerical_cols):
    """
    Perform t-tests comparing churned vs non-churned customers on numerical variables.
    
    Parameters:
    -----------
    df_processed : pd.DataFrame
        Preprocessed dataframe
    numerical_cols : list
        List of numerical column names
        
    Returns:
    --------
    pd.DataFrame
        Results of t-tests
    """
    print("=" * 60)
    print("STATISTICAL SIGNIFICANCE TESTING (T-TESTS)")
    print("=" * 60)
    print("\nTwo-sample t-tests comparing churned vs non-churned customers:")
    print("-" * 60)
    
    results = []
    for col in numerical_cols:
        churned = df_processed[df_processed['churn_flag'] == 1][col].dropna()
        not_churned = df_processed[df_processed['churn_flag'] == 0][col].dropna()
        
        t_stat, p_value = stats.ttest_ind(churned, not_churned)
        significance = "***" if p_value < 0.001 else "**" if p_value < 0.01 else "*" if p_value < 0.05 else ""
        
        results.append({
            'Feature': col,
            'T-Statistic': round(t_stat, 3),
            'P-Value': f"{p_value:.2e}",
            'Significant': significance
        })
    
    results_df = pd.DataFrame(results)
    print(results_df.to_string(index=False))
    print("\n*** p < 0.001, ** p < 0.01, * p < 0.05")
    
    return results_df


def perform_chi_square_tests(df_processed, categorical_cols):
    """
    Perform chi-square tests for categorical variables against churn.
    
    Parameters:
    -----------
    df_processed : pd.DataFrame
        Preprocessed dataframe
    categorical_cols : list
        List of categorical column names
        
    Returns:
    --------
    pd.DataFrame
        Results of chi-square tests
    """
    print("=" * 60)
    print("CHI-SQUARE TESTS FOR CATEGORICAL VARIABLES")
    print("=" * 60)
    print("\nTesting independence between categorical features and churn:")
    print("-" * 60)
    
    results = []
    for col in categorical_cols:
        contingency_table = pd.crosstab(df_processed[col], df_processed['churn_flag'])
        chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
        
        # Cramér's V for effect size
        n = contingency_table.sum().sum()
        min_dim = min(contingency_table.shape) - 1
        cramers_v = np.sqrt(chi2 / (n * min_dim)) if min_dim > 0 else 0
        
        significance = "***" if p_value < 0.001 else "**" if p_value < 0.01 else "*" if p_value < 0.05 else ""
        effect_size = 'Large' if cramers_v > 0.25 else 'Medium' if cramers_v > 0.1 else 'Small'
        
        results.append({
            'Feature': col,
            'Chi-Square': round(chi2, 2),
            'P-Value': f"{p_value:.2e}",
            "Cramér's V": round(cramers_v, 4),
            'Effect Size': effect_size,
            'Sig': significance
        })
    
    results_df = pd.DataFrame(results)
    print(results_df.to_string(index=False))
    print("\n*** p < 0.001, ** p < 0.01, * p < 0.05")
    print("Cramér's V: Small < 0.1, Medium 0.1-0.25, Large > 0.25")
    
    return results_df


def calculate_mean_comparison(df_processed, numerical_cols):
    """
    Calculate and display mean values comparison between churned and non-churned.
    
    Parameters:
    -----------
    df_processed : pd.DataFrame
        Preprocessed dataframe
    numerical_cols : list
        List of numerical column names
        
    Returns:
    --------
    pd.DataFrame
        Mean comparison dataframe
    """
    print("=" * 60)
    print("MEAN VALUES BY CHURN STATUS")
    print("=" * 60)
    
    mean_by_churn = df_processed.groupby('churn_flag')[numerical_cols].mean()
    mean_comparison = pd.DataFrame({
        'Feature': numerical_cols,
        'Non-Churned (Mean)': mean_by_churn.loc[0].values,
        'Churned (Mean)': mean_by_churn.loc[1].values,
        'Difference': mean_by_churn.loc[1].values - mean_by_churn.loc[0].values,
        'Diff %': ((mean_by_churn.loc[1].values - mean_by_churn.loc[0].values) / mean_by_churn.loc[0].values * 100)
    })
    mean_comparison = mean_comparison.round(2)
    print(mean_comparison.to_string(index=False))
    
    return mean_comparison

