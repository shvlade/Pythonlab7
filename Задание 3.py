import pandas as pd

r = pd.read_csv("students.csv")

print("Пропуски по столбцам:")
print(r.isnull().sum())


if r["Score"].isnull().any():
    Score = r["Score"].mean()
    r["Score"].fillna(Score, inplace=True)
    print(f"\n Пропуски в 'Score' заполнены средним значением: {Score}")


if r["Group"].isnull().any():
    before = len(r)
    r.dropna(subset=["Group"], inplace=True)
    after = len(r)
    print(f"\n Удалено {before - after} строк с пустыми значениями в 'Group'")