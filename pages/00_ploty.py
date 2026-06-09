import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(
    page_title="글로벌 시가총액 TOP10 대시보드",
    page_icon="📈",
    layout="wide"
)

st.title("📈 글로벌 시가총액 TOP10 주식 대시보드")
st.markdown("최근 1년 주가 변화 비교")

# 글로벌 시가총액 상위 기업 (2025~2026 기준)
TOP10 = {
    "Microsoft": "MSFT",
    "NVIDIA": "NVDA",
    "Apple": "AAPL",
    "Amazon": "AMZN",
    "Alphabet": "GOOGL",
    "Meta": "META",
    "Saudi Aramco": "2222.SR",
    "Broadcom": "AVGO",
    "TSMC": "TSM",
    "Berkshire Hathaway": "BRK-B"
}

@st.cache_data(ttl=3600)
def load_data():
    end_date = datetime.today()
    start_date = end_date - timedelta(days=365)

    all_data = pd.DataFrame()

    for company, ticker in TOP10.items():
        try:
            df = yf.download(
                ticker,
                start=start_date,
                end=end_date,
                progress=False,
                auto_adjust=True
            )

            if not df.empty:
                all_data[company] = df["Close"]

        except:
            pass

    return all_data

with st.spinner("데이터 불러오는 중..."):
    data = load_data()

if data.empty:
    st.error("데이터를 불러올 수 없습니다.")
    st.stop()

selected = st.multiselect(
    "기업 선택",
    list(data.columns),
    default=list(data.columns[:5])
)

normalize = st.checkbox(
    "100 기준 수익률 비교",
    value=True
)

chart_data = data[selected].copy()

if normalize:
    chart_data = chart_data / chart_data.iloc[0] * 100

fig = go.Figure()

for col in chart_data.columns:
    fig.add_trace(
        go.Scatter(
            x=chart_data.index,
            y=chart_data[col],
            mode="lines",
            name=col
        )
    )

fig.update_layout(
    height=650,
    hovermode="x unified",
    template="plotly_white",
    xaxis_title="날짜",
    yaxis_title="주가" if not normalize else "상대수익률 (100 기준)",
    legend_title="기업"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("🏆 최근 1년 수익률")

returns = (
    data.iloc[-1] / data.iloc[0] - 1
) * 100

returns = returns.sort_values(ascending=False)

ranking = pd.DataFrame({
    "기업": returns.index,
    "수익률(%)": returns.values.round(2)
})

st.dataframe(
    ranking,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.subheader("📊 현재 종가")

latest = pd.DataFrame({
    "기업": data.columns,
    "종가": data.iloc[-1].round(2).values
})

st.dataframe(
    latest,
    use_container_width=True,
    hide_index=True
)
