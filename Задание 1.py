import pandas as pd
r = pd.read_csv("students.csv")

print(r.head(5))
print("Данные")
print(r.info())
print('Статистика')
print(r.describe())
sr_ball = r['Score'].mean() #Находим средний бал
print('Средний бал', sr_ball)
