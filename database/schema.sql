CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    roll_number VARCHAR(50) UNIQUE NOT NULL,
    branch VARCHAR(100) NOT NULL,
    semester INT NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    phone VARCHAR(20),
    password_hash VARCHAR(255) NOT NULL,
    photo_url TEXT,
    address TEXT
);

CREATE TABLE attendance (
    attendance_id SERIAL PRIMARY KEY,
    student_id INT NOT NULL REFERENCES students(student_id),
    subject VARCHAR(100) NOT NULL,
    total_classes INT NOT NULL,
    present INT NOT NULL,
    percentage DECIMAL(5,2) NOT NULL
);

CREATE TABLE marks (
    mark_id SERIAL PRIMARY KEY,
    student_id INT NOT NULL REFERENCES students(student_id),
    subject VARCHAR(100) NOT NULL,
    internal INT,
    external INT,
    total INT,
    grade VARCHAR(5)
);

CREATE TABLE fee_status (
    fee_id SERIAL PRIMARY KEY,
    student_id INT NOT NULL REFERENCES students(student_id),
    total_fee DECIMAL(12,2) NOT NULL,
    paid DECIMAL(12,2) NOT NULL,
    remaining DECIMAL(12,2) NOT NULL,
    due_date DATE NOT NULL
);

CREATE TABLE timetable (
    timetable_id SERIAL PRIMARY KEY,
    day VARCHAR(20) NOT NULL,
    time VARCHAR(20) NOT NULL,
    subject VARCHAR(100) NOT NULL,
    faculty VARCHAR(120) NOT NULL,
    room VARCHAR(50) NOT NULL
);

CREATE TABLE faculty (
    faculty_id SERIAL PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    department VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    cabin VARCHAR(50),
    phone VARCHAR(20)
);

CREATE TABLE notices (
    notice_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT NOT NULL,
    pdf_url TEXT,
    date DATE NOT NULL
);

CREATE TABLE assignment (
    assignment_id SERIAL PRIMARY KEY,
    subject VARCHAR(100) NOT NULL,
    faculty VARCHAR(120) NOT NULL,
    submission_date DATE NOT NULL,
    pdf_url TEXT
);
