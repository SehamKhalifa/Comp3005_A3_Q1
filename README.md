## Student Management System
Youtube Channel Handle: @SehamKhalifa-3005
URL:  https://www.youtube.com/watch?v=wGEtR1acooU

This Python application connects to a PostgreSQL database to manage student records.  
It allows and give users option to:
- View all students
- Add new students
- Update a student's email
- Delete a student

## Requirements
- Python 3.10 or newer
- PostgreSQL database
- `psycopg2` library installed

You must also include a file named **`db_config.py`** that defines the database connection.

Example `db_config.py`:
```python
import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="your_database_name",
        user="your_username",
        password="your_password"
    )

## Setup

### Database Setup

Make sure PostgreSQL is running and the `students` table exists. You can create it using:

```sql
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    enrollment_date DATE
);

#Install:

pip install psycopg2

#To run program

python main.py


#In VScode the menu options:
app.py  #Main program logic
db_config.py # Database connection setup
README.md  # Setup and run instructions

