import pandas as pd  
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

covid_df = pd.read_csv('covid_clean.csv') 
employment_df = pd.read_csv('employment_clean.csv')

employment_df = employment_df.head(14)

employment_df['Case/Day'] = covid_df['Case/Day'] 

x = employment_df['Employed'] 
y = employment_df['Case/Day']
pearson_correlation = stats.pearsonr(x,y)
#scatter plot
employment_df.plot(kind='scatter', x='Employed', y='Case/Day', figsize=(10,7))
plt.title("Number of persons employed ('000 units) vs New Cases per month in Victoria")  
plt.grid(True)
ax = sns.regplot(x=x, y=y)
ax.set(xlabel="Number of persons employed ('000units)", ylabel = "Case/Day")
ax.xaxis.label.set_color('green')
ax.yaxis.label.set_color('blue')
for i, date in enumerate(employment_df['Month/Year']):
    ax.annotate(date, (x[i], y[i]))
    

plt.savefig('scatterplot.png')
print("The pearson correlation coefficient and it's two-tailed p-value is:")
print(pearson_correlation)





