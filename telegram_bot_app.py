import streamlit as st
import telebot

# Function to send data to a Telegram bot using telebot
def send_to_telegram(name, college_name, course, stream, phone_number, project):
    telegram_token = '7303279676:AAEK2V3L6iAJpL4jAGmuB3YTBEaEe7MMhYo'
    chat_id = '2034283378'
    message = (
        f"New Candidate Registration:\n\n"
        f"**Name:** {name}\n"
        f"**College Name:** {college_name}\n"
        f"**Course:** {course}\n"
        f"**Stream:** {stream}\n"
        f"**Phone Number:** {phone_number}\n"
        f"**Project Needed:** {project}"
    )
    
    bot = telebot.TeleBot(telegram_token)
    try:
        bot.send_message(chat_id, message, parse_mode='Markdown')
        return True
    except Exception as e:
        st.error(f"Failed to send message to Telegram. Error: {str(e)}")
        return False

# Streamlit UI
st.title("Registration Form")

# Create a form
with st.form(key='college_form'):
    name = st.text_input("Enter Your Name")
    college_name = st.text_input("Enter Your College Name")
    course = st.text_input("Enter Your Course")
    
    stream = st.radio("Stream", ("CSE", "AIML", "Data Science", "Cyber Security", "Others"))
    
    phone_number = st.text_input("Enter Your Whatsapp Number to Contact With You")
    
    project = st.radio("Do You Need Project", ("Yes", "No"))
    
    # Submit button
    submit_button = st.form_submit_button(label='Submit')

# Display submitted data and save to Telegram
if submit_button:
    st.write("## Submitted Data")
    st.write(f"**Name:** {name}")
    st.write(f"**College Name:** {college_name}")
    st.write(f"**Course, Year:** {course}")
    st.write(f"**Stream:** {stream}")
    st.write(f"**Phone Number:** {phone_number}")
    st.write(f"**Project Needed:** {project}")
    
    # Send the data to Telegram
    if send_to_telegram(name, college_name, course, stream, phone_number, project):
        st.success("You are Registered Successfully We'll Contact you shortly!")
    else:
        st.error("Failed to send data to Telegram. Please check your Telegram bot token and chat ID and try again.")

