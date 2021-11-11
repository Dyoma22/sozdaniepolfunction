
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
	"""Ruudu külg
	Annab vastust ruudu pindala,diogonaal,ümbermööt
	:param int külg: kui pikk külg
	:rtype float:
	"""
	p=4*a
	s=a*a
	d=(a**2)/2
	d=d**0.5
	
	r = (p, s, d)
	return r

def kuupaev(kuu):
	"""Aasta kuu
	programm küsib kuu päeva 1-12, et teada saada, mis kuu
	:param int kuu:Kuu
	:rtype bool:
	"""
	if kuu==12 or 1<=kuu<=2:
		print("Talv")
	elif 3<=kuu<=5:
		print("Kevad")
	elif 6<=kuu<=8:
		print("Suvi")
	elif 9<=kuu<=11:
		print("Sügis")
	else:
		print("Kehtetu kuu!")
	return kuu

def bank(raha,aasta):
	"""Kasutaja teeb n-rublase sissemakse aastateks 10% aastas
	(iga aastaga suureneb tema panuse suurus 10%).
	Igal aastal teatab kasutaja pangale miljoni rubla suuruse summa.
	(See raha lisatakse sissemakse summale ja nende jaoks järgmisel aastal
	on samuti protsent)

	Kirjutage pangafunktsioon, mis võtab argumentidena n, m ja aastad ning tagastab summa,
	mis jääb kasutaja kontole.
	"""
	raha=a
	aasta=b
	def money():
		if aasta>0:
			raha=a*1,1+c
			aasta=aasta-1
			return money()
		else:
			return raha







