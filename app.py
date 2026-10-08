import streamlit as st

# ==========================================
#              PYTHON QUIZ GAME
# ==========================================

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "Who wrote the national anthem of India?",
        "options": [
            "A. Rabindranath Tagore",
            "B. Mahatma Gandhi",
            "C. Jawaharlal Nehru",
            "D. Subhash Chandra Bose"
        ],
        "answer": "A"
    },
    {
        "question": "How many days are there in a leap year?",
        "options": ["A. 365", "B. 366", "C. 364", "D. 367"],
        "answer": "B"
    },
    {
        "question": "Which language is used to create this program?",
        "options": ["A. HTML", "B. Java", "C. Python", "D. CSS"],
        "answer": "C"
    }
]


# ==========================================
#              PAGE DESIGN
# ==========================================

st.set_page_config(
    page_title="Python Quiz Game",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Python Quiz Game")
st.write("### Test your knowledge!")
st.divider()

# ==========================================
#              PLAYER NAME
# ==========================================

name = st.text_input("👤 Enter your name:")

st.write("### 📝 Answer the following questions")
st.write("Choose one answer for each question.")

# ==========================================
#              QUIZ FORM
# ==========================================

with st.form("quiz_form"):

    answers = []

    for number, question in enumerate(questions, start=1):

        st.subheader(f"Question {number}")
        st.write(question["question"])

        answer = st.radio(
            "Choose your answer:",
            question["options"],
            key=f"question_{number}",
            index=None
        )

        answers.append(answer)

        st.divider()

    submitted = st.form_submit_button(
        "🚀 Submit Quiz",
        use_container_width=True
    )


# ==========================================
#              RESULT
# ==========================================

if submitted:

    if name.strip() == "":
        st.warning("⚠️ Please enter your name first.")

    elif None in answers:
        st.warning("⚠️ Please answer all questions.")

    else:

        score = 0

        for i, answer in enumerate(answers):

            selected_letter = answer[0]
            correct_answer = questions[i]["answer"]

            if selected_letter == correct_answer:
                score += 1

        total_questions = len(questions)
        percentage = (score / total_questions) * 100

        st.divider()

        st.header("🏆 QUIZ RESULT")

        st.success(f"Hello, {name}!")

        st.metric(
            "Your Score",
            f"{score} / {total_questions}"
        )

        st.metric(
            "Percentage",
            f"{percentage:.2f}%"
        )

        # ==========================================
        #              GRADE
        # ==========================================

        if percentage == 100:
            grade = "A+"
            message = "Excellent! 🏆"
            st.balloons()

        elif percentage >= 80:
            grade = "A"
            message = "Very Good! 🌟"

        elif percentage >= 60:
            grade = "B"
            message = "Good Job! 👍"

        elif percentage >= 40:
            grade = "C"
            message = "Keep Practicing! 📚"

        else:
            grade = "D"
            message = "Try Again! 💪"

        st.write(f"### Grade: {grade}")
        st.info(message)

        st.divider()

        # ==========================================
        #          ANSWER REVIEW
        # ==========================================

        st.subheader("📋 Answer Review")

        for i, answer in enumerate(answers):

            correct = questions[i]["answer"]

            if answer[0] == correct:
                st.success(
                    f"Question {i + 1}: ✅ Correct"
                )
            else:
                st.error(
                    f"Question {i + 1}: ❌ Wrong — "
                    f"Correct answer: {correct}"
                )

        st.write("---")
        st.write("🎉 Thanks for playing!")
