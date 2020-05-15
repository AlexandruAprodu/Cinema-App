import mysql.connector

DB = mysql.connector.connect(
    host="127.0.0.2",
    user="root",
    passwd="1234",
    database="Cinematograf"
)
CURSOR = DB.cursor()


# CURSOR.execute("CREATE DATABASE Cinematograf")
# CURSOR.execute("""
#     CREATE TABLE Filme(
#         id_film tinyint NOT NULL AUTO_INCREMENT,
#         titlu_film varchar(50) NOT NULL,
#         durata_film varchar(50) DEFAULT '0 minute',
#         sala tinyint DEFAULT NULL,
#         varsta_minima int(11) NOT NULL,
#         audio_dublat varchar(50) DEFAULT 'nu',
#         limba_dublare varchar(50) DEFAULT 'nu',
#         categorie varchar(50) DEFAULT NULL,
#         adaugat_de tinyint NOT NULL,
#         informatii_rulare varchar(50),
#         PRIMARY KEY (id_film),
#         FOREIGN KEY(sala) REFERENCES `sala`(id_sala),
#         FOREIGN KEY (adaugat_de) REFERENCES `Administratori`(id_administrator))
#
# """)

# CURSOR.execute("""CREATE Table Sala(
#     id_sala tinyint NOT NULL AUTO_INCREMENT,
#     nume_sala varchar(50) DEFAULT NULL,
#     PRIMARY KEY (id_sala)
# )""")
# sali_cinema = [
#     ('sala_new_york',),
#     ('sala_munchen',),
#     ('sala_londra',)
# ]
# CURSOR.executemany("INSERT INTO sala(nume_sala) VALUES (%s)", sali_cinema)

# CURSOR.execute("""CREATE TABLE Administratori(
#     id_administrator tinyint NOT NULL AUTO_INCREMENT,
#     nume varchar(50) NOT NULL,
#     prenume varchar(50) NOT NULL,
#     email_address varchar(50) NOT NULL,
#     PRIMARY KEY (id_administrator)
#     )""")


def adauga_drama(drame):

    CURSOR.executemany("""INSERT INTO Filme(titlu_film, durata_film, sala, varsta_minima, audio_dublat, limba_dublare, 
                                            categorie, adaugat_de, informatii_rulare) 
                                            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)""", drame)
    return DB.commit()


def adauga_animate(animate):
    CURSOR.executemany("""INSERT INTO Filme(titlu_film, durata_film, sala, varsta_minima, audio_dublat, limba_dublare, 
                                            categorie, adaugat_de, informatii_rulare) 
                                            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)""", animate)
    return DB.commit()


def adauga_administrator(administrator):
    CURSOR.executemany("""INSERT INTO administratori(nume, prenume, email_address) VALUES(%s, %s, %s)""", administrator)
    return DB.commit()

def verifica_filme():
    CURSOR.execute("""SELECT * FROM filme WHERE informatii_rulare = 'RULEAZA ACUM'""")
    fetch = CURSOR.fetchall()
    return fetch

def arhiva_filme():
    CURSOR.execute("""SELECT * FROM filme WHERE informatii_rulare = 'ARHIVA'""")
    fetch = CURSOR.fetchall()
    return fetch


def afiseaza_film(nume):
    CURSOR.execute(f"SELECT * FROM filme WHERE titlu_film = '{nume}'")
    fetch = CURSOR.fetchone()
    print(fetch)


def elimina_film(id_film):
    CURSOR.execute(f"DELETE FROM filme WHERE id_film = {id_film}")
    print('Filmul a fost sters din baza de date')
    return DB.commit()


def afiseaza_numar_filme():
    CURSOR.execute("SELECT * FROM filme")
    fetch = CURSOR.fetchall()
    return fetch


def afiseaza_nume_filme():
    CURSOR.execute("SELECT titlu_film FROM filme")
    fetch = CURSOR.fetchall()
    for filme in fetch:
        print(filme)


def schimbare_limita_de_varsta(noua_varsta, id_film):
    CURSOR.execute('SELECT * FROM filme')
    fetch = CURSOR.fetchall()
    for filme in fetch:
        print(filme)

    CURSOR.execute(f"UPDATE filme SET varsta_minima = {noua_varsta} WHERE id_film = {id_film}")
    print('Limita de varsta a fost modificata!')
    return DB.commit()


def afiseaza_toate_filmele():
    CURSOR.execute('SELECT * FROM filme')
    fetch = CURSOR.fetchall()
    for filme in fetch:
        print(filme)


def selecteaza_film(id_film):
    CURSOR.execute(f'SELECT * FROM filme WHERE id_film = {id_film}')
    fetch = CURSOR.fetchone()
    DB.commit()
    print(fetch)
