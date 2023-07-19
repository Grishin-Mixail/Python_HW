import pickle

my_dict = [{"father": "John","mother": "Mary"},{"father": "Alex","mother": "Suzi"},{"father": "Bob","mother": "Marina"}]

with open('dict.pickle', 'wb') as f:
    pickle.dump(my_dict, f)