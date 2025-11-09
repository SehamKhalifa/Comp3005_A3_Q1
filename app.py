import psycopg2
from datetime import date

from db_config import get_connection
'''
Retrieves and displays all records from the students table
'''
def get_All_students(cursor):   
    cursor.execute("SELECT * FROM students ORDER BY student_id") #execute the query to get all students ordered by student_id
    print("Student ID, First Name, Last Name, Email, Enrollment Date")
    for record in cursor: #iterate through each record in the result set
        print(*record, sep=", ") #unpack the tuple and print with comma separation

'''
Inserts a new student record into the students table
'''
def add_student(conn, cursor):
    first_name = input("Enter their First Name: ")
    last_name = input("Enter their Last Name: ")
    email = input("Enter their email: ")
    enrollment_date = input("Enter Enrollment Date: ")

    try:
        cursor.execute(
            "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
            (first_name, last_name, email, date.fromisoformat(enrollment_date)))  #insert new student to record with all their details
        conn.commit()
        print(f"New student created: {first_name} {last_name}\n")

    except Exception as e:
        print("failed to create student: " + str(e)) #print error message if insertion fails

'''
Updates the email address for a student with the specified student_id
'''
def update_student_email(conn, cursor):
    student_id = input("Enter ID of student to update: ")
    new_email = input("Enter chosen student's new email: ")

    try:
        cursor.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id)) #update email of student with given student_id
        conn.commit()

        if cursor.rowcount == 0: #check if any rows were affected by the update
            print(f"No student with ID found '{student_id}'\n")
        else:
            print(f"Successfully updated email address of student with ID '{student_id}'\n")

    except Exception as e:
        print("failed to update student: " + str(e))

'''
 Deletes the record of the student with the specified student_id
'''
def delete_student(conn, cursor):
    student_id = input("Enter ID of student to delete: ")

    try:
        cursor.execute("DELETE FROM students WHERE student_id = (%s)",(student_id,))
        conn.commit()

        if cursor.rowcount == 0:
            print(f"No student with ID found '{student_id}'")
        else:
            print(f"Successfully deleted student with ID '{student_id}'")

    except Exception as e:
        print("failed to delete student: " + str(e))

'''
Resets the students table to a known state with predefined records
'''
def reset_students_table(conn, cursor):
    cursor.execute("DELETE FROM students")  #clear existing records and reset table to restart fresh
    cursor.execute("""
        INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
        ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
        ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
        ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')
    """)
    conn.commit()

'''
Print the different commands
'''
def print_options():
    print("""
your options are:
    1. Get all students
    2. Add a new student
    3. Update the email of a student
    4. Delete a student
    5. Exit to quit Program
    """)

def main():
    with get_connection() as conn: 
        with conn.cursor() as cursor:
            reset_students_table(conn, cursor)  
        print("Welcome to the Student Management System!")
        print_options()

        with conn.cursor() as cursor:
            while True:
                result = input(">")

                match result.lower():
                    case '1': get_All_students(cursor)
                    case '2': add_student(conn, cursor)
                    case '3': update_student_email(conn, cursor)
                    case '4': delete_student(conn, cursor)
                    case '5': break 
                    case _: 
                        print("Invalid command")

                print_options()

if __name__ == "__main__":
    main()

