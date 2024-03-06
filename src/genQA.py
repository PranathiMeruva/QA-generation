import spacy
import sys

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")

def parse_and_generate_questions_answers(text_input):
    doc = nlp(text_input)
    for sentence in doc.sents:
        gen_complex_question_and_answer(sentence)

def gen_complex_question_and_answer(sentence):
    subject = ""
    verb = ""
    obj = ""
    for token in sentence:
        if "subj" in token.dep_:
            subject = token.text
        elif "obj" in token.dep_:
            obj = token.text
        elif "ROOT" in token.dep_:
            verb = token.text

    if verb and (subject or obj):
        question_how = f"How does {subject} {verb} {obj}?"
        question_who = f"Who {verb} {obj}?"
        question_when = f"When does {subject} {verb} {obj}?"
        question_where = f"Where does {subject} {verb} {obj}?"

        answer = f"{subject} {verb} {obj}."

        print('\n', 'Original Sentence:', sentence)
        print('Question (How):', question_how)
        print('Question (Who):', question_who)
        print('Question (When):', question_when)
        print('Question (Where):', question_where)
        print('Answer:', answer)

def main():
    if len(sys.argv) == 2:
        text_input = sys.argv[1]
        parse_and_generate_questions_answers(text_input)
    elif len(sys.argv) == 3 and sys.argv[2] == '-w':
        try:
            from docx import Document
        except ImportError:
            print("To read from Word documents, install the python-docx library: pip install python-docx")
            sys.exit(1)

        document_path = sys.argv[1]
        try:
            doc = Document(document_path)
            text_input = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
            parse_and_generate_questions_answers(text_input)
        except Exception as e:
            print(f"Error reading Word document: {str(e)}")
    else:
        print("Usage: python script.py <text_input_or_doc_path> [-w]")

if __name__ == "__main__":
    main()
