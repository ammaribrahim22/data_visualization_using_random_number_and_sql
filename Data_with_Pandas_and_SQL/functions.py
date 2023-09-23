import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import random
df = pd.read_csv("data.csv")


num1 = random.randrange(1, 100)
num2 = random.randrange(1, 100)
num3 = random.randrange(1, 100)


conn = sqlite3.connect('data.db')
cursor = conn.cursor()

data = (num1, num2, num3)
cursor.execute('''
        INSERT INTO test (Name, Age, Color)
        VALUES (?, ?, ?)
    ''', data)

# this code is inserting data from csv file into database using for loop
# if you want to insert data from csv file with 3 columns you can use this code
# for index, row in df.iterrows():
#     name = row['Name']
#     age = row['Age']
#     column3 = row['Color']
#
#     user_data = (num1, num2, num3)
#     cursor.execute('''
#         INSERT INTO test (Name, Age, Color)
#         VALUES (?, ?, ?)
#     ''', user_data)

conn.commit()
conn.close()

print("Data has been inserted into the database successfully.")


# this function reading database table columns data and calling in main.py and show data using matplotlib
def reading():
    database = sqlite3.connect('data.db')
    sql_query = "SELECT * FROM test"
    sql_file = pd.read_sql(sql_query, database)
    database.close()
    age = sql_file["Age"]
    color = sql_file["Color"]
    plt.scatter(age, color)
    plt.show()
