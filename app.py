# Import the required Flask functions
from flask import Flask, render_template, request

# Create the Flask app instance
app = Flask(__name__)

# Route for the homepage (form)
@app.route('/')
def form():
    # Render the HTML form
    return render_template('form.html')

# Route to handle the form submission and show resume preview
@app.route('/resume', methods=['POST'])
def resume():
    # Get the submitted form data from the user
    name = request.form['name']
    email = request.form['email']
    summary = request.form['summary']
    skills = request.form['skills'].split(',')  # Turn comma-separated skills into a list

    # Render the resume preview page with the submitted info
    return render_template(
        'resume.html',
        name=name,
        email=email,
        summary=summary,
        skills=skills
    )

# Run the app when this file is executed
if __name__ == '__main__':
    app.run(debug=True)  # Starts the development server
