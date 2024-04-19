import json


class TechnicalInterviewer:
    def __init__(self) -> None:
        with open('questions.json') as questions:
            self.question_database: dict = json.load(questions)

    def generate_questions(self, skills: set):
        questions: list[str] = []
        for skill in skills:
            if skill in self.question_database:
                questions.extend(self.question_database[skill])
        return questions


if __name__ == '__main__':
    ti = TechnicalInterviewer()
