from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Creates a list of objects(the attributes that the objects have are text and answer)
question_bank = []
for i in question_data:
    new = Question(i['question'], i['correct_answer'])
    question_bank.append(new)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


