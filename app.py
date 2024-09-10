import os
from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from image_compression import compress_image  # Absolute import

app = Flask(__name__)

# Path to store uploaded and compressed images temporarily
UPLOAD_FOLDER = 'static/uploads/'
COMPRESSED_FOLDER = 'static/compressed/'

# Allowed image extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['COMPRESSED_FOLDER'] = COMPRESSED_FOLDER

# Check if the file is an allowed type
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Compress the image
            compressed_filename = f"compressed_{filename}"
            compressed_path = os.path.join(app.config['COMPRESSED_FOLDER'], compressed_filename)
            compress_image(file_path, compressed_path)  # Call the imported function

            # Provide the compressed image as a download
            return send_file(compressed_path, as_attachment=True, download_name=compressed_filename)

    return render_template('index.html')

@app.after_request
def delete_files(response):
    # Clean up uploaded files
    upload_folder = app.config['UPLOAD_FOLDER']
    try:
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        for filename in os.listdir(upload_folder):
            file_path = os.path.join(upload_folder, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
    except Exception as e:
        app.logger.error(f"Error deleting files in {upload_folder}: {e}")

    # Clean up compressed files
    compressed_folder = app.config['COMPRESSED_FOLDER']
    try:
        if not os.path.exists(compressed_folder):
            os.makedirs(compressed_folder)
        for filename in os.listdir(compressed_folder):
            file_path = os.path.join(compressed_folder, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
    except Exception as e:
        app.logger.error(f"Error deleting files in {compressed_folder}: {e}")

    return response

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(COMPRESSED_FOLDER, exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
