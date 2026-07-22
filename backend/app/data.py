STUDENTS = [
    {
        "student_id": 1,
        "name": "Samarth Mishra",
        "roll_number": "21CS101",
        "branch": "Computer Science",
        "semester": 6,
        "email": "samarth@example.com",
        "phone": "9876543210",
        "password": "student123",
        "photo": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=120&q=80",
        "address": "Delhi, India",
    }
]

ATTENDANCE = [
    {"student_id": 1, "subject": "Operating System", "total_classes": 20, "present": 18, "percentage": 90},
    {"student_id": 1, "subject": "DBMS", "total_classes": 20, "present": 16, "percentage": 82},
    {"student_id": 1, "subject": "Python", "total_classes": 20, "present": 19, "percentage": 95},
]

MARKS = [
    {"student_id": 1, "subject": "Operating System", "internal": 24, "external": 56, "total": 80, "grade": "A"},
    {"student_id": 1, "subject": "DBMS", "internal": 20, "external": 45, "total": 65, "grade": "B"},
    {"student_id": 1, "subject": "Python", "internal": 25, "external": 59, "total": 84, "grade": "A"},
]

FEES = [
    {"fee_id": 1, "student_id": 1, "total_fee": 180000, "paid": 162000, "remaining": 18000, "due_date": "2026-08-25"}
]

TIMETABLE = [
    {"day": "Monday", "time": "09:00", "subject": "Operating System", "faculty": "Dr. Mehta", "room": "CS-301"},
    {"day": "Monday", "time": "11:00", "subject": "DBMS", "faculty": "Prof. Sharma", "room": "CS-208"},
    {"day": "Tuesday", "time": "10:00", "subject": "Python", "faculty": "Ms. Sinha", "room": "LAB-2"},
]

FACULTY = [
    {"faculty_id": 1, "name": "Dr. Mehta", "department": "CSE", "email": "mehta@college.edu", "cabin": "A-12", "phone": "9998887776"},
    {"faculty_id": 2, "name": "Prof. Sharma", "department": "CSE", "email": "sharma@college.edu", "cabin": "A-21", "phone": "9988776655"},
]

NOTICES = [
    {"notice_id": 1, "title": "Mid-Sem Exam Schedule", "description": "Mid-semester exams begin on 12 August 2026.", "pdf": "exam-schedule.pdf", "date": "2026-07-10"},
    {"notice_id": 2, "title": "Library Renewal", "description": "Library books need to be renewed before 30 July 2026.", "pdf": "library-renewal.pdf", "date": "2026-07-12"},
]

ASSIGNMENTS = [
    {"assignment_id": 1, "subject": "Python", "faculty": "Ms. Sinha", "submission_date": "2026-07-28", "pdf": "python-assignment.pdf"},
    {"assignment_id": 2, "subject": "DBMS", "faculty": "Prof. Sharma", "submission_date": "2026-07-31", "pdf": "dbms-assignment.pdf"},
]

HOSTEL = {
    "room_type": "2-sharing AC",
    "fee": "₹48,000/year",
    "contact": "Hostel office: 8800-9000",
    "rules": "Students must maintain discipline and submit hostel form before 15 August.",
}

PLACEMENTS = [
    {"company": "Microsoft", "role": "Software Engineer Intern", "date": "2026-08-01", "status": "Open"},
    {"company": "TCS", "role": "Campus Recruitment", "date": "2026-08-12", "status": "Registered"},
]

LIBRARY = [
    {"book": "Artificial Intelligence", "shelf": "QA76.76", "available": True},
    {"book": "Database Management Systems", "shelf": "QA76.9", "available": True},
    {"book": "Python Programming", "shelf": "QA76.73", "available": False},
]

ACADEMIC_EVENTS = [
    {"title": "Tech Fest 2026", "date": "2026-08-15", "description": "Innovation expo and coding challenge."},
    {"title": "Annual Cultural Night", "date": "2026-09-02", "description": "College annual cultural event."},
]

HOLIDAYS = [
    {"date": "2026-08-15", "name": "Independence Day"},
    {"date": "2026-09-02", "name": "Teacher's Day"},
]

KNOWLEDGE_BASE = {
    "attendance_policy": "Minimum attendance required is 75% in each subject to be eligible for semester exams.",
    "hostel_policy": "Hostel applications must be submitted before 15 August and students must follow the code of conduct.",
    "exam_policy": "Students should bring the university ID card and seating plan on the day of the examination.",
    "placement_policy": "Students with at least 7.0 CGPA and no backlogs are prioritized for placement drives.",
    "library_policy": "Students can borrow at most 3 books and must return them before the due date.",
}
