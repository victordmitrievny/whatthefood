<p align="center">
     THE PROJECT IS DEPLOYED ONLINE AT:  <br>
   https://whatthefood-249651900b96.herokuapp.com/
</p>

_**Description:**_

WhatTheFood app is designed to help people understand the health implications of the ingredients in the food they're buying. When users upload the picture with the ingredients 
from a given food label, 
the app analazyes it and suggests wether this product contains potentially dangerous compounds. 
This way people, can eliminate harmful products from their diet and eat more healthy


This is a full-stack web app. Front-end is written in HTML, CSS and JavaScript; backend is written in Python, is attached to an SQL database, and uses Tesseract OCR for picture
processing. Some of the main libraries used are: <br>
-Pandas <br>
-Sqlalchemy <br>
-Pytesseract <br>
-Flask <br>

The project is deployed on Heroku.
 
_**Files Summary:**_ <br>

-script.js - Front-end generation, animations and communication with the backend <br>
-index.html - HTML layout <br>
-styles.css - CSS styles <br>
-server.py - Backend picture processing, data formatting, algorthims to find ingredients and generate the table <br>
-images - images for an HTML layout <br>
-Foods.xlxs - backup data for an SQL database (can be replaced within the code if SQL stops working) <br>
-Procfile, Aptfile, requirements.txt - supplemental files needed for Heroku deployment <br>


To start the program:

1. Pip install requirements.txt
2. Launch **server.py** 

_**Methodology Breakdown:**_

1. The program starts with Python server launch
2. Using HTML and CSS, the program generates basic page layout, its elements, text and the upload button
3. With Javascript, the page listens to the image-upload event and passes it to the backend
4. Using Python, the program recieves the picture on the back-end
5. Using Tesseract OCR, given the image is in the right format, the program converts the image to a text string
6. The program then formats the text string to make ingredients identification process easier
7. The program then identifies each ingredient by splitting the formatted string by commas (",") and writes each ingredient in a list of dictionaries
8. The program checks each of the ingredients present in the dictionary against the ingredients present in the SQL database
9. If there is a match, the program generates a dynamic HTML table, and adds the matched ingredient, its category and its effect to a new row
10. The process repeats until the algorithm goes through all of the dictionary ingredients
11. The program passes the resulting HTML table back to Javascript on the front-end
12. Javascript generates the table passed from the back-end and updates the overall HTML layout and CSS styles

13.* The program then is deployed on Heroku, alongside the SQL database I've created for this project
   


