import pandas

alpha_map_df = pandas.read_csv("scripts\\Day 26 - NATO\\nato_phonetic_alphabet.csv")
alpha_map_dict = alpha_map_df.to_dict()

alpha_map = {row.letter:row.code for (index, row) in alpha_map_df.iterrows()}
print(alpha_map)

word = input("Please enter a word:")
word_nato = [alpha_map[letter.upper()] for letter in word]
print(word_nato)