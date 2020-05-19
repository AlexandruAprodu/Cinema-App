from Database import db_seeder_drame, db_seeder_animate, adauga_administrator, verifica_filme,\
    afiseaza_film, elimina_film, afiseaza_numar_filme, afiseaza_nume_filme, schimbare_limita_de_varsta,\
    afiseaza_toate_filmele, selecteaza_film, adauga_drama, adauga_animata, afiseaza_administratori
from db_seeder import db_seeder



from Administrator import administrator



def meniu():
    while True:
        db_seeder()
        meniul_meu = int(input("""
    
            1. adauga_drama
            2. adauga_animate
            3. adauga_administrator
            4. verifica_filme 
            5. afiseaza_film 
            6. elimina_film 
            7. afiseaza_animatii
            8. afiseaza_drame
            9. afiseaza_numar_filme
            10.schimba limita de varsta pentru vizionare filme
            11. Quit
    
            """))


        if meniul_meu == 1:
            afiseaza_administratori()
            from Drame import drama
            drama()
            adauga_drama([
                (drama.titlu, drama.durata, drama.sala, drama.varsta_minima, drama.audio_dublat, drama.limba_dublare,
                 drama.categorie, int(input('Scrie in in cifre idul unuia dintre administratori: ')),
                 input("Scrie 'ARHIVA' pentru filmele care au rulat in trecut sau 'RULEAZA ACUM' pentru filmele"
                       " care ruleaza in prezent: "))
            ])
            print('Filmul a fost adaugat cu succes!')

        elif meniul_meu == 2:
            afiseaza_administratori()
            from Animate import animata
            animata()
            adauga_animata([
                ((animata.titlu, animata.durata, animata.sala, animata.varsta_minima, animata.audio_dublat, animata.limba_dublare,
                 animata.categorie, int(input('Scrie in in cifre idul unuia dintre administratori: ')),
                 input("Scrie 'ARHIVA' pentru filmele care au rulat in trecut sau 'RULEAZA ACUM' pentru filmele"
                       " care ruleaza in prezent: ")))
            ])
            print('Filmul a fost adaugat cu succes!')

        elif meniul_meu == 3:
            from Administrator import administrator
            administrator()
            adauga_administrator([
                administrator.nume, administrator.prenume, administrator.email_address
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


meniu()
