import psycopg2

university_database = psycopg2.connect(
    database="University_Database",
    user="postgres",
    password="Yeshua2530!",
    host="localhost",
    port="5432"
)

sendQ = university_database.cursor();

def getAllStudents():
    sendQ.execute("SELECT * FROM students")
    sTable = sendQ.fetchall() #get back all students from student table

    for student in sTable:
        print(student)
def addStudent(fn,ln,em,ed):
    addNew = """INSERT INTO students(first_name,last_name,email,enrollment_date) VALUES (%s,%s,%s,%s)"""
    newStudent = (fn,ln,em,ed)
    sendQ.execute(addNew,newStudent)
    university_database.commit()
    getAllStudents()
def updateStudentEmail(s_id,n_email):
    updated="""UPDATE students SET email = %s WHERE student_id = %s """
    u_email = (n_email,s_id)
    sendQ.execute(updated,u_email)
    university_database.commit()
    getAllStudents()
def deleteStudent(s_id):
    deleted="""DELETE FROM students WHERE student_id = %s"""
    d_student = (s_id)
    sendQ.execute(deleted,(d_student,))
    university_database.commit()
    getAllStudents()

def menu():
    flag = 1
    while flag!=0:
        choice = input('MY UNIVERSITY DATABASE\nSELECT A NUMBER...\n1-To get all students\n2-To add a new student\n3-To update a student email\n4-To delete a student\n5-To exit\n\n')
        
        if choice=='1':
            getAllStudents()
        elif choice=='2':
            first = input('Insert new student first name: ')
            last = input('Insert new student last name: ')
            mail = input('Insert new student email: ')
            ed = input('Insert new student enrollment date: ')
            addStudent(first,last,mail,ed)
        elif choice=='3':
            id = input('Insert student ID: ')
            n_mail = input('Insert new email: ')
            updateStudentEmail(id,n_mail)
        elif choice=='4':
            id = input('Insert student ID: ')
            deleteStudent(id)
        elif choice=='5':
            sendQ.close()
            university_database.close()
            flag = 0;
            print('GOODBYE!')
            break;
        

menu()