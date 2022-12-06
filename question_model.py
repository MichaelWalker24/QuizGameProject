# Step 1: Create a question model (Class)

# Create a Class that can be used as a constructor to build new questions

class Question: 
    # Use the __init__ keyword to indicate the function is a constructor
    # Set up 2 attributes for the question text and answer
    def __init__(self, q_text, q_answer):
    # Be sure to use the "self" syntax to be able refer back the object and to access the attributes later
        self.text = q_text
        self.answer = q_answer



# Test to make sure it is functioning properly
# new_q = Question("Hello", "False")
# print(new_q.text)