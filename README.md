# QA-generation
This project leverages natural language processing to automatically generate meaningful questions and answers from given textual input. It aims to provide a tool for extracting key information and creating insightful queries, enhancing the understanding and interaction with textual content.

# Features
Single Sentence Mode: When provided with a single sentence, the system generates one relevant question and answer pair, utilizing question words such as 'What,' 'When,' 'Where,' 'Who,' and 'How.'

Paragraph Mode: For longer texts or paragraphs, the project generates multiple questions and answers, employing different or identical question words. This allows for a comprehensive exploration of the content.

Avoid Duplicate Questions: Optionally, the system can be configured to avoid creating duplicate questions using different patterns. This enhances the variety of questions generated.

# Usage
To use the project, simply run the main.py script with the path to your input text file or document. You can customize the behavior by adjusting the parameters and options in the code.

python main.py path/to/your/file.txt

# Requirements
* Python 3
* spaCy library (pip install spacy)
* spaCy English language model (python -m spacy download en_core_web_sm)
