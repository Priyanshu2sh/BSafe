import requests
import re
from django.conf import settings



# Format response into bullet points
def format_response_as_points(text):
    # Find steps like 1., 2., 3.
    steps = re.findall(r"(\d+\.\s.*?)(?=\d+\.|\Z)", text, re.DOTALL)

    if not steps:
        # Fallback: split by newlines or periods
        steps = re.split(r"\n+|\.\s+", text)

    # Remove empty strings and strip
    cleaned_steps = [step.strip() for step in steps if step.strip()]
    return cleaned_steps

# Mistral API query function
def query_mistral(prompt, context, history=None):
    # Build history string
    history_str = ""
    if history:
        for h in history:
            history_str += f"User: {h['user']}\nAssistant: {h['bot']}\n"
    history_str += f"User: {prompt}\n"

    full_prompt = (
        "You are a polite, helpful assistant. "
        "For greetings, goodbyes, and general conversation, answer naturally using your general knowledge. "
        "For all other questions, use the information provided below if relevant. "
        "If you do not know the answer, reply exactly: 'Sorry, the answer is not available.'\n\n"
        "Do not mention the provided document or its contents directly.\n\n"
        f"{context}\n\n"
        f"Conversation history:\n{history_str}"
    )

    api_url = "https://api.mistral.ai/v1/chat/completions"
    api_key = settings.MISTRAL_API_KEY  # Replace with your secure key
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistral-tiny",
        "messages": [
            {"role": "user", "content": full_prompt}
        ],
        "temperature": 0.2
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()
        answer = response.json()["choices"][0]["message"]["content"].strip()
        return answer
    except Exception as e:
        answer = f"Error communicating with Mistral API: {e}. Sorry, I could not get a response from the chatbot server."
        return answer


