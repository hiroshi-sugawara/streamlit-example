import streamlit as st
import cv2
import datetime
from PIL import Image

#インタープリンターオプション　-m streamlit run cloud_cameraTest.pyを記載

st.title("finger auth app")
st.write("single auth ", datetime.date.today())


cap = cv2.VideoCapture(0)
image_loc = st.empty()
while cap.isOpened:
    ret, img = cap.read()
    if cv2.waitKey() & 0xFF == ord("q"):
        break

    if ret :
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (320, 320))
        img_ = img[85:205, :]

        img_ = Image.fromarray(img_)
        image_loc.image(img_)


cap.release()
