app.pyimport streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="이상권 명품 시계 검색기", page_icon="🥕", layout="centered")

# 2. 커스텀 CSS (심플 로고 디자인 및 폰트 설정)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Nanum+Gothic:wght@400;700&display=swap');

    /* 브랜드 로고 그리드 */
    .logo-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
        gap: 12px;
        margin-top: 20px;
    }

    .brand-logo {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 55px;
        background-color: #ffffff;
        border: 1px solid #eeeeee;
        border-radius: 8px;
        text-decoration: none !important;
        color: #111111 !important;
        font-family: 'Playfair Display', serif;
        font-size: 12px;
        font-weight: bold;
        text-align: center;
        transition: all 0.2s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }

    .brand-logo:hover {
        border-color: #ff7e36;
        color: #ff7e36 !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 10px rgba(255, 126, 54, 0.1);
    }
    
    .modern { font-family: 'Nanum Gothic', sans-serif; letter-spacing: 0.5px; }

    .search-section {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #f0f0f0;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# --- UI 레이아웃 ---

# 메인 타이틀 변경
st.title("🥕 이상권 명품 시계 검색기")
st.write("찾으시는 브랜드 로고를 클릭하면 당근마켓 매물 페이지가 즉시 열립니다.")

# 1. 브랜드 데이터 정의 (시계 및 럭셔리 브랜드 중심)
brands = [
    ("Patek Philippe", "serif"), ("Audemars Piguet", "serif"), ("Vacheron Constantin", "serif"),
    ("Breguet", "serif"), ("A. Lange & Söhne", "serif"), ("Rolex", "modern"),
    ("Omega", "modern"), ("Cartier", "serif"), ("IWC", "modern"),
    ("Jaeger-LeCoultre", "serif"), ("Chanel", "modern"), ("Hermès", "serif"),
    ("Louis Vuitton", "modern"), ("Gucci", "modern"), ("Dior", "modern")
]

# 2. 로고 버튼 그리드 생성
st.markdown("### ✨ 하이엔드 브랜드 퀵 서치")
brand_html = '<div class="logo-grid">'
for name, style in brands:
    url = f"https://www.daangn.com/search/{name}"
    font_class = "brand-logo" if style == "serif" else "brand-logo modern"
    brand_html += f'<a href="{url}" target="_blank" class="{font_class}">{name.upper()}</a>'
brand_html += '</div>'

st.markdown(brand_html, unsafe_allow_html=True)

# 3. 직접 검색 섹션
with st.container():
    st.markdown('<div class="search-section">', unsafe_allow_html=True)
    st.write("🔍 **특정 모델명이나 다른 물품 검색**")
    col1, col2 = st.columns([4, 1])
    
    with col1:
        custom_keyword = st.text_input("검색어 입력", placeholder="예: 서브마리너, 데이저스트, 가습기...", label_visibility="collapsed")
    
    with col2:
        if custom_keyword:
            target_url = f"https://www.daangn.com/search/{custom_keyword.strip()}"
            st.markdown(f"""
                <a href="{target_url}" target="_blank" style="
                    display: block; width: 100%; text-align: center; text-decoration: none;
                    background-color: #ff7e36; color: white; padding: 10px; border-radius: 8px;
                    font-weight: bold; font-size: 14px;
                ">검색</a>
            """, unsafe_allow_html=True)
        else:
            st.button("검색", disabled=True, key="disabled_btn")
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()
st.caption("© 이상권 명품 시계 검색기 | 당근마켓 실시간 매물 연결 서비스")
