OCR Text Extraction and Keyword Search Project

Overview
This project aims to develop an Optical Character Recognition (OCR) solution that can extract text from images containing both Hindi and English text. 
The application allows users to upload images, extract the text, and search for specific keywords within the extracted content. 
The web application is built using Gradio for a user-friendly interface.

Requirements
To run this project, ensure you have the following installed:

Python 3.x
Libraries:
transformers: For loading and using the OCR model.
torch: Required for PyTorch-based models.
gradio: For developing the web application interface.

Environment Setup
Create and activate a virtual environment
Install the required libraries

OCR Model Integration
In this project, you can choose between various OCR models. Here is a sample code to integrate an OCR model

Sample Code
python

# Load the OCR model
ocr_model = pipeline("image-to-text", model="your_model_here")

def extract_text(image):
    """Extract text from the uploaded image."""
    return ocr_model(image)[0]['text']
This function uses the chosen OCR model to process the uploaded image and returns the extracted text.

Web Application Development with Gradio
The web application allows users to upload images and displays the extracted text. The code is in app.py file 

Deployment
Deploying with Gradio
Run the application locally: Save the above code in a file (e.g., app.py) and run:

python app.py
Access the application: Open your web browser and navigate to [http://localhost:7860](http://127.0.0.1:7860) to interact with the application.

Public link
This share link expires in 72 hours. 
https://d10a0b5b4532d01324.gradio.live

python

iface.launch(share=True)
This will provide a public URL that you can share with others.
Public link
This share link expires in 72 hours. 


Conclusion
This OCR Text Extraction project provides a robust solution for extracting text from images in multiple languages and searching for keywords. 
By utilizing Gradio, the application is easy to use and deploy, making it accessible to a wide audience.

THE IMAGES OF THE APP
1st Interface of the webapp

![image](https://github.com/user-attachments/assets/0f1f6084-dd05-4980-9552-fc6d59f7e4c8)

Uploaded image in the webapp
![image](https://github.com/user-attachments/assets/091918cf-1b86-4ebc-810b-dfa828acc49d)

Extracted Text
![image](https://github.com/user-attachments/assets/5aeefb8f-f31f-49ee-8c33-9a10937827d5)

For Searching the Keyword
![image](https://github.com/user-attachments/assets/3cd2c123-9f04-47ea-8c5f-d6cb7a0f430b)

