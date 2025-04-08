# Import necessary Flask modules
from flask import Flask, render_template, request, flash

# Create a new Flask app instance
app = Flask(__name__)
app.secret_key = '123'  # Secret key is required for flashing messages (temporary alerts)

# ---------------------------------------
# Route: Homepage (form)
# ---------------------------------------
@app.route('/', methods=['GET', 'POST'])
def form():
    # Show the form on GET; POST is allowed but not used here directly
    return render_template('form.html')

# ---------------------------------------
# Route: Resume preview (after form submission)
# ---------------------------------------
@app.route('/resume', methods=['POST'])
def resume():
    # Collect form input values
    name = request.form['name']
    email = request.form['email']
    summary = request.form['summary']
    skills = request.form['skills'].split(',')  # Convert comma-separated string to list
    job_title = request.form['job_title']
    experience = request.form['experience']
    education = request.form['education']
    linkedin = request.form['linkedin']

    # Get current timestamp to show when resume was generated
    from datetime import datetime
    timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")

    # Show success message (displayed in resume.html)
    flash('Resume generated successfully!')

    # Render the resume preview template with the submitted data
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

# ---------------------------------------
# Run the Flask app (development mode)
# ---------------------------------------
if __name__ == '__main__':
    app.run(debug=True)  # Starts the app with debug mode enabled for live updates
