# module import
import json
import re

import PyPDF4 as pypdf

# literals
filepath = r"/home/xl/ebooks/Computer Science/Network/CompTIA/"
filename = r"CompTIA Network Practice Tests Exam N10 008 2nd Edition 1119807301"
filetype = r".pdf"

EXPORT_PATH = r"/home/xl/projects/exam_simulator/"

# preparations
answers = []  # empty list for captured answers/questions
questions = []
answer_dict = {}  # empty dictionary for answers/questions
question_dict = {}


def pdf_to_text(page_start, page_end):

    content = ""

    file = open("".join([filepath, filename, filetype]), "rb")
    # print("file open")

    # creating a pdf reader object
    pdf = pypdf.PdfFileReader(file)

    # parsing
    for page in range(page_start, page_end):
        page = pdf.getPage(page).extractText()
        content += page

    # closing the pdf file object
    file.close()
    # print("file close")

    return content


net_fund_answers = pdf_to_text(325, 360)  # 360


# fix to capture only half of last page, new chapter starts on same page
regex = "Chapter.2: Network Implementation"
regex_object = re.compile(regex)
match = regex_object.search(net_fund_answers)
start, stop = match.span()
net_fund_answers = net_fund_answers[:start]

# fix to capture last answer
net_fund_answers = net_fund_answers + "\n1."

# complete answer regex

regex = r"\n(\d{1,3}\.\n.*?\n)\d{1,3}\."
regex_object = re.compile(regex, re.DOTALL)

while match is not None:
    match = regex_object.search(net_fund_answers)
    if match is not None:
        start, end = match.span()
        answers.append(match.group(1))
        net_fund_answers = net_fund_answers[end - 10 :]

# fix
answers[120] = answers[120] + "".join(answers[121:127]).replace(".", "")
answers[121:127] = []

# print([answers[0]])


for idx, value in enumerate(answers):

    # regex
    # answer number
    regex = r"^\d{1,3}\."
    regex_object = re.compile(regex)
    match = regex_object.search(answers[idx])
    answer_nbr = match.group().replace(".", "")
    # print(answer_nbr)

    # answer
    regex = r"(([A-G],\s)*[A-G])\."
    regex_object = re.compile(regex)
    match = regex_object.search(answers[idx])
    answer = match.group(1).replace(" ", "").split(",")
    # print(answer)

    # explanation
    regex = r"[A-G]\.\n \n(.*)"
    regex_object = re.compile(regex, re.DOTALL)
    match = regex_object.search(answers[idx])
    explanation = (
        match.group(1).replace("\n-\n", "").replace("\n", "").replace("\u02dc", " ")
    )
    # print(explanation)

    # populate dict
    answer_dict[answer_nbr] = {"answer": answer, "explanation": explanation}


# questions Networking Fundamentals 23-82
net_fund_questions = pdf_to_text(23, 82)

# fix to capture last question
net_fund_questions = net_fund_questions + "\n1."

# capture and replace all IPv4 addresses
regex = r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})"
pattern_object = re.compile(regex)
net_fund_questions = pattern_object.sub(r"\1,\2,\3,\4", net_fund_questions)

# fix dash newline pattern
regex = r"-\n \n"
pattern_object = re.compile(regex)
net_fund_questions = pattern_object.sub(r"-", net_fund_questions)

regex = r"\n(\d{1,3}\..*?\n)\d{1,3}\."
regex_object = re.compile(regex, re.DOTALL)
while match is not None:
    match = regex_object.search(net_fund_questions)
    if match is not None:
        start, end = match.span()
        questions.append(match.group(1))
        net_fund_questions = net_fund_questions[end - 10 :]


for idx, value in enumerate(questions):

    # print(questions[idx])
    # regex
    # question number
    regex = r"^\d{1,3}\."
    regex_object = re.compile(regex)
    match = regex_object.search(questions[idx])
    question_nbr = match.group().replace(".", "")
    # print(question_nbr)

    # question
    regex = r"^\d{1,3}\.\n \n(.*)\nA\.\n"
    regex_object = re.compile(regex, re.DOTALL)
    match = regex_object.search(questions[idx])
    question = match.group(1).replace("\n-\n", "").replace("\n", "")
    # print(question)

    # choice characters
    regex = r"([A-G])\.\n"
    regex_object = re.compile(regex)
    anwer_chars = regex_object.findall(questions[idx])
    # print(anwer_chars)

    # choices
    # regex = r"[A-G]\.\n \n(.+?)\n"
    # regex = r"[A-G]\.\n \n(.*?)\n"
    # regex_object = re.compile(regex, re.DOTALL)
    # choices = regex_object.findall(questions[idx])
    # print(choices)

    # regex = r"A\."
    # match = regex_object.search(questions[idx])
    # start, end = match.span()
    regex = r"[A-G]\.\n \n"
    # print(questions[idx][start:])
    # choices = re.split(regex, questions[idx][start:])
    choices = re.split(regex, questions[idx])
    choices = choices[1:]
    for idx, value in enumerate(choices):
        choices[idx] = (
            value.replace("\n", "").replace("\u02dc", " ").replace("\u2122", "'")
        )

    # populate dict
    question_dict[question_nbr] = {
        "question": question,
        "choices": dict(zip(anwer_chars, choices)),
    }

for ans_key in list(answer_dict.keys()):
    for ques_key in list(question_dict.keys()):
        if ans_key == ques_key:
            question_dict[ques_key]["answer"] = answer_dict[ans_key]["answer"]
            question_dict[ques_key]["explanation"] = answer_dict[ans_key]["explanation"]

# print(question_dict["293"])
# dumb
questionJ = json.dumps(question_dict, indent=0, sort_keys=False)
# print(questionJ)

with open(
    "".join(
        [
            EXPORT_PATH,
            f"export.json",
        ]
    ),
    "w",
    encoding="UTF-8",
) as json_file:
    questionJ.split("\n")
    json_file.write(questionJ)
