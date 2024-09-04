// main.js

$(document).ready(function() {
    // Function to add new internship fields
    $('#addInternship').click(function() {
        $('#internships').after('<textarea name="internships[]" rows="4" class="w-full px-3 py-2 border rounded-lg focus:outline-none mt-4" placeholder="Example: Title, Company, Date Range, Description" required></textarea>');
    });

    // Function to add new skill fields
    $('#addSkill').click(function() {
        $('#skills').after('<textarea name="skills[]" rows="2" class="w-full px-3 py-2 border rounded-lg focus:outline-none mt-4" placeholder="Separate each skill with a comma, e.g., Python, Machine Learning, Data Analysis" required></textarea>');
    });

    // Function to add new position fields
    $('#addPosition').click(function() {
        $('#positions').after('<textarea name="positions[]" rows="4" class="w-full px-3 py-2 border rounded-lg focus:outline-none mt-4" placeholder="Example: Role, Organization, Date Range" required></textarea>');
    });

    // Function to add new project fields
    $('#addProject').click(function() {
        $('#projects').after('<textarea name="projects[]" rows="4" class="w-full px-3 py-2 border rounded-lg focus:outline-none mt-4" placeholder="Example: Title, Description" required></textarea>');
    });

    // Simple form validation before submission
    $('#resumeForm').submit(function(event) {
        let valid = true;

        // Basic validation
        $('input, textarea').each(function() {
            if ($(this).val() === '') {
                valid = false;
                $(this).addClass('border-red-500');
            } else {
                $(this).removeClass('border-red-500');
            }
        });

        if (!valid) {
            alert('Please fill in all fields.');
            event.preventDefault();
        }
    });
});
