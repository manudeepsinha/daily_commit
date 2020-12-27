#exploring categorical plots in seaborn
import seaborn as sns
import numpy as np

#NOTE: Each set of statements after print('\n\n') were run on different cell in the notebook.
tips = sns.load_dataset('tips')

#barplot() default uses mean as an estimator but with numpy, we can pass other estimator too.
sns.barplot(x='sex',y='total_bill',data=tips, estimator = np.std)
print('\n\n')

#countplot() only takes one categorical argument and simply plots the count on y axis
sns.countplot(x='sex',data=tips)
print('\n\n')

#boxplot() is mostly used to present data to executives due to its understandability and
#variety of information provided
#by passing hue with some categorical parameter, boxplot() can incluce one comparison as well
sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker')
print('\n\n')

#violinplot() is not preferred but can be used to analyze data by our own or to present it to
#fellow data scientists. It can also take hue parameter; with split, it can represent more data.
sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',split=True)
print('\n\n')

#stripplot() is mainly used to analyze data on your own as it represents many aspects of the data
sns.stripplot(x='day',y='total_bill',data=tips)
print('\n\n')

#by using violinplot() and swarmplot() simultaneously, it'll be sumperimposed on each other
#which is helpful in understanding data better than stripplot() and violinplot() individually
sns.violinplot(x='day',y='total_bill',data=tips)
sns.swarmplot(x='day',y='total_bill',data=tips,color='white')
print('\n\n')

#catplot() can be used with kind parameter for common categorical plots
sns.catplot(x='day',y='total_bill',data=tips,kind='bar')
