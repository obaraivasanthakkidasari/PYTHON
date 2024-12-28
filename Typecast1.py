# Type Casting Techniques in Python
#Type casting types
#Example1: Float type() into int()
a=12.34
print(a,type(a))
b=int(a)
print(b,type(b))
a=0.45
print(a,type(a))
b=int(a)
print(b,type(b))

#Example 2: Bool type() into int()
a=True
print(a,type(a))
b=int(a)
print(b,type(b))
a=False
print(a,type(a))
b=int(a)
print(b,type(b))

#Example3: complex type into int type----NOT POSSIBLE
#a=2+3.5j
#print(a,type(a))
#b=int(a)

#Example 4: str() type() into int()

#Case:1 Str into Int() Possible
a="123"
print(a,type(a))
b=int(a)
print(b,type(b))

#Case-2: str float into  int---NOT POSSIBLE
a="12.34"
print(a,type(a))
b=int(a)

#Case-3: str bool  into int-----NOT POSSIBLE
a="True"
print(a,type(a))
b=int(a)

#Case-4: str complex into int--Not POSSIBLE
a=2+3j
print(a,type(a))
b=int(a)

#Case-5: pure str into int--NOT POSSIBLE
a="PYTHON"
print(a,type(a))
b=int(a)