import pickle

d = dict(url='index.html', title='首页', content='首页')
print(pickle.dumps(d))
f = open(r'd:\new.txt', 'wb')
pickle.dump(d, f)
f.close()
