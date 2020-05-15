from Database import adauga_drama, adauga_animate, adauga_administrator, verifica_filme,\
    afiseaza_film, elimina_film, afiseaza_numar_filme, afiseaza_nume_filme, schimbare_limita_de_varsta,\
    afiseaza_toate_filmele, selecteaza_film
from Film import drama1, drama2, drama3, drama4, drama5, drama6, drama7, animate1, animate2, animate3, animate4,\
    animate5

from Administrator import administrator1, administrator2


def meniu():

    meniul_meu = int(input("""
        1. adauga_drama
        2. adauga_animate
        3. adauga_administrator
        4. verifica_filme - va returna informatii despre filmele ce se afla in prezent in derulare
        5. afiseaza_film - va afisa informatii legate de un film specificat printr-un argument unic
        6. elimina_film - sterge un film din programul curent de rulare
        7. afiseaza_animatii
        8. afiseaza_drame
        9. afiseaza_numar_filme
        10.schimba limita de varsta pentru vizionare filme
        11. Quit

        """))

    while True:
        if meniul_meu == 1:
            adauga_drama([
                (drama1.titlu, drama1.durata, drama1.sala, drama1.varsta_minima, drama1.audio_dublat,
                 drama1.limba_dublare, drama1.categorie, 1, 'RULEAZA ACUM'),
                (drama2.titlu, drama2.durata, drama2.sala, drama2.varsta_minima, drama2.audio_dublat,
                 drama2.limba_dublare, drama2.categorie, 1, 'RULEAZA ACUM'),
                (drama3.titlu, drama3.durata, drama3.sala, drama3.varsta_minima, drama3.audio_dublat,
                 drama3.limba_dublare, drama3.categorie, 1, 'RULEAZA ACUM'),
                (drama4.titlu, drama4.durata, drama4.sala, drama4.varsta_minima, drama4.audio_dublat,
                 drama4.limba_dublare, drama4.categorie, 1, 'ARHIVA'),
                (drama5.titlu, drama5.durata, drama5.sala, drama5.varsta_minima, drama5.audio_dublat,
                 drama5.limba_dublare, drama5.categorie, 1, 'ARHIVA'),
                (drama6.titlu, drama6.durata, drama6.sala, drama6.varsta_minima, drama6.audio_dublat,
                 drama6.limba_dublare, drama6.categorie,  1, 'ARHIVA'),
                (drama7.titlu, drama7.durata, drama7.sala, drama7.varsta_minima, drama7.audio_dublat,
                 drama7.limba_dublare, drama7.categorie,  1, 'RULEAZA ACUM')
                    ])

        elif meniul_meu == 2:
            adauga_animate([
                (animate1.titlu, animate1.durata, animate1.sala, animate1.varsta_minima, animate1.audio_dublat,
                 animate1.limba_dublare, animate1.categorie, 2, 'RULEAZA ACUM'),
                (animate2.titlu, animate2.durata, animate2.sala, animate2.varsta_minima, animate2.audio_dublat,
                 animate2.limba_dublare, animate2.categorie, 2, 'RULEAZA ACUM'),
                (animate3.titlu, animate3.durata, animate3.sala, animate3.varsta_minima, animate3.audio_dublat,
                 animate3.limba_dublare, animate3.categorie, 2, 'ARHIVA'),
                (animate4.titlu, animate4.durata, animate4.sala, animate4.varsta_minima, animate4.audio_dublat,
                 animate4.limba_dublare, animate4.categorie, 2, 'ARHIVA'),
                (animate5.titlu, animate5.durata, animate5.sala, animate5.varsta_minima, animate5.audio_dublat,
                 animate5.limba_dublare, animate5.categorie, 2, 'RULEAZA ACUM')
                    ])

        elif meniul_meu == 3:
            adauga_administrator([
                ('Ardin', 'Cioparca', 'ardin_cioparca@cinema.ro'),
                ('Hazara', 'Ramadan', 'hazara_ramadan@cinema.ro')
            ])
        elif meniul_meu == 4:

            for film in verifica_filme():
                print(film)

        elif meniul_meu == 5:
            afiseaza_nume_filme()
            afiseaza_film(input('Scrie numele filmului: '))

        elif meniul_meu == 6:
            for film in verifica_filme():
                print(film)
            elimina_film(int(input('Scrie numele filmului pe care doresti sa il stergi: ')))

        elif meniul_meu == 7:
            x = lambda x: True if x in film else False
            for film in afiseaza_numar_filme():
                if x('animate'):
                    print(film)

        elif meniul_meu == 8:
            x = lambda x: True if x in film else False
            for film in afiseaza_numar_filme():
                if x('drama'):
                    print(film)

        elif meniul_meu == 9:
            print(f'{len(afiseaza_numar_filme())} filme avem in acest moment in baza de date !')

        elif meniul_meu == 10:
            afiseaza_toate_filmele()
            id_film = int(input('Scrie idul filmului pe care doresti sa il modifici: '))
            selecteaza_film(id_film)
            schimbare_limita_de_varsta(int(input('Scrie noua limita de varsta in cifre: ')), id_film)

        elif meniul_meu == 11:
            print("Va multumim ca ne-ati vizitat!")
            break
        return

meniu()