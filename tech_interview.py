import re

import pypdf

with open('Path for resume', 'rb') as file:
    pdf_reader = pypdf.PdfReader(file)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

question_database = {
    'python': [
        'What are the key features of Python?',
        'Explain the difference between lists and tuples in Python.',
        'How do you handle exceptions in Python?'
    ],
    'java': [
        'What is the difference between abstract classes and interfaces in Java?',
        'Explain the concept of garbage collection in Java.',
        'How do you implement inheritance in Java?'
    ],
    'sql': [
        'What is the difference between an inner join and an outer join?',
        'Explain the concept of normalization in database design.',
        'How do you optimize SQL queries for better performance?'
    ],
    'react': [
        'What are the key features of React?',
        'Explain the concept of virtual DOM in React.',
        'How do you handle state management in React?'
    ]
}


def extract_skills(text):
    skills = set(re.findall(r'\b\w+\b', text.lower()))
    return skills


def generate_questions(skills):
    questions = []
    for skill in skills:
        if skill in question_database:
            questions.extend(question_database[skill])
    return questions


skills = extract_skills(text)
questions = generate_questions(skills)

print("\nGenerated Interview Questions:")
for question in questions:
    print("- " + question)
