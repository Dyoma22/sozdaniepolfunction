
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
		r="Tundmatu sym"
	return r#1	
def is_year_leap(aasta:int):
	"""Liigaasta leidmine
	Tagastab True kui aasta on liigaasta ja False kui ei ole
	:param int aasta: Aasta number
	:rtype bool: Funktsioni vastus logilises formaadis
	"""
	if aasta%4==0:
		vastus=True
	else:
		vastus=False
	return vastus#2
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
	return r#3
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
	return kuu#4
def bank(a, years):
	"""Kasutaja teeb n-rublase sissemakse aastateks 10% aastas
	(iga aastaga suureneb tema panuse suurus 10%).
	Igal aastal teatab kasutaja pangale miljoni rubla suuruse summa.
	(See raha lisatakse sissemakse summale ja nende jaoks järgmisel aastal
	on samuti protsent)
	Kirjutage pangafunktsioon, mis võtab argumentidena n, m ja aastad ning tagastab summa,
	mis jääb kasutaja kontole.
	"""
	for _ in range(years):
		a=((1.1*1/100)*a)*100
		print("Ваш баланс:",a)
		return("")#5
def is_prime(b):
	"""Kirjutage funktsioon is_prime, mis võtab 1 argumendi, arvu vahemikus 0 kuni
    1000 ja tagastab tõene, kui see on algarvuga, ja False muul juhul.
	"""
	k=2
	while k*k<=b:
		if b%k==0:
			return False
		k+=1
	return True#6
def xor_cipher(string:str, key:str)->str:
    """Tavaline sõna kodeeristakse.
    """
    result=""
    temp=int()
    for i in range(len(string)):
        temp=ord(string[i])
        for j in range(len(key)):
            temp^=ord(key[j])
        result+=chr(temp)
    return result#7
def xor_uncipher(string:str, key: str)->str:
    """Koderiumine text dekodeeritakse.
    """
    result = ""
    temp = []
    for i in range(len(string)):
        temp.append(string[i])
        for j in reversed(range(len(key))):
            temp[i] = chr(ord(key[j]) ^ ord(temp[i]))
        result += temp[i]
    return result#7.1
def date(day:int, month:int,year:int):
	#Kirjutage funktsiooni kuupäev, millel on 3 argumenti – päev, kuu ja aasta. Tagasta True, kui selline kuupäev on meie kalendris olemas, ja False muul juhul.	
    set_months = {1: 31,2: 28, 3: 31,4: 30,5: 31,6: 30,7: 31,8: 31,9: 30,10: 31,11: 30,12: 31}
    if year>0 and (month>=1 and month<=12):
        if day in range(1, set_months[month]+1):
           return True
        else:
            return False
    else:
        return False#8
