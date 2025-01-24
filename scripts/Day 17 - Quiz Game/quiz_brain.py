class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_bank = question_bank
        self.score = 0
        self.gameover = False

    def next_question(self):
        current_question = self.question_bank[self.question_number]
        guess = input(f"{current_question.text} (True/False): ")
        self.question_number += 1
        self.is_answer_correct(guess, current_question.answer)    

    def has_questions_remaining(self):
        #print(f"{self.question_number} : {len(self.question_bank)}")
        return self.question_number < len(self.question_bank)
    
    def is_answer_correct(self,  guess, answer):
        correct = guess.lower() == answer.lower()
        if correct:
            print("You Got It!")
            self.score += 1
            print(f"Your Score: {self.score}/{self.question_number}")
                        
        else: 
            print(f"Not Quite. The answer is {answer}.")
            self.gameover = True
