# ## The Data
# We will be working with a famous titanic data set for these exercises. Later on in the Machine Learning section of the course, we will revisit this data, and use it to predict survival rates of passengers. For now, we'll just focus on the visualization of the data with seaborn:

import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

sns.set_style('whitegrid')

titanic = sns.load_dataset('titanic')

titanic.head()

# # Exercises
# ** Recreate the plots below using the titanic dataframe. There are very few hints since most of the plots can be done with just one or two lines of code and a hint would basically give away the solution. Keep careful attention to the x and y labels for hints.**

sns.jointplot(x='fare',y='age',data=titanic)

sns.displot(titanic['fare'], kde=False, color='red', bins=30)

sns.boxplot(x='class',y='age',data=titanic,palette='rainbow')

sns.swarmplot(x='class',y='age',data=titanic,palette='Set2')

sns.countplot(x='sex',data=titanic)

sns.heatmap(titanic.corr(),cmap='coolwarm')
plt.title('titanic.corr()')

g = sns.FacetGrid(data=titanic,col='sex')
g.map(plt.hist,'age')
