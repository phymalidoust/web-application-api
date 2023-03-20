from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    # return '''
    #     <html>
    #         <head>
    #             <title>File Upload</title>
    #         </head>
    #         <body>
    #             <h1>File Upload</h1>
    #             <form method="POST" enctype="multipart/form-data" id="upload-form">
    #                 <input type="file" name="file" id="file-input">
    #                 <button type="submit" id="submit-button">Upload</button>
    #             </form>
    #             <script src="../frontEnd/js/script.js"></script>
    #         </body>
    #     </html>
    # '''

@app.route("/upload", methods=['POST'])
def upload():
    # check if the POST request contains files
    if 'json-file-1' not in request.files or 'json-file-2' not in request.files:
        return jsonify({'error': 'No JSON files were uploaded.'}), 400

    # get the uploaded files
    file1 = request.files['json-file-1']
    file2 = request.files['json-file-2']

    # check if the files have allowed extensions (e.g., .json)
    allowed_extensions = ['.json']
    if not all(file.filename.endswith(tuple(allowed_extensions)) for file in [file1, file2]):
        return jsonify({'error': 'Only JSON files are allowed.'}), 400

    # save the uploaded files to a temporary directory
    tmp_dir = './uploads'
    os.makedirs(tmp_dir, exist_ok=True)
    file1_path = os.path.join(tmp_dir, file1.filename)
    file1.save(file1_path)
    file2_path = os.path.join(tmp_dir, file2.filename)
    file2.save(file2_path)

    # do something with the uploaded files (e.g., process and return some result)
    result = {'message': 'Files uploaded successfully.', 'file1_path': file1_path, 'file2_path': file2_path}
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(port='8000', debug="True")
