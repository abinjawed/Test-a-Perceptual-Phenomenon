
#Import the frameworks
import math
import seaborn as sns
import numpy as np
import pandas as pd
from scipy.stats import t as pt
import matplotlib.pyplot as plt
%matplotlib inline

#Take all the data from the csv file and print
data = pd.read_csv("stroopdata.csv")
data

#Find the mean,Median and standard deviation for congruent and incongruent
#Find the mean
c_mean = data['Congruent'].mean()
i_mean = data['Incongruent'].mean()

#Find the median
c_median = data['Congruent'].median()
i_median = data['Incongruent'].median()

#Find the standard deviation
c_std = data['Congruent'].std()
i_std = data['Incongruent'].std()

#print mean,median and standard deviation in a table
ls = [[int(24),int(24)],[c_mean,i_mean],[c_median,i_median],[c_std,i_std]]
detail = pd.DataFrame(ls,index=['Sample Size','Mean','Median','Standard Deviation'],columns=['Congruent','Incongruent'])
detail

#Make a boxplot for both datasets
sns.set_style("whitegrid")
sns.boxplot(data=data[['Congruent', 'Incongruent']], orient="v",width=0.4, palette="colorblind");
plt.ylabel("Time");

#Plot a Graph for congruent dataset
sns.distplot(data['Congruent'])
plt.xlabel("Time");
plt.ylabel("Frequency");
plt.title("Response Time for Congruent Words");


#Plot a Graph for congruent dataset
sns.distplot(data['Incongruent'])
plt.xlabel("Time");
plt.ylabel("Frequency");
plt.title("Response Time for Incongruent Words");


#Compare Both the datasets and make a graph
sns.distplot(data['Congruent'],label = "Congruent")
sns.distplot(data['Incongruent'],label = "Incongruent")
plt.xlabel("Time");
plt.ylabel("Frequency");
plt.title("Response Time For Congruent Vs Incongruent Words");
plt.legend();

#find t-critical value for 95% confidance interval and 23 degree of freedom for two tailed test

print("t-critical value for two tailed test is: ",round(pt.ppf(0.975,23),4))

#find the diffenence of each data
data['difference'] = data['Congruent'] - data['Incongruent']
data

#sd and mean of the differenced dataset
s_std = data['difference'].std()
print("Standard Deviation of the diffenenced dataset: ", round(s_std,4))
s_mean = c_mean - i_mean
print("Mean of Difference: ", round(s_mean,4))

# Calculate the t-value
t_value = s_mean/(s_std/math.sqrt(24))
print("t-Value is: ",t_value)

