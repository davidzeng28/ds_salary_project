# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 15:31:06 2023

@author: David Zeng
"""

import pandas as pd

## Read the scrap data
df = pd.read_csv('glassdoor_jobs.csv')

## clean the salary estimate column
### Remove Salary Estimate equal -1 because that is lack of salary info when we scrapped the data
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df = df[df['Salary Estimate'] != '-1']
df['Salary Estimate'] = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = df['Salary Estimate'].apply(lambda x:x.replace('K','').replace('$',''))

min_hr = minus_kd.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:',''))
df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['max_salary'].dtype
df['avg_salary'] = (df.min_salary + df.max_salary)/2

## clean the company name column
df['company_txt'] =df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis=1)

## State field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1])
df.job_state.value_counts()

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis =1)
## Age of company
df['age'] =df.Founded.apply(lambda x: x if x < 1 else 2023 - x)

## parsing of the description(python, etc.)

#python
df['python_yn'] =df['Job Description'].apply(lambda x: 1 if "python" in x.lower() else 0)
df['python_yn'].value_counts()

# r studio
df['R_yn'] =df['Job Description'].apply(lambda x: 1 if "r studio" in x.lower() or 'r-studio' in x.lower() else 0)
df['R_yn'].value_counts()

#spark
df['spark'] =df['Job Description'].apply(lambda x: 1 if "spark" in x.lower() else 0)
df['spark'].value_counts()
#aws 
df['aws'] =df['Job Description'].apply(lambda x: 1 if "aws" in x.lower() else 0)
df['aws'].value_counts()
#excel
df['excel'] =df['Job Description'].apply(lambda x: 1 if "excel" in x.lower() else 0)
df['excel'].value_counts()


## drop the first column
df = df.drop('Unnamed: 0', axis =1)

## export to csv
df.to_csv('salary_data_cleaned.csv', index = False)


