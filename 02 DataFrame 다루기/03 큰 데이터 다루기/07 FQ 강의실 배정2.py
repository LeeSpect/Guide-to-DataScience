# 아래 세 가지 조건을 만족하도록 코드를 작성하세요.
# 1. 같은 크기의 강의실이 필요한 과목에 대해 알파벳 순서대로 방 번호를 배정하세요.
# 2. 예를 들어 Auditorium이 필요한 과목으로 “arts”, “commerce”, “science” 세 과목이 있다면, “arts”는 “Auditorium-1”, “commerce”는 “Auditorium-2”, “science”는 “Auditorium-3” 순서로 방 배정이 되어야 합니다.
# “status” column이 “not allowed”인 수강생은 “room assignment” column을 그대로 “not assigned”로 남겨둡니다.
# 3. “room assignment” column의 이름을 “room number”로 바꿔주세요.

import pandas as pd

df = pd.read_csv('data/enrolment_3.csv')

auditorium = df['room assignment'] == 'Auditorium'
auditorium_list = list(df.loc[auditorium, 'course name'].unique())
large = df['room assignment'] == 'Large room'
large_list = list(df.loc[large, 'course name'].unique())
medium = df['room assignment'] == 'Medium room'
medium_list = list(df.loc[medium, 'course name'].unique())
small = df['room assignment'] == 'Small room'
small_list = list(df.loc[small, 'course name'].unique())
all_list = [auditorium_list, large_list, medium_list, small_list]
allowed = df['status'] == 'allowed'

for lists in all_list:
    lists = sorted(lists)
    for course in lists:
        if course in auditorium_list:
            df.loc[(df['course name']==course)&allowed, 'room assignment'] = 'Auditorium-'+ str(lists.index(course)+1)
    for course in lists:
        if course in large_list:
            df.loc[(df['course name']==course)&allowed, 'room assignment'] = 'Large-'+ str(lists.index(course)+1)
    for course in lists:
        if course in medium_list:
            df.loc[(df['course name']==course)&allowed, 'room assignment'] = 'Medium-'+ str(lists.index(course)+1)
    for course in lists:
        if course in small_list:
            df.loc[(df['course name']==course)&allowed, 'room assignment'] = 'Small-'+ str(lists.index(course)+1)
df.rename(columns ={'room assignment':'room number'}, inplace=True)
df

'''
---------------------------------------------------------------------------------------------------
import pandas as pd

df = pd.read_csv('data/enrolment_3.csv')

# 과목별 인원 가져오기
allowed = df["status"] == "allowed"
course_counts = df.loc[allowed, "course name"].value_counts()

# 각 강의실 규모에 해당되는 과목 리스트 만들기
auditorium_list = list(course_counts[course_counts >= 80].index)
large_room_list = list(course_counts[(80 > course_counts) & (course_counts >= 40)].index)
medium_room_list = list(course_counts[(40 > course_counts) & (course_counts >= 15)].index)
small_room_list = list(course_counts[(15 > course_counts) & (course_counts > 4)].index)

# 강의실 이름 붙이기
for i in range(len(auditorium_list)):
    df.loc[(df["course name"] == sorted(auditorium_list)[i]) & allowed, "room assignment"] = "Auditorium-" + str(i + 1)

for i in range(len(large_room_list)):
    df.loc[(df["course name"] == sorted(large_room_list)[i]) & allowed, "room assignment"] = "Large-" + str(i + 1)
    
for i in range(len(medium_room_list)):
    df.loc[(df["course name"] == sorted(medium_room_list)[i]) & allowed, "room assignment"] = "Medium-" + str(i + 1)
    
for i in range(len(small_room_list)):
    df.loc[(df["course name"] == sorted(small_room_list)[i]) & allowed, "room assignment"] = "Small-" + str(i + 1)

# column 이름 바꾸기
df.rename(columns={"room assignment": "room number"}, inplace = True)
    
# 정답 출력
df
---------------------------------------------------------------------------------------------------
'''
