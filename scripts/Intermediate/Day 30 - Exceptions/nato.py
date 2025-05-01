import pandas

alpha_map_df = pandas.read_csv("scripts\\Intermediate\\Day 26 - NATO\\nato_phonetic_alphabet.csv")
alpha_map_dict = alpha_map_df.to_dict()

alpha_map = {row.letter:row.code for (index, row) in alpha_map_df.iterrows()}

def convert_to_nato():  
    word = input("Please enter a word:")
    try:
        word_nato = [alpha_map[letter.upper()] for letter in word]
    except KeyError as key:
        print(f"Invalid character {key}. Please use english letters only.")
        convert_to_nato()
    else:
        print(word_nato)

convert_to_nato()