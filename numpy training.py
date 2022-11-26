import numpy as np
import pandas as pd
person = pd.read_csv(r'C:\Users\mhbk8\Downloads\archive(1)\500_Person_Gender_Height_Weight_Index.csv')
data = person.iloc[:,1:].values
#find the number of dimensions & size & shape
# print(data.ndim,data.size,data.shape)
#what is the data type
# print(data.dtype)
# find the target value
target_value = data[:,-1]
# print(target_value)
three_obs =data[::3]
# print(three_obs)
#extract the first and last feature
col1 = data[:,0].reshape(500,1)
col3 = data[:,-1].reshape(500,1)

# f = np.hstack((col1,col3))
# print(f)
reverse = data[::-1]
# print(reverse)
#max and min height
max = np.max(data,axis=0)
min = np.min(data,axis=0)
# print("max height = ",max[0])
# print("min height = ",min[0])
# print("max weight = ",max[1])
# print("min weight = ",min[1])
#mean and std
mean = np.mean(data,axis=0)
std = np.std(data,axis=0)
med = np.median(data,axis=0)
# print("mean of height = ",mean[0])
# print("std of height = ",std[0])
# print("mean of weight = ",mean[1])
# print("std of weight = ",std[1])
# print("median of height = ",med[0])
# print("median of weight = ",med[1])
perc1 = np.percentile(data,25,axis=0)
perc2 = np.percentile(data,75,axis=0)
# print("the percentile  of height for 25th = ",perc1[0])
# print("the percentile  of height for 75th = ",perc2[0])
# print("the percentile  of weight for 25th = ",perc1[1])
# print("the percentile  of weight for 75th = ",perc2[1])
norm = (data-mean)/std
# print("normalizing = ",norm[0:2])
max_ind = np.argmax(data,axis=0)[0]
# print("the tallest person index = ",max_ind)
target_value.reshape(500,1)
print(target_value.reshape(500,1))








