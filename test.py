import mysql.connector

DB = mysql.connector.connect(
    host="127.0.0.2",
    user="root",
    passwd="1234",
    database="Cinematograf"
)
CURSOR = DB.cursor()

insert_statement = ("INSERT INTO Filme(titlu_film, durata_film, sala, varsta_minima, audio_dublat, limba_dublare, categorie, adaugat_de, informatii_rulare) "
                    "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    )
values = ('The Way Back', '120 minute', 3, 12, 'NU', 'NU', 'drama', 1, 'RULEAZA ACUM')

CURSOR.execute(insert_statement, values)
DB.commit()
