from __future__ import annotations

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


TRAINING_EXAMPLES = [
    ("what is my attendance", "attendance"),
    ("show my attendance percentage", "attendance"),
    ("how many classes did i miss", "attendance"),
    ("what is my result", "marks"),
    ("show semester result", "marks"),
    ("what is my grade", "marks"),
    ("how much fee is pending", "fees"),
    ("do i have any dues", "fees"),
    ("what is my fee status", "fees"),
    ("when is my next class", "timetable"),
    ("show timetable", "timetable"),
    ("which class is tomorrow", "timetable"),
    ("what assignments are due", "assignments"),
    ("submission date for assignment", "assignments"),
    ("when do i submit python assignment", "assignments"),
    ("when is my exam", "exam"),
    ("exam schedule", "exam"),
    ("what is the hostel fee", "hostel"),
    ("how do i apply for hostel", "hostel"),
    ("who is my faculty", "faculty"),
    ("faculty information", "faculty"),
    ("placement drive details", "placement"),
    ("tell me about internships", "placement"),
    ("show library books", "library"),
    ("is python book available", "library"),
    ("which events are happening", "events"),
    ("college festival", "events"),
    ("when is independence day", "holiday"),
    ("holiday list", "holiday"),
]


class IntentClassifier:
    def __init__(self) -> None:
        texts, labels = zip(*TRAINING_EXAMPLES)
        self.pipeline = Pipeline(
            steps=[
                ("tfidf", TfidfVectorizer(ngram_range=(1, 2), stop_words="english")),
                ("clf", LogisticRegression(max_iter=500)),
            ]
        )
        self.pipeline.fit(texts, labels)

    def predict(self, question: str) -> str:
        return str(self.pipeline.predict([question.lower()])[0])


INTENT_CLASSIFIER = IntentClassifier()
