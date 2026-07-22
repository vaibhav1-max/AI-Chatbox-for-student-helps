from typing import Dict

from .data import ATTENDANCE, ASSIGNMENTS, FACULTY, FEES, HOLIDAYS, LIBRARY, MARKS, NOTICES, PLACEMENTS, STUDENTS, TIMETABLE, HOSTEL, ACADEMIC_EVENTS
from .rag import RAG_ENGINE


IntentKeywords = {
    "attendance": ["attendance", "present", "absent", "class"],
    "marks": ["marks", "result", "grade", "semester result", "score"],
    "fees": ["fee", "fees", "pending", "dues", "payment"],
    "timetable": ["timetable", "schedule", "class timing", "time table"],
    "assignments": ["assignment", "submission", "homework"],
    "exam": ["exam", "exam schedule", "mid sem", "semester exam"],
    "notices": ["notice", "notice board", "circular"],
    "hostel": ["hostel", "room", "mess"],
    "faculty": ["faculty", "teacher", "professor", "hod"],
    "placement": ["placement", "campus drive", "internship", "job"],
    "library": ["library", "book", "shelf"],
    "events": ["event", "fest", "cultural"],
    "holiday": ["holiday", "leave", "vacation"],
}


def detect_intent(question: str) -> str:
    normalized = question.lower()
    for intent, keywords in IntentKeywords.items():
        if any(keyword in normalized for keyword in keywords):
            return intent
    return "general"


def retrieve_knowledge(question: str) -> str:
    return RAG_ENGINE.search(question)


def format_student_response(student_id: int, intent: str, question: str) -> Dict:
    student = next((item for item in STUDENTS if item["student_id"] == student_id), None)
    if student is None:
        return {"answer": "Invalid student id.", "intent": intent, "source": "database"}

    if intent == "attendance":
        return {
            "answer": f"{student['name']}, your attendance record is: " + "; ".join(
                f"{item['subject']}: {item['percentage']}%" for item in ATTENDANCE if item["student_id"] == student_id
            ),
            "intent": intent,
            "source": "database",
        }

    if intent == "marks":
        return {
            "answer": f"{student['name']}, your latest marks summary is: " + "; ".join(
                f"{item['subject']}: {item['total']} ({item['grade']})" for item in MARKS if item["student_id"] == student_id
            ),
            "intent": intent,
            "source": "database",
        }

    if intent == "fees":
        fee = next((item for item in FEES if item["student_id"] == student_id), None)
        if fee is None:
            return {"answer": "No fee record found.", "intent": intent, "source": "database"}
        return {
            "answer": f"Pending fee is ₹{fee['remaining']} and due date is {fee['due_date']}.",
            "intent": intent,
            "source": "database",
        }

    if intent == "timetable":
        return {
            "answer": "Your timetable entries: " + "; ".join(
                f"{item['day']} {item['time']} - {item['subject']} ({item['faculty']}, {item['room']})" for item in TIMETABLE
            ),
            "intent": intent,
            "source": "database",
        }

    if intent == "assignments":
        return {
            "answer": "Upcoming assignments: " + "; ".join(
                f"{item['subject']} due on {item['submission_date']}" for item in ASSIGNMENTS
            ),
            "intent": intent,
            "source": "database",
        }

    if intent == "exam":
        return {
            "answer": "Exam-related policy: Students should carry the ID card and follow the seating instructions. Mid-sem exams are scheduled from 12 August 2026.",
            "intent": intent,
            "source": "rag",
        }

    if intent == "notices":
        return {
            "answer": "Latest notices: " + "; ".join(item["title"] for item in NOTICES),
            "intent": intent,
            "source": "database",
        }

    if intent == "hostel":
        return {
            "answer": f"Hostel details: {HOSTEL['room_type']} with fee {HOSTEL['fee']}. {HOSTEL['rules']}",
            "intent": intent,
            "source": "knowledge-base",
        }

    if intent == "faculty":
        return {
            "answer": "Faculty details: " + "; ".join(
                f"{item['name']} ({item['department']}, Cabin {item['cabin']})" for item in FACULTY
            ),
            "intent": intent,
            "source": "database",
        }

    if intent == "placement":
        return {
            "answer": "Placement information: " + "; ".join(
                f"{item['company']} - {item['role']} - {item['status']}" for item in PLACEMENTS
            ),
            "intent": intent,
            "source": "database",
        }

    if intent == "library":
        return {
            "answer": "Library availability: " + "; ".join(
                f"{item['book']} ({'available' if item['available'] else 'currently unavailable'})" for item in LIBRARY
            ),
            "intent": intent,
            "source": "database",
        }

    if intent == "events":
        return {
            "answer": "Upcoming events: " + "; ".join(
                f"{item['title']} on {item['date']}" for item in ACADEMIC_EVENTS
            ),
            "intent": intent,
            "source": "database",
        }

    if intent == "holiday":
        return {
            "answer": "Upcoming holidays: " + "; ".join(
                f"{item['date']} - {item['name']}" for item in HOLIDAYS
            ),
            "intent": intent,
            "source": "database",
        }

    return {
        "answer": retrieve_knowledge(question),
        "intent": intent,
        "source": "rag",
    }
