from pathlib import Path

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from .chatbot import format_student_response, detect_intent
from .config import SETTINGS
from .data import STUDENTS, ATTENDANCE, MARKS, FEES, TIMETABLE, ASSIGNMENTS, NOTICES, FACULTY
from .llm_service import LLM_SERVICE
from .ml_intent import INTENT_CLASSIFIER

app = FastAPI(title="AI-Powered Student Support Assistant", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class LoginRequest(BaseModel):
    email: str
    password: str


class ChatRequest(BaseModel):
    student_id: int
    question: str


@app.get("/api/health")
def health_check():
    return {"status": "ok", "message": "AI-Powered Student Support Assistant is running"}


@app.post("/api/auth/login")
def login(request: LoginRequest):
    student = next((item for item in STUDENTS if item["email"] == request.email and item["password"] == request.password), None)
    if not student:
        return {"success": False, "message": "Invalid credentials"}

    return {
        "success": True,
        "message": "Login successful",
        "student": {
            "student_id": student["student_id"],
            "name": student["name"],
            "roll_number": student["roll_number"],
            "branch": student["branch"],
            "semester": student["semester"],
        },
    }


@app.get("/api/student/profile")
def profile(student_id: int = Query(...)):
    student = next((item for item in STUDENTS if item["student_id"] == student_id), None)
    if not student:
        return {"success": False, "message": "Student not found"}
    return {"success": True, "student": student}


@app.get("/api/student/attendance")
def get_attendance(student_id: int = Query(...)):
    return {"success": True, "data": [item for item in ATTENDANCE if item["student_id"] == student_id]}


@app.get("/api/student/marks")
def get_marks(student_id: int = Query(...)):
    return {"success": True, "data": [item for item in MARKS if item["student_id"] == student_id]}


@app.get("/api/student/fees")
def get_fees(student_id: int = Query(...)):
    return {"success": True, "data": [item for item in FEES if item["student_id"] == student_id]}


@app.get("/api/student/timetable")
def get_timetable():
    return {"success": True, "data": TIMETABLE}


@app.get("/api/student/assignments")
def get_assignments():
    return {"success": True, "data": ASSIGNMENTS}


@app.get("/api/student/notices")
def get_notices():
    return {"success": True, "data": NOTICES}


@app.get("/api/student/faculty")
def get_faculty():
    return {"success": True, "data": FACULTY}


@app.post("/api/chat/ask")
def ask_chat(request: ChatRequest):
    intent = INTENT_CLASSIFIER.predict(request.question) if SETTINGS.use_ml_classifier else detect_intent(request.question)
    reply = format_student_response(request.student_id, intent, request.question)

    if reply.get("source") in {"rag", "knowledge-base"}:
        generated = LLM_SERVICE.generate(reply["answer"], request.question)
        reply["answer"] = generated
        reply["source"] = "llm+rag"

    return {"success": True, "intent": intent, **reply}


workspace_root = Path(__file__).resolve().parents[2]
frontend_dir = workspace_root / "frontend"
app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")
