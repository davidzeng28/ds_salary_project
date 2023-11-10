# Data Science Salary Estimator: Project Overview<br>
- Scraped over 1000 job descriptions from glassdoor using python and selenium <br>
- Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.<br>
- Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.<br>
- Built a client facing API using flask <be>
## Code and resources references <br>
- Packages: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
- Scraper Github: https://github.com/arapfaik/scraping-glassdoor-selenium

# Web scrapping
### Tweaked the web scraper github repo (above) to scrape 1000 job postings from glassdoor.com. With each job, we got the following:<br>
    * Job title<br>
    * Salary Estimate<br>
    * Job Description<br>
    * Rating<br>
    * Company<br>
    * Location<br>
    * Company Headquarters<br>
    * Company Size<br>
    * Company Founded Date<br>
    * Type of Ownership<br>
    * Industry<br>
    * Sector<br>
    * Revenue<br>
    * Competitors<br>
## Data Cleaning <br>
- After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables: <br>

 * Parsed numeric data out of salary <br>
 * Made columns for employer provided salary and hourly wages<br>
 * Removed rows without salary<br>
 * Parsed rating out of company text<br>
 * Made a new column for company state<br>
 * Added a column for if the job was at the company’s headquarters<br>
 * Transformed founded date into age of company<br>
 * Made columns for if different skills were listed in the job description:<br>
         1. Python<br>
         2. R<br>
         3. Excel<br>
         3. AWS<br>
         4. Spark<br>
 * Column for simplified job title and Seniority<br>
 * Column for description length<br>

## EDA <br>
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables. <br>
![correlation_visual](https://github.com/davidzeng28/ds_salary_project/blob/master/correlation_visual.png)
![positions_by_state](https://github.com/davidzeng28/ds_salary_project/blob/master/positions_by_state.png)
![salary_by_job_title](https://github.com/davidzeng28/ds_salary_project/blob/master/salary_by_job_title.png)

## Model building <br>
First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%. <br>

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.<br>
I tried three different models: <br>
   1. Multiple Linear Regression – Baseline for the model <br>
   2. Lasso Regression – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective. <br>
   3. Random Forest – Again, with the sparsity associated with the data, I thought that this would be a good fit. <br>
   
