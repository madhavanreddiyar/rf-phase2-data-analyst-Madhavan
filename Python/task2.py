import pandas as pd

# 1. Load dataset
df = pd.read_csv("customer_data.csv")

# 2. Initial inspection
print("First 5 rows:")
print(df.head(), "\n")

print("Dataset info:")
print(df.info(), "\n")

print("Missing values:")
print(df.isnull().sum(), "\n")

# 3. Handle missing values (email column)

df['email'] = df['email'].fillna('Not Provided')

# 4. Remove duplicate rows (if any)
df = df.drop_duplicates()

# 5. Feature Engineering: Create age groups
df['Age_Group'] = pd.cut(
    df['age'],
    bins=[17, 25, 35, 45, 60, 100],
    labels=['18–25', '26–35', '36–45', '46–60', '60+']
)

# Q1. Age distribution
age_distribution = df['Age_Group'].value_counts()
print("Age Distribution:")
print(age_distribution, "\n")

# Q2. City-wise customer count
city_customers = df['city'].value_counts()
print("Customers by City:")
print(city_customers, "\n")

# Q3. Gender distribution (percentage)
gender_distribution = df['gender'].value_counts(normalize=True) * 100
print("Gender Distribution (%):")
print(gender_distribution.round(2), "\n")

# Q4. Customers without email
missing_email_count = (df['email'] == 'Not Provided').sum()
print("Customers without email:", missing_email_count, "\n")

# Q5. Most common age group per city
age_group_per_city = (
    df.groupby('city')['Age_Group']
      .agg(lambda x: x.value_counts().idxmax())
)
print("Most common age group per city:")
print(age_group_per_city, "\n")

# 6. Final cleaned dataset preview
print("Cleaned dataset preview:")
print(df.head())
