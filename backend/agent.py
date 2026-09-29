import os
from dotenv import load_dotenv
from groq import Groq
from backend.memory_service import recall_memories, retain_memory

# Load environment variables explicitly
load_dotenv()

# Verify API key is present
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is missing from environment variables or .env file.")

# Initialize Groq client safely
groq_client = Groq(api_key=api_key)
GROQ_MODEL = "openai/gpt-oss-120b"  # Fast, highly performant model option

def analyze_incident(service, symptoms, error_logs):
    """
    1. Recalls similar historical incidents using Hindsight.
    2. Sends context + current incident to Groq LLM to generate recommendations.
    """
    query_string = f"Service: {service}. Symptoms: {symptoms}. Error logs: {error_logs}"
    historical_matches = recall_memories(query_string)
    
    formatted_history = "\n".join([f"- {m}" for m in historical_matches]) if historical_matches else "No direct historical match found in memory."

    prompt = f"""
You are an expert Production Incident Response Agent. 
A new incident has occurred:
- Service: {service}
- Symptoms: {symptoms}
- Error Logs: {error_logs}

Here is relevant historical experience recalled from Hindsight memory:
{formatted_history}

Based on this historical memory (if available) and your technical reasoning, provide:
1. Likely Root Cause
2. Recommended Fix
3. Step-by-Step Runbook
4. Why this recommendation works based on past learnings.

Format your response clearly with headings.
"""

    chat_completion = groq_client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful DevOps incident assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=1024
    )
    
    agent_response = chat_completion.choices[0].message.content

    return {
        "historical_matches": historical_matches,
        "recommendation": agent_response
    }

def process_resolution(data):
    """
    Captures post-resolution feedback and retains it into Hindsight.
    """
    incident_id = data.get("incident_id")
    service = data.get("service")
    root_cause = data.get("root_cause")
    fix_applied = data.get("fix_applied")
    lesson = data.get("lesson", "")

    memory_content = (
        f"Incident ID: {incident_id} | Service: {service} | "
        f"Root Cause: {root_cause} | Fix Applied: {fix_applied} | "
        f"Lessons Learned: {lesson}"
    )

    success = retain_memory(memory_content, context_label="post_mortem_learning")
    return {"retained": success, "content_stored": memory_content}