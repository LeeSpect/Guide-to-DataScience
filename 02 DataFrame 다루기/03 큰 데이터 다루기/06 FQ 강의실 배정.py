# 아래 조건에 따라 강의실 종류를 지정해 주세요.
# 1. 80명 이상의 학생이 수강하는 과목은 “Auditorium”에서 진행됩니다.
# 2. 40명 이상, 80명 미만의 학생이 수강하는 과목은 “Large room”에서 진행됩니다.
# 3. 15명 이상, 40명 미만의 학생이 수강하는 과목은 “Medium room”에서 진행됩니다.
# 4. 5명 이상, 15명 미만의 학생이 수강하는 과목은 “Small room”에서 진행됩니다.
# 5. 폐강 등의 이유로 status가 “not allowed”인 수강생은 room assignment 또한 “not assigned”가 되어야 합니다.

import pandas as pd

df = pd.read_csv('data/enrolment_2.csv')

df['room assignment'] = 'not assigned'
assigned = (df['room assignment'] == 'not assigned') & (df['status'] == 'allowed')

for course in df['course name'].unique():
    size = df['course name'].value_counts()
    if size[course] >= 80:
        df.loc[(df['course name'] == course) & assigned, 'room assignment'] = 'Auditorium'
    elif size[course] >= 40:
        df.loc[(df['course name'] == course) & assigned, 'room assignment'] = 'Large room'
    elif size[course] >= 15:
        df.loc[(df['course name'] == course) & assigned, 'room assignment'] = 'Medium room'
    elif size[course] >= 5:
        df.loc[(df['course name'] == course) & assigned, 'room assignment'] = 'Small room'

df


'''
--------------------------------------------------------------------------------------------------------------
import pandas as pd

df = pd.read_csv('data/enrolment_2.csv')

# 과목별 인원 가져오기
allowed = df["status"] == "allowed"
course_counts = df.loc[allowed, "course name"].value_counts()

# 각 강의실 규모에 해당되는 과목 리스트 만들기
auditorium_list = list(course_counts[course_counts >= 80].index)
large_room_list = list(course_counts[(80 > course_counts) & (course_counts >= 40)].index)
medium_room_list = list(course_counts[(40 > course_counts) & (course_counts >= 15)].index)
small_room_list = list(course_counts[(15 > course_counts) & (course_counts > 4)].index)

# not allowed 과목에 대해 값 지정해주기
not_allowed = df["status"] == "not allowed"
df.loc[not_allowed, "room assignment"] = "not assigned"

# allowed 과목에 대해 값 지정해주기
for course in auditorium_list:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Auditorium"

for course in large_room_list:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Large room"
    
for course in medium_room_list:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Medium room"
    
for course in small_room_list:
    df.loc[(df["course name"] == course) & allowed, "room assignment"] = "Small room"
    
# 정답 출력
df
--------------------------------------------------------------------------------------------------------------
'''
