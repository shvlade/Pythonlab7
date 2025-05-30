import pandas as pd
r = pd.read_csv("students.csv")
Scores = r[r['Score'] > 80]
sorted_down_scores = Scores.sort_values(by="Score", ascending=False)
oldest_student = r["Age"].max()
youngest_student = r["Age"].min()
print(Scores)
print("Оценки на убывание", sorted_down_scores)
print("Самый взрослый студент", oldest_student)
print("Самый молодой студент", youngest_student)