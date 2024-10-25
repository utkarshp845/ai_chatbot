from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)

# Set your OpenAI API key
  # Ensure you have your API key set in environment variables

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get("message")

    # Call OpenAI API to get chatbot response
    try:
        response = client.chat.completions.create(model="gpt-4o-mini",  # Or use another available model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ],
        max_tokens=150)
        message = response.choices[0].message.content
        return jsonify({"response": message})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
