


class Film:

    def __init__(self, titlu, durata, sala):
        self.titlu = titlu
        self.durata = durata
        self.sala = sala

    def drama(self, varsta_minima):
        self.varsta_minima = varsta_minima

    def animatii(self, audio_dublat, limba_dublare):
        self.audio_dublat = audio_dublat
        self.limba_dublare = limba_dublare

    def categorii(self, categorie):
        self.categorie = categorie


drama1 = Film('1917: Speranta si moarte', '120 minute', 3)
drama1.drama(12)
drama1.animatii('DA', 'ROMANA')
drama1.categorii('drama')

drama2 = Film('Bombshell: Scandalul', '110 minute', 3)
drama2.drama(16)
drama2.animatii('NU', 'NU')
drama2.categorii('drama')

drama3 = Film('The Gentlemen', '130 minute', 2)
drama3.drama(18)
drama3.animatii('NU', 'NU')
drama3.categorii('drama')

drama4 = Film('Birds of prey', '120 minute', 1)
drama4.drama(12)
drama4.animatii('NU', 'NU')
drama4.categorii('drama')

drama5 = Film('Little women ', '130 minute', 2)
drama5.drama(18)
drama5.animatii('NU', 'NU')
drama5.categorii('drama')

drama6 = Film('Emma', '90 minute', 3)
drama6.drama(12)
drama6.animatii('NU', 'NU')
drama6.categorii('drama')

drama7 = Film('Bad Boys for Life', '120 minute', 1)
drama7.drama(16)
drama7.animatii('NU', 'NU')
drama7.categorii('drama')


animate1 = Film('REGATUL DE GHEAȚĂ II', '120 minute', 1)
animate1.drama(0)
animate1.animatii('DA', 'ROMANA')
animate1.categorii('animate')

animate2 = Film('SPIONI DEGHIZATI', '130 minute', 2)
animate2.drama(0)
animate2.animatii('DA', 'ROMANA')
animate2.categorii('animate')

animate3 = Film('CATEII ARCTICI:CURSA PE ZAPADA ', '110 minute', 3)
animate3.drama(0)
animate3.animatii('DA', 'ROMANA')
animate3.categorii('animate')

animate4 = Film('PRINTESA "CONDURI ROSII" SI CEI 7 PITICI', '110 minute', 1)
animate4.drama(0)
animate4.animatii('DA', 'ROMANA')
animate4.categorii('animate')

animate5 = Film('DOCTOR DOLITTLE', '130 minute', 2)
animate5.drama(0)
animate5.animatii('DA', 'ROMANA')
animate5.categorii('animate')

