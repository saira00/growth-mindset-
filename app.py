import streamlit as st

st.set_page_config(page_title="Growth Mindset Challenge", layout="wide")

# Custom CSS
custom_css = """
   <style>
    body {
        background-color: black !important;
        color: white !important;
    }

    section[data-testid="stSidebar"] {
        background-color: rgb(239, 228, 228) !important;
    }

    h1 {
        color: rgb(241, 53, 36) !important;
        text-align: center;
        font-size: 28px !important;
        font-weight: bold !important;
    }

    h2, h3 {
        color: rgb(231, 206, 20) !important;
        font-size: 22px !important;
        font-weight: bold !important;
    }

    div.stButton > button {
        background-color: #FF8C00 !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 10px 15px !important;
        font-size: 16px !important;
        font-weight: bold !important;
        transition: 0.3s ease-in-out !important;
        border: none !important;
    }

    div.stButton > button:hover {
        background-color: #FF4500 !important;
    }

  textarea {
    background-color: #222 !important;
    color: white !important;
    font-weight: normal !important;
    border-radius: 5px !important;
    border: 1px solid #777 !important;
    padding: 10px !important;
    font-size: 16px !important;
    resize: vertical !important; /* Allow resizing */
    min-height: 100px !important; /* Ensure height */
}

    input::placeholder, textarea::placeholder {
        color: #ccc !important;
        opacity: 0.8 !important;
    }
   </style>
"""


# Inject CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Daily Growth", "Daily Progress", "Create account"])

# Content for each page
if page == "Home":
    st.title("💡 Growth Mindset Challenge")
    st.subheader("Understanding a Growth Mindset")
    st.write("""
A growth mindset is about believing that skills and intelligence can improve with effort and practice.
A growth mindset is a concept developed by Carol Dweck, a psychologist. It's the idea that your abilities
and intelligence can be developed through hard work, dedication, and persistence. People with
a growth mindset believe that challenges and failures are opportunities for growth and learning.
In contrast, a fixed mindset is the idea that your abilities and intelligence are fixed and can't be changed.
Having a growth mindset can be really helpful for learning and achieving your goals. It can help you stay motivated,
overcome obstacles, and develop a love for learning. As a front-end developer, having a growth mindset can be especially
important, since the field is constantly evolving and there's always more to learn.
""")


elif page == "Daily Growth":
    st.title("🌟 Daily Growth")
    st.write("Here you can get motivational quotes and stories.")
    st.number_input("Pick a number", 0, 100)

elif page == "Daily Progress":
    st.title("📊 Daily Progress")
    st.write("Track your progress and set daily goals.")
    st.slider("Pick a number", 0, 100)

elif page == "Create account":
    st.title("📝 Create Account")
    
    name = st.text_input("Enter your name")
    fname = st.text_input("Enter your father name")
    adr = st.text_area("Enter your message")
    button = st.button("Done")
    if button :
        st.markdown(f"""
                    # Name: {name}  
                    # Father Name: {fname}  
                    # Address: {adr}  
                    """)

# Sidebar Footer
st.sidebar.markdown("---")
st.sidebar.subheader("Web Developer")
st.sidebar.write("📌 Created by: **Saira Kanwal**")
st.sidebar.write("📧 [Send Email](mailto:Sairawarisha8995@gmail.com)")
st.sidebar.write("🌐 [My Portfolio](https://your-portfolio-link.com)")  # Apna actual portfolio link dalna
