from fpdf import FPDF
import io

def generate_resume(details):
    pdf = FPDF()
    pdf.add_page()

    # Title
    name = details.get('name', 'Unnamed')
    profile_title = details.get('profile_title', 'No Profile Title Provided')

    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=name, ln=True, align='C')

    pdf.set_font("Arial", '', 12)
    pdf.cell(200, 10, txt=profile_title, ln=True, align='C')

    pdf.ln(10)

    # Personal Profile
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="PERSONAL PROFILE", ln=True, align='L')

    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, details.get('personal_profile', 'No personal profile provided'))

    pdf.ln(5)

    # Internship Experience
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="INTERNSHIP EXPERIENCE", ln=True, align='L')

    pdf.set_font("Arial", '', 12)
    internships = details.get('internships', [])
    for internship in internships:
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, txt=f"{internship['title']}, {internship['company']} ({internship['date_range']})", ln=True, align='L')
        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(0, 10, internship['description'])

    pdf.ln(5)

    # Skills and Abilities
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="SKILLS AND ABILITIES", ln=True, align='L')

    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, ", ".join(details.get('skills', [])))

    pdf.ln(5)

    # Academic Profile
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="ACADEMIC PROFILE", ln=True, align='L')

    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, f"{details.get('university', 'Unknown University')} - {details.get('degree', 'Unknown Degree')} (CGPA: {details.get('cgpa', 'N/A')})")

    pdf.ln(5)

    # Positions of Responsibility
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="POSITIONS OF RESPONSIBILITY", ln=True, align='L')

    pdf.set_font("Arial", '', 12)
    positions = details.get('positions', [])
    for position in positions:
        pdf.multi_cell(0, 10, f"{position['role']}, {position['organization']} ({position['date_range']})")

    pdf.ln(5)

    # Projects
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="PROJECTS", ln=True, align='L')

    pdf.set_font("Arial", '', 12)
    projects = details.get('projects', [])
    for project in projects:
        pdf.multi_cell(0, 10, f"{project['title']}: {project['description']}")

    pdf.ln(5)

    # Contact Information
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="CONTACT INFORMATION", ln=True, align='L')

    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, f"Email: {details.get('email')}\nLinkedIn: {details.get('linkedin')}\nPhone: {details.get('phone')}")

    return pdf.output(dest='S').encode('latin1')  # Return PDF as a byte string
