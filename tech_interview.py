import json


class TechnicalInterviewer:
    def __init__(self, question_database_file) -> None:
        with open(question_database_file) as questions_file:
            self.question_database: dict = json.load(questions_file)
        self.current_index = 0
        self.current_questions = []

    def generate_questions(self, skills: set):
        self.current_questions = []
        for skill in skills:
            if skill in self.question_database:
                self.current_questions.extend(self.question_database[skill])
        return self.current_questions

    def get_next_question(self):
        if self.current_index < len(self.current_questions):
            question = self.current_questions[self.current_index]
            self.current_index += 1
            return question
        else:
            return None


if __name__ == '__main__':
    ti = TechnicalInterviewer()
