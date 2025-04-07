# Import the required Flask functions
from flask import Flask, render_template, request, flash

# Create the Flask app instance
app = Flask(__name__)
app.secret_key = '123'  # can be any random string


# Route for the homepage (form)
@app.route('/', methods=['GET', 'POST'])
def form():
    # Render the HTML form
    return render_template('form.html')

# Route to handle the form submission and show resume preview
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

    from datetime import datetime
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

# Run the app when this file is executed
if __name__ == '__main__':
    app.run(debug=True)  # Starts the development server
