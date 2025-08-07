import pandas as pd

data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR'],
    'Salary': [50000, 60000, 70000, 65000, 48000],
    'JoinDate': ['2020-01-15', '2019-07-23', '2021-03-12', '2018-11-01', '2022-05-18']
}

df = pd.DataFrame(data)

#Filtering data
it_employees = data[data['Department']=='IT']
print(it_employees)

#Grouping by
avg_salary = data.groupby('Department')['Salary'].mean()
print(avg_salary)

#Adding Column
data['JoinDate'] = pd.to_datetime(data['JoinDate'])

df['Experience'] = (pd.Timestamp.today() - df['JoinDate']).dt.days // 365

df_sorted = df.sort_values(by='Experience', ascending=False)
print(df_sorted)

#Merging two dataframes
project_data = {
    'EmployeeID': [101, 102, 104],
    'Project': ['Recruitment', 'Website Revamp', 'Cloud Migration']
}
projects_df = pd.DataFrame(project_data)

merged_df = df.merge(projects_df, on='EmployeeID', how='left')
print(merged_df)
