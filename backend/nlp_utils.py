from textblob import TextBlob
import openai

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return {
        "polarity": sentiment.polarity,
        "subjectivity": sentiment.subjectivity
    }

def generate_response(user_input):
    prompt = f"The user is feeling stressed or anxious. They said: '{user_input}'. Provide an empathetic response and suggest short-term and long-term actions to help them."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()