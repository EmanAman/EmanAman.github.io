from keras.preprocessing import image
from skimage.transform import resize
from PIL import Image
import os
import requests
from PIL import ExifTags
from fastai.learner import load_learner
from fastai.vision.core import PILImage
import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow import keras

st.set_page_config(
    page_title="Animal Classifier Demo by Emmanuel Mekonnen",

)

st.write("# Animal Classifier")
st.subheader('By Emmanuel Mekonnen')

st.write("This project classifies different animal photos using a CNN.")
with st.expander("More info about the model"):
    st.markdown("""
        <p>This project used a Convolution Neural Network pre-trained on ImageNet, using
        a ResNet-50 architecture. The implementation was done using Keras and TenserFlow. 
        The training dataset was based on the <a href="https://www.akc.org/dog-breeds/" target="_blank">AKC-recognized dog breeds</a>, 
        with approximately 150 images per dog breed taken from the internet. (An earlier iteration of 
        this project used the <a href="http://vision.stanford.edu/aditya86/ImageNetDogs/" target="_blank">Stanford dogs dataset</a>, 
        but I found that the images in that dataset were not representative of images "in the wild", as the 
        same model trained on those images gave unrealistically high accuracies but did not generalize well.)</p>
        <p>10% of the data were set aside for the test set (holdout set), and 20% of the data
        were used for the validation set. Images were resized to 128x128 pixel squares before
        training using random-resize cropping.</p>
        <p>The final model was trained for a total of 8 epochs: 3 with the ResNet layers frozen,
        training only the new classification head, and 5 additional epochs with all layers unfrozen.
        The final <b>validation set accuracy was 76.3%</b>, and the <b>test set/holdout accuracy was 75.4%</b>.</p>
        <p>The code used to train the model is available at <a href="https://github.com/willjobs/dog-classifier" target="_blank">https://github.com/willjobs/dog-classifier</a>.</p>
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


learn = keras.models.load_model("animal_model_v1")

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