from flask import Flask, render_template, request, send_file
from sf_hierarchy_processing import hierarchy_builder
import pandas as pd
import os
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    if file:
        file_path = 'uploaded_file.csv'
        file.save(file_path)
        
        hierarchy_df = hierarchy_builder(file_path)
        
        # Remove the uploaded file after processing
        os.remove(file_path)
        
        
        csv_string = hierarchy_df.to_csv(index=False)
        csv_bytes = csv_string.encode('utf-8')
        return send_file(
            io.BytesIO(csv_bytes),
            mimetype='text/csv',
            as_attachment=True,
            download_name='processed_file.csv'  # Specify the filename directly
        )

if __name__ == '__main__':
    app.run(debug=True)
