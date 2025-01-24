# # Class names are in PascalCase
# class User:
#     # constructor
#     def __init__(self, id, name):
#         # Attributes
#         self.id = id
#         self.name = name
#         self.followers = 0
#         self.following = 0

#     # Methods
#     def follow(self, user_to_follow):
#         user_to_follow.followers += 1
#         self.following += 1


# user1 = User("001", "Chabi")
# user2 = User("001", "Dummy")
# user1.follow(user2)
# # user1.id = "001"
# # user1.name = "Chabi"
# print(f"{user1.id} : {user1.name} : {user1.followers} : {user1.following}")

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

brain = QuizBrain(question_bank)
while not brain.gameover and brain.has_questions_remaining():
    brain.next_question()
    
print(f"You've Completed the quiz! \nYour final score is {brain.score}/{brain.question_number}")