import mysql.connector

DB = mysql.connector.connect(
    host="127.0.0.2",
    user="root",
    passwd="1234",
    # database="Cinematograf"
)
CURSOR = DB.cursor()

CURSOR.execute("CREATE DATABASE IF NOT EXISTS Cinematograf")


CURSOR.execute("""CREATE TABLE IF NOT EXISTS Cinematograf.Administratori(
    id_administrator tinyint NOT NULL AUTO_INCREMENT,
    nume varchar(50) NOT NULL,
    prenume varchar(50) NOT NULL,
    email_address varchar(50) NOT NULL,
    PRIMARY KEY (id_administrator)
    )""")


CURSOR.execute("""CREATE Table IF NOT EXISTS Cinematograf.Sala(
    id_sala tinyint NOT NULL AUTO_INCREMENT,
    nume_sala varchar(50) DEFAULT NULL,
    PRIMARY KEY (id_sala)
)""")


CURSOR.execute("""
    CREATE TABLE IF NOT EXISTS Cinematograf.Filme(
        id_film tinyint NOT NULL AUTO_INCREMENT,
        titlu_film varchar(50) NOT NULL,
        durata_film varchar(50) DEFAULT '0 minute',
        sala tinyint DEFAULT NULL,
        varsta_minima int(11) NOT NULL,
        audio_dublat varchar(50) DEFAULT 'nu',
        limba_dublare varchar(50) DEFAULT 'nu',
        categorie varchar(50) DEFAULT NULL,
        adaugat_de tinyint NOT NULL,
        informatii_rulare varchar(50),
        PRIMARY KEY (id_film),
        FOREIGN KEY(sala) REFERENCES `sala`(id_sala),
        FOREIGN KEY (adaugat_de) REFERENCES `Administratori`(id_administrator))
 """)


sali_cinema = [
    ('sala_new_york',),
    ('sala_munchen',),
    ('sala_londra',)
]

CURSOR.executemany("INSERT INTO Cinematograf.sala(nume_sala) VALUES (%s)", sali_cinema)

administrator = [
    ('Ardin', 'Cioparca', 'ardin_cioparca@cinema.ro'),
    ('Hazara', 'Ramadan', 'hazara_ramadan@cinema.ro')
]

CURSOR.executemany("""INSERT INTO Cinematograf.administratori(nume, prenume, email_address) VALUES(%s, %s, %s)""",
                   administrator)
DB.commit()

drame = [
    ('1917: Speranta si moarte', '120 minute', 3, 12, 'NU', 'NU', 'drama', 1, 'RULEAZA ACUM'),
    ('Bombshell: Scandalul', '110 minute', 2, 12, 'NU', 'NU', 'drama', 1, 'RULEAZA ACUM'),
    ('The Gentlemen', '130 minute', 2, 16, 'NU', 'NU', 'drama', 1, 'RULEAZA ACUM'),
    ('Birds of prey', '120 minute', 2, 12, 'NU', 'NU', 'drama', 1, 'ARHIVA'),
    ('Little women ', '130 minute', 1, 16, 'NU', 'NU', 'drama', 1, 'ARHIVA'),
    ('Emma', '90 minute', 2, 12, 'NU', 'NU', 'drama', 1, 'ARHIVA'),
    ('Bad Boys for Life', '120 minute', 1, 16, 'NU', 'NU', 'drama', 1, 'RULEAZA ACUM')
]


CURSOR.executemany("""INSERT INTO Cinematograf.Filme(titlu_film, durata_film, sala, varsta_minima, audio_dublat,
 limba_dublare, categorie, adaugat_de, informatii_rulare) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)""", drame)
DB.commit()

animate = [
    ('REGATUL DE GHEAȚĂ II', '120 minute', 3, 0, 'DA', 'ROMANA', 'ANIMATE', 2, 'RULEAZA ACUM'),
    ('SPIONI DEGHIZATI', '130 minute', 3, 0, 'DA', 'ROMANA', 'ANIMATE', 2, 'RULEAZA ACUM'),
    ('CATEII ARCTICI:CURSA PE ZAPADA ', '110 minute', 3, 0, 'DA', 'ROMANA', 'ANIMATE', 2, 'ARHIVA'),
    ('PRINTESA "CONDURI ROSII" SI CEI 7 PITICI', '110 minute', 3, 0, 'DA', 'ROMANA', 'ANIMATE', 2, 'ARHIVA'),
    ('DOCTOR DOLITTLE', '130 minute', 3, 0, 'DA', 'ROMANA', 'ANIMATE', 2, 'RULEAZA ACUM')
]

CURSOR.executemany("""INSERT INTO Cinematograf.Filme(titlu_film, durata_film, sala, varsta_minima, audio_dublat,
 limba_dublare, categorie, adaugat_de, informatii_rulare) 
                                        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)""", animate)
DB.commit()
