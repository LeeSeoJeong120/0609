import streamlit as st
import random

st.set_page_config(
    page_title="🌈 MBTI 진로 탐험대",
    page_icon="🚀",
    layout="wide"
)

# --------------------------
# MBTI 데이터
# --------------------------

career_data = {
    "INTJ": {
        "emoji": "🧠",
        "jobs": ["과학자", "데이터 분석가", "AI 개발자", "연구원", "전략기획가"],
        "major": ["컴퓨터공학", "물리학", "수학", "통계학"],
        "person": "일론 머스크"
    },
    "INTP": {
        "emoji": "🔬",
        "jobs": ["프로그래머", "발명가", "교수", "시스템 설계자", "엔지니어"],
        "major": ["컴퓨터공학", "전자공학", "철학"],
        "person": "알베르트 아인슈타인"
    },
    "ENTJ": {
        "emoji": "👑",
        "jobs": ["CEO", "변호사", "정치인", "사업가", "프로젝트 관리자"],
        "major": ["경영학", "법학", "행정학"],
        "person": "스티브 잡스"
    },
    "ENTP": {
        "emoji": "💡",
        "jobs": ["창업가", "마케팅 전문가", "발명가", "광고기획자"],
        "major": ["경영학", "광고홍보학"],
        "person": "토머스 에디슨"
    },
    "INFJ": {
        "emoji": "🌱",
        "jobs": ["상담사", "심리학자", "교사", "작가"],
        "major": ["교육학", "심리학", "사회복지학"],
        "person": "넬슨 만델라"
    },
    "INFP": {
        "emoji": "🎨",
        "jobs": ["작가", "예술가", "디자이너", "상담사"],
        "major": ["문예창작", "디자인", "심리학"],
        "person": "J.K. 롤링"
    },
    "ENFJ": {
        "emoji": "🤝",
        "jobs": ["교사", "상담사", "HR 전문가", "사회복지사"],
        "major": ["교육학", "심리학"],
        "person": "오프라 윈프리"
    },
    "ENFP": {
        "emoji": "🎉",
        "jobs": ["유튜버", "기획자", "마케터", "방송인"],
        "major": ["미디어학", "광고홍보학"],
        "person": "로빈 윌리엄스"
    },
    "ISTJ": {
        "emoji": "📋",
        "jobs": ["공무원", "회계사", "판사", "행정가"],
        "major": ["행정학", "회계학", "법학"],
        "person": "워런 버핏"
    },
    "ISFJ": {
        "emoji": "💖",
        "jobs": ["간호사", "교사", "사회복지사"],
        "major": ["간호학", "교육학"],
        "person": "마더 테레사"
    },
    "ESTJ": {
        "emoji": "🏆",
        "jobs": ["경영자", "군인", "행정가"],
        "major": ["경영학", "행정학"],
        "person": "존 D. 록펠러"
    },
    "ESFJ": {
        "emoji": "😊",
        "jobs": ["교사", "간호사", "서비스 관리자"],
        "major": ["교육학", "간호학"],
        "person": "테일러 스위프트"
    },
    "ISTP": {
        "emoji": "🛠️",
        "jobs": ["정비사", "파일럿", "엔지니어"],
        "major": ["기계공학", "항공학"],
        "person": "베어 그릴스"
    },
    "ISFP": {
        "emoji": "🎵",
        "jobs": ["음악가", "디자이너", "사진작가"],
        "major": ["음악", "디자인"],
        "person": "마이클 잭슨"
    },
    "ESTP": {
        "emoji": "⚡",
        "jobs": ["기업가", "영업 전문가", "운동선수"],
        "major": ["경영학", "체육학"],
        "person": "도널드 트럼프"
    },
    "ESFP": {
        "emoji": "🌟",
        "jobs": ["연예인", "방송인", "이벤트 기획자"],
        "major": ["연극영화", "미디어학"],
        "person": "엘튼 존"
    }
}

# --------------------------
# 디자인
# --------------------------

st.markdown("""
<style>
.main {
    background-color:#F8FBFF;
}
.big-title{
    text-align:center;
    font-size:55px;
    font-weight:bold;
    color:#4B6CB7;
}
.sub{
    text-align:center;
    font-size:24px;
}
.result-box{
    padding:20px;
    border-radius:20px;
    background:#EEF5FF;
    margin-top:10px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------
# 헤더
# --------------------------

st.markdown(
    '<div class="big-title">🚀 MBTI 진로 탐험대 🌈</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub">✨ 나의 MBTI로 미래 직업을 탐험해보자! ✨</div>',
    unsafe_allow_html=True
)

st.write("")
st.balloons()

# --------------------------
# 선택
# --------------------------

mbti = st.selectbox(
    "🧩 나의 MBTI를 선택하세요",
    list(career_data.keys())
)

# --------------------------
# 결과 버튼
# --------------------------

if st.button("🔮 미래 직업 보기"):

    data = career_data[mbti]

    st.success(f"{data['emoji']} 당신의 MBTI는 {mbti} 입니다!")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 💼 추천 직업")

        for job in data["jobs"]:
            st.write(f"✅ {job}")

    with col2:
        st.markdown("### 🎓 추천 학과")

        for major in data["major"]:
            st.write(f"📚 {major}")

    st.markdown("---")

    st.markdown("### 🌟 닮은 유명인")

    st.info(f"🎤 {data['person']}")

    st.markdown("---")

    strengths = [
        "창의력이 뛰어나요 🎨",
        "문제 해결 능력이 뛰어나요 🧠",
        "사람들과 협력하는 능력이 좋아요 🤝",
        "리더십이 강해요 👑",
        "도전 정신이 뛰어나요 🚀",
        "세심하고 책임감이 강해요 📋"
    ]

    st.markdown("### 💖 나의 강점")

    st.success(random.choice(strengths))

    st.markdown("---")

    st.markdown(
        f"""
        ## 🎯 진로 한 줄 조언

        > {mbti} 유형은 자신의 강점을 살릴 수 있는 분야를 찾을 때 가장 크게 성장할 수 있습니다!
        >
        > 🌈 다양한 경험을 하며 자신만의 꿈을 찾아보세요.
        """
    )

    st.snow()

# --------------------------
# 하단
# --------------------------

st.markdown("---")
st.caption("🏫 MBTI 진로 탐험대 | 진로교육용 웹앱")
