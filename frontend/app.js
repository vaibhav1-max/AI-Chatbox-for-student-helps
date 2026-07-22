const API_BASE = 'http://localhost:8000/api';
let currentStudent = null;

const loginForm = document.getElementById('loginForm');
const loginMessage = document.getElementById('loginMessage');
const loginCard = document.getElementById('loginCard');
const dashboard = document.getElementById('dashboard');
const welcomeLabel = document.getElementById('welcomeLabel');
const studentMeta = document.getElementById('studentMeta');
const logoutBtn = document.getElementById('logoutBtn');
const chatForm = document.getElementById('chatForm');
const chatWindow = document.getElementById('chatWindow');
const chatInput = document.getElementById('chatInput');
const attendanceStat = document.getElementById('attendanceStat');
const resultStat = document.getElementById('resultStat');
const feeStat = document.getElementById('feeStat');
const assignmentStat = document.getElementById('assignmentStat');

function addMessage(text, who = 'bot') {
  const el = document.createElement('div');
  el.className = `message ${who}`;
  el.textContent = text;
  chatWindow.appendChild(el);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

async function fetchJson(url, options = {}) {
  const response = await fetch(url, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  });
  return response.json();
}

async function login(event) {
  event.preventDefault();
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  const result = await fetchJson(`${API_BASE}/auth/login`, {
    method: 'POST',
    body: JSON.stringify({ email, password }),
  });

  if (result.success) {
    currentStudent = result.student;
    loginCard.classList.add('hidden');
    dashboard.classList.remove('hidden');
    welcomeLabel.textContent = `Welcome ${currentStudent.name}`;
    studentMeta.textContent = `${currentStudent.roll_number} • ${currentStudent.branch} • Semester ${currentStudent.semester}`;
    loginMessage.textContent = '';
    await loadDashboardData();
  } else {
    loginMessage.textContent = result.message;
  }
}

async function loadDashboardData() {
  const [attendance, marks, fees, assignments] = await Promise.all([
    fetchJson(`${API_BASE}/student/attendance?student_id=${currentStudent.student_id}`),
    fetchJson(`${API_BASE}/student/marks?student_id=${currentStudent.student_id}`),
    fetchJson(`${API_BASE}/student/fees?student_id=${currentStudent.student_id}`),
    fetchJson(`${API_BASE}/student/assignments`),
  ]);

  attendanceStat.textContent = `Attendance: ${attendance.data.length} subjects`;
  resultStat.textContent = `Marks: ${marks.data.length} subjects`;
  feeStat.textContent = `Fees: ₹${fees.data[0]?.remaining ?? 0} pending`;
  assignmentStat.textContent = `Assignments: ${assignments.data.length}`;
}

async function sendQuestion(question) {
  addMessage(question, 'user');
  const result = await fetchJson(`${API_BASE}/chat/ask`, {
    method: 'POST',
    body: JSON.stringify({ student_id: currentStudent.student_id, question }),
  });
  addMessage(result.answer, 'bot');
}

loginForm.addEventListener('submit', login);
chatForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  const question = chatInput.value.trim();
  if (!question) return;
  await sendQuestion(question);
  chatInput.value = '';
});

document.querySelectorAll('[data-question]').forEach((button) => {
  button.addEventListener('click', () => sendQuestion(button.dataset.question));
});

logoutBtn.addEventListener('click', () => {
  currentStudent = null;
  dashboard.classList.add('hidden');
  loginCard.classList.remove('hidden');
  chatWindow.innerHTML = '<div class="message bot">Hello Samarth 👋 How can I help?</div>';
});
