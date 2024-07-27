$(document).ready(function() {
    $('.delete-course').click(function(event) {
        event.preventDefault();
        var courseId = $(this).find('i').data('course-id'); // Adjust selector to find the icon element
        console.log(courseId);

        if (confirm('Are you sure you want to delete this course?')) {
            // Send a DELETE request using AJAX
            $.ajax({
                type: 'DELETE',
                url: '/course/' + courseId,
                success: function(response) {
                    if (response.status === 'ok') {
                        // Remove the deleted row from the UI or perform any other action
                        $(event.target).closest('tr').remove();
                        alert('Course deleted successfully.');
                    } else {
                        alert('Failed to delete the course: ' + response.message);
                    }
                },
                error: function() {
                    alert('Failed to delete the course.');
                }
            });
        }
    });
    const editButtonsCourse = document.querySelectorAll('.edit-course');
    editButtonsCourse.forEach(button => {
        button.addEventListener('click', () => {
       
            const courseName = button.getAttribute('data-course-name');
            const editCourseNameField = document.getElementById('editCourseName');
            editCourseNameField.value = courseName;
           
        });
    });

    
    

    
    

});

$('.edit-course').click(function() {
    var courseId = $(this).data('course-id');
    console.log(courseId);
    
    // Set the courseId value in a hidden input field inside the editCourseForm
    $('#editCourseId').val(courseId);
});

$('#editCourseForm').submit(function(e) {
    e.preventDefault();
    var courseId = $('#editCourseId').val();
    console.log(courseId);
    var newCourseName = $(this).find('#editCourseName').val();
    console.log(newCourseName)
    
    // Save the reference to the row
    const row = document.querySelector(`#course-row-${courseId}`);

    // Send a PUT request using AJAX
    $.ajax({
        type: 'PUT',
        url: '/course/' + courseId,
        contentType: 'application/json',
        data: JSON.stringify({ courseName: newCourseName }),
        success: function(response) {
            if (response.status === 'ok') {
                alert('Course updated successfully.');
                
                $('#editCourseModal').modal('hide'); // Hide the modal after successful update
                
                // Update the UI with the new course name
                row.querySelector("#course-name").textContent = newCourseName;
            } else {
                alert('Failed to update the course: ' + response.message);
            }
        },
        error: function() {
            alert('Failed to update the course.');
        }
    });
});
