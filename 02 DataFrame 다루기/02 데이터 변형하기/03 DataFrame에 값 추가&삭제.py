import pandas as pd

iphone_df = pd.read_csv('Desktop/iphone.csv', index_col=0)

iphone_df.loc['iPhone XR'] = ['2018-10-26', 6.1, '3GB', 'iOS 12.0.1', 'Yes']
iphone_df  # 새로운 값 추가 = 빈 row에 새로운 정보 저장
'''
--------------------------------------------------------------------------------------------------------------
	출시일	디스플레이	메모리	출시 버전	Face ID
iPhone 7	2016-09-16	4.7	2GB	iOS 10.0	No
iPhone 7 Plus	2016-09-16	5.5	3GB	iOS 10.0	No
iPhone 8	2017-09-22	4.7	2GB	iOS 11.0	No
iPhone 8 Plus	2017-09-22	5.5	3GB	iOS 11.0	No
iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes
iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes
iPhone XS Max	2018-09-21	6.5	4GB	iOS 12.0	Yes
iPhone XR	2018-10-26	6.1	3GB	iOS 12.0.1	Yes
--------------------------------------------------------------------------------------------------------------
'''

iphone_df['제조사'] = 'Apple'
iphone_df  # 새로운 column에 새로운 값 저장
'''
--------------------------------------------------------------------------------------------------------------
	출시일	디스플레이	메모리	출시 버전	Face ID	제조사
iPhone 7	2016-09-16	4.7	2GB	iOS 10.0	No	Apple
iPhone 7 Plus	2016-09-16	5.5	3GB	iOS 10.0	No	Apple
iPhone 8	2017-09-22	4.7	2GB	iOS 11.0	No	Apple
iPhone 8 Plus	2017-09-22	5.5	3GB	iOS 11.0	No	Apple
iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes	Apple
iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes	Apple
iPhone XS Max	2018-09-21	6.5	4GB	iOS 12.0	Yes	Apple
iPhone XR	2018-10-26	6.1	3GB	iOS 12.0.1	Yes	Apple
--------------------------------------------------------------------------------------------------------------
'''

iphone_df.drop('iPhone XR', axis='index', inplace=True)
# iPhone XR 행(row/index)을 지우기 위해 axis= 'index'라고 지정
# inplace가 False라면 변경된 내용이 iphone_df에는 저장되지 않음.
iphone_df # inplace=False라면 iphone_df를 입력하지 않아도 바로 위 단계에서 iphoneXR이 삭제된 정보가 출력됨
'''
--------------------------------------------------------------------------------------------------------------
	출시일	디스플레이	메모리	출시 버전	Face ID	제조사
iPhone 7	2016-09-16	4.7	2GB	iOS 10.0	No	Apple
iPhone 7 Plus	2016-09-16	5.5	3GB	iOS 10.0	No	Apple
iPhone 8	2017-09-22	4.7	2GB	iOS 11.0	No	Apple
iPhone 8 Plus	2017-09-22	5.5	3GB	iOS 11.0	No	Apple
iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes	Apple
iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes	Apple
iPhone XS Max	2018-09-21	6.5	4GB	iOS 12.0	Yes	Apple
--------------------------------------------------------------------------------------------------------------
'''

iphone_df.drop('제조사', axis='columns', inplace=True)
iphone_df  # 제조사 column 삭제
'''
--------------------------------------------------------------------------------------------------------------

출시일	디스플레이	메모리	출시 버전	Face ID
iPhone 7	2016-09-16	4.7	2GB	iOS 10.0	No
iPhone 7 Plus	2016-09-16	5.5	3GB	iOS 10.0	No
iPhone 8	2017-09-22	4.7	2GB	iOS 11.0	No
iPhone 8 Plus	2017-09-22	5.5	3GB	iOS 11.0	No
iPhone X	2017-11-03	5.8	3GB	iOS 11.1	Yes
iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes
iPhone XS Max	2018-09-21	6.5	4GB	iOS 12.0	Yes
--------------------------------------------------------------------------------------------------------------
'''

iphone_df.drop(['iPhone 7', 'iPhone 8', 'iPhone X'], axis='index', inplace=True)
iphone_df  # 여러 줄 한꺼번에 삭제
'''
--------------------------------------------------------------------------------------------------------------
	출시일	디스플레이	메모리	출시 버전	Face ID
iPhone 7 Plus	2016-09-16	5.5	3GB	iOS 10.0	No
iPhone 8 Plus	2017-09-22	5.5	3GB	iOS 11.0	No
iPhone XS	2018-09-21	5.8	4GB	iOS 12.0	Yes
iPhone XS Max	2018-09-21	6.5	4GB	iOS 12.0	Yes
--------------------------------------------------------------------------------------------------------------
'''
