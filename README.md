# 🚨 RecallOps Agent

> An AI-powered production incident response agent equipped with **Hindsight** persistent memory. It stops repeating past mistakes by automatically recalling historical post-mortems, root causes, and runbooks.

---

## 💡 What Problem Does This Solve?

Traditional AI assistants and chatbots suffer from **production amnesia**. Every time an incident occurs or a new chat session starts, they treat it as a blank slate—forgetting past organizational knowledge, previous failures, and team-tested fixes. 

**RecallOps** bridges this gap by integrating **Hindsight Cloud**, a dedicated memory layer for AI agents. 
* **Recall:** When a new incident strikes, the agent instantly queries historical memory to find similar past failures and surface proven runbooks.
* **Retain:** Once resolved, engineers feed the post-mortem back into the agent so that future identical incidents trigger the correct fix automatically.

---

## 🏗️ System Architecture

RecallOps is built with a lightweight, decoupled stack:
* **Frontend:** Clean Tailwind CSS dashboard for live incident triage and memory retention[cite: 1].
* **Backend:** Python Flask server handling API endpoints and coordination[cite: 1].
* **Reasoning Layer:** Groq LLM API generating fast, contextual operational guidance[cite: 1].
* **Memory Layer:** Hindsight Cloud (`hindsight-client`) acting as the persistent operational brain[cite: 1, 2].

```text
[ Engineering UI ] 
       │
       ▼ (HTTP Requests)
   [ Flask App ] ──► [ Groq LLM (Reasoning) ]
       │
       ├─────────────────────────┐
       ▼                         ▼
[ Hindsight Cloud ]       [ Hindsight Cloud ]
   (Recall Memory)          (Retain Post-Mortem)
```
# 🚀 Getting Started
## 1. Clone the Repository
git clone [https://github.com/RuthvikaReddy256/Incident_Response_Agent.git](https://github.com/RuthvikaReddy256/Incident_Response_Agent.git)
cd incident-response-agent

## 2. Set Up a Virtual Environment & Install Dependencies
* On Windows:
python -m venv venv
* On macOS/Linux:
venv\Scripts\activate

source venv/bin/activate

pip install -r requirements.txt
## 3. Configure Your Environment Variables
Create a .env file in the root directory and add your API keys:
## 4.Run the application
python app.py


Open your browser and navigate to: http://127.0.0.1:5000

# 🖥️ Usage Guide
Teach the Agent (Retain Memory):

Scroll down to the Teach Agent section on the UI.

Input a past incident (e.g., Incident ID: INC-1042, Service: Payment API, Root Cause: Database connection pool exhaustion).

Click Retain into Hindsight Memory[cite: 1].

Triage a New Incident (Recall & Reason):

Go to the Triage New Production Incident section at the top[cite: 1].

Enter a similar failure scenario for the Payment API[cite: 1].

Click Investigate with Hindsight Memory to watch the agent pull up the exact historical match and generate an instant runbook[cite: 1].

#📦 Project Structure
```text
incident-response-agent/
├── app.py                      # Flask web server entry point
├── requirements.txt            # Project dependencies
├── .gitignore                  
├── backend/
│   ├── __init__.py             # Package initializer
│   ├── agent.py                # Groq LLM prompt logic & orchestration
│   └── memory_service.py       # Hindsight Cloud retain/recall client wrapper
└── templates/
    └── index.html              # Tailwind CSS frontend dashboard

```
# 🔗 Resources & References
[Hindsight GitHub Repository](https://github.com/vectorize-io/hindsight
)

[cite: 1, 2]

[Hindsight Documentation](https://github.com/vectorize-io/hindsight)


[cite: 1, 2]

[Vectorize Agent Memory Overview](https://vectorize.io/what-is-agent-memory)
