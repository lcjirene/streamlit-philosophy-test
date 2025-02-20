import streamlit as st

def calculate_educational_philosophy(scores):
    """
    Calculate the subscale scores based on the user's responses.
    :param scores: List of 36 integers (Likert scale 1-5)
    :return: Dictionary with scores for each philosophy and the highest scoring philosophies
    """
    if len(scores) != 36:
        raise ValueError("Invalid number of responses. Expected 36 values.")
    
    philosophies = {
        "Essentialism": sum([scores[i-1] for i in [1, 7, 13, 19, 25, 31]]),
        "Behaviorism": sum([scores[i-1] for i in [2, 8, 14, 20, 26, 32]]),
        "Progressivism": sum([scores[i-1] for i in [3, 9, 15, 21, 27, 33]]),
        "Existentialism": sum([scores[i-1] for i in [4, 10, 16, 22, 28, 34]]),
        "Perennialism": sum([scores[i-1] for i in [5, 11, 17, 23, 29, 35]]),
        "Reconstructionism": sum([scores[i-1] for i in [6, 12, 18, 24, 30, 36]])
    }
    
    max_score = max(philosophies.values())
    highest_philosophies = [k for k, v in philosophies.items() if v == max_score]
    
    descriptions = {
        "Essentialism": "A conservative approach that focuses on core knowledge, discipline, and respect for authority. Influential thinkers: William C. Bagley, Arthur Bestor, E.D. Hirsch.",
        "Behaviorism": "Learning is shaped by external rewards and reinforcements, denying free will. The role of educator is to identify behavioural goals and establish reinforcers to achieve goals. Key figures: B.F. Skinner, Ivan Pavlov, J.B. Watson.",
        "Progressivism": "Education should be student-centered, emphasizing critical thinking and real-world problem-solving. Education should help learners develop personal and social values. Notable proponents: John Dewey, Francis Parker.",
        "Existentialism": "Education stresses the importance of personal choice, self-definition, and individual experiences. Key contributors: Jean-Paul Sartre, Carl Rogers, Maxine Greene.",
        "Perennialism": "Education should focus on intellectual development through great works and highest level of knowledge in each field should be the focus of the curriculum. Prominent thinkers: Robert Hutchins, Mortimer Adler, Allan Bloom.",
        "Reconstructionism": "Schools should go beyond mere knowledge transmission; they should lead social change and transform society through education. Influential figures: Theodore Brameld, Paulo Freire, Henry Giroux."
    }
    
    return philosophies, highest_philosophies, [descriptions[ph] for ph in highest_philosophies]

st.title("Educational Philosophy Inventory")
st.write("This inventory, adapted from Robert Leahy (1995) for 'Becoming a Teacher: Accepting the Challenge of a Profession' (3rd Ed.), is a tool to help you identify your educational philosophy.")
st.write("Respond to the following statements on a scale from 1 ‘Strongly Disagree’ to 5 ‘Strongly Agree’ that most closely matches your perspective.")

questions = [
        f"{i+1}. {q}" for i, q in enumerate([
    "1. The curriculum should emphasize essential knowledge, not students’ personal interests.",
    "2. All learning results from rewards controlled by the external environment.",
    "3. Educators should emphasize interdisciplinary subject matter that encourages project-oriented, democratic classrooms.",
    "4. Education should emphasize the search for personal meaning, not a fixed body of knowledge.",
    "5. The ultimate aim of education is constant, absolute, and universal: to develop the rational person and cultivate the intellect.",
    "6. Education should actively involve learners in social change to reform society.",
    "7. Educational institutions should teach basic skills, not humanistic ideals.",
    "8. Eventually, human behavior will be explained by scientific laws, proving there is no free will.",
    "9. Educators should be facilitators and resources who guide learners’ inquiry, not managers of behavior.",
    "10. The best educators encourage personal responses and develop self-awareness in learners.",
    "11. The curriculum should be the same for everyone: the collective wisdom of Western culture delivered through lecture and discussion.",
    "12. Education should lead society toward radical social change, not transmit traditional values.",
    "13. The purpose of education is to ensure practical preparation for life and work, not to encourage personal development.",
    "14. Good teaching establishes an environment to control learner’s behavior and to measure learning of prescribed objectives.",
    "15. Curriculum should emerge from learners’ needs and interests; therefore, it should not be prescribed in advance.",
    "16. Helping learners develop personal values is more important than transmitting traditional values.",
    "17. The best education consists primarily of exposure to great works in the humanities.",
    "18. It is more important for teachers to involve learners in activities to criticize and transform society than to teach the Great Books.",
    "19. Educators should emphasize discipline, hard work, and respect for authority, not encourage free choice.",
    "20. Human learning can be controlled: Anyone can be taught to be a scientist or a thief; therefore, personal choice is a myth.",
    "21. Education should enhance personal growth through problem solving in the present, not emphasize preparation for a distant future.",
    "22. Because we are born with an unformed personality, personal growth should be the focus of education.",
    "23. Human nature is a constant – its most distinctive quality is the ability to reason; therefore, the intellect should be the focus of education.",
    "24. Educational institutions perpetrate racism and sexism camouflaged as traditional values.",
    "25. Educators should efficiently transmit a common core of knowledge, not experiment with curriculum.",
    "26. Teaching is primarily management of learners’ behavior to achieve the teacher’s objectives.",
    "27. Educators should involve learners in democratic activities and reflective thinking.",
    "28. Learners should have significant involvement in choosing what and how they learn.",
    "29. Educators should promote the permanency of the classics.",
    "30. Learning should lead learners to involvement in social reform.",
    "31. On the whole, educational institutions should and must indoctrinate learners with traditional values.",
    "32. If ideas cannot be proved by science, they should be ignored as superstition and nonsense.",
    "33. The major goal for educators is to create an environment where learners can learn on their own by guided reflection on their experiences.",
    "34. Educators should create opportunities for learners to make personal choices, not shape their behavior.",
    "35. The aim of education should be the same in every age and society, not differ from educator to educator.",
    "36. Education should lead society toward social betterment, not confine itself to essential skills."
])
]

responses = []
for question in questions:
    responses.append(st.radio(question, ["1 - Strongly Disagree", "2 - Disagree", "3 - Neutral", "4 - Agree", "5 - Strongly Agree"], index=2))

if st.button("Submit"):
    scores, highest_philosophies, descriptions = calculate_educational_philosophy([int(radio.split(" - ")[0]) for radio in responses])
    
    st.write("### Your Highest Educational Philosophies:", ", ".join(highest_philosophies))
    st.write("### Scores:", scores)
    
    for philosophy, description in zip(highest_philosophies, descriptions):
        st.write(f"#### {philosophy}")
        st.write(description)
    
    st.write("\nThis tool was prepared by Robert Leahy (1995) for 'Becoming a Teacher: Accepting the Challenge of a Profession' (3rd Ed.)")
