import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_phonetic_alphabet_df = pandas.read_csv('nato_phonetic_alphabet.csv')
# print(nato_phonetic_alphabet_df)
# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_dict = {letter: word for (letter, word) in nato_phonetic_alphabet_df.to_numpy()}
print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word \n").upper()
if len(word) > 0 and any([x for x in word if x not in nato_dict]):
    print(f"A letter in {word} is not in the Nato Phonetic Alphabet. Quitting")
else:
    print([nato_dict[x] for x in word])
