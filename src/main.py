# src/main.py
from genQA import parse_and_generate_questions_answers

def run_question_generation(file_path):
    try:
        with open(file_path, 'r') as file:
            text_input = file.read()
            parse_and_generate_questions_answers(text_input)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        run_question_generation(file_path)
    else:
        print("Usage: python main.py <text_input_file>")
