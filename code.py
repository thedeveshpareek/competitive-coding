import requests
import json
import csv
import pandas as pd
import time
# currenttime as epoch
currenttime = int(time.time())
url= "https://api.viotel.co/sensors/"

# currenttime 
currenttime= int(time.strftime("%H"))*60*60 + int(time.strftime("%M"))*60 + int(time.strftime("%S"))

payload = json.dumps({
    "sensors": "viot00203-1",
    "epochmin": 1633305500,
    "epochmax": 1633410000

    # "epochmin": currenttime-60*60*60,
    # "epochmax": currenttime
})

headers = {
    'Content-Type': 'application/json',
    'Content-Length':'',
    'x-Api-Key': 'Jl4I88ilnQ5ZIz4ll9JzdrarvUyiAKK8v7F5NbF8'
}

# make empty dataframe
df = pd.DataFrame()
response = requests.request("GET", url, headers=headers, data=payload)


data=json.loads(response.text)
body_data=data['body']
sensordata=json.loads(body_data)
for i in sensordata['sensordata']:
    df = df.append(i, ignore_index=True)

df = df.drop(['location1', 'measure_name', 'name','type'], axis=1)


date=[i.split(' ')[0] for i in df['time']]
# change formet of date of dd/mm/yyyy
date=[i.split('-')[2]+'/'+i.split('-')[1]+'/'+i.split('-')[0] for i in date]
time=[i.split(' ')[1] for i in df['time']]
time=[i[:-10] for i in time]

df['time']=[i+' '+j for i,j in zip(date,time)]
df = df.rename(columns={'time':'date/time','DisplayName':'name','measure_value::double':'measuredouble'})
cols=['date/time','name','measuredouble']
df=df[cols]
df['measuredouble1']=''
df['measuredouble2']=''
df['measuredouble1']=df['measuredouble']
df['measuredouble2']=df['measuredouble']
# make type int of measuredouble, measuredouble1, measuredouble2
df['measuredouble']=df['measuredouble'].astype(float)
df['measuredouble1']=df['measuredouble1'].astype(float)
df['measuredouble2']=df['measuredouble2'].astype(float)
k=len(df)
for i in range(0,k,3):
    df['measuredouble'][1+i]=0
    df['measuredouble'][2+i]=0
    df['measuredouble1'][i]=0
    df['measuredouble2'][i]=0
    df['measuredouble1'][i+2]=0
    df['measuredouble2'][1+i]=0

    df['measuredouble'][i]=df['measuredouble'][i]+df['measuredouble'][i+1]+df['measuredouble'][i+2]
    df['measuredouble1'][i]=df['measuredouble1'][i]+df['measuredouble1'][i+1]+df['measuredouble1'][i+2]
    df['measuredouble2'][i]=df['measuredouble2'][i]+df['measuredouble2'][i+1]+df['measuredouble2'][i+2]

df2=pd.DataFrame()
for i in range(0,k,3):
    df2=df2.append(df.iloc[i])

for i in df2:
    a=i[measuredouble]
    b=i[measuredouble1]
    c=i[measuredouble2]
    if a>b and a>c:
        df2[measuredouble][i]=a
        if b>c:
            df2[measuredouble1]=b
            df2[measuredouble2]=c
        else:
            df2[measuredouble1]=c
            df2[measuredouble2]=a
    elif b>a and b>c:
        df2[measuredouble][i]=b
        if a>c:
            df2[measuredouble1]=a
            df2[measuredouble2]=c
        else:
            df2[measuredouble1]=c
            df2[measuredouble2]=a
    else:
        df2[measuredouble][i]=c
        if a>b:
            df2[measuredouble1]=a
            df2[measuredouble2]=b
        else:
            df2[measuredouble1]=b
            df2[measuredouble2]=a
            
# make csv file
# df2.to_csv('data.csv', index=False)
# print(df2)
