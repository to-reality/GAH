#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:06:05 2024

@author: miaomiao
"""

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

# Read the content of the uploaded docx file
file_path = r'/Users/miaomiao/Desktop/留学/2.CHC5904 WED 1530 N103/Assignment 2/The statistical presentation of the location frequency of the Scholars.docx'
doc_content = read_docx(file_path)

# Streamlit app
st.title('The Statistical Presentation of the Location Frequency of the Scholars')

st.header('1. Workflow')
st.subheader('1.1 Use Python and Excel to Make Statistics on the Frequency of Locations')
st.image(r'/Users/miaomiao/Desktop/留学/2.CHC5904 WED 1530 N103/Assignment 2/images/1.1-1.png',
         caption='1.1-1', use_column_width=True)
st.image(r'/Users/miaomiao/Desktop/留学/2.CHC5904 WED 1530 N103/Assignment 2/images/1.1-2.png',
         caption='1.1-2', use_column_width=True)
st.image(r'/Users/miaomiao/Desktop/留学/2.CHC5904 WED 1530 N103/Assignment 2/images/1.1-3.png',
         caption='1.1-3', use_column_width=True)
st.image(r'/Users/miaomiao/Desktop/留学/2.CHC5904 WED 1530 N103/Assignment 2/images/1.1-4.png',
         caption='1.1-4', use_column_width=True)
st.image(r'/Users/miaomiao/Desktop/留学/2.CHC5904 WED 1530 N103/Assignment 2/images/1.1-5.png',
         caption='1.1-5', use_column_width=True)
st.image(r'/Users/miaomiao/Desktop/留学/2.CHC5904 WED 1530 N103/Assignment 2/images/1.1-6.png',
         caption='1.1-6', use_column_width=True)
st.image(r'/Users/miaomiao/Desktop/留学/2.CHC5904 WED 1530 N103/Assignment 2/images/1.1-7.png',
         caption='1.1-7', use_column_width=True)


st.subheader('1.2 Use Python and Excel to Correlate Specific Characters with Chapters and Locations and Make Frequency Statistics')
st.image(r'/Users/miaomiao/Desktop/留学/2.CHC5904 WED 1530 N103/Assignment 2/images/1.2-1.png',
         caption='1.2-1', use_column_width=True)
st.image(r'/Users/miaomiao/Desktop/留学/2.CHC5904 WED 1530 N103/Assignment 2/images/1.2-2.png',
         caption='1.2-2', use_column_width=True)
st.image(r'/Users/miaomiao/Desktop/留学/2.CHC5904 WED 1530 N103/Assignment 2/images/1.2-3.png',
         caption='1.2-3', use_column_width=True)

st.subheader('1.3 Use GIS Tools for Visualization on Maps')
st.write('1.3.1 Layer Creation')
st.image(r'/Users/miaomiao/Desktop/留学/2.CHC5904 WED 1530 N103/Assignment 2/images/1.3.1-1.png',
         caption='1.3.1-1', use_column_width=True)
st.image(r'/Users/miaomiao/Desktop/留学/2.CHC5904 WED 1530 N103/Assignment 2/images/1.3.1-2.png',
         caption='1.3.1-2', use_column_width=True)
st.image(r'/Users/miaomiao/Desktop/留学/2.CHC5904 WED 1530 N103/Assignment 2/images/1.3.1-3.png',
         caption='1.3.1-3', use_column_width=True)

st.write('1.3.2 Adding Separate Text Layers')
st.image(r'/Users/miaomiao/Desktop/留学/2.CHC5904 WED 1530 N103/Assignment 2/images/1.3.2-1.png',
         caption='1.3.2-1', use_column_width=True)

st.write('1.3.3 Connecting a Point Layer to a Data Table')
st.image(r'/Users/miaomiao/Desktop/留学/2.CHC5904 WED 1530 N103/Assignment 2/images/1.3.3-1.png',
         caption='1.3.3-1', use_column_width=True)
st.image(r'/Users/miaomiao/Desktop/留学/2.CHC5904 WED 1530 N103/Assignment 2/images/1.3.3-2.png',
         caption='1.3.3-2', use_column_width=True)

st.write('1.3.4 Making Column Chart')
st.image(r'/Users/miaomiao/Desktop/留学/2.CHC5904 WED 1530 N103/Assignment 2/images/1.3.4-1.png',
         caption='1.3.4-1', use_column_width=True)
st.image(r'/Users/miaomiao/Desktop/留学/2.CHC5904 WED 1530 N103/Assignment 2/images/1.3.4-2.png',
         caption='1.3.4-2', use_column_width=True)
st.image(r'/Users/miaomiao/Desktop/留学/2.CHC5904 WED 1530 N103/Assignment 2/images/1.3.4-3.png',
         caption='1.3.4-3', use_column_width=True)
st.image(r'/Users/miaomiao/Desktop/留学/2.CHC5904 WED 1530 N103/Assignment 2/images/1.3.4-4.png',
         caption='1.3.4-4', use_column_width=True)
st.image(r'/Users/miaomiao/Desktop/留学/2.CHC5904 WED 1530 N103/Assignment 2/images/1.3.4-5.png',
         caption='1.3.4-5', use_column_width=True)
st.image(r'/Users/miaomiao/Desktop/留学/2.CHC5904 WED 1530 N103/Assignment 2/images/1.3.4-6.png',
         caption='1.3.4-6', use_column_width=True)
