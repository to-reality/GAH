#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import docx
from PyPDF2 import PdfReader

# Function to read the content of the docx file
def read_docx(file):
    doc = docx.Document(file)
    content = []
    for para in doc.paragraphs:
        content.append(para.text)
    return "\n".join(content)

# Function to read the content of the csv file
def read_csv(file):
    try:
        df = pd.read_csv(file)
        return df
    except ValueError as e:
        st.error(f"Error reading the CSV file: {e}")
        return None

# Function to read the content of the pdf file
def read_pdf(file):
    try:
        pdf_reader = PdfReader(file)
        content = []
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            content.append(page.extract_text())
        return "\n".join(content)
    except Exception as e:
        st.error(f"Error reading the PDF file: {e}")
        return None

# Function to read the content of the py file
def read_py(file):
    try:
        content = file.read().decode("utf-8")
        return content
    except Exception as e:
        st.error(f"Error reading the Python file: {e}")
        return None

# Initialize session state
if 'doc_content' not in st.session_state:
    st.session_state['doc_content'] = None
if 'csv_content1' not in st.session_state:
    st.session_state['csv_content1'] = None
if 'csv_content2' not in st.session_state:
    st.session_state['csv_content2'] = None
if 'pdf_content' not in st.session_state:
    st.session_state['pdf_content'] = None
if 'py_content_01' not in st.session_state:
    st.session_state['py_content_01'] = None
if 'py_content_02' not in st.session_state:
    st.session_state['py_content_02'] = None
if 'py_content_03' not in st.session_state:
    st.session_state['py_content_03'] = None

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

# File uploader for DOCX
uploaded_docx_file = st.file_uploader("Choose a DOCX file", type="docx")
if uploaded_docx_file is not None:
    st.session_state['doc_content'] = read_docx(uploaded_docx_file)
if st.session_state['doc_content'] is not None:
    st.write(st.session_state['doc_content'])

# File uploader for first CSV
uploaded_csv_file_01 = st.file_uploader("Choose the first CSV file", type="csv")
if uploaded_csv_file_01 is not None:
    st.session_state['csv_content_01'] = read_csv(uploaded_csv_file_01)
if st.session_state['csv_content_01'] is not None:
    st.write(st.session_state['csv_content_01'])

# File uploader for second CSV
uploaded_csv_file_02 = st.file_uploader("Choose the second CSV file", type="csv")
if uploaded_csv_file_02 is not None:
    st.session_state['csv_content_02'] = read_csv(uploaded_csv_file_02)
if st.session_state['csv_content_02'] is not None:
    st.write(st.session_state['csv_content_02'])

# File uploader for PDF
uploaded_pdf_file = st.file_uploader("Choose a PDF file", type="pdf")
if uploaded_pdf_file is not None:
    st.session_state['pdf_content'] = read_pdf(uploaded_pdf_file)
if st.session_state['pdf_content'] is not None:
    st.write(st.session_state['pdf_content'])

# File uploader for first Python file
uploaded_py_file_01 = st.file_uploader("Choose the first Python file", type="py")
if uploaded_py_file_01 is not None:
    st.session_state['py_content_01'] = read_py(uploaded_py_file_01)
if st.session_state['py_content_01'] is not None:
    st.code(st.session_state['py_content_01'], language='python')

# File uploader for second Python file
uploaded_py_file_02 = st.file_uploader("Choose the second Python file", type="py")
if uploaded
