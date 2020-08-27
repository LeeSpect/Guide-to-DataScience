import pandas as pd

iphone_df = pd.read_csv('Desktop/iphone.csv', index_col=0)
iphone_df

#출시일	디스플레이	메모리	출시 버전	Face ID
#iPhone 7	2016-09-16	4.7	2GB	iOS 10.0	No
#iPhone 7 Plus	2016-09-16	5.5	3GB	iOS 10.0	No
#iPhone 8	2017-09-22	4.7	2GB	iOS 11.0	No
#iPhone 8 Plus	2017-09-22	5.5	3GB	iOS 11.0	No
#iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes
#iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes
#iPhone XS Max	2018-09-21	6.5	4GB	iOS 12.0	Yes

iphone_df.loc['iPhone 8', '메모리']  # DataFrame에서 딱 1개의 값을 가져온다.
#'2GB'

iphone_df.loc['iPhone X', :]  # :은 'iPhone'에 해당하는 내용을 전부 다 가져오라는 명령
#출시일        2017-11-03
#디스플레이             5.8
#메모리               3GB
#출시 버전        iOS 11.1
#Face ID           Yes
#Name: iPhone X, dtype: object

iphone_df.loc['iPhone X']  # :부분을 빈칸으로 두어도 모든 내용이 출력됨
#출시일        2017-11-03
#디스플레이             5.8
#메모리               3GB
#출시 버전        iOS 11.1
#Face ID           Yes
#Name: iPhone X, dtype: object

type(iphone_df.loc['iPhone X'])  
#pandas.core.series.Series  # series는 pandas의 1차원 자료형. 1줄을 받아왔으니 1차원 자료형을 출력

iphone_df.loc[:, '출시일']
#iPhone 7         2016-09-16
#iPhone 7 Plus    2016-09-16
#iPhone 8         2017-09-22
#iPhone 8 Plus    2017-09-22
#iPhone X         2017-11-03
#iPhone XS        2018-09-21
#iPhone XS Max    2018-09-21
#Name: 출시일, dtype: object

iphone_df['출시일']  # 모든 행에 대한 한 열의 정보는 loc 없이도 출력 가능
#iPhone 7         2016-09-16
#iPhone 7 Plus    2016-09-16
#iPhone 8         2017-09-22
#iPhone 8 Plus    2017-09-22
#iPhone X         2017-11-03
#iPhone XS        2018-09-21
#iPhone XS Max    2018-09-21
#Name: 출시일, dtype: object
