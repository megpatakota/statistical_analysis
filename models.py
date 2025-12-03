"""
Machine Learning Models module for Hotels.com Churn Analysis
Contains model training, evaluation, and feature preparation functions
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import (classification_report, accuracy_score, precision_score, 
                             recall_score, f1_score, roc_auc_score)


def prepare_features(customer_df):
    """
    Prepare features for model training.
    
    Parameters:
    -----------
    customer_df : pd.DataFrame
        Customer-level aggregated dataframe
        
    Returns:
    --------
    tuple
        X (features), y (target), feature_cols, model_df_dummies
    """
    print("=" * 60)
    print("FEATURE PREPARATION FOR MODELLING")
    print("=" * 60)
    
    model_df = customer_df.copy()
    
    # Drop identifier and date columns
    model_df = model_df.drop(['email_address', 'first_booking', 'last_booking'], axis=1)
    
    # Handle NaN values
    model_df = model_df.fillna(0)
    
    # Encode categorical variables
    categorical_cols_model = ['primary_platform', 'primary_channel', 'customer_type']
    
    for col in categorical_cols_model:
        le = LabelEncoder()
        model_df[col + '_encoded'] = le.fit_transform(model_df[col].astype(str))
    
    # Create dummy variables
    model_df_dummies = pd.get_dummies(model_df, columns=categorical_cols_model, drop_first=True)
    
    # Get feature columns
    feature_cols = [col for col in model_df_dummies.columns if col != 'churned' 
                    and not col.endswith('_bookings') and col not in categorical_cols_model]
    
    X = model_df_dummies[feature_cols]
    y = model_df_dummies['churned']
    
    print(f"\n📊 Feature matrix shape: {X.shape}")
    print(f"📊 Target distribution:")
    print(f"   • Non-churned: {(y==0).sum():,} ({(y==0).mean()*100:.1f}%)")
    print(f"   • Churned: {(y==1).sum():,} ({(y==1).mean()*100:.1f}%)")
    
    return X, y, feature_cols, model_df_dummies


def split_and_scale_data(X, y, test_size=0.25, random_state=42):
    """
    Split data and scale features.
    
    Parameters:
    -----------
    X : pd.DataFrame
        Feature matrix
    y : pd.Series
        Target variable
    test_size : float
        Test set proportion
    random_state : int
        Random seed
        
    Returns:
    --------
    tuple
        X_train, X_test, y_train, y_test, X_train_scaled, X_test_scaled, scaler
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"\n✓ Train set: {len(X_train):,} samples")
    print(f"✓ Test set: {len(X_test):,} samples")
    
    return X_train, X_test, y_train, y_test, X_train_scaled, X_test_scaled, scaler


def train_logistic_regression(X_train_scaled, y_train, X_test_scaled, y_test):
    """
    Train and evaluate Logistic Regression model.
    
    Parameters:
    -----------
    X_train_scaled, X_test_scaled : array
        Scaled feature matrices
    y_train, y_test : array
        Target variables
        
    Returns:
    --------
    tuple
        model, y_pred, y_prob
    """
    print("=" * 60)
    print("MODEL 1: LOGISTIC REGRESSION")
    print("=" * 60)
    
    model = LogisticRegression(max_iter=1000, random_state=42, class_weight='balanced')
    model.fit(X_train_scaled, y_train)
    
    y_pred = model.predict(X_test_scaled)
    y_prob = model.predict_proba(X_test_scaled)[:, 1]
    
    _print_model_performance(y_test, y_pred, y_prob)
    
    return model, y_pred, y_prob


def train_random_forest(X_train, y_train, X_test, y_test):
    """
    Train and evaluate Random Forest model.
    
    Parameters:
    -----------
    X_train, X_test : pd.DataFrame
        Feature matrices
    y_train, y_test : array
        Target variables
        
    Returns:
    --------
    tuple
        model, y_pred, y_prob
    """
    print("=" * 60)
    print("MODEL 2: RANDOM FOREST")
    print("=" * 60)
    
    model = RandomForestClassifier(
        n_estimators=200, max_depth=15, min_samples_split=10,
        random_state=42, class_weight='balanced', n_jobs=-1
    )
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]
    
    _print_model_performance(y_test, y_pred, y_prob)
    
    return model, y_pred, y_prob


def train_gradient_boosting(X_train, y_train, X_test, y_test):
    """
    Train and evaluate Gradient Boosting model.
    
    Parameters:
    -----------
    X_train, X_test : pd.DataFrame
        Feature matrices
    y_train, y_test : array
        Target variables
        
    Returns:
    --------
    tuple
        model, y_pred, y_prob
    """
    print("=" * 60)
    print("MODEL 3: GRADIENT BOOSTING")
    print("=" * 60)
    
    model = GradientBoostingClassifier(
        n_estimators=150, max_depth=5, learning_rate=0.1,
        random_state=42, min_samples_split=10
    )
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]
    
    _print_model_performance(y_test, y_pred, y_prob)
    
    return model, y_pred, y_prob


def _print_model_performance(y_test, y_pred, y_prob):
    """Print model performance metrics."""
    print("\n📊 Model Performance:")
    print("-" * 40)
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred):.4f}")
    print(f"Recall: {recall_score(y_test, y_pred):.4f}")
    print(f"F1-Score: {f1_score(y_test, y_pred):.4f}")
    print(f"ROC-AUC: {roc_auc_score(y_test, y_prob):.4f}")
    
    print("\n📋 Classification Report:")
    print(classification_report(y_test, y_pred, target_names=['Retained', 'Churned']))


def get_logistic_regression_odds_ratios(model, feature_names):
    """
    Calculate odds ratios from logistic regression coefficients.
    
    Parameters:
    -----------
    model : LogisticRegression
        Trained model
    feature_names : list
        Feature names
        
    Returns:
    --------
    pd.DataFrame
        Odds ratios dataframe
    """
    print("=" * 60)
    print("LOGISTIC REGRESSION - ODDS RATIOS")
    print("=" * 60)
    
    odds_ratios = pd.DataFrame({
        'Feature': feature_names,
        'Coefficient': model.coef_[0],
        'Odds_Ratio': np.exp(model.coef_[0])
    })
    odds_ratios['Abs_Coef'] = np.abs(odds_ratios['Coefficient'])
    odds_ratios = odds_ratios.sort_values('Abs_Coef', ascending=False)
    
    print("\n📊 Top 15 Most Important Features (by Odds Ratio):")
    print("-" * 60)
    print("\nInterpretation: Odds Ratio > 1 = increases churn risk")
    print("               Odds Ratio < 1 = decreases churn risk\n")
    
    for _, row in odds_ratios.head(15).iterrows():
        direction = "↑ INCREASES" if row['Odds_Ratio'] > 1 else "↓ DECREASES"
        print(f"  {row['Feature'][:35]:35} | OR: {row['Odds_Ratio']:.3f} | {direction} churn risk")
    
    return odds_ratios


def score_customers(model, X, model_df_dummies):
    """
    Score all customers with churn probability.
    
    Parameters:
    -----------
    model : trained model
        Model to use for scoring
    X : pd.DataFrame
        Feature matrix
    model_df_dummies : pd.DataFrame
        Full dataframe with target
        
    Returns:
    --------
    pd.DataFrame
        Dataframe with churn probabilities and risk categories
    """
    customer_scores = model_df_dummies.copy()
    customer_scores['churn_probability'] = model.predict_proba(X)[:, 1]
    customer_scores['risk_category'] = pd.cut(
        customer_scores['churn_probability'], 
        bins=[0, 0.3, 0.5, 0.7, 1.0],
        labels=['Low Risk', 'Medium Risk', 'High Risk', 'Critical Risk']
    )
    
    return customer_scores

