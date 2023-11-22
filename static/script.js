

// This code finds hello container and puts helo world in there
// const helloText = document.createTextNode("Hello, World!");
// const findDiv = document.getElementById("hello-container");
// findDiv.appendChild(helloText);


// This code finds all the containers for further JS manipulations
const Pageloader = document.getElementById("loading-screen0")
const Body = document.getElementById("body");
const Image = document.getElementById("image-container");
const LoadingScreen = document.getElementById("loading-screen1");
const Welcome = document.getElementById("welcome");
const Description = document.getElementById("description");
const UploadString = document.getElementById("upload-string");
const Ellipse1 = document.getElementById("ellipse1");
const Ellipse2 = document.getElementById("ellipse2");
const Precitationdiv = document.getElementById("pre-citation-div");
const CitationDiv = document.getElementById("citation-div");
const CitationP = document.getElementById("citation-p");


//This code listens for the page to load in order to hide pageloader
window.addEventListener("load", function () {
    // Hide the loader when the page has finished loading
    Pageloader.style.display = "none";
  });


//------------------Main Code-----------


// This is codes retrieves uploaded file and puts it into image container and sends to server (BUT I DONT UNDERSTAND IT)
document.getElementById('file-input').addEventListener('change', function(event) {
    const imageContainer = document.getElementById('image-container');
    const fileInput = event.target;


   // If not empty file uploaded
    if (fileInput.files && fileInput.files[0]) {
        const reader = new FileReader();

         // Print photo on the page
        reader.onload = function(e) {
            imageContainer.src = e.target.result;
        };


        LoadingScreen.style.display = "flex";



        // New code to send the file to the Python file
        const formData = new FormData();
        formData.append('uploadedFile', fileInput.files[0]);
        fetch('/uploadimage', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text()) // Uses response.text() for plain text
        .then(data => {
            // Handles the response from the server here
    
            // Example: Update a <p> element with the received text
            const generatedTextElement = document.getElementById('generatedText');
            generatedTextElement.innerHTML = data;

            // Update HTML layout and elements
            LoadingScreen.style.display = "none";
            Welcome.style.display = "none";
            Description.style.display = "none";
            UploadString.style.display = "none";
            Ellipse1.style.display = "none";
            Ellipse2.style.display = "block";
            //Precitationdiv.style.display = "none";

            console.log(Body.offsetHeight, Body.clientHeight)

            //If the Client Height (Screen Height) is more than 700, I am changing string position to display correctly
            if (Body.clientHeight > 700) {
                CitationDiv.style.position = "relative";
            } else
               {CitationDiv.style.position = "absolute"}
            

        })
        .catch(error => {
            
            console.log(error)
            
            // Handles any errors that may occur during the fetch request
        })


        //I believe this code used to showing uploaded picture on the front end
        //reader.readAsDataURL(fileInput.files[0]);

        

    }
    });
