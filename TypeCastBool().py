#3.Bool()
#Example1: int type into bool type---POSSIBLE
a=123
print(a,type(a))
b=bool(a)
print(b,type(b))
a=0
print(a,type(a))
b=bool(a)
print(b,type(b))
a=-124
print(a,type(a))
b=bool(a)
print(b,type(b))
#Example2:float type into bool type--POSSIBLE
a=23.45
print(a,type(a))
b=bool(a)
print(b,type(b))
a=0.0
print(a,type(a))
b=bool(a)
print(b,type(b))
a=0.000000000000001
print(a,type(a))
b=bool(a)
print(b,type(b))
#Example3: complex type into bool type--POSSIBLE
a=2+3j
print(a,type(a))
b=bool(a)
print(b,type(b))
a=0+0j
print(a,type(a))
b=bool(a)
print(b,type(b))
#Example: str type into float  type
#Case-1:  str int into  bool--POSSIBLE
a="123"
print(a,type(a))
b=bool(a)
print(b,type(b))
a="0"
print(a,type(a))
b=bool(a)
print(b,type(b))
a="10-10"
print(a,type(a))
b=bool(a)
print(b,type(b))
len(a)
#Case-2: str float into  bool--Possible.
a="12.34"
print(a,type(a))
b=bool(a)
print(b,type(b))
a="0.0"
print(a,type(a))
b=bool(a)
print(b,type(b))
#Case-3: str bool  into bool--POSSIBLE
a="True"
print(a,type(a))
b=bool(a)
print(b,type(b))
a="FALSE"
print(a,type(a))
b=bool(a)
print(b,type(b))
#Case-4: str complex into bool--POSSIBLE
a="2+3j"
print(a,type(a))
b=bool(a)
print(b,type(b))
a="0+0j"
print(a,type(a))
b=bool(a)
print(b,type(b))
#Case-5: pure str into bool--POSSIBLE
a="PYTHON"
print(a,type(a))
b=bool(a)
print(b,type(b))
a="JAVA"
print(a,type(a))
b=bool(a)
print(b,type(b))
a="    "
print(a,type(a))
b=bool(a)
print(b,type(b))

a=""
print(a,type(a))
b=bool(a)
print(b,type(b))

