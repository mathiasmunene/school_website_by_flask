from flask import Flask, send_from_directory, render_template, request
import os

app = Flask(__name__)

# Define the directory where your images are stored (project root)
UPLOAD_FOLDER = os.path.abspath('.')  # Points to school_website_by_flask/
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return "<p>Hello Moringa World</p>"

@app.route('/courses')
def courses():
    return "This is the courses page"

@app.route('/courses/<int:course_id>')
def course_details(course_id):
    return f'This is course id is: {course_id}'

# Route to serve images
@app.route('/courses/<path:course_file>')
def course_file(course_file):
    # Extract filename for serving
    filename = os.path.basename(course_file)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        image_url = f"/serve_image/{filename}"
        return render_template('image.html', image_url=image_url)
    return "File not found", 404

@app.route('/serve_image/<path:filename>')
def serve_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Route for course name (original)
@app.route('/courses/<course_name>')
def course_name(course_name):
    return f'This is course name is : {course_name}'

# New route for course details with query parameters
@app.route('/course_details')
def course_details_query():
    c_name = request.args.get('name')
    c_date = request.args.get('date')
    return f'This is course {c_name} created on date: ==> {c_date}'

@app.route('/about')
def about():
    return "About"

@app.route('/contact')
def contact():
    return "contact"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)