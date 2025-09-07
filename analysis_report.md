# Customer Churn Prediction: Analysis Report

## 1. Introduction

**Business Problem:** The primary goal of this project is to address customer churn by building a machine learning model that can predict which customers are at high risk of leaving. By identifying these customers proactively, the business can implement targeted retention strategies to reduce revenue loss.

**Approach:** We used a dataset of customer information and shipping history to train a Random Forest classification model. The process involved exploring the data for initial insights, engineering new features to improve model performance, and evaluating the model based on its ability to correctly identify churning customers.

## 2. Key Findings: What Drives Churn?

The model identified several key factors that are strong predictors of customer churn:

- **Inactivity:** The number of days since a customer's last shipment is the most significant predictor. Customers who have not shipped recently are at a much higher risk of churning.
- **Contract Type:** Customers on flexible, 'Month-to-month' contracts are significantly more likely to churn compared to those on 'One year' or 'Two year' contracts.
- **Customer Satisfaction:** Low customer satisfaction scores are a strong indicator of potential churn.
- **High Monthly Charges:** Customers with higher monthly charges are more likely to churn.

## 3. Model Performance

The Random Forest model performs well in identifying at-risk customers, with the following key metrics:

- **Accuracy:** The model correctly predicts whether a customer will churn or not with high accuracy.
- **Recall:** For the 'Churn' class, the model demonstrates a strong ability to identify the majority of customers who are actually at risk of churning. This is the most important metric for this business problem, as it ensures we are not missing opportunities to retain customers.
- **Precision:** When the model predicts that a customer will churn, it is correct a high percentage of the time. This ensures that retention efforts are not wasted on customers who were not at risk.

## 4. Recommendations: An Actionable Retention Plan

Based on the insights from the model, we propose the following 3-step retention plan:

1.  **Launch a "Win-Back" Campaign:**
    - **Trigger:** A customer has not shipped for a significant period (e.g., > 30 days).
    - **Action:** Proactively contact these customers with a targeted offer, discount, or a service call to re-engage them.

2.  **Convert High-Value, High-Risk Customers:**
    - **Trigger:** A customer is on a 'Month-to-month' contract but has high total charges.
    - **Action:** Offer these customers an incentive to switch to a more stable 'One year' or 'Two year' contract, increasing their loyalty.

3.  **Address Customer Dissatisfaction:**
    - **Trigger:** A customer has a low satisfaction score or a high number of support tickets.
    - **Action:** Assign an account manager to investigate the underlying issues and provide a resolution, improving the customer's experience.

By implementing these targeted strategies, we can significantly reduce churn, improve customer retention, and protect quarterly revenue.
