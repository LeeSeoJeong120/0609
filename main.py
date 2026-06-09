import streamlit as st
import random

st.set_page_config(
    page_title="🪑 자리 배치 프로그램",
    page_icon="🪑",
    layout="wide"
)

# -------------------
# 세션 상태
# -------------------
if "blocked" not in st.session_state:
    st.session_state.blocked = set()

if "seats" not in st.session_state:
    st.session_state.seats = []

# -------------------
# 제목
# -------------------
st.title("🪑 랜덤 자리 배치")
st.write("### ❌ 사용할 수 없는 자리를 선택하세요")

# -------------------
# 자리 선택
# -------------------

for row in range(5):

    cols = st.columns(6)

    for col in range(6):

        seat_num = row * 6 + col + 1

        blocked = seat_num in st.session_state.blocked

        label = f"❌ {seat_num}" if blocked else f"{seat_num}"

        if cols[col].button(
            label,
            key=f"seat_{seat_num}",
            use_container_width=True
        ):

            if blocked:
                st.session_state.blocked.remove(seat_num)
            else:
                st.session_state.blocked.add(seat_num)

            st.rerun()

st.divider()

# -------------------
# 배치 형태
# -------------------

seat_type = st.radio(
    "🪑 자리 형태 선택",
    ["1인용 (6×5)", "2인용 (3분단)"],
    horizontal=True
)

# -------------------
# 자리 뽑기
# -------------------

available = [
    i for i in range(1, 31)
    if i not in st.session_state.blocked
]

col1, col2 = st.columns(2)

with col1:
    if st.button("🎲 자리 뽑기", use_container_width=True):

        students = list(range(1, len(available)+1))

        random.shuffle(students)

        st.session_state.seats = students

with col2:
    if st.button("🔄 다시 섞기", use_container_width=True):

        if st.session_state.seats:

            students = st.session_state.seats.copy()

            random.shuffle(students)

            st.session_state.seats = students

# -------------------
# 정보 표시
# -------------------

st.sidebar.header("📊 현황")

st.sidebar.metric(
    "사용 가능 자리",
    len(available)
)

st.sidebar.metric(
    "제외된 자리",
    len(st.session_state.blocked)
)

# -------------------
# 결과 출력
# -------------------

if st.session_state.seats:

    st.divider()
    st.header("📋 자리 배치 결과")

    students = st.session_state.seats

    seat_map = {}

    for seat_num, student_num in zip(
        available,
        students
    ):
        seat_map[seat_num] = student_num

    # -------------------
    # 1인용
    # -------------------

    if seat_type == "1인용 (6×5)":

        for row in range(5):

            cols = st.columns(6)

            for col in range(6):

                seat_num = row * 6 + col + 1

                if seat_num in st.session_state.blocked:

                    text = "❌"
                    border = "red"

                elif seat_num in seat_map:

                    text = f"👨‍🎓 {seat_map[seat_num]}"
                    border = "#4CAF50"

                else:

                    text = ""
                    border = "gray"

                cols[col].markdown(
                    f"""
                    <div style="
                        height:80px;
                        border:3px solid {border};
                        border-radius:10px;
                        text-align:center;
                        padding-top:20px;
                        font-size:22px;
                        font-weight:bold;
                    ">
                    {text}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    # -------------------
    # 2인용
    # -------------------

    else:

        idx = 0

        for section in range(3):

            st.subheader(f"🏫 {section+1}분단")

            for row in range(5):

                cols = st.columns(2)

                left = ""
                right = ""

                if idx < len(students):
                    left = f"👨‍🎓 {students[idx]}"
                    idx += 1

                if idx < len(students):
                    right = f"👨‍🎓 {students[idx]}"
                    idx += 1

                cols[0].markdown(
                    f"""
                    <div style="
                        border:3px solid #2196F3;
                        border-radius:10px;
                        height:80px;
                        text-align:center;
                        padding-top:20px;
                        font-size:22px;
                        font-weight:bold;
                    ">
                    {left}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                cols[1].markdown(
                    f"""
                    <div style="
                        border:3px solid #2196F3;
                        border-radius:10px;
                        height:80px;
                        text-align:center;
                        padding-top:20px;
                        font-size:22px;
                        font-weight:bold;
                    ">
                    {right}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.divider()
