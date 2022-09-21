from this import d
import pandas as pd
df=pd.read_csv('scooter.csv')


#print(df.columns)
#print(df.dtypes)

#pd.set_option('display.max_columns', 500)
#print (df.head(10))

#print(df["DURATION"])

#print (df[['trip_id','DURATION','start_location_name']])

#print(df.loc[34221])

#print (df.at[2,'DURATION'])

#user=df.where(df['user_id']==8417864)
#print(user)

#print (df[(df['user_id']==8417864)])

#one=df['user_id']==8417864
#two=df['trip_ledger_id']==1488838
#print (df[(one & two)])

#print (df.describe())

#print(df['start_location_name'].describe())

#print(df['DURATION'].value_counts())

#print(df['DURATION'].value_counts(normalize=True))

#print(df['end_location_name'].value_counts(dropna=False))

#print(df.isnull().sum())

#print(df['trip_id'].value_counts(bins=10))

#print(df['start_location_name'][(df['start_location_name'].isnull())])

#df.dropna(subset=['start_location_name'],inplace=True)

#print(df['start_location_name'][(df['start_location_name'].isnull())])

#print(df.fillna(value='00:00:00',axis='columns'))

#startstop=df[(df['start_location_name'].isnull())&(df['end_location_name'].isnull())]
#value={'start_location_name':'Start St.','end_location_name':'Stop St.'}
#startstop.fillna(value=value)
#print((startstop[['start_location_name','end_location_name']]).fillna(value=value))

may=df[(df['month']=='May')]
print(may)
#df.drop(index=may.index,inplace=True)
#print(df['month'].value_counts())

#df.columns=[x.lower() for x in df.columns]
#print(df.columns)

#df.columns=[x.upper() for x in df.columns] 
#print(df.columns)

#df.rename(columns={'DURATION':'duration','region_id':'region'},inplace=True)
#print(df.columns)

#df['month']=df['month'].str.upper()
#print (df['month'].head())

for i,r in df.head().iterrows():
    if r['trip_id']==1613335:
        df.at[i,'new_column']='Yes'
    else:
        df.at[i,'new_column']='No'
print(df[['trip_id','new_column']].head())

df.loc[df['trip_id']==1613335,'new_column']='1613335'
print(df[['trip_id','new_column']].head())

print(df[['trip_id','started_at']].head())

df[['trip_id','started_at']].head()

print(df['started_at'].str.split())

new=df['started_at'].str.split(expand=True).head()
print(new)

when = '2019-05-23'
x=df[(df['started_at']>when)]
print(len(x))
df['started_at']=pd.to_datetime(df['started_at'],format='%m/%d/%Y %H:%M')

when = '2019-05-23'
print(df[(df['started_at']>when)])




