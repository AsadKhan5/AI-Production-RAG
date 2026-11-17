
import os
from dotenv import load_dotenv
from langsmith import traceable

load_dotenv(override=True)

print("Tracing:", os.getenv("LANGSMITH_TRACING"))
print("API key configured:", bool(os.getenv("LANGSMITH_API_KEY")))
print("Project:", os.getenv("LANGSMITH_PROJECT"))
print("Endpoint:", os.getenv("LANGSMITH_ENDPOINT"))

@traceable(name="langsmith_connection_test")
def test_tracing():
    return {
        "status": "LangSmith tracing test successful"
    }

result = test_tracing()
print(result)
