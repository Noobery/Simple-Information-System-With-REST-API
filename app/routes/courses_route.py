from flask import Blueprint, render_template, request, jsonify, flash, redirect
import requests  # Import the requests module

courses = Blueprint('courses', __name__)

@courses.route('/course-list', methods=['GET'])
def display_courses():
    try:
        # Make a GET request to the RESTful server's /courses endpoint
        response = requests.get('http://127.0.0.1:5001/courses')  # Use requests.get for making HTTP requests
        print(response)
        # Check if the request was successful
        if response.status_code == 200:
            # Extract courses data from the response
            courses_data = response.json().get('Message')
            # Render a template with the courses data
            print(courses_data)
            return render_template('courses.html', courses=courses_data)
        else:
            # Handle errors if the request was not successful
            return render_template('courses.html', message="Failed to fetch courses data")
    except Exception as e:
        # Handle exceptions
        return render_template('courses.html', message=str(e))

@courses.route('/add-course', methods=['POST'])
def add_course():
    try:
        # Extract course data from the form
        course_name = request.form.get('courseName')
        
        # Construct the course data dictionary
        course_data = {"course": course_name}
        
        # Make a POST request to the RESTful server's /course endpoint
        response = requests.post('http://127.0.0.1:5001/course', json=course_data)
        
        # Check if the request was successful
        if response.status_code == 200:  # Assuming 200 indicates successful creation
            flash('Course added successfully', 'success')
        else:
            flash('Failed to add course', 'error')
    except Exception as e:
        # Handle exceptions
        flash('Failed to add course: ' + str(e), 'error')

    return redirect('/course-list')

@courses.route('/course/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    try:
        # Make a DELETE request to the RESTful server's /course endpoint
        response = requests.delete(f'http://127.0.0.1:5001/course/{course_id}')
        
        # Check if the request was successful
        if response.status_code == 200:
            return jsonify({"status": "ok", "message": "Course deleted successfully"})
        else:
            return jsonify({"status": "error", "message": "Failed to delete course"})
    except Exception as e:
        # Handle exceptions
        return jsonify({"status": "error", "message": str(e)})

@courses.route('/course/<int:course_id>', methods=['PUT'])
def edit_course(course_id):
    try:
        # Extract the new course name from the request
        new_course_name = request.json.get('courseName')

        # Make a PUT request to the RESTful server's /course endpoint
        response = requests.put(f'http://127.0.0.1:5001/course/{course_id}', json={'course': new_course_name})
        
        # Check if the request was successful
        if response.status_code == 200:
            return jsonify({"status": "ok", "message": "Course updated successfully"})
        else:
            return jsonify({"status": "error", "message": "Failed to update course"})
    except Exception as e:
        # Handle exceptions
        return jsonify({"status": "error", "message": str(e)})


@courses.route("/")
def index():
    return redirect("/course-list")
