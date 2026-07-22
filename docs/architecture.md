# System Architecture

## High-Level Layers

1. Frontend UI
   - HTML/CSS/JavaScript dashboard
   - Chat interface for student support questions

2. Backend API
   - FastAPI endpoints for auth, profile, attendance, marks, fees, notices, and chatbot question handling

3. Business Logic
   - Intent detection for natural-language student questions
   - Rule-based retrieval for structured data + lightweight RAG-style knowledge lookup

4. Data Layer
   - Demo data in Python for local prototype
   - Planned PostgreSQL/MySQL schema in `database/schema.sql`

## Future Enhancements

- Add JWT-based auth
- Add real vector DB with FAISS and embeddings
- Store documents in PDF and knowledge-base folders
- Add admin management panel
- Deploy frontend on Vercel and backend on Render or Azure
