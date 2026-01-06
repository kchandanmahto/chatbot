import os
from fastapi import FastAPI, Request, HTTPException
from twilio.twiml.messaging_response import MessagingResponse
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    api_key=os.getenv('GROQ_API_KEY')
)

# Create CrewAI Agent
chat_agent = Agent(
    role="Chatbot Assistant",
    goal="Respond helpfully to user messages in a conversational manner.",
    backstory="You are a friendly AI chatbot powered by Groq, ready to assist with any questions or conversations.",
    llm=llm,
    verbose=True
)

# Create FastAPI app
app = FastAPI()

@app.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    # Parse incoming message
    form_data = await request.form()
    incoming_msg = form_data.get('Body', '').strip()
    from_number = form_data.get('From', '')

    if not incoming_msg:
        raise HTTPException(status_code=400, detail="No message body")

    # Create a task for the agent
    chat_task = Task(
        description=f"Respond to the user's message: {incoming_msg}",
        agent=chat_agent,
        expected_output="A helpful response to the user's message."
    )

    # Create crew and run
    crew = Crew(
        agents=[chat_agent],
        tasks=[chat_task],
        verbose=True
    )

    result = crew.kickoff()

    # Prepare response
    resp = MessagingResponse()
    resp.message(str(result))

    return str(resp)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)