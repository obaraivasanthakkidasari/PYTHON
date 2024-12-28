#Example1: int type into float type--POSSIBLE
a=123
print(a,type(a))
b=float(a)
print(b,type(b))

#Example2: bool type into float type--POSSIBLE
a=True
print(a,type(a))
b=float(a)
print(b,type(b))
a=False
print(a,type(a))
b=float(a)
print(b,type(b))

#Example3: complex type into float type--NOT POSSIBLE
#a=2+3j
#print(a,type(a))
#b=float(a)
#print(b,type(b))

#Example: str type into float  type
#Case-1:  str int into  float--POSSIBLE
a="1234"
print(a,type(a))
b=float(a)
print(b,type(b))
#Case-2: str float into  float---POSSIBLE
a="12.34"
print(a,type(a))
b=float(a)
print(b,type(b))

#a="198.0.0.1"
#print(a,type(a))
#b=float(a)
#Case-3: str bool  into float----NOT POSSIBLE
a="True"
print(a,type(a))
b=float(a)
print(b,type(b))
#Case-4: str complex into float--NOT POSSIBLE
a="2+3.6j"
print(a,type(a))
b=float(a)
print(b,type(b))
#Case-5: pure str into float--NOT POSSIBLE
a="PYTHON.Java"
print(a,type(a))
b=float(a)