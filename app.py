# ===========================
# Imports and Setup
# ===========================
from flask import Flask, render_template, request, flash, jsonify
from datetime import datetime
from dotenv import load_dotenv
import openai
import os

# Load environment variables from .env
load_dotenv()

# Set your OpenAI API key securely
openai.api_key = os.getenv("OPENAI_API_KEY")

# ===========================
# Initialize Flask App
# ===========================
app = Flask(__name__)
app.secret_key = '123'  # Needed for flash messages

# ===========================
# Route: Home Form Page
# ===========================
@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

# ===========================
# Route: Resume Preview
# ===========================
@app.route('/resume', methods=['POST'])
def resume():
    name = request.form['name']
    email = request.form['email']
    summary = request.form['summary']
    skills = request.form['skills'].split(',')
    job_title = request.form['job_title']
    experience = request.form['experience']
    education = request.form['education']
    linkedin = request.form['linkedin']

    timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    flash('Resume generated successfully!')

    return render_template(
        'resume.html',
        name=name,
        email=email,
        summary=summary,
        skills=skills,
        job_title=job_title,
        experience=experience,
        education=education,
        linkedin=linkedin,
        timestamp=timestamp
    )

# ===========================
# Route: Generate Summary with OpenAI
# ===========================
@app.route('/generate-summary', methods=['POST'])
def generate_summary():
    data = request.get_json()
    job_title = data.get('job_title', '')
    experience = data.get('experience', '')

    prompt = (
        f"Write a professional, concise summary for a resume. "
        f"The person is applying for a job as a {job_title} and has the following work experience:\n{experience}"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{ "role": "user", "content": prompt }],
            temperature=0.7,
            max_tokens=150
        )
        summary = response['choices'][0]['message']['content'].strip()
        return jsonify({'summary': summary})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ===========================
# Run App
# ===========================
if __name__ == '__main__':
    app.run(debug=True)
