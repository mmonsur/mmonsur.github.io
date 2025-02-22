import openai
import os
from dotenv import load_dotenv
from flask import Flask, request, render_template

# Load environment variables
load_dotenv()

# Get OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Flask app
app = Flask(__name__, template_folder=".")

# Function to get response from ChatGPT API
def get_chatgpt_response(user_message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Flask route to render index.html from root
@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = get_chatgpt_response(user_input)
    return render_template("index.html", response=response)

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
