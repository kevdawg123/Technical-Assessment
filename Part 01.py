# Population of data into university database

import mysql.connector
import random
from datetime import datetime, timedelta

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'university'
}


def generate_and_insert_data():
    """Generate and insert dummy data"""

    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()

    # Step 1: Insert 8 subjects
    print("Inserting 8 subjects...")
    subjects = [
        "Mathematics", "Physics", "Chemistry", "Biology",
        "Computer Science", "English Literature", "History", "Economics"
    ]

    for subject in subjects:
        # Regular INSERT (no IGNORE) - will show error if duplicate
        cursor.execute(
            "INSERT INTO subjects (subject_name, credits) VALUES (%s, 3)",
            (subject,)
        )
        print(f"  - Inserted: {subject}")

    # Step 2: Generate and insert 20 students
    print("\nGenerating and inserting 20 students...")
    first_names = ["John", "Emma", "Michael", "Sophia", "William", "Olivia", "James", "Ava",
                   "Robert", "Isabella", "David", "Mia", "Richard", "Charlotte", "Joseph",
                   "Amelia", "Thomas", "Harper", "Charles", "Evelyn"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
                  "Davis", "Rodriguez", "Martinez", "Wilson", "Anderson", "Taylor", "Thomas",
                  "Moore", "Jackson", "Martin", "Lee", "White", "Harris"]

    for i in range(20):
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        random_days = random.randint(0, 1460)
        enrollment_date = datetime(2020, 1, 1) + timedelta(days=random_days)
        email = f"{name.lower().replace(' ', '.')}{i + 1}@university.edu"

        # Regular INSERT - will show error if duplicate email
        cursor.execute(
            "INSERT INTO students (name, enrollment_date, email) VALUES (%s, %s, %s)",
            (name, enrollment_date, email)
        )
        print(f"  - Inserted: {name}")

    # Step 3: Get IDs
    cursor.execute("SELECT student_id FROM students")
    student_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT subject_id FROM subjects")
    subject_ids = [row[0] for row in cursor.fetchall()]

    # Step 4: Insert marks
    print(f"\nInserting marks for {len(student_ids)} students × {len(subject_ids)} subjects...")

    for student_id in student_ids:
        for subject_id in subject_ids:
            score = random.randint(40, 100)
            # Regular INSERT - will show error if duplicate mark exists
            cursor.execute("""
                INSERT INTO marks (student_id, subject_id, score) 
                VALUES (%s, %s, %s)
            """, (student_id, subject_id, score))

    connection.commit()
    print(f"\n✓ Complete! Inserted:")
    print(f"  - 8 subjects")
    print(f"  - 20 students")
    print(f"  - {len(student_ids) * len(subject_ids)} marks")

    cursor.close()
    connection.close()


if __name__ == "__main__":
    generate_and_insert_data()