import streamlit as st
import cv2
import datetime
from streamlit_webrtc import webrtc_streamer
import av
from PIL import Image

#インタープリンターオプション　-m streamlit run cloud_cameraTest.pyを記載

st.title("finger auth app")
st.write("single auth ", datetime.date.today())


def callback(frame):
    img = frame.to_ndarray(format="bgr24")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (160,120))
    img = av.VideoFrame.from_ndarray(img, format='gray')
    #img = av.VideoFrame.from_ndarray(img, fformat="bgr24")
    return img

webrtc_streamer(key="Sample img",
    video_frame_callback=callback,
    )
