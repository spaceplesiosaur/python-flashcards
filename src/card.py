class Card:
    def __init__(self, id_num, question_string, answers_array, correct_answer_string):
        self.id = id_num
        self.question = question_string
        self.answers = answers_array
        self.correctAnswer = correct_answer_string
