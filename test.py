import streamlit as st
import pandas as pd
import datetime

# 페이지 설정
st.set_page_config(page_title="우리 축구팀", layout="wide")

# 팀 소개
st.title("⚽ 우리 축구팀 웹페이지")
st.header("팀 소개")
st.image("team_logo.png", width=200)
st.write("우리 팀은 2024년에 창단된 축구팀으로, 열정과 팀워크를 바탕으로 경기에 임합니다!")

# 팀원 소개
st.subheader("👥 팀원 소개")
players = pd.DataFrame({
    "이름": ["김민수", "이영호", "박정우", "최서연", "정하늘"],
    "포지션": ["FW", "MF", "DF", "GK", "MF"],
    "등번호": [9, 7, 5, 1, 10]
})
st.dataframe(players, hide_index=True)

# 경기 일정 및 결과
st.subheader("📅 경기 일정 및 결과")
match_data = pd.DataFrame({
    "날짜": ["2025-03-10", "2025-03-17", "2025-03-24"],
    "상대팀": ["팀 A", "팀 B", "팀 C"],
    "결과": ["2-1 승", "1-3 패", "3-3 무"]
})
st.dataframe(match_data, hide_index=True)

# 선수별 통계
st.subheader("📊 선수별 경기 통계")
player_stats = pd.DataFrame({
    "이름": ["김민수", "이영호", "박정우", "최서연", "정하늘"],
    "득점": [5, 2, 0, 0, 3],
    "어시스트": [1, 4, 2, 0, 1],
    "출전 경기 수": [3, 3, 3, 3, 3]
})
st.dataframe(player_stats, hide_index=True)

# 사진/영상 갤러리
st.subheader("📸 사진 및 영상 갤러리")
st.image(["match1.jpg", "match2.jpg", "match3.jpg"], width=300)
st.video("highlight.mp4")

st.write("© 2025 우리 축구팀. 모든 권리 보유.")
