#Type Casting Complex()
#Example1: int type into complex--POSSIBLE
a=10
print(a,type(a))
b=complex(a)
print(b,type(b))

#Example2: float type into complex type--POSSIBLE
a=1.3
print(a,type(a))
b=complex(a)
print(b,type(b))

#Example3: bool type  into complex type --POSSIBLE
a=True
print(a,type(a))
b=complex(a)
print(b,type(b))

#Example: str type into complex type
#Case-1: Stt int into complex -Possible
a="12"
print(a,type(a))
b=complex(a)
print(b,type(b))
#Case-2: str float into  complex---POSSIBLE
a="4.5"
print(a,type(a))
b=complex(a)
print(b,type(b))
#Case-3: str bool  into compelx--NOT POSSIBLE
#a="True"
#print(a,type(a))
#b=complex(a)
#print(b,type(b))
#Case-4: str complex into complex---POSSIBLE
a="2+3j"
print(a,type(a))
b=complex(a)
print(b,type(b))
#Case-5: pure str into complex---NOT POSSIBLE
a="PYTHON"
print(a,type(a))
b=complex(a)
print(b,type(b))