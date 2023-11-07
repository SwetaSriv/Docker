from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from digit_recognition_module import predict_digit  

app = Flask(_name_)

@app.route('/api/compare_digits', methods=['POST'])
def compare_digits():
    # Check if the post request has the file part
    if 'image1' not in request.files or 'image2' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file1 = request.files['exmp1']
    file2 = request.files['exmp2']

    if file1.filename == '' or file2.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file1 and file2:
        # Make the filename safe, remove unsupported chars
        filename1 = secure_filename(file1.filename)
        filename2 = secure_filename(file2.filename)

        # You might want to save the files, or just pass the file stream
        path1 = os.path.join('/path/to/temp/dir', filename1)
        path2 = os.path.join('/path/to/temp/dir', filename2)
        file1.save(path1)
        file2.save(path2)

        # Use your prediction function on the saved images
        digit1 = predict_digit(path1)
        digit2 = predict_digit(path2)

        # Remove the files after prediction if you want
        os.remove(path1)
        os.remove(path2)

        # Return True if both predictions are the same
        result = digit1 == digit2
        return jsonify(result), 200

if _name_ == '_main_':
    app.run(debug=True)