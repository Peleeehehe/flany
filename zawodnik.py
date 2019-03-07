import random

class Zawodnik:
	def __init__(self, celnosc_rzutu, sila_rzutu, szybkosc_picia, szybkosc_biegu, nick, druzyna, zawartosc_butelki):
			self.celnosc = int(celnosc_rzutu)
			self.sila = int(sila_rzutu)
			self.szybkosc_picia = int(szybkosc_picia)
			self.szybkosc_biegu = int(szybkosc_biegu)
			self.druzyna = str(druzyna)
			self.zawartosc_butelki = int(zawartosc_butelki)
			self.imie = str(nick)

	def trening(attr):
			self.attr += 1
	
	def picie(self,ile_wypil):
			self.zawartosc_butelki -= ile_wypil*self.szybkosc_picia
			print(self.imie, " WYPIL ", ile_wypil*self.szybkosc_picia)
	
	def rzut(self):
		if ( self.celnosc >= random.randint(1,10)):
			print(self.imie," TRAFIL W BUTELKE")
			return True
		else:
			print(self.imie,"NIE TRAFIL")
			return False

	def skonczyl_grac(self):
		if self.zawartosc_butelki <= 0:
			print(self.imie," JUZ WYZEROWAL")
			return True
		else:
			print("ZOSTALO MU",self.zawartosc_butelki)
			return False


	
