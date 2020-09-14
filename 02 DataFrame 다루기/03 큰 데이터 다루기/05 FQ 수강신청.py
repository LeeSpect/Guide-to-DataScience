import pandas as pd
df = pd.read_csv('Desktop/enrolment_1.csv')
df["status"] = "allowed"

# “information technology” 과목은 심화과목이라 1학년은 수강할 수 없습니다.
boolean1 = df["course name"] == "information technology"
boolean2 = df["year"] == 1
df.loc[boolean1 & boolean2, "status"] = "not allowed"

# “commerce” 과목은 기초과목이고 많은 학생들이 듣는 수업이라 4학년은 수강할 수 없습니다.
boolean3 = df["course name"] == "commerce"
boolean4 = df["year"] == 4
df.loc[boolean3 & boolean4, "status"] = "not allowed"

# 수강생이 5명이 되지 않으면 강의는 폐강되어 수강할 수 없습니다.
allowed = df["status"] == "allowed"
course_counts = df.loc[allowed, "course name"].value_counts()
print(allowed)
'''
--------------------------------------------------------------------------------------------------------------
0       True
1       True
2       True
3       True
4       True
        ... 
1995    True
1996    True
1997    True
1998    True
1999    True
Name: status, Length: 2000, dtype: bool
--------------------------------------------------------------------------------------------------------------
'''
# value_counts()를 사용하면, 각 과목별 신청 인원을 확인할 수 있습니다.
print(course_counts)
'''
--------------------------------------------------------------------------------------------------------------
arts                                      158
science                                   124
commerce                                  101
english                                    56
education                                  41
                                         ... 
chemstry                                    1
jmc                                         1
b.ed                                        1
pgdca                                       1
sciences                                    1
Name: course name, Length: 296, dtype: int64
--------------------------------------------------------------------------------------------------------------
'''
  # 각 과목별 신청 인원이 5 이하인 과목의 index만 골라서 리스트로 만들어줍니다.
closed_courses = list(course_counts[course_counts < 5].index)
print(course_counts < 5)
'''
--------------------------------------------------------------------------------------------------------------
arts                               False
science                            False
commerce                           False
english                            False
education                          False
                                   ...  
library & information & science     True
pgdca                               True
biological sciences                 True
pg.diploma                          True
school of management                True
Name: course name, Length: 296, dtype: bool
--------------------------------------------------------------------------------------------------------------
'''
print(course_counts[course_counts < 5])
'''
--------------------------------------------------------------------------------------------------------------
computer architecture              4
physical education                 4
database                           4
tool & die making                  4
mechanical engg.                   4
                                  ..
library & information & science    1
pgdca                              1
biological sciences                1
pg.diploma                         1
school of management               1
Name: course name, Length: 214, dtype: int64
--------------------------------------------------------------------------------------------------------------
'''
print(list(course_counts[course_counts < 5]))
'''
--------------------------------------------------------------------------------------------------------------
[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 
3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 
3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
1, 1, 1, 1, 1]
--------------------------------------------------------------------------------------------------------------
'''
print(list(course_counts[course_counts < 5].index))
'''
--------------------------------------------------------------------------------------------------------------
['computer architecture', 'physical education', 'database', 'tool & die making', 'mechanical engg.', 'refactoring', 'electronics and instrumentation', 'bpt', 'korean', 'electron
ics & communication engineering', 'electrical engg', 'environment', 'pathology', 'mechanical related subjects', 'electrical and electronics engineering', 'instrumentation engine
ering', 'electronics and communication', 'electros & communicationnic', 'computer engg with specialization in cloud computing.', 'fashion communication', 'agriculture', 'chemica
l', 'data structure', 'applied sc.', 'information subjects', 'engg. & tech.', 'civil engg', 'mech', 'leather design', 'software computer science', 'mobile communication', 'elect
ronics & communication engineeering', 'bsc mpe', 'i.t', 'bcom (general)', 'electronics & comm. engg.', 'saskrit', 'medicine', 'bjmc', 'administration services', 'mangement', 'bc
om computer', 'b.com.', 'sahitya', 'comp science', 'bcom marketing', 'professional  accounting', 'all subjects', 'digital electronics', 'btzc', 'tax procedure and practice', 'co
-operation', 'admistrator', 'b.com.(gen.e/m)', 'cmmerce', 'ai & as', 'res', 'industrial microbiology', 'deee', 'electronics & comm engg', 'if', 'em', 'corporate secaratoryship',
'vocational', 'bsc btmc', 'kayachikitsa', 'tb & chest', 'mat', 'b.b.m', 'science(bzc)', 'bsc bzc', 'computer engg', 'compulsory', 'bca', 'pol-science', 'music vocal', 'computers
(ug)', 'bbi', 'm.i.l', 'rasshastra evum bhaisgya kalpana', 'b.sc-m.p.c', 'bcom finance and taxation', 'yes', 'co', 'microbiology-botany-chemistry', 'b.com (p)', 'master of compu
ter application', 'computers', 'comp(em)', 'mca 2nd shift', 'eep', 'english literature', 'anaesthesiology', 'buisiness administration', 'hons.', 'community medicine', 'travel to
urism & hospitality management', 'c bc bt', 'politics', 'discipline', 'jain darshan', 'applied science & humanities', 'gandhian thought', 'electronic', 'diploma', '3 year ll.b c
ourse', 'diploma in computer engineering', 'electronics engineering', 'tm', 'dcp', 'civit', 'taalvadya-parichay', 'construction technology and management', 'social science', 'gi
t', 'molecular virology', 'drugs and pharmaceuticals', 'information security', 'mba 2nd shift', 'chmistry', 'btc 2013', 'automobile engineering', 'science arts', 'co-education',
'lab technology', 'd.el.ed', 'nano science & technology', 'it cs', 'm.sc chemistry(analytical chemistry)', 'mpharmacy', 'international business', 'computer integrated manufactur
ing', 'pharmaceutics', 'political sc', 'arts/commerce/science/maths', 'infra structural engineering', 'medical surgical nursing', 'social work', 'mass relation', 'material scien
ce and engineering', 'cad/cam', 'scientific computing', 'electro nics and commun ications enginee ring', 'dmrd', 'nuclear science & engineering', 'dharmashastra', 'spl. educatio
n', 'special education (h.i.)', 'power & energy systems', 'nutrition & dietetics', 'electronics & communication engg.  with specialization in  vlsi design & embedded systems', '
social studies', 'dance-parangat', 'computer appplication', 'm.com', 'english geography', 'd.ed', 'environmental engg.', 'math chemistry', 'construction technology', 'thermal po
wer engineering', 'structural engineering', 'polotical', 'b.ed.', 'civil and environmental engineering', 'computational mathematics', 'transportation engineering', 'vlsi design 
and signal processing', 'vlsi', 'pharmacognosy', 'architecture', 'msc cs', 'hcl', 'mpharmacypa', 'digital communicati ons', 'communication and signal processing', 'physical scie
nce', 'aero dynamics', 'veterinary epidemiology & preventive medicine', 'data science', 'biochemistry', '(biotechnology))', 'quality assurance', 'history & archeology', 'fibre o
ptics and communication', 'power systems engineering', 'bio technology', 'btc-2012', 'arts/science', 'computer science (lateral entry)', 'lib. & info sci', 'library', 'arthrosco
py', 'environmental science', 'humanities and social science (h', 'full time', 'sciences', 'dcl', 'b.ed', 'library and information', 'aqua culture', 'aih', 'technician', 'home s
c. food & nutrition', 'jmc', 'punjabi', 'statistics', 'physical edu.', 'chemstry', 'library & information & science', 'pgdca', 'biological sciences', 'pg.diploma', 'school of ma
nagement']
--------------------------------------------------------------------------------------------------------------
'''

# for문을 통해 not allowed 문구를 넣어줍시다.
for course in closed_courses:
    df.loc[df["course name"] == course, "status"] = "not allowed"
    
df
