import pandas as pd

liverpool_df = pd.read_csv('Desktop/liverpool.csv', index_col=0)
liverpool_df
'''
--------------------------------------------------------------------------------------------------------------

position	born	number	nationality
Roberto Firmino	FW	1991	no. 9	Brazil
Sadio Mane	FW	1992	no. 10	Senegal
Mohamed Salah	FW	1992	no. 11	Egypt
Joe Gomez	DF	1997	no. 12	England
Alisson Becker	GK	1992	no. 13	Brazil
--------------------------------------------------------------------------------------------------------------
'''

# 앞글자만 다 대문자로 바꾸고 싶을 때
liverpool_df.rename(columns={'position': 'Position'})  # 정보를 변경한 새로운 내용을 출력
'''
--------------------------------------------------------------------------------------------------------------
	Position	born	number	nationality
Roberto Firmino	FW	1991	no. 9	Brazil
Sadio Mane	FW	1992	no. 10	Senegal
Mohamed Salah	FW	1992	no. 11	Egypt
Joe Gomez	DF	1997	no. 12	England
Alisson Becker	GK	1992	no. 13	Brazil
--------------------------------------------------------------------------------------------------------------
'''

liverpool_df  # 다시 liverpool_df를 출력하면 변경되지 않은 내용이 출력됨
'''
--------------------------------------------------------------------------------------------------------------
	position	born	number	nationality
Roberto Firmino	FW	1991	no. 9	Brazil
Sadio Mane	FW	1992	no. 10	Senegal
Mohamed Salah	FW	1992	no. 11	Egypt
Joe Gomez	DF	1997	no. 12	England
Alisson Becker	GK	1992	no. 13	Brazil
--------------------------------------------------------------------------------------------------------------
'''

liverpool_df.rename(columns={'position': 'Position'}, inplace=True)
liverpool_df  # inplace=True를 적용하면 기존의 내용이 영구적으로 변경되어 사용됨
'''
--------------------------------------------------------------------------------------------------------------
	Position	born	number	nationality
Roberto Firmino	FW	1991	no. 9	Brazil
Sadio Mane	FW	1992	no. 10	Senegal
Mohamed Salah	FW	1992	no. 11	Egypt
Joe Gomez	DF	1997	no. 12	England
Alisson Becker	GK	1992	no. 13	Brazil
--------------------------------------------------------------------------------------------------------------
'''

liverpool_df.rename(columns={'position': 'Position', 'born': 'Born', 'number': 'Number', 'nationality': 'Nationality'}, inplace=True)
liverpool_df  # 여러가지 정보를 변경
'''
--------------------------------------------------------------------------------------------------------------
	Position	Born	Number	Nationality
Roberto Firmino	FW	1991	no. 9	Brazil
Sadio Mane	FW	1992	no. 10	Senegal
Mohamed Salah	FW	1992	no. 11	Egypt
Joe Gomez	DF	1997	no. 12	England
Alisson Becker	GK	1992	no. 13	Brazil
--------------------------------------------------------------------------------------------------------------
'''

# index 이름 변경
liverpool_df.index.name = 'Player Name'
liverpool_df
'''
--------------------------------------------------------------------------------------------------------------

Position	Born	Number	Nationality
Player Name				
Roberto Firmino	FW	1991	no. 9	Brazil
Sadio Mane	FW	1992	no. 10	Senegal
Mohamed Salah	FW	1992	no. 11	Egypt
Joe Gomez	DF	1997	no. 12	England
Alisson Becker	GK	1992	no. 13	Brazil
--------------------------------------------------------------------------------------------------------------
'''

# 기존의 선수 이름을 이전에 새로운 column으로 지정해줘야 함 1
liverpool_df.index
'''
--------------------------------------------------------------------------------------------------------------
Index(['Roberto Firmino', 'Sadio Mane', 'Mohamed Salah', 'Joe Gomez',
       'Alisson Becker'],
      dtype='object', name='Player Name')
--------------------------------------------------------------------------------------------------------------
'''

# 기존의 선수 이름을 이전에 새로운 column으로 지정해줘야 함 2
liverpool_df['Player Name'] = liverpool_df.index
liverpool_df
'''
--------------------------------------------------------------------------------------------------------------
	Position	Born	Number	Nationality	Player Name
Player Name					
Roberto Firmino	FW	1991	no. 9	Brazil	Roberto Firmino
Sadio Mane	FW	1992	no. 10	Senegal	Sadio Mane
Mohamed Salah	FW	1992	no. 11	Egypt	Mohamed Salah
Joe Gomez	DF	1997	no. 12	England	Joe Gomez
Alisson Becker	GK	1992	no. 13	Brazil	Alisson Becker
--------------------------------------------------------------------------------------------------------------
'''

# # 기존의 선수 이름을 이전에 새로운 column으로 지정해줘야 함 2에 이어서 set_index메서드 사용
liverpool_df.set_index('Number')
'''
--------------------------------------------------------------------------------------------------------------
	Position	Born	Nationality	Player Name
Number				
no. 9	FW	1991	Brazil	Roberto Firmino
no. 10	FW	1992	Senegal	Sadio Mane
no. 11	FW	1992	Egypt	Mohamed Salah
no. 12	DF	1997	England	Joe Gomez
no. 13	GK	1992	Brazil	Alisson Becker
--------------------------------------------------------------------------------------------------------------
'''

liverpool_df  # 하지만 다시 liverpool_df를 출력하면 index값이 바뀌지 않은 것이 출력됨
'''
--------------------------------------------------------------------------------------------------------------

Position	Born	Number	Nationality	Player Name
Player Name					
Roberto Firmino	FW	1991	no. 9	Brazil	Roberto Firmino
Sadio Mane	FW	1992	no. 10	Senegal	Sadio Mane
Mohamed Salah	FW	1992	no. 11	Egypt	Mohamed Salah
Joe Gomez	DF	1997	no. 12	England	Joe Gomez
Alisson Becker	GK	1992	no. 13	Brazil	Alisson Becker
--------------------------------------------------------------------------------------------------------------
'''

liverpool_df.set_index('Number', inplace=True)
liverpool_df  # inplace를 잊지 말자
'''
--------------------------------------------------------------------------------------------------------------
	Position	Born	Nationality	Player Name
Number				
no. 9	FW	1991	Brazil	Roberto Firmino
no. 10	FW	1992	Senegal	Sadio Mane
no. 11	FW	1992	Egypt	Mohamed Salah
no. 12	DF	1997	England	Joe Gomez
no. 13	GK	1992	Brazil	Alisson Becker
--------------------------------------------------------------------------------------------------------------
'''
