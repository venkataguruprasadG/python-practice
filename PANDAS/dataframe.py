import pandas as pd

student_data = [
    [1, 'John', 15],
    [2, 'Alice', 14],
    [3, 'Bob', 13],
    [4, 'Diana', 16],
]

df = pd.DataFrame(student_data, columns=['id','name','age'])

df['grade']=['10th','11th','12th']

average_mean = df['age'].mean()
max_value = df['age'].max()
min_value = df['age'].min()

print("Average Age:", average_mean)
print("Maximum Age:", max_value)
print("Minimum Age:", min_value)

df.to_csv('students.csv',index=False)

new_df=pd.read_csv('students.csv')

print(new_df)

print(df)

dd=df[df['age']>14][['name','age']]

print(dd)