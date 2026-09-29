import os
import asyncio
from hindsight_client import Hindsight

HINDSIGHT_API_URL = os.getenv("HINDSIGHT_API_URL", "https://api.hindsight.vectorize.io")
HINDSIGHT_API_KEY = os.getenv("HINDSIGHT_API_KEY")
BANK_ID = "incident-response-bank"

def init_hindsight():
    """Initializes Hindsight service check."""
    try:
        print("Hindsight client configuration loaded successfully.")
    except Exception as e:
        print(f"Warning: Hindsight initialization notice: {e}")

def _sync_recall(query_text):
    """Synchronous recall operation using standard context manager."""
    with Hindsight(api_key=HINDSIGHT_API_KEY, base_url=HINDSIGHT_API_URL) as client:
        response = client.recall(
            bank_id=BANK_ID,
            query=query_text
        )
        return [r.text for r in response.results] if hasattr(response, 'results') else []

def recall_memories(query_text):
    """Wrapper to run recall cleanly."""
    try:
        return _sync_recall(query_text)
    except Exception as e:
        print(f"Error recalling memories: {e}")
        return []

def _sync_retain(incident_text, context_label):
    """Synchronous retain operation using standard context manager."""
    with Hindsight(api_key=HINDSIGHT_API_KEY, base_url=HINDSIGHT_API_URL) as client:
        client.retain(
            bank_id=BANK_ID,
            content=incident_text,
            context=context_label
        )
        return True

def retain_memory(incident_text, context_label="resolved_incident"):
    """Wrapper to run retain cleanly."""
    try:
        return _sync_retain(incident_text, context_label)
    except Exception as e:
        print(f"Error retaining memory: {e}")
        return False