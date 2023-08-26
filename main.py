# Import required libraries
import nltk
import language_tool_python as lt

# Initialize the language tool
tool = lt.LanguageTool('en-US')

# Download resources for NLTK
nltk.download('punkt')

# Function to tokenize text into sentences
def tokenize_text(text):
    return nltk.sent_tokenize(text)

# Function to check spelling and grammar
def check_spelling_grammar(sentences):
    corrected_text = ""
    for sentence in sentences:
        matches = tool.check(sentence)
        try:
            corrected_sentence = tool.correct(sentence)
        except Exception as e:
            print(f"An error occurred: {e}")
            corrected_sentence = sentence
        corrected_text += corrected_sentence + " "
    return corrected_text.strip()

# Main function
def main():
    # Take user input
    user_text = input("Please enter the text you want to correct: ")
    
    # Tokenize the text into sentences
    sentences = tokenize_text(user_text)
    
    # Check and correct spelling and grammar
    corrected_text = check_spelling_grammar(sentences)
    
    print(f"Original Text: {user_text}")
    print(f"Corrected Text: {corrected_text}")

# Entry point of the program
if __name__ == "__main__":
    main()
