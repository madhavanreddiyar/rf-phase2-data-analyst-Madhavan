📌 Project Overview

This project contains a Python script that performs data cleaning, preprocessing, and demographic analysis on a customer dataset containing 25,000 records.

The script uses Pandas to clean the data, create new features, and generate business insights.

📂 Dataset Information

The dataset includes:
customer_id – Unique identifier
age – Customer age
gender – Gender of customer
city – City of residence
email – Customer email address

⚙️ What the Python Script Does
1️⃣ Data Loading
Reads dataset using pandas.read_csv()

2️⃣ Data Cleaning
Checks for missing values
Fills missing emails with "Not Provided"
Removes duplicate records

3️⃣ Feature Engineering

Creates age group categories:
18–25
26–35
36–45
46–60
60+

4️⃣ Business Analysis

The script answers key business questions:
Total number of customers
Customer distribution by city
Gender distribution (percentage)
Number of customers without email
Most common age group per city

📊 Output Generated
Age group distribution
City-wise customer counts
Gender percentage breakdown
Data quality metrics (missing emails)
Cleaned dataset preview

🛠 Technologies Used
Python
Pandas

🎯 Objective

The purpose of this script is to demonstrate:
Data cleaning best practices
Feature engineering
Business-focused data analysis
Writing clean, future-safe Pandas code
Converting raw data into actionable insights
