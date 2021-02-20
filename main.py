import pandas

alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}

my_name = input("print your name:").upper()
phonetic_word = [nato_dict[char] for char in my_name]

print(phonetic_word)