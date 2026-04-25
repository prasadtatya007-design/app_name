
import streamlit as st
import pandas as pd

# Page Config
st.set_page_config(
    page_title="Space Explorer Adventure",
    page_icon="🚀",
    layout="wide"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>

/* Main App Background */
.stApp {
    background: linear-gradient(to bottom, #020111, #191621, #000000);
    color: white;
}

/* Home Page Starry Background */
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1446776811953-b23d57bd21aa");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Transparent container */
.block-container {
    background: rgba(0,0,0,0.55);
    padding: 2rem;
    border-radius: 20px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(10, 10, 30, 0.95);
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #3a0ca3, #4361ee);
    color: white;
    border-radius: 25px;
    padding: 10px 22px;
    font-size: 18px;
    border: none;
    box-shadow: 0 0 15px #4361ee;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.08);
    box-shadow: 0 0 25px #7209b7;
}

/* Titles */
h1, h2, h3 {
    color: #ffffff;
    text-shadow: 0 0 10px cyan;
}

/* Radio labels */
label {
    color: white !important;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

# ------------------ TITLE ------------------
st.title("🚀 Space Explorer Adventure")

# Sidebar Navigation
st.sidebar.title("🛰️ Navigation")
choice = st.sidebar.radio(
    "Choose Destination:",
    ["🏠 Home", "🧑‍🚀 Space Quiz", "🛰️ Mission Planner"]
)

# ------------------ HOME ------------------
if choice == "🏠 Home":
    st.header("🌌 Welcome Astronaut!")

    col1, col2 = st.columns([2,1])

    with col1:
        st.markdown("""
        ## Explore the Universe 🌠

        Welcome to the most exciting space journey ever!

        ### What You Can Do:
        - 🧑‍🚀 Take the Space Quiz  
        - 🛰️ Plan Your Own Mission  
        - 🌍 Discover Space Facts  

        ### Fun Fact:
        There are more stars in the universe than grains of sand on Earth!
        """)

        st.success("✨ Ready for liftoff? Use the sidebar!")

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1451187580459-43490279c0fa",
            use_container_width=True
        )

# ------------------ QUIZ ------------------
elif choice == "🧑‍🚀 Space Quiz":

    st.header("🧑‍🚀 Test Your Space Knowledge")

    q1 = st.radio(
        "Q1: Largest planet?",
        ["Earth", "Jupiter", "Mars"]
    )

    q2 = st.radio(
        "Q2: First human in space?",
        ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin"]
    )

    q3 = st.radio(
        "Q3: Our galaxy?",
        ["Milky Way Galaxy", "Andromeda Galaxy", "Whirlpool Galaxy"]
    )

    if st.button("🚀 Submit Quiz"):
        score = 0
        score += 1 if q1 == "Jupiter" else 0
        score += 1 if q2 == "Yuri Gagarin" else 0
        score += 1 if q3 == "Milky Way Galaxy" else 0

        st.subheader(f"⭐ Score: {score}/3")

        if score == 3:
            st.balloons()
            st.success("🌟 Perfect! You are Space Commander!")
        elif score == 2:
            st.info("🚀 Great Job!")
        else:
            st.warning("🪐 Keep Learning!")

# ------------------ MISSION ------------------
elif choice == "🛰️ Mission Planner":

    st.header("🛰️ Plan Your Space Mission")

    spacecraft = st.text_input("🚀 Spacecraft Name", "Star Explorer")

    launch_date = st.date_input("📅 Launch Date")

    launch_time = st.time_input("⏰ Launch Time")

    spaceship = st.selectbox(
        "Choose Vehicle",
        ["🚀 Rocket", "🛸 Shuttle", "🏢 Space Station"]
    )

    planet = st.selectbox(
        "Destination",
        ["🌕 Moon", "🔴 Mars", "🪐 Saturn", "🌍 Earth Orbit"]
    )

    if st.button("✅ Save Mission"):
        st.success(
            f"Mission '{spacecraft}' launching on {launch_date} at {launch_time} "
            f"using {spaceship} to {planet}"
        )
