from flask import Flask, render_template, request
from analyzer import analyze_resume
import os
from werkzeug.utils import secure_filename
from utils import extract_text_from_file

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        file = request.files['resume']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            text = extract_text_from_file(filepath)
            result = analyze_resume(text)
        else:
            result = "Unsupported file type. Please upload a .txt, .pdf, or .docx file."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
