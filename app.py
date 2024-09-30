git commit -m"first commit"import gradio as gr
import pytesseract
from PIL import Image



def ocr_extract(image):
    """Extract text from the uploaded image using Tesseract OCR."""
    extracted_text = pytesseract.image_to_string(image, lang='hin+eng')
    return extracted_text

def keyword_search(text, keyword):
    """Search for a keyword in the extracted text."""
    if keyword.lower() in text.lower():
        return f"'{keyword}' found in text."
    else:
        return f"'{keyword}' not found."

# Define the Gradio app
with gr.Blocks() as demo:
    image_input = gr.Image(label="Upload Image")
    extracted_text_output = gr.Textbox(label="Extracted Text")
    keyword_input = gr.Textbox(label="Enter Keyword")
    keyword_search_output = gr.Textbox(label="Keyword Search Result")

    btn_ocr = gr.Button("Extract Text")
    btn_search = gr.Button("Search Keyword")

    # Button to extract text from the uploaded image
    btn_ocr.click(fn=ocr_extract, inputs=image_input, outputs=extracted_text_output)

    # Button to search for a keyword in the extracted text
    btn_search.click(fn=keyword_search, inputs=[extracted_text_output, keyword_input], outputs=keyword_search_output)

demo.launch(share=True)
