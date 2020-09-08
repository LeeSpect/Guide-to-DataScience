import pandas as pd
laptops_df = pd.read_csv('Desktop/laptops.csv')
laptops_df
'''
--------------------------------------------------------------------------------------------------------------
	brand	model	ram	hd_type	hd_size	screen_size	price	processor_brand	processor_model	clock_speed	graphic_card_brand	graphic_card_size	os	weight	comments
0	Dell	Inspiron 15-3567	4	hdd	1024	15.6	40000	intel	i5	2.5	intel	NaN	linux	2.50	NaN
1	Apple	MacBook Air	8	ssd	128	13.3	55499	intel	i5	1.8	intel	2.0	mac	1.35	NaN
2	Apple	MacBook Air	8	ssd	256	13.3	71500	intel	i5	1.8	intel	2.0	mac	1.35	NaN
3	Apple	MacBook Pro	8	ssd	128	13.3	96890	intel	i5	2.3	intel	2.0	mac	3.02	NaN
4	Apple	MacBook Pro	8	ssd	256	13.3	112666	intel	i5	2.3	intel	2.0	mac	3.02	NaN
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
162	Asus	A555LF	8	hdd	1024	15.6	39961	intel	i3 4th gen	1.7	nvidia	2.0	windows	2.30	NaN
163	Asus	X555LA-XX172D	4	hdd	500	15.6	28489	intel	i3 4th gen	1.9	intel	NaN	linux	2.30	NaN
164	Asus	X554LD	2	hdd	500	15.6	29199	intel	i3 4th gen	1.9	intel	1.0	linux	2.30	NaN
165	Asus	X550LAV-XX771D	2	hdd	500	15.6	29990	intel	i3 4th gen	1.7	intel	NaN	linux	2.50	NaN
166	Asus	X540LA-XX538T	4	hdd	1024	15.6	30899	intel	i3 5th gen	2.0	intel	NaN	windows	2.30	NaN
167 rows × 15 columns
--------------------------------------------------------------------------------------------------------------
'''

# 몇줄만 출력하고 싶다면
laptops_df.head(3)  # 위에서 3줄만 출력
'''
--------------------------------------------------------------------------------------------------------------
	brand	model	ram	hd_type	hd_size	screen_size	price	processor_brand	processor_model	clock_speed	graphic_card_brand	graphic_card_size	os	weight	comments
0	Dell	Inspiron 15-3567	4	hdd	1024	15.6	40000	intel	i5	2.5	intel	NaN	linux	2.50	NaN
1	Apple	MacBook Air	8	ssd	128	13.3	55499	intel	i5	1.8	intel	2.0	mac	1.35	NaN
2	Apple	MacBook Air	8	ssd	256	13.3	71500	intel	i5	1.8	intel	2.0	mac	1.35	NaN
--------------------------------------------------------------------------------------------------------------
'''

laptops_df.tail(2)  # 뒤에서 2줄만 출력
'''
--------------------------------------------------------------------------------------------------------------
brand	model	ram	hd_type	hd_size	screen_size	price	processor_brand	processor_model	clock_speed	graphic_card_brand	graphic_card_size	os	weight	comments
165	Asus	X550LAV-XX771D	2	hdd	500	15.6	29990	intel	i3 4th gen	1.7	intel	NaN	linux	2.5	NaN
166	Asus	X540LA-XX538T	4	hdd	1024	15.6	30899	intel	i3 5th gen	2.0	intel	NaN	windows	2.3	NaN
--------------------------------------------------------------------------------------------------------------
'''

# DataFrame이 얼마나 큰지 보기
laptops_df.shape  # 총 167개의 row, 15개의 column
'''
--------------------------------------------------------------------------------------------------------------
(167, 15)
--------------------------------------------------------------------------------------------------------------
'''

laptops_df.columns  # 어떤 column들이 있는지
'''
--------------------------------------------------------------------------------------------------------------
Index(['brand', 'model', 'ram', 'hd_type', 'hd_size', 'screen_size', 'price',
       'processor_brand', 'processor_model', 'clock_speed',
       'graphic_card_brand', 'graphic_card_size', 'os', 'weight', 'comments'],
      dtype='object')
--------------------------------------------------------------------------------------------------------------
'''

# 어떤 column들이 있는지와 각 column들에 대한 기본 정보
laptops_df.info()
'''
--------------------------------------------------------------------------------------------------------------
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 167 entries, 0 to 166
Data columns (total 15 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   brand               167 non-null    object 
 1   model               167 non-null    object 
 2   ram                 167 non-null    int64  
 3   hd_type             167 non-null    object 
 4   hd_size             167 non-null    int64  
 5   screen_size         167 non-null    float64
 6   price               167 non-null    int64  
 7   processor_brand     167 non-null    object 
 8   processor_model     167 non-null    object 
 9   clock_speed         166 non-null    float64
 10  graphic_card_brand  163 non-null    object 
 11  graphic_card_size   81 non-null     float64
 12  os                  167 non-null    object 
 13  weight              160 non-null    float64
 14  comments            55 non-null     object 
dtypes: float64(4), int64(3), object(8)
memory usage: 19.7+ KB
--------------------------------------------------------------------------------------------------------------
'''

laptops_df.describe()  # 각 column에 대한 통계값이 나옴
'''
--------------------------------------------------------------------------------------------------------------
	ram	hd_size	screen_size	price	clock_speed	graphic_card_size	weight
count	167.000000	167.00000	167.000000	167.000000	166.000000	81.000000	160.000000
mean	6.898204	768.91018	14.775210	64132.898204	2.321084	52.160494	2.250813
std	3.787479	392.99080	1.376526	42797.674010	0.554187	444.134142	0.648446
min	2.000000	32.00000	10.100000	13872.000000	1.100000	1.000000	0.780000
25%	4.000000	500.00000	14.000000	35457.500000	1.900000	2.000000	1.900000
50%	8.000000	1024.00000	15.600000	47990.000000	2.300000	2.000000	2.200000
75%	8.000000	1024.00000	15.600000	77494.500000	2.600000	4.000000	2.600000
max	16.000000	2048.00000	17.600000	226000.000000	3.800000	4000.000000	4.200000
--------------------------------------------------------------------------------------------------------------
'''

laptops_df.sort_values(by='price')  # price column을 기준으로 오름차순 정렬
'''
--------------------------------------------------------------------------------------------------------------
	brand	model	ram	hd_type	hd_size	screen_size	price	processor_brand	processor_model	clock_speed	graphic_card_brand	graphic_card_size	os	weight	comments
148	Acer	Aspire SW3-016	2	ssd	32	10.1	13872	intel	Atom Z8300	1.44	intel	NaN	windows	1.2	NaN
83	Acer	A315-31CDC UN.GNTSI.001	2	ssd	500	15.6	17990	intel	Celeron	1.10	intel	NaN	windows	2.1	NaN
108	Acer	Aspire ES-15 NX.GKYSI.010	4	hdd	500	15.6	17990	amd	A4-7210	1.80	amd	NaN	windows	2.4	NaN
100	Acer	A315-31-P4CRUN.GNTSI.002	4	hdd	500	15.6	18990	intel	pentium	1.10	intel	NaN	windows	NaN	NaN
73	Acer	Aspire ES1-523	4	hdd	1024	15.6	19465	amd	A4-7210	1.80	amd	NaN	linux	2.4	NaN
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
154	Microsoft	Surface Book CR9-00013	8	ssd	128	13.5	178799	intel	i5	1.80	intel	NaN	windows	1.5	NaN
31	Acer	Predator 17	16	ssd	256	17.3	178912	intel	i7	2.60	nvidia	NaN	windows	4.2	Integrated Graphics
96	Alienware	AW13R3-7000SLV-PUS	8	ssd	256	13.3	190256	intel	i7	3.00	nvidia	6.0	windows	2.6	13.3 inch FHD (1920 x 1080) IPS Anti-Glare 300...
90	Alienware	15 Notebook	16	hdd	1024	15.6	199000	intel	i7	2.60	nvidia	8.0	windows	3.5	Maximum Display Resolution : 1920 x 1080 pixel
5	Apple	MacBook Pro (TouchBar)	16	ssd	512	15.0	226000	intel	i7	2.70	intel	2.0	mac	2.5	NaN
167 rows × 15 columns
--------------------------------------------------------------------------------------------------------------
'''

laptops_df.sort_values(by='price', ascending=False)  # price column을 기준으로 내림차순 정렬
'''
--------------------------------------------------------------------------------------------------------------
	brand	model	ram	hd_type	hd_size	screen_size	price	processor_brand	processor_model	clock_speed	graphic_card_brand	graphic_card_size	os	weight	comments
5	Apple	MacBook Pro (TouchBar)	16	ssd	512	15.0	226000	intel	i7	2.70	intel	2.0	mac	2.5	NaN
90	Alienware	15 Notebook	16	hdd	1024	15.6	199000	intel	i7	2.60	nvidia	8.0	windows	3.5	Maximum Display Resolution : 1920 x 1080 pixel
96	Alienware	AW13R3-7000SLV-PUS	8	ssd	256	13.3	190256	intel	i7	3.00	nvidia	6.0	windows	2.6	13.3 inch FHD (1920 x 1080) IPS Anti-Glare 300...
31	Acer	Predator 17	16	ssd	256	17.3	178912	intel	i7	2.60	nvidia	NaN	windows	4.2	Integrated Graphics
154	Microsoft	Surface Book CR9-00013	8	ssd	128	13.5	178799	intel	i5	1.80	intel	NaN	windows	1.5	NaN
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
73	Acer	Aspire ES1-523	4	hdd	1024	15.6	19465	amd	A4-7210	1.80	amd	NaN	linux	2.4	NaN
100	Acer	A315-31-P4CRUN.GNTSI.002	4	hdd	500	15.6	18990	intel	pentium	1.10	intel	NaN	windows	NaN	NaN
108	Acer	Aspire ES-15 NX.GKYSI.010	4	hdd	500	15.6	17990	amd	A4-7210	1.80	amd	NaN	windows	2.4	NaN
83	Acer	A315-31CDC UN.GNTSI.001	2	ssd	500	15.6	17990	intel	Celeron	1.10	intel	NaN	windows	2.1	NaN
148	Acer	Aspire SW3-016	2	ssd	32	10.1	13872	intel	Atom Z8300	1.44	intel	NaN	windows	1.2	NaN
167 rows × 15 columns
--------------------------------------------------------------------------------------------------------------
'''

laptops_df.sort_values(by='price', ascending=False, inplace=True)
laptops_df  # 기존의 데이터를 정렬된 상태로 변경하고 싶다면 inplace=True를 사용한다.
'''
--------------------------------------------------------------------------------------------------------------
	brand	model	ram	hd_type	hd_size	screen_size	price	processor_brand	processor_model	clock_speed	graphic_card_brand	graphic_card_size	os	weight	comments
5	Apple	MacBook Pro (TouchBar)	16	ssd	512	15.0	226000	intel	i7	2.70	intel	2.0	mac	2.5	NaN
90	Alienware	15 Notebook	16	hdd	1024	15.6	199000	intel	i7	2.60	nvidia	8.0	windows	3.5	Maximum Display Resolution : 1920 x 1080 pixel
96	Alienware	AW13R3-7000SLV-PUS	8	ssd	256	13.3	190256	intel	i7	3.00	nvidia	6.0	windows	2.6	13.3 inch FHD (1920 x 1080) IPS Anti-Glare 300...
31	Acer	Predator 17	16	ssd	256	17.3	178912	intel	i7	2.60	nvidia	NaN	windows	4.2	Integrated Graphics
154	Microsoft	Surface Book CR9-00013	8	ssd	128	13.5	178799	intel	i5	1.80	intel	NaN	windows	1.5	NaN
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
73	Acer	Aspire ES1-523	4	hdd	1024	15.6	19465	amd	A4-7210	1.80	amd	NaN	linux	2.4	NaN
100	Acer	A315-31-P4CRUN.GNTSI.002	4	hdd	500	15.6	18990	intel	pentium	1.10	intel	NaN	windows	NaN	NaN
108	Acer	Aspire ES-15 NX.GKYSI.010	4	hdd	500	15.6	17990	amd	A4-7210	1.80	amd	NaN	windows	2.4	NaN
83	Acer	A315-31CDC UN.GNTSI.001	2	ssd	500	15.6	17990	intel	Celeron	1.10	intel	NaN	windows	2.1	NaN
148	Acer	Aspire SW3-016	2	ssd	32	10.1	13872	intel	Atom Z8300	1.44	intel	NaN	windows	1.2	NaN
167 rows × 15 columns
--------------------------------------------------------------------------------------------------------------
'''
