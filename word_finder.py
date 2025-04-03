import pandas as pd
from fuzzywuzzy import process

# Load word list
word_df = pd.read_csv('spelling_words.csv', header=None)
word_list = word_df[0].tolist()

def search_word(user_input, word_list, top_n=5):
    matches = process.extract(user_input, word_list, limit=top_n)
    return matches

# Example usage
if __name__ == "__main__":
    print("Welcome to Spelling Bee Word Finder!")
    while True:
        query = input("\nEnter a word (or part of it) to search (or type 'exit' to quit): ").strip()
        if query.lower() == "exit":
            print("Goodbye! Keep practicing 😊")
            break
        results = search_word(query, word_list)
        print(f"Top Matches:")
        for match, score in results:
            print(f"{match} (Confidence: {score}%)")

