from math import *
def arithmetic(a: float,b:float,c:str):
	"""Lihtne kalkulaator
	+ - liitmine
	- - lahutamine
	* - korrutamine
	/ - jagamine
    :param float a: Esimene arv
	:param float b: Teine arv
	:param str c: Aritmeetiline tehing
	:rtype float:
	"""

	if c=="+":
		r=a+b
	elif c=="-":
		r=a-b
	elif c=="*":
		r=a*b
	elif c=="/":
		if b!=0:
			r=a/b
		else:
			print("Div0")
			r=0.0
	else:
		print("Viga")
		r=0.0
	return r 			

def is_year_leap(aasta: int):
	"""Liigaasta leidmine
	Tagastab True kui aasta on liigaasta ja False kui ei ole
	:param int aasta: Aasta number
	:rtype bool: Funktsioni vastus logilises formaadis
	"""
	if aasta%4==0:
		vastus=True
	else:
		vastus=False
	return vastus

def square(a):
	p=4*a
	s=a*a
	d=(a**2)/2
	d=d**0.5
	
	r = (p, s, d)
	return r

def season(num):
	if sea==12 or 1 <= sea <2:
		print("Talv")
	


