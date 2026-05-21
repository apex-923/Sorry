import streamlit as st
import time

# Set up page config for a cute title and emoji
st.set_page_config(
    page_title="The Friendship Repair Kit 🛠️❤️",
    page_icon="✨",
    layout="centered"
)

# Custom CSS to give it a soft, cute aesthetic
st.markdown("""
    <style>
    .reportview-container {
        background: #FFF5F5;
    }
    h1 {
        color: #FF6B6B;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    h3 {
        color: #4A4A4A;
    }
    .stButton>button {
        background-color: #FF8E8E;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #FF6B6B;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("The Friendship Repair Kit 🛠️❤️")
st.write("---")

# Step 1: Verification (Inside joke or her name)
# Replace 'bestie' with her actual name or a nickname!

st.subheader("🔒 Verification Required")
user_input = st.text_input("Enter the secret code word to unlock this app:", type="password", placeholder="Hint: What am I to u?")

if user_input.lower() == "mate" or user_input.lower() == "best friend": 
    st.balloons()
    st.success("Access Granted! Welcome back, Best Friend. ✨")
    
    st.write("---")
    
    # Step 2: The Core Apology Message
    st.subheader("A Quick Message From Me to You 📝")
    st.write(
        "Hey! I built this little app because words over text don't always cut it, "
        "and I wanted to show you how much our friendship means to me. "
        "I am incredibly sorry for messing up the other day. You're my best friend, "
        "and the last thing I ever want to do is upset you. 🥺"
    )
    
    # Step 3: Interactive Reasons Box
    with st.expander("💖 Click here for 3 reasons why you are irreplaceable:"):
        st.write("1. **You understand me in a way very few people do, and talking to you always feels natural.**")
        st.write("2. **The memories, support, and bond we built over the years can’t simply be replaced by another person.**")
        st.write("3. **Even after arguments, your presence still matters to me because you became an important part of my daily life.**")
    
    st.write("---")
    
    # Step 4: Interactive Peace Offering Selector
    st.subheader("Choose Your Peace Offering ☕🍕")
    st.write("Since I messed up, the ball is entirely in your court. Pick how you want me to make it up to you:")
    
    offering = st.multiselect(
    "Select one or more options:",
    [
        "I'll buy you jhumkas and your favorite snacks 🍬",
        "A small trip with just us two 🏞️",
        "I'll sing any song you want 🎤",
        "Just a long talk to clear the air whenever you're ready 💬"
    ]
)
    
    if st.button("Confirm Choice"):
        with st.spinner("Locking in your choice..."):
            time.sleep(1.5)
        st.success(f"Done! You selected: **{offering}**. I am holding myself to this!")

    st.write("---")

    # Step 5: The Interactive Forgiveness Slider
    st.subheader("The Forgiveness Gauge 📊")
    st.write("Where are we currently standing? (Be completely honest, no pressure!)")
    
    forgive_level = st.slider("Forgiveness Level:", 0, 100, 50)
    
    if forgive_level < 30:
        st.warning("Understandable. I'll give you your space and wait until you're ready. 💔")
    elif 30 <= forgive_level < 70:
        st.info("Making progress! I'll keep working to earn that trust back. ⏳🌱")
    else:
        st.success("Yay! Best friends again? I promise to keep being a better friend to you! 🥰🎉")
        st.snow()

elif user_input:
    st.error("Incorrect code word! 👀")
else:
    st.info("Waiting for the secret code word...")