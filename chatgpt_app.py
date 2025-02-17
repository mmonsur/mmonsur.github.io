import openai
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Flask app
app = Flask(__name__)

# Function to get response from ChatGPT API
def get_chatgpt_response(user_message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Change to "gpt-4" if needed
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150  # Adjust response length as needed
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Web interface
@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = get_chatgpt_response(user_input)
    return render_template("index.html", response=response)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
