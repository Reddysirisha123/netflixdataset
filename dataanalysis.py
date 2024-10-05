import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

# Load the data
df = pd.read_csv('netflixdata/abc.csv')

# Convert date columns to datetime
df['Join Date'] = pd.to_datetime(df['Join Date'])
df['Last Payment Date'] = pd.to_datetime(df['Last Payment Date'])


# 1. Gender distribution among subscription plans
def gender_distribution_by_plan():
    gender_plan_dist = df.groupby(['Subscription Type', 'Gender']).size().unstack()
    gender_plan_dist_percentage = gender_plan_dist.div(gender_plan_dist.sum(axis=1), axis=0) * 100

    print("Gender distribution by subscription plan:")
    print(gender_plan_dist_percentage)

    gender_plan_dist_percentage.plot(kind='bar', stacked=True)
    plt.title('Gender Distribution by Subscription Plan')
    plt.xlabel('Subscription Type')
    plt.ylabel('Percentage')
    plt.legend(title='Gender')
    plt.tight_layout()
    plt.show()


# 2. Percentage of users by country
def users_by_country():
    country_counts = df['Country'].value_counts()
    country_percentages = country_counts / len(df) * 100

    print("\nPercentage of users by country:")
    print(country_percentages)

    plt.figure(figsize=(10, 6))
    country_percentages.plot(kind='bar')
    plt.title('Percentage of Users by Country')
    plt.xlabel('Country')
    plt.ylabel('Percentage')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# 3. Age group with highest subscription rate for each plan type
def age_group_subscription_rate():
    df['Age Group'] = pd.cut(df['Age'], bins=[0, 18, 25, 35, 45, 55, 65, 100],
                             labels=['0-18', '19-25', '26-35', '36-45', '46-55', '56-65', '65+'])

    age_plan_dist = df.groupby(['Subscription Type', 'Age Group']).size().unstack()
    age_plan_dist_percentage = age_plan_dist.div(age_plan_dist.sum(axis=1), axis=0) * 100

    print("\nAge group with highest subscription rate for each plan type:")
    print(age_plan_dist_percentage.idxmax(axis=1))


# 4. Average age of users for each subscription type
def average_age_by_plan():
    avg_age = df.groupby('Subscription Type')['Age'].mean()

    print("\nAverage age of users for each subscription type:")
    print(avg_age)



# 6. Monthly revenue by subscription type
def monthly_revenue_by_plan():
    revenue_by_plan = df.groupby('Subscription Type')['Monthly Revenue'].sum()

    print("\nMonthly revenue by subscription type:")
    print(revenue_by_plan)


# 7. Average duration of subscription plans
def average_subscription_duration():
    df['Subscription Duration'] = (df['Last Payment Date'] - df['Join Date']).dt.days
    avg_duration = df.groupby('Subscription Type')['Subscription Duration'].mean()

    print("\nAverage duration of subscription plans (in days):")
    print(avg_duration)


# 10. Average time between join date and last payment date
def average_time_join_to_last_payment():
    df['Time Since Join'] = (df['Last Payment Date'] - df['Join Date']).dt.days
    avg_time = df['Time Since Join'].mean()

    print("\nAverage time between join date and last payment date (in days):")
    print(avg_time)


# 11. Payment behavior based on device usage
def payment_behavior_by_device():
    device_payment_behavior = df.groupby('Device')['Time Since Join'].mean()

    print("\nAverage time since join by device type (in days):")
    print(device_payment_behavior)


# 12. Percentage of users with recent payments
def recent_payment_percentage():
    current_date = df['Last Payment Date'].max()
    one_month_ago = current_date - pd.Timedelta(days=30)
    three_months_ago = current_date - pd.Timedelta(days=90)

    recent_1m = (df['Last Payment Date'] > one_month_ago).mean() * 100
    recent_3m = (df['Last Payment Date'] > three_months_ago).mean() * 100

    print("\nPercentage of users with payments in the last month:", recent_1m)
    print("Percentage of users with payments in the last three months:", recent_3m)


# 13. Most common devices by subscription type
def common_devices_by_plan():
    device_plan_dist = df.groupby(['Subscription Type', 'Device']).size().unstack()
    device_plan_dist_percentage = device_plan_dist.div(device_plan_dist.sum(axis=1), axis=0) * 100

    print("\nMost common devices by subscription type:")
    print(device_plan_dist_percentage.idxmax(axis=1))


# 14. Correlation between device type and subscription plan
def device_plan_correlation():
    device_plan_corr = pd.crosstab(df['Device'], df['Subscription Type'])
    device_plan_corr_norm = device_plan_corr.div(device_plan_corr.sum(axis=1), axis=0)

    print("\nCorrelation between device type and subscription plan:")
    print(device_plan_corr_norm)


# 15. User sign-up trends over time
def signup_trends():
    df['Join Month'] = df['Join Date'].dt.to_period('M')
    signups_by_month = df['Join Month'].value_counts().sort_index()
    plt.figure(figsize=(12, 6))
    signups_by_month.plot(kind='line')
    plt.title('User Sign-up Trends Over Time')
    plt.xlabel('Month')
    plt.ylabel('Number of Sign-ups')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



# 17. Average tenure of subscribers
def average_tenure():
    df['Tenure'] = (df['Last Payment Date'] - df['Join Date']).dt.days
    avg_tenure = df['Tenure'].mean()

    print("\nAverage tenure of subscribers (in days):")
    print(avg_tenure)


# 18. Total revenue by country
def revenue_by_country():
    revenue_country = df.groupby('Country')['Monthly Revenue'].sum()
    print("\nTotal revenue by country:")
    print(revenue_country)


# 19. Revenue correlation with number of subscribers by country
def revenue_subscriber_correlation():
    country_revenue = df.groupby('Country')['Monthly Revenue'].sum()
    country_subscribers = df['Country'].value_counts()
    correlation = country_revenue.corr(country_subscribers)

    print("\nCorrelation between revenue and number of subscribers by country:")
    print(correlation)


# 20. Average revenue per user (ARPU) by country and subscription type
def arpu_by_country_and_plan():
    arpu = df.groupby(['Country', 'Subscription Type'])['Monthly Revenue'].mean()

    print("\nAverage Revenue Per User (ARPU) by country and subscription type:")
    print(arpu)



revenue_by_plan = df.groupby('Subscription Type')['Monthly Revenue'].sum()

# Create a bar plot
plt.figure(figsize=(10, 6))
revenue_by_plan.plot(kind='bar')
plt.title('Monthly Revenue by Subscription Type')
plt.xlabel('Subscription Type')
plt.ylabel('Total Monthly Revenue')
plt.xticks(rotation=0)

# Add value labels on top of each bar
for i, v in enumerate(revenue_by_plan):
    plt.text(i, v, f'${v:,.0f}', ha='center', va='bottom')

plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('netflixdata/abc.csv')

# Create a cross-tabulation of device types and subscription plans
device_plan_corr = pd.crosstab(df['Device'], df['Subscription Type'])

# Normalize the data to show percentages
device_plan_corr_norm = device_plan_corr.div(device_plan_corr.sum(axis=1), axis=0)

# Create a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(device_plan_corr_norm, annot=True, cmap='YlGnBu', fmt='.2%')

plt.title('Correlation between Device Type and Subscription Plan')
plt.xlabel('Subscription Type')
plt.ylabel('Device Type')

plt.tight_layout()
plt.show()

# Print the correlation data
print("Correlation between device type and subscription plan:")
print(device_plan_corr_norm)


import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('netflixdata/abc.csv')

# Count the number of subscribers for each plan
subscribers_by_plan = df['Subscription Type'].value_counts()

# Create a pie chart
plt.figure(figsize=(10, 8))
plt.pie(subscribers_by_plan.values, labels=subscribers_by_plan.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Subscribers by Subscription Plan')

# Add a circle at the center to make it a donut chart (optional)
center_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(center_circle)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.tight_layout()
plt.show()

# Print the subscriber counts
print("Number of subscribers for each subscription plan:")
print(subscribers_by_plan)


# 5. Total number of subscribers for each subscription plan
def subscribers_by_plan():
    sub_counts = df['Subscription Type'].value_counts()

    print("\nTotal number of subscribers for each subscription plan:")
    print(sub_counts)



# Run the analysis functions
gender_distribution_by_plan()
users_by_country()
age_group_subscription_rate()
average_age_by_plan()
subscribers_by_plan()
monthly_revenue_by_plan()
average_subscription_duration()
average_time_join_to_last_payment()
payment_behavior_by_device()
recent_payment_percentage()
common_devices_by_plan()
device_plan_correlation()
signup_trends()
average_tenure()
revenue_by_country()
revenue_subscriber_correlation()
arpu_by_country_and_plan()