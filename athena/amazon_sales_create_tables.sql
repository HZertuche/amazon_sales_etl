-- Read the first 50 rows of the file
SELECT * 
FROM "amazon_sales"."outputv2"
limit 50;

-- Total numbers of units by category 1
SELECT category_lvl1,
count(*) AS number_units
FROM "amazon_sales"."outputv2"
group by category_lvl1 ;

-- Show all the results where the discounted price is below 300
SELECT * 
FROM "amazon_sales"."outputv2"
where discounted_price < 300;

-- Show only the selected columns where the discounted price is below 300 and the rating is greater than or equal to four. 
-- Ordered by rating.
SELECT product_name, discounted_price, actual_price, rating
FROM "amazon_sales"."outputv2"
where discounted_price < 300
AND rating >= 4
order by rating ;

-- Show the average rating and number of units sold by category
SELECT category_lvl1, 
count(*) as number_units,
avg(rating) as avg_rating
FROM "amazon_sales"."outputv2"
group by category_lvl1
order by number_units desc;