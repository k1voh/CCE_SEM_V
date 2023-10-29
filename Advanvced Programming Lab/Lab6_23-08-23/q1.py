import sqlite3

#create a database
conn = sqlite3.connect('student.db')

#create a cursor
curr = conn.cursor()

#create a table
try:
    curr.execute(" CREATE TABLE students(REGNO integer PRIMARY KEY, NAME text, AGE integer, COURSE text) ")
except:
    pass

def insert():
    regno = input("Enter registration no. of the student : ")
    name = input("Enter name of the student : ")
    age = int(input("Enter age of the student : "))
    crs = input("Enter course of the student : ")
    #inserts user inputted values into the table
    curr.execute(f" INSERT INTO students VALUES('{regno}','{name}','{age}','{crs}')")

def delete():
    regno = int(input("Enter the registration no. of the person you want to delete : "))
    #deletes the tuple of the given registration number
    curr.execute(f"DELETE FROM students where REGNO = {regno}")
    
def update():
    regno = int(input("Enter the registration no. of the person you want to change : "))
    set = input("What do you want to change? NAME? AGE? COURSE? : ")
    into = input("into what value would you like to change : ")
    #updates the table, sets given parameter to new value where regno intersects
    curr.execute(f"UPDATE students set {set} = '{into}' where REGNO = '{regno}'")
     
def display():
    #displays all values
    curr.execute("SELECT * FROM students")
    for tuples in curr.fetchall():
        print(tuples)
    
def main():
    print("""
        \n1. INSERT
        \n2. DELETE
        \n3. UPDATE
        \n4. DISPLAY
        \n5. EXIT""")

    while(True):
        option = int(input("\nEnter your choice : "))
        if(option == 1):
            insert()
        elif(option == 2):
            delete()
        elif(option == 3):
            update()
        elif(option == 4):
            display()
        elif(option == 5):
            break
        

if __name__ == "__main__":
    main()
    
    #commiting changes
    conn.commit()

    conn.close()

