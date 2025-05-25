# StudBud – ATLAS SkillTech Placement Assistant

StudBud is a web-based AI-powered placement assistant built as a Pinnacle 3 project at ATLAS SkillTech University. It helps students generate professional resumes, find internships, and receive AI-driven answers to placement-related queries.

> Developed by: Leisha Totani and Mohit Bhimrajka  
> Mentor: Prof. Shashikant Patil  
> In collaboration with: Placement Cell, ATLAS (Mr. Sagar Nichani)

---

## 🌟 Features

- 🎓 **AI Chatbot for Placement Queries** – Answers placement-related questions using LLM powered by Ollama.
- 📄 **Resume Generator** – Create customized resumes in PDF format based on ATLAS formatting standards.
- 💼 **Internship Finder** – Browse available internships and express interest.
- 🧠 **Custom LLM** – Trained with system prompts and deployed locally using Ollama (`Modelfile`).

---

## 🧾 Directory Structure

```

mohitbhimrajka-studbud/
├── app.py                    # Main Flask application
├── chatbot.py                # Placeholder for future chatbot logic
├── internships.py            # Dummy internship data
├── llm.py                    # Custom prompt handling via Ollama
├── resume\_builder.py         # Generates PDF resumes using fpdf
├── Modelfile                 # Configuration for Ollama LLM
├── requirements.txt          # Project dependencies
├── LICENSE                   # Apache License 2.0
├── static/                   # Static assets
│   ├── css/style.css
│   ├── js/main.js
│   └── pdf/
├── templates/                # HTML pages (Jinja2 templates)
│   ├── index.html
│   ├── internship\_finder.html
│   └── resume\_generator.html
└── README.md                 # 📘 You're here!

````

---

## 🚀 Getting Started

### 🧰 Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running locally
- Virtual Environment (recommended)

### 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/mohitbhimrajka-studbud.git
cd mohitbhimrajka-studbud

# Create and activate virtual environment (Windows)
python -m venv bud
.\bud\Scripts\Activate.ps1

# Set execution policy if activation fails
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# Install dependencies
pip install -r requirements.txt
````

---

## 🧪 Running the Application

1. **Start your Ollama model**
   Ensure `studbud` model is available and served on `localhost:11434`.

2. **Run the Flask server**

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

---

## 💡 Usage Overview

* `/` – Homepage with chatbot interface
* `/resume-generator` – Fill in your details to generate a resume
* `/internship-finder` – View and express interest in available internships

---

## 🧠 About the AI Model

StudBud uses [LangChain](https://www.langchain.com/) to interact with a locally hosted LLM (via Ollama). The model responds professionally to queries using a structured system prompt defined in the `Modelfile`.

---

## 📄 License

This project is licensed under the Apache License 2.0 – see the [LICENSE](./LICENSE) file for details.

---

## 🙌 Acknowledgements

* ATLAS SkillTech University
* Prof. Shashikant Patil (Mentor)
* Mr. Sagar Nichani (Placement Cell Head)
* TailwindCSS, jQuery, Flask, LangChain, Ollama

---
