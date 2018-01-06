import pandas as pd

data = pd.read_csv("~/Desktop/attendance.csv", header=0)

years = list(range(1998, 2016))

for i in years:
    attstr = str(i) + "_attend"
    data_temp = data[['team', attstr]]
    data_temp['year'] = i
    data_temp.columns = ['team', 'year', 'attendance']
    data_temp = data_temp[['team', 'year', 'attendance']]
    if i==1998:
        newdata = data_temp
    else:
        newdata = newdata.append(data_temp)

newdata = newdata.sort_values(by=['team','year'])

newdata.to_csv("newdata.csv")
