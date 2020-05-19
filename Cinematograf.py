from Functii_aplicatie import *


class Cinematograf:
    __instance = None

    def __new__(cls, nume_cinematograf, adresa_cinematograf, capacitate_totala_cinematograf):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        cls.__instance.nume_cinematograf = nume_cinematograf
        cls.__instance.adresa_cinematograf = adresa_cinematograf
        cls.__instance.capacitate_totala_cinematograf = capacitate_totala_cinematograf
        return cls.__instance

    def __call__(cls, *args, **kwargs):
        print(f'Numele cinematografului este {cls.__instance.nume_cinematograf} si are capacitatea de'
              f' {cls.__instance.capacitate_totala_cinematograf}')

    adresa_cinematograf = 'Strada Ion Ghica 3, București '
    capacitate_totala_cinematograf = 450
    sala_new_york = 100
    sala_munchen = 80
    sala_londra = 150
    filme_rulare_prezent = verifica_filme()
    filme_arhiva = arhiva_filme()


cinema_phoenix = Cinematograf('Phoenix', Cinematograf.adresa_cinematograf, Cinematograf.capacitate_totala_cinematograf)
print(Cinematograf.filme_rulare_prezent)
print(Cinematograf.filme_arhiva)
