d = {
    'Namem':'Yash',
    'age': 33
}
print(d)

d['height']= '5 feet'
print(d)

for key,value in d.items():
    print(key,value)

llist=['key']
vi= ['value']

dicc = dict(zip(llist,vi))
print(dicc)