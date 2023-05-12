# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:
import sqlite3;
con=sqlite3.connect("teatchers.db")
cursor=con.cursor()
cursor.execute("DROP TABLE IF EXISTS Students")
cursor.execute("""CREATE TABLE IF NOT EXISTS Students(
    School_Id INTEGER PRIMARY KEY,
    Student_Name TEXT,
    Student_Id INTEGER);
    """)
students=[
    [201,"Иван",1],
    [202,"Петр",2],
    [203,"Анастасия",3],
    [204,"Игорь",4],
    ]
cursor.executemany("INSERT INTO Students VALUES(?,?,?);", students)
con.commit()
ID_students=input("Введите ID студента от 1 до 4 : ")
try:
    cursor.execute("SELECT Student_Id,Student_Name,Students.School_Id,School_Name FROM Students JOIN School ON Students.Student_Id=School.School_Id WHERE Student_Id=?", ID_students)
    rows=cursor.fetchall()
    print(f"ID Студента: {rows[0][0]} \nИмя студента: {rows[0][1]} \nID школы: {rows[0][2]} \nНазвание школы: {rows[0][3]}")
except:
    print("Неверное значение")