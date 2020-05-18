from Database import db_seeder_drame, db_seeder_animate, adauga_administrator, verifica_filme,\
    afiseaza_film, elimina_film, afiseaza_numar_filme, afiseaza_nume_filme, schimbare_limita_de_varsta,\
    afiseaza_toate_filmele, selecteaza_film, adauga_drama, adauga_animata, create_database_cinematograf,\
    create_administratori, create_and_execute_sala, create_filme, afiseaza_administratori



from Administrator import administrator



def meniu():
    while True:
        meniul_meu = int(input("""
        NOTA: CAND RULEZI PENTRU PRIMA OARA APLICATIA:
         - ALEGE 11 PENTRU A CREEA BAZA DE DATE;
         - UNCOMMENT Database.py > database="Cinematograf"
         - ALEGE 12 PENTRU A CREA TABELELE SI PENTRU A LE POPULA
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
            11. Creaza baza de date
            12. Creaza tabelele si adauga la baza de date filmele existente si administratorii existenti;
            13. Quit
    
            """))


        if meniul_meu == 1:
            afiseaza_administratori()
            from Drame import drama
            drama()
            adauga_drama([
                (drama.titlu, drama.durata, drama.sala, drama.varsta_minima, drama.audio_dublat, drama.limba_dublare,
                 drama.categorie, int(input('Scrie in in cifre idul unuia dintre administratori: ')),
                 input("Scrie 'ARHIVA' pentru filmele care au rulat sau 'RULEAZA ACUM' pentru filmele"
                       " care ruleaza in prezent: "))
            ])

        elif meniul_meu == 2:
            afiseaza_administratori()
            from Animate import animata
            animata()
            adauga_animata([
                ((animata.titlu, animata.durata, animata.sala, animata.varsta_minima, animata.audio_dublat, animata.limba_dublare,
                 animata.categorie, int(input('Scrie in in cifre idul unuia dintre administratori: ')),
                 input("Scrie 'ARHIVA' pentru filmele care au rulat sau 'RULEAZA ACUM' pentru filmele"
                       " care ruleaza in prezent: ")))
            ])

        elif meniul_meu == 3:
            pass
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
            create_database_cinematograf()
            print('Porneste aplicatia din nou dupa uncomment!')
            break

        elif meniul_meu == 12:
            create_administratori()
            create_and_execute_sala()
            create_filme()
            adauga_administrator([
                ('Ardin', 'Cioparca', 'ardin_cioparca@cinema.ro'),
                ('Hazara', 'Ramadan', 'hazara_ramadan@cinema.ro')
            ])

            db_seeder_drame([
                ('1917: Speranta si moarte', '120 minute', 3, 12, 'NU', 'NU', 'drama', 1, 'RULEAZA ACUM'),
                ('Bombshell: Scandalul', '110 minute', 2, 12, 'NU', 'NU', 'drama', 1, 'RULEAZA ACUM'),
                ('The Gentlemen', '130 minute', 2, 16, 'NU', 'NU', 'drama', 1, 'RULEAZA ACUM'),
                ('Birds of prey', '120 minute', 2, 12, 'NU', 'NU', 'drama', 1, 'ARHIVA'),
                ('Little women ', '130 minute', 1, 16, 'NU', 'NU', 'drama', 1, 'ARHIVA'),
                ('Emma', '90 minute', 2, 12, 'NU', 'NU', 'drama', 1, 'ARHIVA'),
                ('Bad Boys for Life', '120 minute', 1, 16, 'NU', 'NU', 'drama', 1, 'RULEAZA ACUM')
            ])

            db_seeder_animate([
                ('REGATUL DE GHEAȚĂ II', '120 minute', 3, 0, 'DA', 'ROMANA', 'ANIMATE', 2, 'RULEAZA ACUM'),
                ('SPIONI DEGHIZATI', '130 minute', 3, 0, 'DA', 'ROMANA', 'ANIMATE', 2, 'RULEAZA ACUM'),
                ('CATEII ARCTICI:CURSA PE ZAPADA ', '110 minute', 3, 0, 'DA', 'ROMANA', 'ANIMATE', 2, 'ARHIVA'),
                (
                    'PRINTESA "CONDURI ROSII" SI CEI 7 PITICI', '110 minute', 3, 0, 'DA', 'ROMANA', 'ANIMATE', 2,
                    'ARHIVA'),
                ('DOCTOR DOLITTLE', '130 minute', 3, 0, 'DA', 'ROMANA', 'ANIMATE', 2, 'RULEAZA ACUM')
            ])

        elif meniul_meu == 13:
            print("Va multumim ca ne-ati vizitat!")
            break


meniu()
