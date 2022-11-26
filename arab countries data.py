import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.style.use('ggplot')
data = pd.read_csv(r'C:\Users\mhbk8\Downloads\kaggle_survey_2021_responses.csv\kaggle_survey_2021_responses.csv')
questions = data.iloc[0]
data.drop(0,inplace=True)
for col in data.columns:
    if data[col].str.isnumeric().all() :
        data[col] = pd.to_numeric(data[col])
countries = data['Q3'].unique() 
counte ='Algeria,Bahrain,the Comoros Islands,Djibouti,Egypt,Iraq,Jordan,Kuwait,Lebanon,Libya,Morocco,Mauritania,Oman,Palestine,Qatar,Saudi Arabia,Somalia,Sudan,Syria,Tunisia,United Arab Emirates,Yemen'      
arab_count = counte.split(',')
arab = data[data['Q3'].isin(arab_count)]
# freq = arab['Q1'].value_counts().sort_index()
# plt.plot(arab['Q1'].unique(),freq)
# plt.xlabel('Age Group')
# plt.ylabel('Frequency')
# plt.title('Age Distribution')
# group_country = arab['Q3'].value_counts()

# plt.bar(group_country.index,group_country.values)
# plt.xlabel('Country')
# plt.ylabel('Frequency')
# plt.title('Country Distribution')
# plt.tight_layout()
# plt.xticks(rotation = 45)
q7 = arab.columns[arab.columns.str.contains('^Q7')]
dict_7 = dict()
for col in arab[q7] :
    key = arab[q7].value_counts().index[0]
    dict_7[key] = arab[col].value_counts()[0]
print(pd.Series(dict_7))
plt.show()

