from flask import Flask, request

app = Flask(__name__)


@app.route('/uploadimage', methods=['POST'])
def upload_file():
    uploaded_file = request.files['imageFile']
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

