import sqlite3

# Connect to database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create table
# c.execute('''CREATE TABLE person (
#                 first_name TEXT,
#                 last_name TEXT,
#                 age INTEGER
#           )''')
# conn.commit()

# Insert a row of data
# c.execute("""INSERT INTO person VALUES
#  ('John', 'Smith', 25),
#  ('Anna', 'Smith', 30),
#  ('Mike', 'Johnson', 40)""")
# conn.commit()

# Query the database
c.execute("""SELECT * FROM person
 WHERE last_name = 'Smith'""")
persons = c.fetchall()
print(persons)

class Person():
    def __init__(self, first=None,
        last=None, age=None):
        self.first = first
        self.last = last
        self.age = age
    
    def clone_person(self, result):
        self.first = result[0]
        self.last = result[1]
        self.age = result[2]

person1 = Person()
person1.clone_person(persons[0])

print(person1.first)
print(person1.last)
print(person1.age)

person2 = Person("Bob", "Davis", 50)
c.execute("INSERT INTO person VALUES (?, ?, ?)", (person2.first, person2.last, person2.age))
conn.commit()


conn.close()