# ** Import pandas as pd.**

import pandas as pd

# ** Read Salaries.csv as a dataframe called sal.**

sal = pd.read_csv('Salaries.csv')

# ** Check the head of the DataFrame. **

sal.head()

# ** Use the .info() method to find out how many entries there are.**

sal.info()

# **What is the average BasePay ?**

sal['BasePay'].mean()

# ** What is the highest amount of OvertimePay in the dataset ? **

sal['OvertimePay'].max()

# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']

# ** How much does JOSEPH DRISCOLL make (including benefits)? **

sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']

# ** What is the name of highest paid person (including benefits)?**

sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName']

# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

sal.iloc[sal['TotalPayBenefits'].argmin()]

# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

sal.groupby('Year').mean()['BasePay']

# ** How many unique job titles are there? **

sal['JobTitle'].nunique()

# ** What are the top 5 most common jobs? **

sal['JobTitle'].value_counts().head(5)

# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)

# ** How many people have the word Chief in their job title? (This is pretty tricky) **

def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False

sum(sal['JobTitle'].apply(lambda x: chief_string(x)))

# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

sal['title_len'] = sal['JobTitle'].apply(len)

sal[['TotalPayBenefits','title_len']].corr()
