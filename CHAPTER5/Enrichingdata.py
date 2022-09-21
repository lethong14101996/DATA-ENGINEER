import pandas as pd
df=pd.read_csv('scooter.csv')

new=pd.DataFrame(df['start_location_name'].value_counts().head())
print(new)

new.reset_index(inplace=True)
new.columns=['address','count']
print(new)

n=new['address'].str.split(pat=',',n=1,expand=True)
replaced=n[0].str.replace("@","and")
new['street']=n[0]
new['street']=replaced
print(new)

geo=pd.read_csv('geocodedstreet.csv')
print(geo)

joined=new.join(other=geo,how='left',lsuffix='_new',rsuffix='_geo')
print(joined[['street_new','street_geo','x','y']])