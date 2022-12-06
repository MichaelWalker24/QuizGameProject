# Step 4: Bring up question and ask the user to answer the question
# All quiz functionality will be in this file

# 4a. Create a Class called QuizBrain
class QuizBrain: 
    # 4b. Create constructor to initialize the necessary attributes: question number and user score which will have default values and question list which will be passed into the constructor
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
    
    #4c. Create a Method that retrieves the question from the question list (created in main.py)
    def next_question(self):
        current_question = self.question_list[self.question_number]
        # 4d. Lists start at 0, so to display the correct question number for the next step increase question number by 1
        self.question_number += 1
        #4e. Show the number, text, and ask for the user's answer
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        # 8e. When advancing to the next question check the answer the user gave
        self.check_answer(user_answer, current_question.answer)

    # Step 7: Create a Method that advances the questions after the user has answered
    def still_has_questions(self):
        # This method will return a Boolean
        return self.question_number < len(self.question_list)
     
    # Step 8: Create a Method that will check the answer that the user gives
    def check_answer(self, user_answer, correct_answer):
        # 8a. Create if/else statement that compares user and correct answer, be sure to account for varying cases in user answer's
        if user_answer.lower() == correct_answer.lower():
            # 8b. Increase score by 1
            self.score += 1
            # 8c. Let user know they are correct
            print("You got it right! Wohoo!")
        # 8d. Create else statement for when user gets answer wrong
        else: 
            print("You got it wrong :(")

            # NEXT STEP IS IN next_question METHOD

        # 8f. Display correct answer
        print(f"The correct answer was: {correct_answer}")
        # 8g. Display the users score out of how many questions have been asked
        print(f"Your current score is: {self.score}/{self.question_number}")
        # 8h. Create a space between the questions for readability
        print("\n")

