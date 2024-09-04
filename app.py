from flask import Flask, render_template, request, send_file, jsonify
from resume_builder import generate_resume
from internships import get_dummy_internships
from llm import get_generated_text  # Ensure this import is correct

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resume-generator')
def resume_generator():
    return render_template('resume_generator.html')

@app.route('/internship-finder')
def internship_finder():
    internships = get_dummy_internships()
    return render_template('internship_finder.html', internships=internships)

@app.route('/generate-resume', methods=['POST'])
def generate_resume_route():
    try:
        details = {
            'name': request.form['name'],
            'profile_title': request.form['profile_title'],
            'personal_profile': request.form.get('personal_profile', 'No profile provided'),
            'internships': request.form.getlist('internships[]'),  # Expecting a list
            'skills': request.form.getlist('skills[]'),
            'university': request.form.get('university', 'Unknown University'),
            'degree': request.form.get('degree', 'Unknown Degree'),
            'cgpa': request.form.get('cgpa', 'N/A'),
            'positions': request.form.getlist('positions[]'),
            'projects': request.form.getlist('projects[]'),
            'email': request.form['email'],
            'linkedin': request.form['linkedin'],
            'phone': request.form['phone'],
        }
        pdf_content = generate_resume(details)
        return send_file(
            io.BytesIO(pdf_content),
            mimetype='application/pdf',
            as_attachment=True,
            download_name='resume.pdf'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/query', methods=['POST'])
def query():
    user_query = request.form['query']
    context = "The placement season will start soon. Students should prepare their resumes and practice interview skills. The placement cell has over 1000 internships available."
    response = get_generated_text(user_query, context)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
