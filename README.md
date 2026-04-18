# Technical Assessment

## Project Overview
This project sets up a university database and generates a High Achievers Report. It includes:
- Database schema design (Students, Subjects, Marks tables)
- Data population script for 20 students and 8 subjects
- High Achievers Report with SQL optimization and data visualization

## Technologies Used
- **Database**: MySQL (via Laragon)
- **Python Libraries**: mysql-connector-python, pandas, matplotlib, seaborn
- **Environment**: Laragon (local MySQL instance)

## Prerequisites

### 1. Install Laragon
- Download from: https://laragon.org/download/
- Install and start Laragon (ensure MySQL service is running - green light)

### 2. Install Python Dependencies
Use bash and run 'pip install mysql-connector-python pandas matplotlib seaborn'

## Database Schema Design

### Database Name: `university`

### Tables Structure

#### 1. Students Table
| Column | Datatype | Constraints | Description |
|--------|----------|-------------|-------------|
| student_id | INT | PRIMARY KEY, AUTO_INCREMENT | Unique student identifier |
| name | VARCHAR(100) | NOT NULL | Student's full name |
| enrollment_date | DATE | NOT NULL | Date student enrolled |
| email | VARCHAR(100) | UNIQUE, NOT NULL | Student's email address |

#### 2. Subjects Table
| Column | Datatype | Constraints | Description |
|--------|----------|-------------|-------------|
| subject_id | INT | PRIMARY KEY, AUTO_INCREMENT | Unique subject identifier |
| subject_name | VARCHAR(100) | NOT NULL, UNIQUE | Name of the subject |
| credits | INT | DEFAULT 3 | Credit hours for subject |

**8 Subjects Inserted:**
- Mathematics
- Physics
- Chemistry
- Biology
- Computer Science
- English Literature
- History
- Economics

#### 3. Marks Table (Linking Table)
| Column | Datatype | Constraints | Description |
|--------|----------|-------------|-------------|
| mark_id | INT | PRIMARY KEY, AUTO_INCREMENT | Unique mark record identifier |
| student_id | INT | NOT NULL, FOREIGN KEY | References students(student_id) |
| subject_id | INT | NOT NULL, FOREIGN KEY | References subjects(subject_id) |
| score | INT | NOT NULL | Score between 0-100 |
