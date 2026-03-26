# Amazon Sales Dashboard

This dashboard was built using Amazon QuickSight to analyze product performance, discounts, ratings, and category trends.

## Full Dashboard

![Main Dashboard](../screenshots/main-dashboard.PNG)

## Dashboard Objective

- The goal of this dashboard is to analyze product performance and consumer behavior, identifying the units with discount, categories, rating and typical products characteristics.

## Business Questions
- Which product categories contain the most expensive items in the inventory?
- How do extreme discounts impact potential revenue and profitability?
- What discount range is most effective at driving higher sales volume?
- What rating range is associated with higher product sales?
- Is there a relationship between product ratings and the number of units sold?

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

## Tech Stack
- **Python** – Data processing and pipeline scripting
- **Amazon S3** – Cloud data storage  
- **AWS Glue** – ETL data transformation
- **Amazon Athena** – Serverless SQL query engine
- **Amazon QuickSight** – Data visualization and dashboarding

## Metrics & Features
- *units* - Number of units

## Visualizations
The dashboard includes the following visualizations:

- Top Products by Price, highlighting the highest-priced items in the inventory.
- Price Distribution by Category, showing how product pricing varies across categories.
- Customer Savings Analysis, illustrating the total savings generated from discounts.
- Units Sold by Discount Percentage, analyzing how discount levels impact sales volume.
- Rating and Units Sold Table, summarizing product performance across categories.
- Units Sold vs Rating, exploring the relationship between customer ratings and sales.
- Units Sold by Rating, identifying which rating ranges drive higher demand.
- Category-Level Price Distribution (Level 1), showing the contribution of top-level categories to total product value.
- Category-Level Price Distribution (Level 2), providing a more granular breakdown of pricing across subcategories.

## Filters
- Category Level 1 Filter: Enables users to dynamically explore product performance across different top-level categories.
- Dynamic Filtering: Most visualizations update automatically based on the selected category, allowing focused analysis of pricing, discounts, and ratings.
- Top N Filtering: Applied to highlight the most expensive products and key contributors within each category.

## Dashboard Highlights

Key analytical components included in the dashboard:

- KPI-driven analysis of pricing, discounts, and product performance.
Product-level insights highlighting the most expensive items and their distribution across categories.
- Discount analysis to evaluate its impact on customer purchasing behavior and sales volume.
- Rating-based analysis to understand how customer perception influences product demand.
- Category-level breakdown of product performance using hierarchical category structures.
- Correlation analysis between product ratings and units sold.
- Interactive filtering to dynamically explore product performance across categories.

## Dashboard Content

| Top Departments | Prices by Category |
|----------------|------------|
| ![Top 5 Products](../screenshots/dashboard-pt1.PNG) | ![Prices by Category](../screenshots/dashboard-pt2.PNG) |

| Clients Savings | Units with Discount |
|---------------|---------------|
| ![Clients Savings](../screenshots/dashboard-pt3.PNG) | ![Clients Savings](../screenshots/dashboard-pt4.PNG) |

| Rating Table | Units Sold by Rating |
|----------------|------------|
| ![Rating Table](../screenshots/dashboard-pt5.PNG) | ![Units Sold by Rating](../screenshots/dashboard-pt6.PNG) |

| Numbers of Units Sold by Rating |
|---------------|---------------|
| ![Numbers of Units Sold by Rating](../screenshots/dashboard-pt7.PNG) |

| Category Level 1 | Category Level 2 |
|----------------|------------|
| ![Category Level 1](../screenshots/dashboard-pt8.PNG) | ![Category Level 2](../screenshots/dashboard-pt9.PNG) |


## Key Insights
- High-priced products are concentrated in the Electronics category, indicating that this segment drives the upper range of the product pricing distribution.
- Extreme discounts can significantly impact potential revenue, as seen in a product with a 91% discount leading to an estimated $91,000 revenue reduction.
- Sales volume peaks when discounts range between 50% and 60%, suggesting an optimal discount window for maximizing customer purchases.
- Products with ratings between 4.0 and 4.4 show higher purchase frequency, indicating that moderately high ratings are sufficient to drive demand.
- Categories with higher rating counts tend to generate more sales, highlighting the importance of customer engagement and review volume.


