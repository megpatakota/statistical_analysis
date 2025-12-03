"""
Visualization module for Hotels.com Churn Analysis
Contains all plotting functions using unified colour scheme
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from config import (COLORS, CHURN_COLORS, RISK_COLORS, MODEL_COLORS, 
                    get_custom_cmap, get_confusion_matrix_cmap, NUMERICAL_COLS)


def plot_churn_distribution(df):
    """
    Plot overall churn distribution with pie and bar charts.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Dataframe with churn_flag column
    """
    churn_counts = df['churn_flag'].value_counts()
    churn_rate = df['churn_flag'].mean() * 100
    
    print("=" * 60)
    print("CHURN RATE ANALYSIS")
    print("=" * 60)
    print(f"\n📈 Overall Churn Rate: {churn_rate:.2f}%")
    print(f"   • Retained: {churn_counts[0]:,} ({100-churn_rate:.2f}%)")
    print(f"   • Churned: {churn_counts[1]:,} ({churn_rate:.2f}%)")
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Pie chart
    axes[0].pie(churn_counts.values, labels=['Retained', 'Churned'], autopct='%1.1f%%', 
                colors=CHURN_COLORS, explode=(0, 0.05), shadow=True, startangle=90,
                textprops={'fontsize': 12, 'fontweight': 'bold'})
    axes[0].set_title('Customer Churn Distribution', fontsize=14, fontweight='bold')
    
    # Bar chart
    bars = axes[1].bar(['Retained', 'Churned'], churn_counts.values, color=CHURN_COLORS, 
                       edgecolor='white', linewidth=2)
    axes[1].set_ylabel('Number of Bookings', fontsize=12)
    axes[1].set_title('Churn Count by Category', fontsize=14, fontweight='bold')
    for bar, count in zip(bars, churn_counts.values):
        axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1000, 
                     f'{count:,}', ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    plt.show()


def plot_churn_by_category(data, column, title, figsize=(10, 5)):
    """
    Plot churn rate by categorical variable with count and rate charts.
    
    Parameters:
    -----------
    data : pd.DataFrame
        Dataframe with the categorical column and churn_flag
    column : str
        Name of categorical column
    title : str
        Display title for the column
    figsize : tuple
        Figure size
        
    Returns:
    --------
    pd.DataFrame
        Churn statistics by category
    """
    fig, axes = plt.subplots(1, 2, figsize=figsize)
    
    # Calculate churn rate by category
    churn_by_cat = data.groupby(column)['churn_flag'].agg(['sum', 'count', 'mean']).reset_index()
    churn_by_cat.columns = [column, 'churned', 'total', 'churn_rate']
    churn_by_cat = churn_by_cat.sort_values('churn_rate', ascending=True)
    
    # Left plot: Count by category
    n_cats = len(churn_by_cat)
    colors_count = [plt.cm.GnBu(0.3 + 0.6 * i / n_cats) for i in range(n_cats)]
    axes[0].barh(churn_by_cat[column].astype(str), churn_by_cat['total'], 
                 color=colors_count, edgecolor='white', linewidth=1)
    axes[0].set_xlabel('Number of Bookings', fontsize=12)
    axes[0].set_title(f'Booking Count by {title}', fontsize=14, fontweight='bold')
    
    # Right plot: Churn rate by category
    colors_rate = [COLORS['churned'] if r > data['churn_flag'].mean() else COLORS['retained'] 
                   for r in churn_by_cat['churn_rate']]
    bars = axes[1].barh(churn_by_cat[column].astype(str), churn_by_cat['churn_rate'] * 100, 
                        color=colors_rate, edgecolor='white', linewidth=1)
    axes[1].axvline(x=data['churn_flag'].mean() * 100, color=COLORS['text'], linestyle='--', 
                    linewidth=2, label=f'Avg: {data["churn_flag"].mean()*100:.1f}%')
    axes[1].set_xlabel('Churn Rate (%)', fontsize=12)
    axes[1].set_title(f'Churn Rate by {title}', fontsize=14, fontweight='bold')
    axes[1].legend(loc='lower right')
    
    # Add value labels
    for bar, rate in zip(bars, churn_by_cat['churn_rate']):
        axes[1].text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2, 
                     f'{rate*100:.1f}%', va='center', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    plt.show()
    
    return churn_by_cat


def plot_binary_flags(df_processed, binary_flags):
    """
    Plot churn rate by binary flags (coupon, pay now, cancel).
    
    Parameters:
    -----------
    df_processed : pd.DataFrame
        Preprocessed dataframe
    binary_flags : list
        List of tuples (column_name, display_name)
    """
    print("=" * 60)
    print("CHURN RATE BY BINARY FLAGS")
    print("=" * 60)
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    for idx, (col, title) in enumerate(binary_flags):
        churn_by_flag = df_processed.groupby(col)['churn_flag'].mean() * 100
        bars = axes[idx].bar(['No (0)', 'Yes (1)'], churn_by_flag.values, 
                             color=CHURN_COLORS, edgecolor='white', linewidth=2)
        axes[idx].set_ylabel('Churn Rate (%)', fontsize=12)
        axes[idx].set_title(f'Churn Rate by {title}', fontsize=14, fontweight='bold')
        axes[idx].axhline(y=df_processed['churn_flag'].mean() * 100, color=COLORS['text'], 
                          linestyle='--', linewidth=2, alpha=0.7)
        
        for bar, rate in zip(bars, churn_by_flag.values):
            axes[idx].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                           f'{rate:.1f}%', ha='center', fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    plt.show()
    
    # Print summary
    print("\n📊 Summary Statistics:")
    for col, title in binary_flags:
        churn_by_flag = df_processed.groupby(col)['churn_flag'].mean() * 100
        print(f"\n{title}:")
        print(f"  • Without (0): {churn_by_flag[0]:.2f}% churn")
        print(f"  • With (1): {churn_by_flag[1]:.2f}% churn")
        print(f"  • Difference: {abs(churn_by_flag[1] - churn_by_flag[0]):.2f}pp")


def plot_numerical_distributions(df_processed, numerical_cols=NUMERICAL_COLS):
    """
    Plot box plots and summary chart for numerical variables by churn status.
    
    Parameters:
    -----------
    df_processed : pd.DataFrame
        Preprocessed dataframe
    numerical_cols : list
        List of numerical column names
    """
    # Box plots
    fig, axes = plt.subplots(3, 3, figsize=(18, 14))
    axes = axes.flatten()
    
    for idx, col in enumerate(numerical_cols):
        data_to_plot = [
            df_processed[df_processed['churn_flag'] == 0][col].dropna(),
            df_processed[df_processed['churn_flag'] == 1][col].dropna()
        ]
        
        bp = axes[idx].boxplot(data_to_plot, labels=['Retained', 'Churned'], patch_artist=True,
                               widths=0.6, showfliers=False)
        
        bp['boxes'][0].set_facecolor(COLORS['retained'])
        bp['boxes'][1].set_facecolor(COLORS['churned'])
        bp['boxes'][0].set_alpha(0.7)
        bp['boxes'][1].set_alpha(0.7)
        
        for box in bp['boxes']:
            box.set_edgecolor('white')
            box.set_linewidth(2)
        for median in bp['medians']:
            median.set_color('white')
            median.set_linewidth(2)
        for whisker in bp['whiskers']:
            whisker.set_color(COLORS['text'])
            whisker.set_linewidth(1.5)
        for cap in bp['caps']:
            cap.set_color(COLORS['text'])
            cap.set_linewidth(1.5)
        
        y_min, y_max = axes[idx].get_ylim()
        y_range = y_max - y_min
        
        mean_retained = data_to_plot[0].mean()
        mean_churned = data_to_plot[1].mean()
        
        axes[idx].text(1, y_max - y_range * 0.08, f'μ={mean_retained:.1f}', 
                       ha='center', fontsize=11, fontweight='bold', color=COLORS['retained'],
                       bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8, edgecolor=COLORS['retained']))
        axes[idx].text(2, y_max - y_range * 0.03, f'μ={mean_churned:.1f}', 
                       ha='center', fontsize=11, fontweight='bold', color=COLORS['churned'],
                       bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8, edgecolor=COLORS['churned']))
        
        axes[idx].set_ylabel(col.replace('_', ' ').title(), fontsize=13)
        axes[idx].set_xlabel('Customer Status', fontsize=13)
        axes[idx].set_title(f'{col.replace("_", " ").title()}', fontweight='bold', fontsize=15)
        axes[idx].tick_params(axis='both', labelsize=11)
        axes[idx].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.suptitle('Numerical Feature Distributions: Retained vs Churned Customers', 
                 fontsize=16, fontweight='bold', y=1.02)
    plt.show()
    
    # Summary bar chart
    print("\n" + "=" * 60)
    print("MEAN VALUE COMPARISON: RETAINED vs CHURNED")
    print("=" * 60)
    
    fig, ax = plt.subplots(figsize=(16, 7))
    
    means_retained = df_processed[df_processed['churn_flag'] == 0][numerical_cols].mean()
    means_churned = df_processed[df_processed['churn_flag'] == 1][numerical_cols].mean()
    pct_diff = ((means_churned - means_retained) / means_retained * 100)
    
    x = np.arange(len(numerical_cols))
    width = 0.7
    colors = [COLORS['churned'] if p < 0 else COLORS['retained'] for p in pct_diff]
    bars = ax.bar(x, pct_diff, width=width, color=colors, edgecolor='white', linewidth=2)
    
    ax.axhline(y=0, color=COLORS['text'], linestyle='-', linewidth=2)
    ax.set_xticks(x)
    ax.set_xticklabels([col.replace('_', ' ').title() for col in numerical_cols], 
                       fontsize=11, ha='center', rotation=45)
    ax.set_ylabel('% Difference (Churned vs Retained)', fontsize=13, fontweight='bold')
    ax.set_xlabel('Engagement Metrics', fontsize=13, fontweight='bold')
    ax.set_title('Churned Customers Have LOWER Engagement Across All Metrics', 
                 fontsize=16, fontweight='bold')
    ax.tick_params(axis='y', labelsize=11)
    ax.grid(axis='y', alpha=0.3)
    
    for i, (bar, pct) in enumerate(zip(bars, pct_diff)):
        height = bar.get_height()
        offset = 3 if i % 2 == 0 else 4
        label_y = height + (offset if height > 0 else -offset - 2)
        ax.text(bar.get_x() + bar.get_width()/2, label_y, 
                f'{pct:.0f}%', ha='center', va='bottom' if height > 0 else 'top', 
                fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(df_processed):
    """
    Plot correlation heatmap for selected features.
    
    Parameters:
    -----------
    df_processed : pd.DataFrame
        Preprocessed dataframe
    """
    print("=" * 60)
    print("CORRELATION ANALYSIS")
    print("=" * 60)
    
    correlation_cols = ['churn_flag', 'coupon_flag', 'pay_now_flag', 'cancel_flag', 'loyalty_tier',
                        'total_visit_minutes', 'total_visit_pages', 'search_pages_count', 
                        'property_pages_count', 'bounce_visits_count', 'searched_destinations_count',
                        'hotel_star_rating', 'pages_per_minute', 'property_page_ratio']
    
    corr_matrix = df_processed[correlation_cols].corr()
    
    plt.figure(figsize=(14, 10))
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', cmap=get_custom_cmap(), center=0,
                square=True, linewidths=0.5, cbar_kws={'shrink': 0.8},
                annot_kws={'fontsize': 9, 'fontweight': 'bold'})
    plt.title('Correlation Matrix - Features vs Churn', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
    
    # Print correlations with churn
    print("\n📊 Correlations with Churn Flag (sorted by absolute value):")
    churn_corr = corr_matrix['churn_flag'].drop('churn_flag').sort_values(key=abs, ascending=False)
    for feature, corr in churn_corr.items():
        direction = "↑" if corr > 0 else "↓"
        print(f"  {direction} {feature}: {corr:.4f}")


def plot_model_comparison(y_test, y_prob_lr, y_prob_rf, y_prob_gb, 
                          y_pred_lr, y_pred_rf, y_pred_gb):
    """
    Plot ROC curves and metrics comparison for all models.
    
    Parameters:
    -----------
    y_test : array
        True labels
    y_prob_* : array
        Predicted probabilities for each model
    y_pred_* : array
        Predicted labels for each model
    """
    from sklearn.metrics import roc_curve, roc_auc_score, accuracy_score, precision_score, recall_score, f1_score
    
    print("=" * 60)
    print("MODEL COMPARISON")
    print("=" * 60)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # ROC Curves
    ax1 = axes[0]
    models = [
        ('Logistic Regression', y_prob_lr, COLORS['model_1']),
        ('Random Forest', y_prob_rf, COLORS['model_2']),
        ('Gradient Boosting', y_prob_gb, COLORS['model_3'])
    ]
    
    for name, y_prob, color in models:
        fpr, tpr, _ = roc_curve(y_test, y_prob)
        auc = roc_auc_score(y_test, y_prob)
        ax1.plot(fpr, tpr, label=f'{name} (AUC = {auc:.3f})', color=color, linewidth=2.5)
    
    ax1.plot([0, 1], [0, 1], color=COLORS['text'], linestyle='--', label='Random Classifier', alpha=0.7)
    ax1.set_xlabel('False Positive Rate', fontsize=12)
    ax1.set_ylabel('True Positive Rate', fontsize=12)
    ax1.set_title('ROC Curves - Model Comparison', fontsize=14, fontweight='bold')
    ax1.legend(loc='lower right')
    ax1.grid(True, alpha=0.3)
    
    # Metrics comparison
    ax2 = axes[1]
    metrics_comparison = pd.DataFrame({
        'Model': ['Logistic Regression', 'Random Forest', 'Gradient Boosting'],
        'Accuracy': [accuracy_score(y_test, y_pred_lr), accuracy_score(y_test, y_pred_rf), 
                     accuracy_score(y_test, y_pred_gb)],
        'Precision': [precision_score(y_test, y_pred_lr), precision_score(y_test, y_pred_rf),
                      precision_score(y_test, y_pred_gb)],
        'Recall': [recall_score(y_test, y_pred_lr), recall_score(y_test, y_pred_rf),
                   recall_score(y_test, y_pred_gb)],
        'F1-Score': [f1_score(y_test, y_pred_lr), f1_score(y_test, y_pred_rf),
                     f1_score(y_test, y_pred_gb)],
        'ROC-AUC': [roc_auc_score(y_test, y_prob_lr), roc_auc_score(y_test, y_prob_rf),
                    roc_auc_score(y_test, y_prob_gb)]
    })
    
    x = np.arange(len(metrics_comparison))
    width = 0.15
    metrics_list = ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'ROC-AUC']
    metric_colors = [COLORS['cat_1'], COLORS['cat_2'], COLORS['cat_3'], COLORS['accent'], COLORS['model_3']]
    
    for i, (metric, color) in enumerate(zip(metrics_list, metric_colors)):
        ax2.bar(x + i*width, metrics_comparison[metric], width, label=metric, color=color, edgecolor='white')
    
    ax2.set_ylabel('Score', fontsize=12)
    ax2.set_title('Model Performance Metrics Comparison', fontsize=14, fontweight='bold')
    ax2.set_xticks(x + width * 2)
    ax2.set_xticklabels(metrics_comparison['Model'], rotation=15)
    ax2.legend(loc='lower right')
    ax2.set_ylim(0, 1)
    ax2.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.show()
    
    print("\n📊 Model Performance Summary:")
    print(metrics_comparison.round(4).to_string(index=False))
    
    return metrics_comparison


def plot_confusion_matrices(y_test, y_pred_lr, y_pred_rf, y_pred_gb):
    """
    Plot confusion matrices for all models.
    
    Parameters:
    -----------
    y_test : array
        True labels
    y_pred_* : array
        Predicted labels for each model
    """
    from sklearn.metrics import confusion_matrix
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    predictions = [
        ('Logistic Regression', y_pred_lr),
        ('Random Forest', y_pred_rf),
        ('Gradient Boosting', y_pred_gb)
    ]
    
    for ax, (name, y_pred) in zip(axes, predictions):
        cm = confusion_matrix(y_test, y_pred)
        sns.heatmap(cm, annot=True, fmt='d', cmap=get_confusion_matrix_cmap(), ax=ax,
                    xticklabels=['Retained', 'Churned'],
                    yticklabels=['Retained', 'Churned'],
                    annot_kws={'fontsize': 12, 'fontweight': 'bold'},
                    linewidths=2, linecolor='white')
        ax.set_xlabel('Predicted', fontsize=12)
        ax.set_ylabel('Actual', fontsize=12)
        ax.set_title(f'{name}\nConfusion Matrix', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.show()


def plot_feature_importance(feature_names, importances, title='Feature Importance', top_n=15):
    """
    Plot horizontal bar chart of feature importance.
    
    Parameters:
    -----------
    feature_names : list
        Names of features
    importances : array
        Importance scores
    title : str
        Plot title
    top_n : int
        Number of top features to show
    """
    importance_df = pd.DataFrame({
        'Feature': feature_names,
        'Importance': importances
    }).sort_values('Importance', ascending=False).head(top_n)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    n_bars = len(importance_df)
    colors = [plt.cm.GnBu(0.4 + 0.5 * (n_bars - i) / n_bars) for i in range(n_bars)]
    ax.barh(range(len(importance_df)), importance_df['Importance'], color=colors, 
            edgecolor='white', linewidth=1)
    ax.set_yticks(range(len(importance_df)))
    ax.set_yticklabels(importance_df['Feature'])
    ax.set_xlabel('Feature Importance', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.gca().invert_yaxis()
    plt.show()
    
    return importance_df


def plot_risk_segmentation(customer_scores):
    """
    Plot customer risk segmentation charts.
    
    Parameters:
    -----------
    customer_scores : pd.DataFrame
        Dataframe with churn_probability and risk_category columns
    """
    print("=" * 60)
    print("CUSTOMER RISK SCORING")
    print("=" * 60)
    
    risk_summary = customer_scores.groupby('risk_category').agg({
        'churned': ['count', 'sum', 'mean']
    }).round(4)
    risk_summary.columns = ['Customer Count', 'Actually Churned', 'Actual Churn Rate']
    
    print("\n📊 Customer Risk Distribution:")
    print(risk_summary.to_string())
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Risk category pie chart
    risk_counts = customer_scores['risk_category'].value_counts().sort_index()
    axes[0].pie(risk_counts.values, labels=risk_counts.index, autopct='%1.1f%%',
                colors=RISK_COLORS, explode=(0, 0, 0.05, 0.1), shadow=True,
                textprops={'fontsize': 11, 'fontweight': 'bold'})
    axes[0].set_title('Customer Distribution by Risk Category', fontsize=14, fontweight='bold')
    
    # Probability histogram
    axes[1].hist(customer_scores['churn_probability'], bins=50, color=COLORS['cat_1'], 
                 edgecolor='white', alpha=0.8, linewidth=0.5)
    axes[1].axvline(x=0.5, color=COLORS['churned'], linestyle='--', linewidth=2.5, 
                    label='Decision Threshold (0.5)')
    axes[1].set_xlabel('Churn Probability', fontsize=12)
    axes[1].set_ylabel('Number of Customers', fontsize=12)
    axes[1].set_title('Distribution of Churn Probabilities', fontsize=14, fontweight='bold')
    axes[1].legend(loc='upper right')
    
    plt.tight_layout()
    plt.show()
    
    high_risk_count = (customer_scores['risk_category'].isin(['High Risk', 'Critical Risk'])).sum()
    total_customers = len(customer_scores)
    print(f"\n💡 {high_risk_count:,} customers ({high_risk_count/total_customers*100:.1f}%) identified as High/Critical Risk")

