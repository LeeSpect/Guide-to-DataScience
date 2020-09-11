import pandas as pd

df = pd.read_csv('Desktop/world_cities.csv')
df
'''
--------------------------------------------------------------------------------------------------------------
	Unnamed: 0	City / Urban area	Country	Population	Land area (in sqKm)
0	0	Buenos Aires	Argentina	11200000	2266
1	1	Melbourne	Australia	3162000	2080
2	2	Sydney	Australia	3502000	1687
3	3	Brisbane	Australia	1508000	1603
4	4	Perth	Australia	1177000	964
...	...	...	...	...	...
244	245	Canton	USA	267000	372
245	246	Spokane	USA	335000	371
246	247	Tashkent	Uzbekistan	2200000	531
247	248	Ho Chi Minh City	Vietnam	4900000	518
248	249	Harare	Zimbabwe	1750000	712
249 rows × 5 columns
--------------------------------------------------------------------------------------------------------------
'''


# 1. 주어진 데이터에는 총 몇 개의 도시와 몇 개의 나라가 있는지 출력하시오.

df['Country'].describe()
'''
--------------------------------------------------------------------------------------------------------------
count     249
unique     61
top       USA
freq      105
Name: Country, dtype: object
--------------------------------------------------------------------------------------------------------------
'''

df['City / Urban area'].value_counts()  # 'City / Urban area' column의 항목들을 볼 수 있습니다.
'''
--------------------------------------------------------------------------------------------------------------
Stockholm                 1
Istanbul                  1
Albuquerque               1
Perth                     1
Bangkok                   1
                         ..
Buenos Aires              1
Belo Horizonte            1
Cairo                     1
Accra                     1
Johannesburg/East Rand    1
Name: City / Urban area, Length: 249, dtype: int64
--------------------------------------------------------------------------------------------------------------
'''
df['City / Urban area'].value_counts().shape  # 총 249개의 도시가 있음을 알 수 있습니다.
'''
--------------------------------------------------------------------------------------------------------------
(249,)
--------------------------------------------------------------------------------------------------------------
'''
df['Country'].value_counts().shape  # 몇 개 나라가 있는지 확인할 수 있습니다.
'''
--------------------------------------------------------------------------------------------------------------
(61,)
--------------------------------------------------------------------------------------------------------------
'''


# 2. 주어진 데이터에서, 인구 밀도(명/sqKm) 가 10000 이 넘는 도시는 총 몇 개인지 출력하시오.
# 인구 밀도는 인구 수 / 땅의 면적 (in sqKm) 로 구할 수 있습니다.

df[df['Population']/df['Land area (in sqKm)']>=10000].info()

#df["Density"] = df["Population"] / df["Land area (in sqKm)"]
#df_high_density = df[df["Density"] > 10000]
#df_high_density .info()
'''
--------------------------------------------------------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
Int64Index: 19 entries, 32 to 129
Data columns (total 5 columns):
 #   Column               Non-Null Count  Dtype 
---  ------               --------------  ----- 
 0   Unnamed: 0           19 non-null     int64 
 1   City / Urban area    19 non-null     object
 2   Country              19 non-null     object
 3   Population           19 non-null     int64 
 4   Land area (in sqKm)  19 non-null     int64 
dtypes: int64(3), object(2)
memory usage: 912.0+ bytes
--------------------------------------------------------------------------------------------------------------
'''


# 3. 인구 밀도가 가장 높은 도시를 출력하시오.

df['Pop/Land'] = df['Population']/df['Land area (in sqKm)']
df.sort_values(by='Pop/Land')
'''
--------------------------------------------------------------------------------------------------------------
	Unnamed: 0	City / Urban area	Country	Population	Land area (in sqKm)	Pop/Land
196	197	Barnstable Town	USA	244000	741	329.284750
220	221	Hickory	USA	188000	546	344.322344
57	57	Pau	France	181000	450	402.222222
223	224	Asheville	USA	222000	536	414.179104
194	195	Chattanooga	USA	344000	751	458.055925
...	...	...	...	...	...	...
34	34	Shenzhen	China	8000000	466	17167.381974
99	99	Lagos	Nigeria	13400000	738	18157.181572
101	101	Karachi	Pakistan	9800000	518	18918.918919
74	74	Kolkata	India	12700000	531	23917.137476
75	75	Mumbai	India	14350000	484	29648.760331
249 rows × 6 columns
--------------------------------------------------------------------------------------------------------------
'''

# 3번 문제 해설
#df["Density"] = df["Population"] / df["Land area (in sqKm)"]  # 인구 밀도를 먼저 계산한 후 Density라는 새로운 column에 삽입합니다.
#density_ranks = df.sort_values(by="Density", ascending = False)  # 인구 밀도를 기준으로 정렬합니다.
#density_ranks['City / Urban area']  # 정렬된 데이터에서 도시 정보만 뽑아서 확인합니다.
'''
--------------------------------------------------------------------------------------------------------------
75                      Mumbai
74                     Kolkata
101                    Karachi
                ...           
57                         Pau
220                    Hickory
196            Barnstable Town
Name: City / Urban area, Length: 249, dtype: object
--------------------------------------------------------------------------------------------------------------
'''
