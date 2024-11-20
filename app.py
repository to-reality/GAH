#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import docx
from PyPDF2 import PdfReader
import tempfile
import os

# Function to read the content of the docx file
def read_docx(file_path):
    doc = docx.Document(file_path)
    content = []
    for para in doc.paragraphs:
        content.append(para.text)
    return "\n".join(content)

# Function to read the content of the csv file
def read_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except ValueError as e:
        st.error(f"Error reading the CSV file: {e}")
        return None

# Function to read the content of the pdf file
def read_pdf(file_path):
    try:
        pdf_reader = PdfReader(file_path)
        content = []
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            content.append(page.extract_text())
        return "\n".join(content)
    except Exception as e:
        st.error(f"Error reading the PDF file: {e}")
        return None

# Function to read the content of the py file
def read_py(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except Exception as e:
        st.error(f"Error reading the Python file: {e}")
        return None

# Streamlit app
st.title('The Statistical Presentation of the Location Frequency of the Scholars')

st.header('1. Workflow')
st.subheader('1.1 Use Python and Excel to Make Statistics on the Frequency of Locations')

# Display images
image_paths = [
    '1.1-1.png',
    '1.1-2.png',
    '1.1-3.png',
    '1.1-4.png',
    '1.1-5.png',
    '1.1-6.png',
    '1.1-7.png'
]

for image_path in image_paths:
    st.image(image_path, caption=image_path.split('/')[-1], use_column_width=True)

st.subheader('1.2 Use Python and Excel to Correlate Specific Characters with Chapters and Locations and Make Frequency Statistics')
st.image('1.2-1.png', caption='1.2-1', use_column_width=True)
st.image('1.2-2.png', caption='1.2-2', use_column_width=True)
st.image('1.2-3.png', caption='1.2-3', use_column_width=True)

st.subheader('1.3 Use GIS Tools for Visualization on Maps')
st.write('1.3.1 Layer Creation')
st.image('1.3.1-1.png', caption='1.3.1-1', use_column_width=True)
st.image('1.3.1-2.png', caption='1.3.1-2', use_column_width=True)
st.image('1.3.1-3.png', caption='1.3.1-3', use_column_width=True)

st.write('1.3.2 Adding Separate Text Layers')
st.image('1.3.2-1.png', caption='1.3.2-1', use_column_width=True)

st.write('1.3.3 Connecting a Point Layer to a Data Table')
st.image('1.3.3-1.png', caption='1.3.3-1', use_column_width=True)
st.image('1.3.3-2.png', caption='1.3.3-2', use_column_width=True)

st.write('1.3.4 Making Column Chart')
st.image('1.3.4-1.png', caption='1.3.4-1', use_column_width=True)
st.image('1.3.4-2.png', caption='1.3.4-2', use_column_width=True)
st.image('1.3.4-3.png', caption='1.3.4-3', use_column_width=True)
st.image('1.3.4-4.png', caption='1.3.4-4', use_column_width=True)
st.image('1.3.4-5.png', caption='1.3.4-5', use_column_width=True)
st.image('1.3.4-6.png', caption='1.3.4-6', use_column_width=True)

# File upload section
st.header('2. Files')

# Helper function to save uploaded file to a temporary directory
def save_uploaded_file(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        return temp_file.name

# File uploader for DOCX
uploaded_docx_file = st.file_uploader("Choose a DOCX file", type="docx")
if uploaded_docx_file is not None:
    docx_path = save_uploaded_file(uploaded_docx_file)
    doc_content = read_docx(docx_path)
    st.write(doc_content)

# File uploader for first CSV
uploaded_csv_file1 = st.file_uploader("Choose the first CSV file", type="csv")
if uploaded_csv_file1 is not None:
    csv_path1 = save_uploaded_file(uploaded_csv_file1)
    csv_content1 = read_csv(csv_path1)
    st.write(csv_content1)

# File uploader for second CSV
uploaded_csv_file2 = st.file_uploader("Choose the second CSV file", type="csv")
if uploaded_csv_file2 is not None:
    csv_path2 = save_uploaded_file(uploaded_csv_file2)
    csv_content2 = read_csv(csv_path2)
    st.write(csv_content2)

# File uploader for PDF
uploaded_pdf_file = st.file_uploader("Choose a PDF file", type="pdf")
if uploaded_pdf_file is not None:
    pdf_path = save_uploaded_file(uploaded_pdf_file)
    pdf_content = read_pdf(pdf_path)
    st.write(pdf_content)

# File uploader for first Python file
uploaded_py_file1 = st.file_uploader("Choose the first Python file", type="py")
if uploaded_py_file1 is not None:
    py_path1 = save_uploaded_file(uploaded_py_file1)
    py_content1 = read_py(py_path1)
    st.code(py_content1, language='python')

# File uploader for second Python file
uploaded_py_file2 = st.file_uploader("Choose the second Python file", type="py")
if uploaded_py_file2 is not None:
    py_path2 = save_uploaded_file(uploaded_py_file2)
    py_content2 = read_py(py_path2)
    st.code(py_content2, language='python')
