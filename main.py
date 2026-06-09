import streamlit as st
import random

st.set_page_config(
    page_title="🎲 자리 뽑기",
    page_icon="🪑",
    layout="wide"
)

# ------------------
# 세션 상태 초기화
# ------------------

if "absent" not in st.session_state:
    st.session_state.absent = []

if "seat_result" not in st.session_state:
    st.session_state.seat_result = None

# ------------------
# 제목
# ------------------

st.title("🎲 랜덤 자리 배치")
st.subheader("학급 자리 자동 배정 프로그램")

st.divider()

# ------------------
# 결번 설정
# ------------------

st.header("❌ 없는 번호 선택")

cols = st.columns(5)

for i in range(30):

    num = i + 1

    with cols[i % 5]:

        checked = num in st.session_state.absent

        if st.checkbox(
            f"{num}번",
            value=checked,
            key=f"absent_{num}"
        ):
            if num not in st.session_state.absent:
                st.session_state.absent.append(num)

        else:
            if num in st.session_state.absent:
                st.session_state.absent.remove(num)

st.write("### 결번")

if st.session_state.absent:
    st.write(sorted(st.session_state.absent))
else:
    st.write("없음")

st.divider()

# ------------------
# 학생 목록 생성
# ------------------

students = [
    str(i)
    for i in range(1, 31)
    if i not in st.session_state.absent
]

# ------------------
# 배치 형태 선택
# ------------------

seat_type = st.radio(
    "🪑 자리 형태 선택",
    ["혼자 앉기", "짝꿍 앉기"],
    horizontal=True
)

# ------------------
# 자리 뽑기
# ------------------

if st.button("🎲 자리 뽑기", use_container_width=True):

    shuffled = students.copy()
    random.shuffle(shuffled)

    st.session_state.seat_result = shuffled

# ------------------
# 짝꿍 자리 구조 생성
# ------------------

def create_pair_layout(student_count):

    sections = [
        [1,2,3,4,5,6,7,8,9,10],
        [11,12,13,14,15,16,17,18,19,20],
        [21,22,23,24,25,26,27,28,29,30]
    ]

    remove_order = [
        30,20,10,
        29,19,9,
        28,18,8,
        27,17,7,
        26,16,6,
        25,15,5,
        24,14,4,
        23,13,3,
        22,12,2,
        21,11,1
    ]

    remove_count = 30 - student_count

    removed = set(remove_order[:remove_count])

    result = []

    for sec in sections:

        result.append([
            seat if seat not in removed else None
            for seat in sec
        ])

    return result

# ------------------
# 결과 출력
# ------------------

if st.session_state.seat_result:

    students = st.session_state.seat_result

    st.divider()

    st.header("📋 자리 배치 결과")

    # ==================
    # 혼자 앉기
    # ==================

    if seat_type == "혼자 앉기":

        st.markdown("## 🧑‍🏫 교탁")

        idx = 0

        for row in range(6):

            cols = st.columns(5)

            for col in range(5):

                with cols[col]:

                    if idx < len(students):

                        st.markdown(
                            f"""
                            <div style="
                            border:2px solid #4CAF50;
                            border-radius:10px;
                            padding:15px;
                            text-align:center;
                            font-size:24px;
                            ">
                            👨‍🎓<br>
                            {students[idx]}번
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    else:

                        st.markdown(
                            """
                            <div style="
                            border:2px dashed gray;
                            border-radius:10px;
                            padding:15px;
                            text-align:center;
                            ">
                            ❌
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    idx += 1

            st.write("")

    # ==================
    # 짝꿍 앉기
    # ==================

    else:

        st.markdown("## 🧑‍🏫 교탁")

        layout = create_pair_layout(len(students))

        student_iter = iter(students)

        sec1, sec2, sec3 = st.columns(3)

        section_columns = [sec1, sec2, sec3]

        for section_idx in range(3):

            with section_columns[section_idx]:

                st.markdown(
                    f"""
                    <h3 style='text-align:center'>
                    🏫 {section_idx+1}분단
                    </h3>
                    """,
                    unsafe_allow_html=True
                )

                section = layout[section_idx]

                for row in range(5):

                    pair_cols = st.columns(2)

                    left = section[row*2]
                    right = section[row*2+1]

                    # 왼쪽 자리

                    if left is None:

                        pair_cols[0].markdown(
                            """
                            <div style="
                            border:2px solid red;
                            border-radius:10px;
                            padding:15px;
                            text-align:center;
                            font-size:22px;">
                            ❌
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    else:

                        try:

                            student = next(student_iter)

                            pair_cols[0].markdown(
                                f"""
                                <div style="
                                border:2px solid #2196F3;
                                border-radius:10px;
                                padding:15px;
                                text-align:center;
                                font-size:22px;">
                                👨‍🎓 {student}
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                        except StopIteration:
                            pass

                    # 오른쪽 자리

                    if right is None:

                        pair_cols[1].markdown(
                            """
                            <div style="
                            border:2px solid red;
                            border-radius:10px;
                            padding:15px;
                            text-align:center;
                            font-size:22px;">
                            ❌
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    else:

                        try:

                            student = next(student_iter)

                            pair_cols[1].markdown(
                                f"""
                                <div style="
                                border:2px solid #2196F3;
                                border-radius:10px;
                                padding:15px;
                                text-align:center;
                                font-size:22px;">
                                👨‍🎓 {student}
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                        except StopIteration:
                            pass

# ------------------
# 현재 학생 수
# ------------------

st.sidebar.header("📊 현재 상태")

st.sidebar.metric(
    "학생 수",
    len(students)
)

st.sidebar.metric(
    "결번 수",
    len(st.session_state.absent)
)
