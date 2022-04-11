class QuizBrain:
    def __init__(self, question_list):
        # question number always starts at 0
        self.question_number = 0
        # takes list of questions as an input
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        # checks if end of questions has been reached
        return self.question_number < len(self.question_list)

    def next_question(self):
        # this line gets the question number from the list, and the .text gets the text(or question)
        current_question = self.question_list[self.question_number]
        # gets input from user
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question.text} ')
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('You got it right!')
            self.score += 1
        else:
            print('That\'s wrong.')
        print(f'The correct answer was: {correct_answer}')
        print(f'Your current score is: {self.score}/{self.question_number}')
        print('\n')
        if self.question_number == len(self.question_list):
            print('You\'ve completed the quiz!')
            print(f'Your final score was: {self.score}/{self.question_number}')

