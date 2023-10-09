

// This code finds hello container and puts helo world in there
const helloText = document.createTextNode("Hello, World!");
const findDiv = document.getElementById("hello-container");
findDiv.appendChild(helloText);

// This code creates an image container
const Image = document.getElementById("image-container");
Image.src = "/Users/victordmitirev/Desktop/Screen Shot 2023-09-17 at 1.55.31 AM.png";

// This is codes retrieves uploaded file and puts it into image container and sends to server (BUT I DONT UNDERSTAND IT)
document.getElementById('file-input').addEventListener('change', function(event) {
    const imageContainer = document.getElementById('image-container');
    const fileInput = event.target;
    
    if (fileInput.files && fileInput.files[0]) {
        const reader = new FileReader();

        reader.onload = function(e) {
            imageContainer.src = e.target.result;
        };

        // New code to send the file to the Python file
        const formData = new FormData();
        formData.append('uploadedFile', fileInput.files[0]);
        fetch('/uploadimage', {
            method: 'POST',
            body: formData
        }).then(response => {
            // Handle the response from the server if needed
        });

        reader.readAsDataURL(fileInput.files[0]);
    }
    });