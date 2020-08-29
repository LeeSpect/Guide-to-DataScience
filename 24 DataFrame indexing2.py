import pandas as pd

iphone_df = pd.read_csv('data/iphone.csv', index_col=0)
iphone_df
# --------------------------------------------------------------------------------------------------------------
#	출시일	디스플레이	메모리	출시 버전	Face ID
#iPhone 7	2016-09-16	4.7	2GB	iOS 10.0	No
#iPhone 7 Plus	2016-09-16	5.5	3GB	iOS 10.0	No
#iPhone 8	2017-09-22	4.7	2GB	iOS 11.0	No
#iPhone 8 Plus	2017-09-22	5.5	3GB	iOS 11.0	No
#iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes
#iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes
#iPhone XS Max	2018-09-21	6.5	4GB	iOS 12.0	Yes
# --------------------------------------------------------------------------------------------------------------
iphone_df.loc['iPhone X']
# --------------------------------------------------------------------------------------------------------------
#출시일        2017-11-03
#디스플레이             5.8
#메모리               3GB
#출시 버전        iOS 11.1
#Face ID           Yes
#Name: iPhone X, dtype: object
# --------------------------------------------------------------------------------------------------------------
iphone_df.loc[['iPhone X', 'iPhone 8']]
# --------------------------------------------------------------------------------------------------------------
#	출시일	디스플레이	메모리	출시 버전	Face ID
#iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes
#iPhone 8	2017-09-22	4.7	2GB	iOS 11.0	No
# --------------------------------------------------------------------------------------------------------------
type(iphone_df.loc[['iPhone X', 'iPhone 8']])
# --------------------------------------------------------------------------------------------------------------
#pandas.core.frame.DataFrame  # 2차원
# --------------------------------------------------------------------------------------------------------------
iphone_df[['Face ID', '출시일', '메모리']]
# --------------------------------------------------------------------------------------------------------------
#	Face ID	출시일	메모리
#iPhone 7	No	2016-09-16	2GB
#iPhone 7 Plus	No	2016-09-16	3GB
#iPhone 8	No	2017-09-22	2GB
#iPhone 8 Plus	No	2017-09-22	3GB
#iPhone X	Yes	2017-11-03	3GB
#iPhone XS	Yes	2018-09-21	4GB
#iPhone XS Max	Yes	2018-09-21	4GB
# --------------------------------------------------------------------------------------------------------------
# 슬라이싱
iphone_df.loc['iPhone 8':'iPhone XS']
# --------------------------------------------------------------------------------------------------------------
#출시일	디스플레이	메모리	출시 버전	Face ID
#iPhone 8	2017-09-22	4.7	2GB	iOS 11.0	No
#iPhone 8 Plus	2017-09-22	5.5	3GB	iOS 11.0	No
#iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes
#iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes
# --------------------------------------------------------------------------------------------------------------
iphone_df.loc[:'iPhone XS']
# --------------------------------------------------------------------------------------------------------------
#출시일	디스플레이	메모리	출시 버전	Face ID
#iPhone 7	2016-09-16	4.7	2GB	iOS 10.0	No
#iPhone 7 Plus	2016-09-16	5.5	3GB	iOS 10.0	No
#iPhone 8	2017-09-22	4.7	2GB	iOS 11.0	No
#iPhone 8 Plus	2017-09-22	5.5	3GB	iOS 11.0	No
#iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes
#iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes
# --------------------------------------------------------------------------------------------------------------
iphone_df['메모리':'Face ID']  # column은 복잡하게 슬래싱해야함
# --------------------------------------------------------------------------------------------------------------
#출시일	디스플레이	메모리	출시 버전	Face ID  # 슬라이싱 내용이 이상하게 출력됨
# --------------------------------------------------------------------------------------------------------------
iphone_df.loc[:, '메모리':'Face ID']  # 모든 row에 대해서 메모리부터 Face ID 값을 받아 오는 것.
# --------------------------------------------------------------------------------------------------------------
#	메모리	출시 버전	Face ID
#iPhone 7	2GB	iOS 10.0	No
#iPhone 7 Plus	3GB	iOS 10.0	No
#iPhone 8	2GB	iOS 11.0	No
#iPhone 8 Plus	3GB	iOS 11.0	No
#iPhone X	3GB	iOS 11.1	Yes
#iPhone XS	4GB	iOS 12.0	Yes
#iPhone XS Max	4GB	iOS 12.0	Yes
# --------------------------------------------------------------------------------------------------------------
iphone_df.loc['iPhone 7':'iPhone X', '메모리':'Face ID']
# --------------------------------------------------------------------------------------------------------------
#	메모리	출시 버전	Face ID
#iPhone 7	2GB	iOS 10.0	No
#iPhone 7 Plus	3GB	iOS 10.0	No
#iPhone 8	2GB	iOS 11.0	No
#iPhone 8 Plus	3GB	iOS 11.0	No
#iPhone X	3GB	iOS 11.1	Yes
