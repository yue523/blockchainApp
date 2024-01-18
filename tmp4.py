import pickle

data = {'key': 'value'}
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)
