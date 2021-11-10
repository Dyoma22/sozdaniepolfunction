from random import *
from keyboard import *
from module1 import *
from math import *

while True:
	print("Funktsioonid".center(50,"+"))
	print("arithmetic - A,\nis_year_leap - Y,\nsquare - S")
	v=input()
	if v.upper()=="A":
		arv1=float(input("Arv 1:"))
		arv2=float(input("Arv 2:"))
		sym=input("Tehe:")
		rezult=arithmetic(arv1,arv2,sym)
		print(rezult)
	elif v.upper()=="Y":
		rezult=is_year_leap(int(input("Sisesta aasta - ")))
		print(rezult)
	elif v.upper()=="S":
		rezult=square(int(input("Sisestage piirkond - ")))
		print(rezult)
