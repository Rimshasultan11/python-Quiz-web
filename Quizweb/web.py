import streamlit as st
import time
import pandas as pd

# Initialize session state
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False

st.set_page_config(
    page_title="Quiz",
    page_icon="🏆",
    layout="centered"
)

st.title("🎉 Welcome to the Quiz! 🏆")

st.write("This quiz will test your knowledge of Python and Streamlit! Ready to challenge yourself?")


# Sidebar Navigation
st.sidebar.markdown("### Enter your details to start the quiz")
name = st.sidebar.text_input("👤 Enter your name:")
roll_number = st.sidebar.text_input("🎓 Enter your Roll Number:")

if name and roll_number:
    st.sidebar.success(f"Hello, {name} (Roll No: {roll_number})! 🎉 Click below to start the quiz.")
    if st.sidebar.button("🚀 Start Quiz"):
        st.session_state.quiz_started = True

# Quiz Section
if st.session_state.quiz_started:
    st.markdown("---")
    st.title("🧠 Python & Streamlit Knowledge Test")
    st.markdown("### Answer the following questions:")
    
    # Quiz Data
    questions = [
        {"question": "🐍 What is the output of print(type([])) in Python?", "options": ["list", "tuple", "dict", "set"], "answer": "list"},
        {"question": "🔄 Which keyword is used to define a function in Python?", "options": ["def", "func", "define", "lambda"], "answer": "def"},
        {"question": "🧮 What will be the output of 3 * 3 ** 3 in Python?", "options": ["27", "81", "9", "None"], "answer": "81"},
        {"question": "🎯 What is the correct way to start a Streamlit app?", "options": ["streamlit launch", "python app.py", "streamlit run app.py", "run streamlit"], "answer": "streamlit run app.py"},
        {"question": "📊 Which Streamlit function is used to display charts?", "options": ["st.line_chart()", "st.graph()", "st.plot()", "st.display_chart()"], "answer": "st.line_chart()"},
        {"question": "💡 What is the purpose of `st.session_state` in Streamlit?", "options": ["Store user sessions", "Track app state", "Both A and B", "None"], "answer": "Both A and B"},
        {"question": "⚙️ Which function in Streamlit allows file uploads?", "options": ["st.upload()", "st.file_uploader()", "st.send_file()", "st.upload_file()"], "answer": "st.file_uploader()"},
        {"question": "🔍 What is the correct way to create a slider in Streamlit?", "options": ["st.slider()", "st.range()", "st.scroll()", "st.slide()"], "answer": "st.slider()"},
        {"question": "📢 What function is used to display messages in Streamlit?", "options": ["st.alert()", "st.popup()", "st.toast()", "st.message()"], "answer": "st.toast()"},
        {"question": "📜 How do you install Streamlit?", "options": ["pip install streamlit", "python install streamlit", "pip get streamlit", "install streamlit"], "answer": "pip install streamlit"},
    ]
    
    score = 0
    results = []
    
    for i, q in enumerate(questions):
        user_answer = st.radio(q["question"], q["options"], key=f"q{i}")
        is_correct = user_answer == q["answer"]
        if is_correct:
            score += 1
        results.append({"Question": q["question"], "Your Answer": user_answer, "Correct Answer": q["answer"], "Result": "✅ Correct" if is_correct else "❌ Incorrect"})
    
    if st.button("🚀 Submit Quiz"):
        with st.spinner("Calculating score..."):
            time.sleep(2)  # Simulate processing time
        
        if score == len(questions):
            st.balloons()
            st.success("🎉 Congratulations! You won the quiz! 🏆")
            st.info(f"🎉 {name} , you scored {score} / {len(questions)}! Well done!")
           
        else:
            st.warning("💔 Oops! You lost. Try again!")
            st.info(f"😢 {name} , you scored {score} / {len(questions)}. Better luck next time!")
             # Display results in a table
            st.markdown("### Quiz Summary")
            st.dataframe(pd.DataFrame(results))
            
    # Footer
    st.markdown("---")
    st.write("📌 Made by || Rimsha sultan 🧡")
else:
    st.info("👈 Let's Start a Fun and Educational Quiz! 🎉")
