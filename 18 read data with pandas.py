import pandas as pd

iphone_df = pd.read_csv('Desktop/iphone.csv', index_col=0) 
# header의 값은 csv의 첫 행으로 자동 지정됨
# iphone_df = pd.read_csv('Desktop/iphone.csv', header=None)  # header=None을 추가하면 헤더를 자동으로 추가하지 않음
# index/row의 값은 0, 1, 2, 3, 4... 로 자동 지정됨
# index_col=0은 0번 째 열(col)의 값을 index/row 이름으로 설정함

iphone_df

#                    출시일	디스플레이	메모리	출시 버전	Face ID
#iPhone 7	      2016-09-16	       4.7	  2GB	 iOS 10.0	     No
#iPhone 7 Plus  2016-09-16	       5.5	  3GB	 iOS 10.0	     No
#iPhone 8	      2017-09-22	       4.7	  2GB	 iOS 11.0	     No
#iPhone 8 Plus  2017-09-22	       5.5	  3GB	 iOS 11.0	     No
#iPhone X	      2017-11-03	       5.8	  3GB	 iOS 11.1	    Yes
#iPhone XS	    2018-09-21	       5.8	  4GB	 iOS 12.0	    Yes
#iPhone XS Max  2018-09-21	       6.5	  4GB	 iOS 12.0     Yes
