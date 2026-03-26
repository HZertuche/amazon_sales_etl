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

## Table of Contents
- [Project Highlights](#project-highlights)
- [Project Overview](#project-overview)
- [Objective](#objective)
- [Dataset Source](#dataset-source)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Project Architecture](#project-architecture)
- [Architecture Diagram](#architecture-diagram)
- [Data Preprocessing](#data-preprocessing)
- [Data Quality Validation](#data-quality-validation)
- [How to Run](#how-to-run)
- [Example SQL Query](#example-sql-query)
- [Dashboard](#dashboard)
- [Key Insights](#key-insights)
- [Business Impact](#business-impact)
- [Assumptions and Limitations](#assumptions-and-limitations)
- [Future Improvements](#future-improvements)

## Project Highlights

- Built an end-to-end ETL pipeline on AWS to process Amazon sales data.
- Transformed raw CSV datasets into optimized Parquet files for analytical workloads.
- Implemented data validation checks to ensure dataset consistency.
- Queried the processed data using Amazon Athena and Python.
- Built an interactive Amazon QuickSight dashboard to analyze product performance.

## Project Overview

This project builds a complete ETL pipeline using an Amazon sales dataset.

The pipeline extracts raw Amazon sales data, performs data cleaning and feature engineering, and stores optimized results in Parquet format for analytics.

## Objective 

The goal of this project is to demonstrate core data engineering practices, including:

- Data cleaning
- Feature engineering
- Columnar storage using Parquet
- SQL analytics with Amazon Athena
- Data visualization using Amazon QuickSight

## Dataset Source
This project uses the **Amazon Sales Dataset**, a public dataset commonly used for analytics and data engineering projects.

- **Source:** [Kaggle - Amazon Sales Dataset](https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset)
- **Usage:** Educational and portfolio purposes only

> **Note:** This dataset is a sample of historical candidate data and does not represent full production data.

## Dataset
The dataset contains product, pricing, discount, rating, and review information. 

Key features include:

- *product_id* – Unique product ID  
- *product_name* – Product Name  
- *category* – Category of the product  
- *discounted_price* – Final price with discount  
- *actual_price* – Actual price
- *discount_percentage* – Percentage of the discount from the actual price
- *rating* – Product rating given by customers   
- *rating_count* – Number of customer ratings for the product
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
- **Python** – Data processing and pipeline scripting
- **Amazon S3** – Cloud data storage  
- **AWS Glue** – ETL data transformation
- **Amazon Athena** – Serverless SQL query engine
- **Amazon QuickSight** – Data visualization and dashboarding

## Project Architecture

Extract → Transform → Load

Raw CSV → Data Cleaning → Feature Engineering → Parquet Storage → SQL Analytics → Visualization Dashboard


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
      Dashboard (Amazon QuickSight)


## Data Preprocessing

Steps performed in the project:

1. Remove special characters from *discounted_price* and *actual_price*, then convert the values to decimal format.  
2. Change columns to string format: *product_id*, *product_name*, *category*, *discount_percentage*, *rating_count*.
3. Change *rating* value to decimal type.
4. Split the text from the column *category* to create subcategories.  
5. Select the columns to visualize.

## Data Quality Validation

During the transformation stage, several validation checks were applied:

- Ensured that critical fields do not contain null values.
- Validated data types for selected fields.
- Verified that the *category* field was properly split into the required hierarchical levels.
- Removal of special characters from *discounted_price* and *actual_price* to ensure consistent decimal format.

## How to Run
1. Download the Amazon Sales dataset from Kaggle.
2. Upload the raw CSV files to the corresponding folders in your Amazon S3 bucket.
3. Run the AWS Glue jobs to clean and preprocess the datasets.
4. Store the final output in Parquet format.
5. Query the curated dataset using Amazon Athena.
6. Connect the final dataset to Amazon QuickSight to build the dashboard.

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

## Dashboard
![Main Dashboard](screenshots/main-dashboard.PNG)

| Top 5 Products | Prices by Category |
|-------------|-------------|
| ![](screenshots/dashboard-pt1.PNG) | ![](screenshots/dashboard-pt2.PNG) |

| Clients Savings by % Discounted | Units by % Discounted |
|--------------|--------------|
| ![](screenshots/dashboard-pt3.PNG) | ![](screenshots/dashboard-pt4.PNG) |

| Rating Table | Units Sold by Rating |
|-------------|-------------|
| ![](screenshots/dashboard-pt5.PNG) | ![](screenshots/dashboard-pt6.PNG) |

| Numbers of Units Sold by Rating |
|--------------------------------|
| ![](screenshots/dashboard-pt7.PNG) |

| Actual Price by Category1 | Actual Price by Category2 |
|--------------|--------------|
| ![](screenshots/dashboard-pt8.PNG) | ![](screenshots/dashboard-pt9.PNG) |


## Key Insights

- Four of the most expensive products belong to the Electronics category.
- One product had a 91% discount, representing a potential loss of $91,000 in revenue.
- Customers tend to purchase more units when discounts range between 50% and 60%.
- Products with ratings between 4.0 and 4.4 have a higher probability of being sold.
- Categories with the highest rating counts tend to generate more sales.


## Business Impact

The analysis of product performance with discounts, can support better business decisions in several areas:

- **Operational planning:** Understanding which product categories generate the highest sales can help businesses prioritize operational resources, including logistics and fulfillment capacity.
- **Inventory optimization:** The Electronics and Home & Kitchen categories represent a significant portion of total sales. Retailers should ensure consistent product availability in these categories.
- **Marketing strategy:** Customers show strong interest in electronics and home-related products. Targeted discount campaigns for these categories could increase conversion rates and boost overall revenue.
- **Category management:** High demand for technology products and household appliances suggests opportunities to expand product offerings within these categories and introduce complementary products.

## Assumptions and Limitations
- This dataset is a public sample and does not represent full Instacart production data.
- The analysis is based on historical sales behavior and should be interpreted as exploratory.
- The project focuses on batch ETL and analytical reporting rather than real-time processing.
- Business insights are inferred from products sales data, not from revenue or profit metrics.

## Future Improvements
- Automate pipeline orchestration with AWS Step Functions or EventBridge
- Add data partitioning strategies to improve Athena query performance
- Integrate data quality monitoring tools
- Deploy dashboards with scheduled refresh workflows
