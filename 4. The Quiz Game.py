# Objective:
# The aim of this assignment is to create a quiz game that asks questions and checks answers.

# Task 1: Develop a list of questions and answers.

import math

Question1 = "How many countries in the world are there? \n"
Answer1 = "195"
Question2 = "Who is the president of the United States currently? \n"
Answer2 = "Joe Biden"
Question3 = "What's the name of this coding school? \n"
Answer3 = "Coding Temple"
Questions = []
Answers = []

Questions.append(Question1)
Questions.append(Question2)
Questions.append(Question3)

Answers.append(Answer1)
Answers.append(Answer2)
Answers.append(Answer3)

Score = 0


# Task 2: Write a function that quizzes the user and takes their answers.
def QuizGame(*Problems):
    global Answers
    global Score
    responses = []
    i = 0

    for x in Problems:
        userAnswer = input(f"{x}")
        responses.append(userAnswer)
    
    while i < len(responses):
        if responses[i] == Answers[i]:
            print(f"for the question: {Problems[i]} you responded {responses[i]}. That's correct!")
            i+=1
            Score += 1
        else:
            print(f"for the question: {Problems[i]} you responded {responses[i]}. That's incorrect! The correct answer was {Answers[i]}")
            i+=1
    return Score

# Task 3: Score the quiz and give the user feedback on their performance.
ResponseScore = QuizGame(*Questions)
totalScore = math.floor((ResponseScore/len(Questions))*100)  
if totalScore == 100:
    print(f"Great Job! Your score was {totalScore}%!")
elif totalScore == 66:
    print(f"Nice! Your score was {totalScore}%!")
elif totalScore == 33:
    print(f"Ok, your score was {totalScore}%. You should try harder next time.")
else:
    print(f"Your score was {totalScore}%. I guess you don't know anything!")

