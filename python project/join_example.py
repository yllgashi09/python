import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
    student_id ITEGER PRIMARY KEY,
    name TEXT
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
    course_id ITEGER PRIMARY KEY,
    course_name TEXT,
    student_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(student_id)
    )
''')

cursor.execute("INSERT INFO students (name) VALUES ('Alice')")
cursor.execute("INSERT INFO students (name) VALUES ('Bob')")


cursor.execute("INSERT INFO courses (courses.name,student_id) VALUES ('Math', 1)")
cursor.execute("INSERT INFO courses (courses.name,student_id) VALUES ('ART', 2)")
cursor.execute("INSERT INFO courses (courses.name,student_id) VALUES ('Science', 1)")

conn.comit()

cursor.execute('''
SELECT students.name, courses.courses_name from students
JOIN courses on students.student_id = courses.student_id
''')

rows = cursor.fetchall()

for row in rows:
    print(f"Student: {row[0]}, Course: {row[1]}")

    conn.close()