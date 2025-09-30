import streamlit as st

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("성적 데이터 시각화 브라우저")
st.write("CSV 파일을 업로드하고 다양한 그래프를 그릴 수 있습니다.")

# 1. CSV 파일 업로드
uploaded_file = st.file_uploader("성적 데이터 CSV 파일을 업로드하세요", type=["csv"])
df = None
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("데이터 업로드 완료!")
    st.dataframe(df)
else:
    st.info("CSV 파일을 업로드하면 시각화 옵션이 활성화됩니다.")

# 2. 시각화 옵션
if df is not None:
    st.header("시각화 옵션")
    chart_type = st.radio(
        "원하는 그래프를 선택하세요",
        ("히스토그램", "막대그래프", "산점도", "상자그림")
    )

    # 3. 변수 선택 및 맞춤형 그래프
    if chart_type == "히스토그램":
        num_cols = df.select_dtypes(include='number').columns.tolist()
        col = st.selectbox("히스토그램을 그릴 변수 선택", num_cols)
        if col:
            fig, ax = plt.subplots()
            sns.histplot(df[col], kde=True, ax=ax)
            ax.set_title(f"{col}의 히스토그램")
            st.pyplot(fig)
    elif chart_type == "막대그래프":
        cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        num_cols = df.select_dtypes(include='number').columns.tolist()
        cat_col = st.selectbox("범주형(막대) 변수 선택", cat_cols)
        num_col = st.selectbox("수치형(막대) 변수 선택", num_cols)
        if cat_col and num_col:
            fig, ax = plt.subplots()
            sns.barplot(x=cat_col, y=num_col, data=df, ax=ax)
            ax.set_title(f"{cat_col}별 {num_col} 막대그래프")
            st.pyplot(fig)
    elif chart_type == "산점도":
        num_cols = df.select_dtypes(include='number').columns.tolist()
        x_col = st.selectbox("X축 변수 선택", num_cols, key="scatter_x")
        y_col = st.selectbox("Y축 변수 선택", num_cols, key="scatter_y")
        if x_col and y_col:
            fig, ax = plt.subplots()
            sns.scatterplot(x=df[x_col], y=df[y_col], ax=ax)
            ax.set_title(f"{x_col} vs {y_col} 산점도")
            st.pyplot(fig)
    elif chart_type == "상자그림":
        num_cols = df.select_dtypes(include='number').columns.tolist()
        cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
        num_col = st.selectbox("수치형(상자) 변수 선택", num_cols, key="box_num")
        cat_col = st.selectbox("범주형(상자) 변수 선택", cat_cols, key="box_cat")
        if num_col and cat_col:
            fig, ax = plt.subplots()
            sns.boxplot(x=cat_col, y=num_col, data=df, ax=ax)
            ax.set_title(f"{cat_col}별 {num_col} 상자그림")
            st.pyplot(fig)
