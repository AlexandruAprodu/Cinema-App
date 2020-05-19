from Functii_aplicatie import adauga_administrator, verifica_filme, \
    afiseaza_film, elimina_film, afiseaza_numar_filme, afiseaza_nume_filme, schimbare_limita_de_varsta, \
    afiseaza_toate_filmele, selecteaza_film, adauga_drama, adauga_animata, afiseaza_administratori
from Drame import *
from Animate import *
from Administrator import *


def meniu():
    while True:
        meniul_meu = int(input("""
    
            1. Adauga_drama
            2. Adauga_animate
            3. Adauga_administrator
            4. Verifica_filme 
            5. Afiseaza_film 
            6. Elimina_film 
            7. Afiseaza_animatii
            8. Afiseaza_drame
            9. Afiseaza_numar_filme
            10. Schimba limita de varsta pentru vizionare filme
            11. Quit
    
            """))

        if meniul_meu == 1:

            drama = Drame(input('Adauga titlul dramei: '),
                          input('Adauga durata filmului: '),
                          int(input('Adauga sala in cifre: ')),
                          int(input('Adauga varsta minima pentru vizionare in cifre: ')),
                          input("Adauga 'NU' daca filmul nu este dublat si 'DA' daca este dublat"),
                          input("Adauga 'NU' daca filmul are limba dublare sau limba in care este dublat: "),
                          input('Adauga categoria ["animatie" / "drama"]din care face parte acest film: '))

            afiseaza_administratori()

            adauga_drama([
                (drama.titlu, drama.durata, drama.sala, drama.varsta_minima, drama.audio_dublat, drama.limba_dublare,
                 drama.categorie, int(input('Scrie in in cifre idul unuia dintre administratori: ')),
                 input("Scrie 'ARHIVA' pentru filmele care au rulat in trecut sau 'RULEAZA ACUM' pentru filmele"
                       " care ruleaza in prezent: "))
            ])
            print('Filmul a fost adaugat cu succes!')

        elif meniul_meu == 2:
            afiseaza_administratori()
            animata = Animate(input('Adauga titlul animatiei: '),
                              input('Adauga durata filmului: '),
                              int(input('Adauga sala in cifre: ')),
                              int(input('Adauga varsta minima pentru vizionare in cifre: ')),
                              input("Adauga 'NU' daca filmul nu este dublat si 'DA' daca este dublat"),
                              input("Adauga 'NU' daca filmul are limba dublare sau limba in care este dublat: "),
                              input('Adauga categoria ["animatie" / "drama"]din care face parte acest film: '))
            adauga_animata([
                ((animata.titlu, animata.durata, animata.sala, animata.varsta_minima, animata.audio_dublat,
                  animata.limba_dublare,
                  animata.categorie, int(input('Scrie in in cifre idul unuia dintre administratori: ')),
                  input("Scrie 'ARHIVA' pentru filmele care au rulat in trecut sau 'RULEAZA ACUM' pentru filmele"
                        " care ruleaza in prezent: ")))
            ])
            print('Filmul a fost adaugat cu succes!')

        elif meniul_meu == 3:

            administrator = Administrator(
                input('Scrie numele administratorului: '),
                input('Scrie prenumele administratorului: '),
                input('Scrie adresa de email: ')
            )
            adauga_administrator([
                (administrator.nume, administrator.prenume, administrator.email_address)
            ])
            print('Administratorul a fost adaugat cu succes!')
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
            y = lambda x: True if x in film else False
            for film in afiseaza_numar_filme():
                if y('animatie'):
                    print(film)

        elif meniul_meu == 8:
            y = lambda x: True if x in film else False
            for film in afiseaza_numar_filme():
                if y('drama'):
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


meniu()
