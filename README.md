# Groq WhatsApp Chatbot

A WhatsApp chatbot using Groq Cloud LLM and CrewAI, built with FastAPI.

## Setup

1. Sign up for Groq Cloud at https://console.groq.com/ and get your API key.
2. Sign up for Twilio at https://www.twilio.com/ and enable WhatsApp.
3. Replace `your_groq_api_key_here` in the `.env` file with your Groq API key.
4. Add your Twilio credentials to `.env`:
   ```
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_WHATSAPP_NUMBER=your_twilio_whatsapp_number
   ```

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Chatbot

Run the FastAPI server:

```bash
python chatbot.py
```

Or with uvicorn:

```bash
uvicorn chatbot:app --host 0.0.0.0 --port 8000
```

## WhatsApp Setup

1. In your Twilio console, set the webhook URL for incoming messages to: `https://your-domain.com/whatsapp`
2. For local testing, use ngrok to expose your local server: `ngrok http 8000`
3. Update the webhook URL in Twilio to the ngrok URL.

## Usage

Send messages to your Twilio WhatsApp number, and the CrewAI agent will respond using Groq LLM.