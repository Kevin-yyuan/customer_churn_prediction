import pandas as pd
import numpy as np
import os

# Create data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Set the number of customers
num_customers = 1000

# Generate customer data
data = {
    'CustomerID': [f'CUS-{i+1:04d}' for i in range(num_customers)],
    'Name': [f'Customer {i+1}' for i in range(num_customers)],
    'Age': np.random.randint(18, 70, size=num_customers),
    'Gender': np.random.choice(['Male', 'Female'], size=num_customers, p=[0.5, 0.5]),
    'Tenure': np.random.randint(1, 72, size=num_customers),
    'Contract': np.random.choice(['Month-to-month', 'One year', 'Two year'], size=num_customers, p=[0.6, 0.3, 0.1]),
    'MonthlyCharges': np.random.uniform(20, 120, size=num_customers).round(2),
    'NumOfShipments': np.random.randint(1, 50, size=num_customers),
    'ShipmentWeight': np.random.uniform(1, 1000, size=num_customers).round(2),
    'OnTimeDelivery': np.random.choice([0, 1], size=num_customers, p=[0.3, 0.7]),
    'CustomerSatisfaction': np.random.randint(1, 6, size=num_customers),
    'DaysSinceLastShipment': np.random.randint(1, 365, size=num_customers),
    'SupportTicketsLodged': np.random.randint(0, 10, size=num_customers),
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate TotalCharges
df['TotalCharges'] = (df['Tenure'] * df['MonthlyCharges']).round(2)

# Generate the 'Churn' column with a more deliberate logic
churn_probability = 0.05  # Base churn probability

# Increase churn probability based on key factors
churn_probability += 0.20 * (df['DaysSinceLastShipment'] > 45)
churn_probability += 0.15 * (df['Contract'] == 'Month-to-month')
churn_probability += 0.10 * (df['SupportTicketsLodged'] > 3)
churn_probability += 0.05 * (df['CustomerSatisfaction'] <= 2)
churn_probability -= 0.05 * (df['Tenure'] > 48)

# Ensure probabilities are within [0, 1] range
churn_probability = np.clip(churn_probability, 0, 1)

df['Churn'] = (np.random.rand(num_customers) < churn_probability).astype(int)

# Save the DataFrame to a CSV file
df.to_csv('data/customer_churn_data.csv', index=False)

print("Sample data regenerated with story-driven logic and saved to data/customer_churn_data.csv")