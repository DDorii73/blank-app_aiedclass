import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit 주요 요소 예시")  # 페이지 제목

st.header("1. 텍스트 관련 요소")
st.subheader("1-1. 일반 텍스트")
st.write("이것은 일반 텍스트입니다.")  # 일반 텍스트
st.markdown("**마크다운** _지원_ :star:")  # 마크다운 지원
st.code('print("Hello, Streamlit!")', language='python')  # 코드 블록
st.latex(r'\\int_0^1 x^2 dx')  # LaTeX 수식

st.header("2. 입력 위젯")
name = st.text_input("이름을 입력하세요")  # 텍스트 입력
age = st.number_input("나이", min_value=0, max_value=120, value=25)  # 숫자 입력
agree = st.checkbox("동의합니다")  # 체크박스
color = st.radio("색상을 선택하세요", ["빨강", "파랑", "초록"])  # 라디오 버튼
hobby = st.selectbox("취미를 선택하세요", ["독서", "운동", "게임"])  # 셀렉트박스
hobbies = st.multiselect("복수 취미 선택", ["독서", "운동", "게임", "음악"])  # 멀티셀렉트
level = st.slider("만족도(0~10)", 0, 10, 5)  # 슬라이더
st.date_input("날짜 선택")  # 날짜 입력
st.time_input("시간 선택")  # 시간 입력
st.file_uploader("파일 업로드")  # 파일 업로더
st.text_area("자기소개를 입력하세요")  # 텍스트 에어리어

st.header("3. 버튼 및 상호작용")
if st.button("클릭하세요"):  # 버튼
    st.success("버튼이 클릭되었습니다!")

st.header("4. 데이터 표시")
df = pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C'])
st.dataframe(df)  # 데이터프레임 표시
st.table(df.head(3))  # 테이블 표시
st.json({"name": name, "age": age, "agree": agree})  # JSON 표시

st.header("5. 차트 및 시각화")
st.line_chart(df)  # 선 그래프
st.bar_chart(df)  # 막대 그래프
st.area_chart(df)  # 영역 그래프

st.header("6. 미디어")
st.image("https://placekitten.com/200/300", caption="고양이 이미지")  # 이미지 표시
st.audio(np.random.randn(44100), sample_rate=44100)  # 오디오 표시 (랜덤)
st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # 비디오 표시

st.header("7. 기타")
st.progress(70)  # 진행 바
with st.spinner("로딩 중..."):
    st.write("잠시만 기다려주세요...")  # 스피너
st.balloons()  # 풍선 애니메이션
# st.toast("이것은 토스트 메시지입니다.")  # 토스트 메시지 (Streamlit 1.22+)

# 각 요소별로 주석(각주)을 달아 설명을 추가했습니다.
import streamlit as st

st.title("🎈 My new app")
import streamlit as st
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
