# Resume Analyzer

An AI-powered web application that analyzes a ** resume** and provides **detailed feedback** using **OpenAI GPT-3.5 Turbo**. Supports `.txt`, `.pdf`, and `.docx` files. Built with **Flask** and **Python**, designed for job seekers who want to optimize their resumes for better impact.

---

## Features

- Upload a resume file (.txt / .pdf / .docx)
- Automatically extracts text and analyzes it using OpenAI GPT
- Gives back actionable feedback (structure, content quality, clarity, etc.)
- Simple, user-friendly web interface
- Fast and accurate suggestions using GPT-3.5 Turbo

---

## Tech Stack

- **Backend**      : Python, Flask
- **Frontend**     : HTML, CSS
- **AI Engine**    : OpenAI GPT-3.5 Turbo
- **File Handling**: Python-docx, PyPDF2

---

## Project Structure


```
resume_analyzer/
├── pycache/
├── static/
│ └── styles.css
├── templates/
│ └── index.html
├── uploads/ # Temporarily stores uploaded files
├── app.py # Flask application entry point
├── analyzer.py # Resume parsing and GPT feedback logic
├── utils.py # File processing utility functions
├── requirements.txt # Required Python libraries
├── README.md # Project documentation

```
---

## Getting Started

### 1. Install dependencies:

pip install -r requirements.txt

### 2. Set your OpenAI API key:

```setx OPENAI_API_KEY "your-openai-api-key" ```(the key is set globally)
or
Set the key in local environment: ```$env:OPENAI_API_KEY = "openai-api-key"```

### 3. **Start the app**:

python app.py

### 4. **Open the server**:

Open your browser and go to http://127.0.0.1:5000

##  Notes

-Only one resume is analyzed at a time.
-The feedback is AI-generated and should be reviewed manually before applying changes.
-Make sure your OpenAI API key has access to GPT-3.5 Turbo.
-Uploaded files are stored temporarily in the uploads folder.
