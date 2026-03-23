# Amazon Sales Analytics | AWS ETL Data Engineering Pipeline

End-to-end AWS Data Engineering project for analyzing product discounts, ratings, and sales performance.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![AWS S3](https://img.shields.io/badge/AWS-S3-red)
![AWS Glue](https://img.shields.io/badge/AWS-Glue-purple)
![Amazon Athena](https://img.shields.io/badge/Amazon-Athena-blue)
![Amazon QuickSight](https://img.shields.io/badge/Amazon-QuickSight-green)
![Parquet](https://img.shields.io/badge/Data%20Format-Parquet-lightgrey)
![ETL Pipeline](https://img.shields.io/badge/Data%20Engineering-ETL-success)

## Project Overview

This project builds a complete ETL pipeline using an Amazon sales dataset.

The pipeline extracts raw Amazon sales data, performs data cleaning and feature engineering, and stores optimized results in Parquet format for analytics.

## Objective 

The goal of this project is to demonstrate core data engineering practices, including:

- Data cleaning
- Feature engineering
- Columnar storage using Parquet
- SQL analytics with Athena
- Data visualization using Amazon QuickSight

## Dataset
The dataset contains information about the products and prices. 

Key features include:

- *product_id* – Unique product ID  
- *product_name* – Product Name  
- *category* – Category of the product  
- *discounted_price* – Final price with discount  
- *actual_price* – Actual price
- *discount_percentage* – Percentage of the discount from the actual price
- *rating* – Client rate of the product   
- *rating_count* – Number of rates from the clients for a certain product
- *about_product* – Description of the product  
- *user_id* – Unique number ID from client
- *user_name* – Username of the client  
- *review_id* – Unique review ID
- *review_title* –  Title of the client review
- *review_content* – Comments of the client review
- *img_link* - URL of the image product
- *product_link* - URL of the product

**Note:** The dataset contains null values and special characters.

## Project Structure

```
amazon_sales_etl
│
├── data/
│ ├── raw/
│ └── processed/
│
├── notebooks/
├── glue_jobs/
├── athena/
└── screenshots/
```

## Tech Stack
- Python 
- Amazon S3 - Storage 
- AWS Glue – Data cleaning and preprocessing    
- Athena - Queries results
- Amazon QuickSight - Data visualization dashboard

## Project Architecture

Extract → Transform → Load

Raw CSV → Data Cleaning → Feature Engineering → Parquet Storage → SQL Analytics → Amazon Quicksight


## Architecture Diagram
        Raw Data (CSV Files)
               │
               ▼
        Amazon S3 (Storage)
               │
               ▼
        AWS Glue Jobs
    Data Cleaning & Feature Engineering
               │
               ▼
        Clean Dataset (Parquet)
               │
               ▼
         Analytics Layer
      (Athena / Python)
               │
               ▼
      Dashboard (Amazon Quicksight)


## Data Preprocessing

Steps performed in the project:

1. Remove special characters from *discounted_price* and *actual_price*, then convert the values to decimal format.  
2. Change columns to string format: *product_id*, *product_name*, *category*, *discount_percentage*, *rating_count*.
3. Change *rating* value to decimal type.
4. Split the text from the column *category* to create subcategories.  
5. Select the columns to visualize.

# Data Quality Validation

During the transformation stage, several validation checks were applied:

- Validation of dtype format for selected fields
- Adequate split levels for category
- Removal of characters on prices

## Example SQL Query
Using Amazon Athena;

Analyze product performance and average rating by category.

```sql
SELECT category_lvl1, 
COUNT(*) as number_units,
avg(rating) as avg_rating
FROM "amazon_sales"."outputv2"
GROUP BY category_lvl1
ORDER BY number_units DESC;
```

## Business Impact

When analyzing product performance with discounts, the following insights were observed:

- Products with discounts between 50% and 60% show the highest sales performance.
- Products with ratings above 4 tend to have higher sales potential.
- Products with a higher number of ratings are more likely to be purchased by customers.

## Dashboard
![Main Dashboard](screenshots/main-dashboard.png)

## Key Insights

- Four of the most expensive products belong to the Electronics category.
- One product had a 91% discount, representing a potential loss of $91,000 in revenue.
- Customers purchase the highest number of units when discounts are between 50% and 60%.
- Products with ratings between 4.0 and 4.4 have a higher probability of being sold.
- Categories with the highest rating counts tend to generate more sales.

### Key Visualizations

| Top 5 Products | Prices by Category |
|-------------|-------------|
| ![](screenshots/dashboard-pt1.png) | ![](screenshots/dashboard-pt2.png) |

| Clients Savings by % Discounted | Units by % Discounted |
|--------------|--------------|
| ![](screenshots/dashboard-pt3.png) | ![](screenshots/dashboard-pt4.png) |

| Rating Table | Units Sold by Rating |
|-------------|-------------|
| ![](screenshots/dashboard-pt5.png) | ![](screenshots/dashboard-pt6.png) |

| Numbers of Units Sold by Rating |
|--------------------------------|
| ![](screenshots/dashboard-pt7.png) |

| Actual Price by Category1 | Actual Price by Category2 |
|--------------|--------------|
| ![](screenshots/dashboard-pt8.png) | ![](screenshots/dashboard-pt9.png) |


