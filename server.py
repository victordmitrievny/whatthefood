from flask import Flask, request, render_template

app = Flask(__name__, template_folder="templates") 


#Launch Frontend
@app.route("/")
def hello(): 
    return render_template('index.html') 

#Launch backend script
@app.route('/uploadimage', methods=['POST'])
def upload_file():
    print('code is running')
    uploaded_file = request.files['uploadedFile']
    if uploaded_file.filename != '':
        # Process the uploaded file here
        # You can use libraries like OpenCV, Pillow, or Tesseract to work with the image
        # For example: img = cv2.imread(uploaded_file)
        # Perform your image processing and text extraction here

        print("File uploaded and processed successfully.")


        return "File uploaded and processed successfully."
    else:

        print("No file selected")

        return "No file selected."

if __name__ == '__main__':
    app.run()


# @app.route("/") 
# def hello(): 
#     return render_template('index.html') 
  
# @app.route('/process', methods=['POST']) 
# def process(): 
#     data = request.get_json() # retrieve the data sent from JavaScript 
#     # process the data using Python code 
#     result = data['value'] * 2
#     return jsonify(result=result) # return the result to JavaScript 
  
# if __name__ == '__main__': 
#     app.run(debug=True) 