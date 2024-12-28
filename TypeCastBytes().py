#TypeCasting bytes()
'''
lst=[100,23,256,7,0,12]
print(lst,type(lst))
b=bytes(lst)

lst=[100,-23,255,7,0,12]
print(lst,type(lst))
b=bytes(lst)
print(b,type(b))
'''
lst=[100,23,255,7,0,12]
print(lst,type(lst))
b=bytes(lst)
print(b,type(b))
for val in b:
    print(val)
for val in b[2:5]:
    print(val)
for val in b[::-1]:
    print(val)
