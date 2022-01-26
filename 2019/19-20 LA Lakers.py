import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.expand_frame_repr', False)
lakers = pd.read_csv('E:\LA_lakers.csv')

#Result의 칼럼이 ex) 111-132 식의 형태여서 홈 점수와 어웨이 점수를 또 다른 칼럼으로 추가
lakers['home_score'] = lakers.Result.str.split('-').str[0]
lakers['away_score'] = lakers.Result.str.split('-').str[1]

#object인 점수 칼럼을 int형으로 변경 (비교하기 위함)
lakers['home_score'] = pd.to_numeric(lakers['home_score'])
lakers['away_score'] = pd.to_numeric(lakers['away_score'])

#띄어쓰기 오류가 발생하여 칼럼의 이름을 변경해줌
lakers.rename(columns={'Home Team': 'Home_Team'}, inplace = True)
lakers.rename(columns={'Away Team': 'Away_Team'}, inplace = True)

#lakers가 홈에서 경기한 조건과 홈일 때 이긴 조건을 추출
home_match = (lakers.Home_Team == 'Los Angeles Lakers')
home_match_data = lakers[home_match]
home_match_data.reset_index(inplace=True)
home_match_win = (lakers['home_score'] > lakers['away_score'])
final_home_match_win = lakers[home_match_win & home_match]
final_home_match_win.reset_index(inplace = True)

#lakers가 어웨이에서 경기한 조건과 어웨이일 때 이긴 조건을 추출
away_match = (lakers.Away_Team == 'Los Angeles Lakers')
away_match_data = lakers[away_match]
away_match_data.reset_index(inplace=True)
away_match_win = (lakers['away_score'] > lakers['home_score'])
final_away_match_win = lakers[away_match_win & away_match]

#홈일때 승리한 비율 구하기
#인덱스를 초기화하지 않고 개수를 세었더니 마지막 인덱스 기준으로 나와서 인덱스 초기화
print("홈에서 경기한 전체 데이터 수 : ", home_match_data.shape[0])
print("홈에서 LA Lakers가 승리한 경기의 수 : ", final_home_match_win.shape[0])
home_percent = round(final_home_match_win.shape[0] * 100 / (home_match_data.shape[0]), 2)
print(f"홈에서 LA Lakers의 승률 : {home_percent}%")

print()
#원정일때 승리한 비율 구하기
print("원정에서 경기한 전체 데이터 수 : ", away_match_data.shape[0])
print("원정에서 LA Lakers가 승리한 경기의 수 : ", final_away_match_win.shape[0])
away_percent = round(final_away_match_win.shape[0] * 100 / (away_match_data.shape[0]), 2)
print(f"원정에서 LA Lakers의 승률 : {away_percent}%")


#시각화 하기
x_data=[home_percent, away_percent]
x_ticks =['home', 'away']
plt.figure(figsize=(6,8))
plt.bar(np.arange(len(x_data)), x_data, width=0.4) #bar(막대를 표시할 위치, 막대의 높이)
plt.ylabel('percent')
plt.xticks(np.arange(len(x_data)), x_ticks)
for index, value in enumerate(x_data):
  plt.text(index - 0.1, value + 0.5, str(value))

plt.show()