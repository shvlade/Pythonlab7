import pandas as pd
r = pd.read_csv('students.csv')
group_stat = r.groupby("Group").agg({
    "Score": "mean",
    "Age": "median"
}).rename(columns={
    "Score": "Average_Score",
    "Age": "Median_Age"
})
print(group_stat)
r["Passed"] = (r["Score"] >= 60)
print(r[["Name", "Group", "Score", "Passed"]].head())