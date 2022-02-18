# ** Import numpy and pandas **

import numpy as np
import pandas as pd

# ** Import visualization libraries and set %matplotlib inline. **

import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

# ** Read in the csv file as a dataframe called df **

df = pd.read_csv('911.csv')

# ** Check the info() of the df **

df.info()

# ** Check the head of df **

df.head()

# ** What are the top 5 zipcodes for 911 calls? **

df['zip'].value_counts().head()

# ** What are the top 5 townships (twp) for 911 calls? **

df['twp'].value_counts().head()

# ** Take a look at the 'title' column, how many unique title codes are there? **

df['title'].nunique()

# ## Creating new features

# ** In the titles column there are "Reasons/Departments" specified before the title code. These are EMS, Fire, and Traffic. Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this string value.**

df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])

# ** What is the most common Reason for a 911 call based off of this new column? **

df['Reason'].value_counts().head(1)

# ** Now use seaborn to create a countplot of 911 calls by Reason. **

sns.countplot(x='Reason',data=df,palette='viridis')

# ** Now let us begin to focus on time information. What is the data type of the objects in the timeStamp column? **

type(df['timeStamp'].iloc[0])

# ** You should have seen that these timestamps are still strings. Use [pd.to_datetime](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html) to convert the column from strings to DateTime objects. **

df['timeStamp'] = pd.to_datetime(df['timeStamp'])

# **Now that the timestamp column are actually DateTime objects, use .apply() to create 3 new columns called Hour, Month, and Day of Week. You will create these columns based off of the timeStamp column, reference the solutions if you get stuck on this step.**

df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)

# ** Notice how the Day of Week is an integer 0-6. Use the .map() with this dictionary to map the actual string names to the day of the week: **

dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}

df['Day of Week'] = df['Day of Week'].map(dmap)

df.head()

# ** Now use seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column. **

sns.countplot(x='Day of Week', data=df, hue='Reason', palette='viridis')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

# **Now do the same for Month:**

sns.countplot(x='Month', data=df, hue='Reason', palette='viridis')
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

# **Did you notice something strange about the Plot?**
# ** You should have noticed it was missing some Months, let's see if we can maybe fill in this information by plotting the information in another way, possibly a simple line plot that fills in the missing months, in order to do this, we'll need to do some work with pandas... **

# ** Now create a gropuby object called byMonth, where you group the DataFrame by the month column and use the count() method for aggregation. Use the head() method on this returned DataFrame. **

byMonth = df.groupby('Month').count()

# ** Now create a simple plot off of the dataframe indicating the count of calls per month. **

byMonth['lat'].plot()

# ** Now see if you can use seaborn's lmplot() to create a linear fit on the number of calls per month. Keep in mind you may need to reset the index to a column. **

sns.lmplot(x='Month', y='twp',data=byMonth.reset_index())

# **Create a new column called 'Date' that contains the date from the timeStamp column. You'll need to use apply along with the .date() method. **

df['Date'] = df['timeStamp'].apply(lambda t:t.date())

# ** Now groupby this Date column with the count() aggregate and create a plot of counts of 911 calls.**

df.groupby('Date').count()['lat'].plot()
plt.tight_layout()

# ** Now recreate this plot but create 3 separate plots with each plot representing a Reason for the 911 call**

df[df['Reason']=='Traffic'].groupby('Date').count()['lat'].plot()
plt.title('Traffic')
plt.tight_layout()

df[df['Reason']=='Fire'].groupby('Date').count()['lat'].plot()
plt.title('Fire')
plt.tight_layout()

df[df['Reason']=='EMS'].groupby('Date').count()['lat'].plot()
plt.title('EMS')
plt.tight_layout()

# ** Now let's move on to creating  heatmaps with seaborn and our data. We'll first need to restructure the dataframe so that the columns become the Hours and the Index becomes the Day of the Week. There are lots of ways to do this, but I would recommend trying to combine groupby with an [unstack](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.unstack.html) method. Reference the solutions if you get stuck on this!**

dayHour = df.groupby(by=['Day of Week', 'Hour']).count()['Reason'].unstack()

# ** Now create a HeatMap using this new DataFrame. **

plt.figure(figsize=(12,6))
sns.heatmap(dayHour,cmap="viridis")

# ** Now create a clustermap using this DataFrame. **

sns.clustermap(dayHour,cmap='viridis')

# ** Now repeat these same plots and operations, for a DataFrame that shows the Month as the column. **

dayMonth = df.groupby(by=['Day of Week', 'Month']).count()['Reason'].unstack()

plt.figure(figsize=(12,6))
sns.heatmap(dayMonth,cmap="viridis")

sns.clustermap(dayMonth,cmap='viridis')
