import tensorflow as tf
from tensorflow import keras

import numpy as np

from PIL import Image

import requests
from PIL import ExifTags
import streamlit as st
import os


st.set_page_config(
    page_title="Animal Classifier Demo by Emmanuel Mekonnen",

)

st.write("# Animal Classifier")
st.subheader('By Emmanuel Mekonnen')

st.write("This project classifies different animal photos using a CNN.")

st.write(os.getcwd())
with st.expander("More info about the model"):
    st.markdown("""
        <p>This project used a Convolution Neural Network pre-trained on ImageNet, using
        a ResNet-50 architecture. The implementation was done using Keras and TenserFlow. 
      
    """, unsafe_allow_html=True)

file_data = st.file_uploader("Select an image", type=["jpg", "jpeg", "png"])
add_selectbox = st.sidebar.selectbox(
    "Which model would you like to use?",
    ("Email", "Bi", "Mobile phone")
)


def download_file(url):
    with st.spinner('Downloading model...'):
        # from https://stackoverflow.com/a/16696317
        local_filename = url.split('/')[-1]
        # NOTE the stream=True parameter below
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    # If you have chunk encoded response uncomment if
                    # and set chunk_size parameter to None.
                    # if chunk:
                    f.write(chunk)
        return local_filename


def fix_rotation(file_data):
    # check EXIF data to see if has rotation data from iOS. If so, fix it.
    try:
        image = PILImage.create(file_data)
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break

        exif = dict(image.getexif().items())

        rot = 0
        if exif[orientation] == 3:
            rot = 180
        elif exif[orientation] == 6:
            rot = 270
        elif exif[orientation] == 8:
            rot = 90

        if rot != 0:
            st.write(
                f"Rotating image {rot} degrees (you're probably on iOS)...")
            image = image.rotate(rot, expand=True)
            # This step is necessary because image.rotate returns a PIL.Image, not PILImage, the fastai derived class.
            image.__class__ = PILImage

    except (AttributeError, KeyError, IndexError):
        pass  # image didn't have EXIF data

    return image


@st.cache(allow_output_mutation=True)
def load_model():
    return tf.keras.models.load_model("animal_CNN_v1.h5")


learn = load_model()

if file_data is not None:
    with st.spinner('Classifying...'):
        # load the image from uploader; fix rotation for iOS devices if necessary
        img = Image.open(file_data)
        st.write('## Your Image')
        st.image(img, width=200)
        print("here3333", type(img))
        img2 = img.resize((150, 150), Image.ANTIALIAS)
        img_array = np.asarray(img2)/255.
        img_batch = np.expand_dims(img_array, axis=0)

        # classify
        st.write(print((img_batch)))
        print(learn.predict(img_batch))
        pred = learn.predict(img_batch)
        y_classes = np.argmax(pred, axis=1)
        print("PREDICCCCTION", y_classes)
        # prepare output
        #out_text = '<table><tr> <th>Breed</th> <th>Confidence</th> <th>Example</th> </tr>'
        #out_text += learn.predict(img)
        #out_text += '</table><br><br>'

        # st.write('## What the model thinks')
        #st.markdown(out_text, unsafe_allow_html=True)
