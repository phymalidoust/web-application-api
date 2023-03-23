from flask import Flask, request, jsonify, render_template
import os
from werkzeug.utils import secure_filename
import datetime
import uuid

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/upload", methods=['POST'])
def upload():
    # check if the POST request contains files
    if 'xlsx-file' not in request.files:
        return jsonify({'error': 'No JSON files were uploaded.'}), 400

    # get the uploaded files
    xlsx_file = request.files['xlsx-file']
    if xlsx_file.filename == '':
        return jsonify({'error': 'No file was uploaded.'}), 400

    # check if the files have allowed extensions (e.g., .json)
    allowed_extensions = ['.xlsx']
    if not all(xlsx_file.filename.endswith(tuple(allowed_extensions)) for file in xlsx_file):
        return jsonify({'error': 'Only .xlsx files are allowed.'}), 400

    # generate unique filename
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
    unique_filename = str(uuid.uuid4())
    filename = secure_filename(f"{current_time}-{unique_filename}-{xlsx_file.filename}")

    # save the uploaded files to a temporary directory
    tmp_dir = './uploads'
    os.makedirs(tmp_dir, exist_ok=True)

    # generate a unique filename for the uploaded file
    file_path = os.path.join(tmp_dir, filename)
    while os.path.isfile(file_path):
        unique_filename = str(uuid.uuid4())
        filename = secure_filename(f"{current_time}-{unique_filename}-{xlsx_file.filename}")
        file_path = os.path.join(tmp_dir, filename)

    file_path = os.path.join(tmp_dir, filename)
    xlsx_file.save(file_path)

    # do something with the uploaded files (e.g., process and return some result)
    result = {'message': 'Files uploaded successfully.', 'file_path': file_path}
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(port='8000', debug="True")


# from flask import Flask, request, jsonify, render_template
# from werkzeug.utils import secure_filename
# import os
# import pandas as pd
# import datetime
# import uuid
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route("/upload", methods=['POST'])
# def upload():
#     # check if the POST request contains files
#     print('hellllooo')
#     if 'xlsx-file1' not in request.files:
#         return jsonify({'error': 'No file was uploaded.'}), 400
#
#     # get the uploaded file
#     file1 = request.files['xlsx-file1']
#
#     # check if the file has allowed extension (e.g., .xlsx)
#     allowed_extensions = ['.xlsx']
#     if not file1.filename.endswith(tuple(allowed_extensions)):
#         return jsonify({'error': 'Only .xlsx files are allowed.'}), 400
#
#     # generate unique filename
#     current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
#     unique_filename1 = str(uuid.uuid4())
#     filename1 = secure_filename(f"{file1.filename}-{current_time}-{unique_filename1}")
#
#     # save the uploaded file to a temporary directory
#     tmp_dir = './uploads'
#     os.makedirs(tmp_dir, exist_ok=True)
#     file1_path = os.path.join(tmp_dir, filename1)
#     while os.path.isfile(file1_path):
#         unique_filename1 = str(uuid.uuid4())
#         filename1 = secure_filename(f"{file1.filename}-{current_time}-{unique_filename1}")
#         file_path1 = os.path.join(tmp_dir, filename1)
#     file1.save(file1_path)
#
#     # display the analysis options
#     return render_template('analysis.html', filename=filename1)
#
# @app.route("/perform_analysis", methods=['POST'])
# def perform_analysis():
#     # get the selected analysis option and uploaded file path
#     option = request.form.get('analysis_option')
#     file1_path = request.form.get('file_path')
#
#     # read the uploaded file
#     data = pd.read_excel(file1_path)
#
#     # perform the selected analysis option
#     if option == 'summary':
#         result = data.describe().to_html()
#     elif option == 'corr':
#         result = data.corr().to_html()
#     elif option == 'hist':
#         result = data.hist().tolist()
#
#     # return the result
#     return jsonify({'result': result}), 200
#
# if __name__ == '__main__':
#     app.run(port='8000', debug=True)



# from flask import Flask, request, jsonify, render_template
# from werkzeug.utils import secure_filename
# import datetime
# import os
#
# app = Flask(__name__)
#
# # set maximum file size (20 MB)
# app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024
#
# # set allowed file extensions
# ALLOWED_EXTENSIONS = ['.xlsx']
#
# def allowed_file(filename):
#     """Check if a file has an allowed extension."""
#     return filename.endswith(tuple(ALLOWED_EXTENSIONS))
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route("/upload", methods=['POST'])
# def upload():
#     # check if the POST request contains files
#     if 'xlsx-file-1' not in request.files:
#         return jsonify({'error': 'No file were uploaded.'}), 400
#
#     # get the uploaded files
#     file1 = request.files['xlsx-file-1']
#     #file2 = request.files['json-file-2']
#
#     # check if the files have allowed extensions (e.g., .json)
#     if not all(allowed_file(file.filename) for file in [file1]):
#         return jsonify({'error': 'Only .xlsx files are allowed.'}), 400
#
#     # check if the files are within the allowed file size
#     if not all(len(file.read()) <= app.config['MAX_CONTENT_LENGTH'] for file in [file1]):
#         return jsonify({'error': 'File size exceeded the limit of 10 MB.'}), 400
#
#     # check if the files exceed the maximum allowed size
#     max_size = app.config['MAX_CONTENT_LENGTH']
#     if not all(file.content_length <= max_size for file in [file1]):
#         return request_entity_too_large(max_size)
#
#     # save the uploaded files to a temporary directory
#     # generate a new filename using the original filename and a timestamp
#     filename1, extension1 = os.path.splitext(secure_filename(file1.filename))
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
#     new_filename1 = f"{filename1}_{timestamp}{extension1}"
#
#     # check if the file with the same name exists, and generate a new name if necessary
#     save_dir = './uploads'
#     os.makedirs(save_dir, exist_ok=True)
#     file1_path = os.path.join(save_dir, new_filename1)
#     while os.path.exists(file1_path):
#         timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
#         new_filename1 = f"{filename1}_{timestamp}{extension1}"
#         file1_path = os.path.join(save_dir, new_filename1)
#
#     # save the uploaded file to the upload folder
#     file1.save(file1_path)
#
#     # do something with the uploaded files (e.g., process and return some result)
#     result = {'message': 'Files uploaded successfully.', 'file1_path': file1_path}
#     return jsonify(result), 200
#
# @app.errorhandler(413)
# def request_entity_too_large(error):
#     """Handle file size limit error."""
#     return jsonify({'error': 'File size exceeded the limit of 10 MB.'}), 413
#
#
# if __name__ == '__main__':
#     app.run(port='8000', debug="True")



'''
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file was uploaded.'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file was uploaded.'}), 400

    # check if the file has allowed extensions (e.g., .xlsx)
    allowed_extensions = ['.xlsx']
    if not file.filename.lower().endswith(tuple(allowed_extensions)):
        return jsonify({'error': 'Only XLSX files are allowed.'}), 400

    # generate a unique filename for the uploaded file
    filename = secure_filename(file.filename)
    i = 0
    while os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
        i += 1
        filename = secure_filename(os.path.splitext(file.filename)[0] + '_' + str(i) + os.path.splitext(file.filename)[1])

    # save the uploaded file to the upload folder
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    return jsonify({'message': 'File uploaded successfully.', 'file_path': file_path}), 200

@app.route('/analysis', methods=['POST'])
def analysis():
    analysis_type = request.form['analysis_type']
    file_path = request.form['file_path']
    if not file_path or not os.path.exists(file_path):
        return jsonify({'error': 'File path is invalid.'}), 400

    df = pd.read_excel(file_path)

    if analysis_type == 'mean':
        results = df.mean().to_dict()
    elif analysis_type == 'median':
        results = df.median().to_dict()
    elif analysis_type == 'mode':
        results = df.mode().to_dict()
    else:
        return jsonify({'error': 'Invalid analysis type.'}), 400

    return jsonify({'results': results}), 200

if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = './uploads'
    app.run(port='8000', debug=True)

'''