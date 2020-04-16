import pickle

f = open(r'd:\new.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)
