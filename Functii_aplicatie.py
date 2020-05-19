import mysql.connector

DB = mysql.connector.connect(
    host="127.0.0.2",
    user="root",
    passwd="1234",
    # database="Cinematograf"
)
CURSOR = DB.cursor()


def adauga_drama(drama):
    CURSOR.executemany("""INSERT INTO Cinematograf.Filme(titlu_film, durata_film, sala, varsta_minima, audio_dublat,
     limba_dublare, categorie, adaugat_de, informatii_rulare) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)""", drama)
    return DB.commit()


def adauga_animata(animata):
    CURSOR.executemany("""INSERT INTO Cinematograf.Filme(titlu_film, durata_film, sala, varsta_minima, audio_dublat,
     limba_dublare, VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)""", animata)
    return DB.commit()


def db_seeder_drame(drame):

    CURSOR.executemany("""INSERT INTO Cinematograf.Filme(titlu_film, durata_film, sala, varsta_minima, audio_dublat,
     limba_dublare, categorie, adaugat_de, informatii_rulare) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)""", drame)
    return DB.commit()


def db_seeder_animate(animate):
    CURSOR.executemany("""INSERT INTO Cinematograf.Filme(titlu_film, durata_film, sala, varsta_minima, audio_dublat,
     limba_dublare,  categorie, adaugat_de, informatii_rulare) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)""", animate)
    return DB.commit()


def adauga_administrator(administrator):
    CURSOR.executemany("""INSERT INTO Cinematograf.administratori(nume, prenume, email_address)
                          VALUES(%s, %s, %s)""", administrator)
    return DB.commit()


def verifica_filme():
    CURSOR.execute("""SELECT * FROM Cinematograf.filme WHERE informatii_rulare = 'RULEAZA ACUM'""")
    fetch = CURSOR.fetchall()
    return fetch


def arhiva_filme():
    CURSOR.execute("""SELECT * FROM Cinematograf.filme WHERE informatii_rulare = 'ARHIVA'""")
    fetch = CURSOR.fetchall()
    return fetch


def afiseaza_film(nume):
    CURSOR.execute(f"SELECT * FROM Cinematograf.filme WHERE titlu_film = '{nume}'")
    fetch = CURSOR.fetchone()
    print(fetch)


def elimina_film(id_film):
    CURSOR.execute(f"DELETE FROM Cinematograf.filme WHERE id_film = {id_film}")
    print('Filmul a fost sters din baza de date')
    return DB.commit()


def afiseaza_numar_filme():
    CURSOR.execute("SELECT * FROM Cinematograf.filme")
    fetch = CURSOR.fetchall()
    return fetch


def afiseaza_nume_filme():
    CURSOR.execute("SELECT titlu_film FROM Cinematograf.filme")
    fetch = CURSOR.fetchall()
    for filme in fetch:
        print(filme)


def schimbare_limita_de_varsta(noua_varsta, id_film):
    CURSOR.execute('SELECT * FROM Cinematograf.filme')
    fetch = CURSOR.fetchall()
    for filme in fetch:
        print(filme)

    CURSOR.execute(f"UPDATE Cinematograf.filme SET varsta_minima = {noua_varsta} WHERE id_film = {id_film}")
    print('Limita de varsta a fost modificata!')
    return DB.commit()


def afiseaza_toate_filmele():
    CURSOR.execute('SELECT * FROM Cinematograf.filme')
    fetch = CURSOR.fetchall()
    for filme in fetch:
        print(filme)


def selecteaza_film(id_film):
    CURSOR.execute(f'SELECT * FROM Cinematograf.filme WHERE id_film = {id_film}')
    fetch = CURSOR.fetchone()
    DB.commit()
    print(fetch)


def afiseaza_administratori():
    CURSOR.execute('SELECT * FROM Cinematograf.administratori')
    fetch = CURSOR.fetchall()
    for admin in fetch:
        print(admin)
