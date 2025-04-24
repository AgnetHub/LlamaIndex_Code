import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. 텍스트 출력
st.title("Streamlit 튜토리얼🚀")
st.header("1. 텍스트 출력😊")
st.text("이것은 일반 텍스트입니다.")
st.markdown("**이것은 마크다운 텍스트**입니다.🌈")
st.latex(r"\begin{pmatrix}a & b \\ c & d\end{pmatrix}")

# 2. 데이터 표시
st.header("2. 데이터 표시")
df = pd.DataFrame(
    {
        "이름": ["Alice", "Bob", "Charlie"],
        "나이": [25, 30, 35],
        "도시": ["서울", "부산", "인천"],
    }
)
st.dataframe(df)

# 3. 차트 그리기
st.header("3. 차트 그리기")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(chart_data)

# 4. 위젯 사용
st.header("4. 위젯 사용")

# 슬라이더
age = st.slider("나이를 선택하세요", 0, 100, 25)
st.write(f"선택한 나이: {age}")

# 선택 박스
option = st.selectbox("좋아하는 색상을 선택하세요", ["빨강", "초록", "파랑"])
st.write(f"선택한 색상: {option}")

# 체크박스
if st.checkbox("상세 정보 보기"):
    st.write("여기에 상세 정보가 표시됩니다.")

# 5. 사이드바
with st.sidebar:
    st.header("5.사이드바 활용")

    # 파일 업로더
    st.header("파일 업로더")
    uploaded_file = st.file_uploader("파일을 선택하세요", type=["csv", "txt"])
    if uploaded_file is not None:
        st.write("파일이 업로드되었습니다!")
        # 여기서 파일 처리 로직을 추가할 수 있습니다.

    # 버튼
    if st.button("클릭하세요"):
        st.write("버튼이 클릭되었습니다!")
