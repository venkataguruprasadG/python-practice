import pandas as pd

student_data = [
    [1, 'John', 15],
    [2, 'Alice', 14],
    [3, 'Bob', 13],
    [4, 'Diana', 16],
]

df = pd.DataFrame(student_data, columns=['id','name','age'])

df['grade']=['10th','11th','12th']
print(df)

dd=df[df['age']>14][['name','age']]

print(dd)