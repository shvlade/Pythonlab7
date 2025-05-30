import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('students.csv')
plt.figure(figsize=(10, 5))
plt.hist(
    df['Score'],
    bins=10,
    color='skyblue',
    edgecolor='black',
    alpha=0.7
)

plt.title('Распределение баллов студентов', fontsize=14)
plt.xlabel('Балл', fontsize=12)
plt.ylabel('Количество студентов', fontsize=12)

plt.show()
group_avg = df.groupby("Group")["Score"].mean().sort_index()

plt.figure(figsize=(8, 5))
plt.bar(group_avg.index, group_avg.values, color="green", edgecolor="black")
plt.title("Средний балл по группам")
plt.xlabel("Группа")
plt.ylabel("Средний балл")
plt.show()