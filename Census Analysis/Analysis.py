# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

census = np.concatenate((data,new_record))
print(data.shape,census.shape)

#Finding mean age

age = census[:,0]
max_age = max(age)
min_age = min(age)
age_mean = np.mean(age)
age_std = np.std(age)
print(age_mean)

#Finding the minority race

race = census[:,2]
race_0, race_1, race_2, race_3, race_4 = [],[],[],[],[] 
for i in race:
    if i == 0:
        race_0.append(i)
    elif i == 1:
        race_1.append(i)
    elif i == 2:
        race_2.append(i)
    elif i==3:
        race_3.append(i)
    else:
        race_4.append(i)
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
races = [len_0,len_1,len_2,len_3,len_4]
min_race = min(races)
minority_race = races.index(min_race)
print(minority_race)

#Finding the average working hours of senior citizens per week

senior_citizens = census[(age>60)]
working_hours_sum = np.sum(senior_citizens[:,6])
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum / senior_citizens_len
print(("%.2f") %(avg_working_hours))

#Finding the average pay of highly educated and lowly educated people

education = census[:,1]
high = census[(education > 10)]
low = census[(education <= 10)]
avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])
print(("%.2f") %(avg_pay_high))
print(("%.2f") %(avg_pay_low))
