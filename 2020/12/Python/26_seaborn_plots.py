#exploring plots in the seaborn library
import seaborn as sns

#for plotting the graphs in the notebook iteself
%matplotlib inline

#tips is a dataset in seaborn
tips = sns.load_dataset('tips')

#printing the top 5 enteries to know the columns and rows structure
print(tips.head())

#NOTE, all the plots were executed in the different cell in the jupyter notebook
#1 distplot() plots histogram, kde False will not draw the curve derived from rugplot
sns.distplot(tips['total_bill'],kde=False, bins= 40)
print('\n\n')

#2 jointplot() takes 3 arguments: first column, second column, and dataset
sns.jointplot(x = 'total_bill' ,y = 'tip' , data = tips)
print('\n\n')

#scatter is default in jointplot. hex or kde can also be used
sns.jointplot(x = 'total_bill' ,y = 'tip' , data = tips, kind = 'hex') 
print('\n\n')

#3 pairplot() will make all the posible plots for numerical data. hue is used to distinguish data, if possible
sns.pairplot(tips,hue='sex')
print('\n\n')

#4 rugplot() draws a line for each input/entry
sns.rugplot(tips['total_bill'])