import streamlit as st
import cv2
import numpy as np

# 1. 사진 업로드
uploaded = st.file_uploader("사진 업로드", type = ["png", "jpg", "jpeg"])

if not uploaded:
    st.write("사진을 업로드 하세요")
else:
    file_bytes = np.asarray(bytearray(uploaded.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    st.write("원본 이미지")
    st.image(RGB_img)

    #2. 사진 수정하는 기능 
    if st.button("수정 기능 1 - 이미지 슬라이싱"):
        output = RGB_img[400:600, 1000:2000].copy()
        st.image(output)
        
        # 3. 수정한 사진을 다운로드 하는 기능 
        ok, buffer = cv2.imencode(".png", cv2.cvtColor(output, cv2.COLOR_RGB2BGR))
        
        if ok:
            st.download_button(
                label="수정1 다운로드",
                data=buffer.tobytes(),
                file_name="slice.png",
                mime="image/png"
            )

    if st.button("수정 기능 2 - 이미지 회전"):
        img90 = cv2.rotate(RGB_img, cv2.ROTATE_90_CLOCKWISE)
        st.image(img90)

        ok, buffer = cv2.imencode(".png", cv2.cvtColor(img90, cv2.COLOR_RGB2BGR))
        
        if ok:
            st.download_button(
                label="수정2 다운로드",
                data=buffer.tobytes(),
                file_name="rotate.png",
                mime="image/png"
            )

    if st.button("수정 기능 3 - 색상 변화(회색)"):
        out = cv2.cvtColor(RGB_img, cv2.COLOR_BGR2GRAY)
        st.image(out)

        ok, buffer = cv2.imencode(".png", cv2.cvtColor(out, cv2.COLOR_RGB2BGR))
        
        if ok:
            st.download_button(
                label="수정1 다운로드",
                data=buffer.tobytes(),
                file_name="colorchange.png",
                mime="image/png"
            )
        

