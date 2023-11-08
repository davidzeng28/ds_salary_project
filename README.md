# Data Science Salary Estimator: Project Overview<br>
- Scraped over 1000 job descriptions from glassdoor using python and selenium <br>
- Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.<br>
- Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model.<br>
- Built a client facing API using flask <br>
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
