#exploring matrix plots
import seaborn as sns

#loading flights dataset from seaborn library
flights = sns.load_dataset('flights')

#before working on matrix plots, prerequisite is to convert the table in matrix form
#two ways are there: dataset_name.corr() and dataset_name.pivot_table(index=,columns=,values=)
fp = flights.pivot_table(index='month',columns = 'year',values='passengers')

#1 heatmap() takes minimum 1 parameter: matrix table
#other aspects are just to make it more presentable/readable
sns.heatmap(fp,cmap = 'magma',linecolor = 'white',linewidths=2)
print('\n\n')

#2 clustermap() takes minimum 1 parameter: matrix table
#other aspects are just to make it more presentable/readable
#it clusters similar characteristics in a hierarchical format(like a tree)
sns.clustermap(fp,cmap='coolwarm',standard_scale=1)