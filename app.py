import streamlit as st
import pytesseract
from PIL import Image
import os

# Agar Windows pe ho, toh Tesseract ka path set karo
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 🎨 Streamlit UI Setup
st.set_page_config(page_title="🖼️ Image to Text Converter (OCR)", layout="centered")
st.title("📜 Image to Text Converter (OCR)")

st.write("Upload an image and extract text using Tesseract OCR.")

# 📂 File Upload
uploaded_image = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_image is not None:
    # Open Image
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # 🔘 Extract Button
    if st.button("Extract Text"):
        with st.spinner("Extracting text... ⏳"):
            extracted_text = pytesseract.image_to_string(image)
            st.success("✅ Text Extracted Successfully!")
            st.text_area("📜 Extracted Text:", extracted_text, height=200)
        
        # 🔗 Download Button
        if extracted_text:
            st.download_button("📥 Download Extracted Text", extracted_text, file_name="extracted_text.txt")
