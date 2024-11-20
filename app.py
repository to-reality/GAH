#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import docx

# Function to read the content of the docx file
def read_docx(file):
    doc = docx.Document(file)
    content = []
    for para in doc.paragraphs:
        content.append(para.text)
    return "\n".join(content)

# Function to read the content of the xlsx file
def read_xlsx(file):
    df = pd.read_excel(file, engine='openpyxl')
    return df
# File uploader for XLSX
uploaded_xlsx_file = st.file_uploader("Choose an XLSX file", type="xlsx")
if uploaded_xlsx_file is not None:
    xlsx_content = read_xlsx(uploaded_xlsx_file)
    st.write(xlsx_content)

# Streamlit app
st.title('The Statistical Presentation of the Location Frequency of the Scholars')

# File uploader
uploaded_file = st.file_uploader("Choose a DOCX file", type="docx")
if uploaded_file is not None:
    doc_content = read_docx(uploaded_file)
    st.write(doc_content)

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
