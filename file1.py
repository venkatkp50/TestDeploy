import streamlit as st
from multimodalReader import getImage

st.write('File 1')
images_array, imgscore = getImage('cold')
st.write('File 2')
st.write(images_array,imgscore)
imagenamex = Image.open(images_array[0],"r")
st.image(imagenamex,width=content_image_width)
