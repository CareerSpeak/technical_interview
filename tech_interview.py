import json
import re

import pypdf

with open('Path for resume', 'rb') as file:
    pdf_reader = pypdf.PdfReader(file)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

question_database = {}

with open('questions.json') as questions:
    question_database = json.load(questions)


def extract_skills(text):
    skills = set(re.findall(r'\b\w+\b', text.lower()))
    return skills


def generate_questions(skills):
    questions = []
    for skill in skills:
        if skill in question_database:
            questions.extend(question_database[skill])
    return questions


print(question_database)

skills = extract_skills(text)
questions = generate_questions(skills)

print("\nGenerated Interview Questions:")
for question in questions:
    print("- " + question)
