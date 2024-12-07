import streamlit as st
import json
from libs.irs import iris

if "answers" not in st.session_state:
    st.session_state.answers = {}

data = {"s1": {}, "s2": {}}

questions = [
    "Which city do you want to visit?",
    "What are you available timings?",
    "What is your budget for the plan?",
    "What are your interests? (e.g. culture, adventure, food, shopping)",
]

st.title("Itinerary Recommendation System (IRS)")

st.subheader("Section 1 - Fill all boxes")

for i, question in enumerate(questions):
    answer_key = f"section1_answer_{i}"
    if answer_key not in st.session_state.answers:
        st.session_state.answers[answer_key] = ""
    st.session_state.answers[answer_key] = st.text_input(
        question, value=st.session_state.answers[answer_key], key=answer_key
    )
    data["s1"][question] = st.session_state.answers[answer_key]

if st.button("Submit Section 1"):
    all_filled = all(
        st.session_state.answers[key].strip()
        for key in st.session_state.answers.keys()
        if key.startswith("section1")
    )
    if all_filled:
        st.success("Section 1 updated successfully!")
    else:
        st.warning("Please fill in all the questions before submitting.")

#############################################################

st.subheader("Section 2 - Fill necessary boxes")

questions = [
    "What is your preferred starting point? (hotel, mall, etc)",
    "Give some preferences for the recommendation you want (leave empty if unsure)",
]

for i, question in enumerate(questions):
    answer_key = f"section2_answer_{i}"
    if answer_key not in st.session_state.answers:
        st.session_state.answers[answer_key] = ""
    st.session_state.answers[answer_key] = st.text_input(
        question, value=st.session_state.answers[answer_key], key=answer_key
    )

    data["s2"][question] = st.session_state.answers[answer_key]


# irs = ItineraryResolver()  # IRS object to handle LLM stuff
if st.button("Submit Section 2"):
    print("\n\n\n\n")
    # print(json.dumps(data, indent=2))

    result_panel = st.empty()
    result_panel.info("Generating itinerary...")

    iris.update_data(data)
    results = iris.ProcessPreference()

    # Update the panel with results
    result_panel.success("Here you go!")
    st.write("Here are the processed results:")
    st.write(results)
