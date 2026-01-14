import pandas as pd
import sqlite3
import os
import time
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_ID = "gemini-2.5-flash" 
client = genai.Client(api_key=API_KEY)
# ================= SYSTEM BRAINS =================
SYSTEM_INSTRUCTION = """
You are a High-Level Business Strategist. You have two main powers:
1. CODE EXECUTION: Use this to analyze the user's 'inventory.db' or Excel files for profit/trends.
2. GOOGLE SEARCH: Use this to check local market trends, prices, and location-based advice.

When the user asks 'what should I buy?', search the web for their location and run code to 
check their current stock before answering.
"""

def get_db_context():
    """Gives the AI a quick summary of what is in the database."""
    if not os.path.exists("inventory.db"): return "No database found."
    conn = sqlite3.connect("inventory.db")
    df = pd.read_sql("SELECT * FROM inventory", conn)
    conn.close()
    return f"Current Inventory Data:\n{df.to_string()}"

def ask_ai_pro(user_input):
    context = get_db_context()
    full_prompt = f"USER LOCATION: Karachi, Pakistan\n\nDATA:\n{context}\n\nUSER REQUEST: {user_input}"

    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=full_prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                tools=[
                    types.Tool(google_search=types.GoogleSearch()),
                    types.Tool(code_execution=types.ToolCodeExecution)
                ]
            )
        )
        return response.text
    except Exception as e:
        if "429" in str(e):
            return "⚠️ AI is busy (Rate Limit). Please wait 60 seconds."
        return f"❌ Error: {str(e)}"

# ================= MAIN LOOP =================
if __name__ == "__main__":
    print("💎 Business Intelligence AI Active.")
    print("Ask: 'What should I restock for max profit next month?'")
    
    while True:
        user_query = input("\nYou: ").strip()
        if user_query.lower() in ["exit", "quit"]: break
        
        print("AI is analyzing your data and searching the web...")
        answer = ask_ai_pro(user_query)
        print(f"\nAI: {answer}")