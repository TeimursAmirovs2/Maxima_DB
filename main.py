import sqlite3


#Pieslegties pie DB
database = sqlite3.connect("veikals.db")
cursor = database.cursor()


#Izveidot tabulu ar klientiem
cursor.execute("""
    CREATE TABLE IF NOT EXISTS klienti(
        klienti_id INTEGER PRIMARY KEY,
        vards TEXT NOT NULL,
        uzvards TEXT NOT NULL)
""")

#Izveidot tabulu ar precem
cursor.execute("""
    CREATE TABLE IF NOT EXISTS preces(
        preces_id INTEGER PRIMARY KEY,
        nosaukums TEXT NOT NULL,
        cena REAL NOT NULL)
""")
#Izveidot tabublu ar pasutījumiem

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pasutijumi(
        pasutijuma_id INTEGER PRIMARY KEY,
        klienti_id INTEGER NOT NULL,
        preces_id INTEGER NOT NULL,  
               
        FOREIGN KEY (klienti_id)
               REFERENCES klienti(klienti_id),
        FOREIGN KEY (preces_id)
               REFERENCES preces(preces_id)
    )
""")

#Ievietot datus tabulās

cursor.execute("""
INSERT OR IGNORE INTO klienti (klienti_id, vards, uzvards)
    VALUES (1, 'Teimurs', 'Amirovs')
""")
cursor.execute("""
INSERT OR IGNORE INTO klienti (klienti_id, vards, uzvards)
    VALUES (2, 'Aleks', 'Briedis')
""")
cursor.execute("""
INSERT OR IGNORE INTO klienti (klienti_id, vards, uzvards)
    VALUES (3, 'Ainars', 'Liepa')
""")

#===================================
cursor.execute("""
INSERT OR IGNORE INTO preces (preces_id, nosaukums, cena)
    VALUES (1, 'Putekļu sucējs', 500.00)
""")
cursor.execute("""
INSERT OR IGNORE INTO preces (preces_id, nosaukums, cena)
    VALUES (2, 'Aleksa Speaker', 249.99)
""")
cursor.execute("""
INSERT OR IGNORE INTO preces (preces_id, nosaukums, cena)
    VALUES (3, 'Šķēres', 5.50)
""")

cursor.execute("""
INSERT OR IGNORE INTO pasutijumi (pasutijuma_id, klienti_id, preces_id)
    VALUES (1, 2, 3)
""")
cursor.execute("""
INSERT OR IGNORE INTO pasutijumi (pasutijuma_id, klienti_id, preces_id)
    VALUES (2, 2, 2)
""")
cursor.execute("""
INSERT OR IGNORE INTO pasutijumi (pasutijuma_id, klienti_id, preces_id)
    VALUES (3, 1, 1)
""")
cursor.execute("""
INSERT OR IGNORE INTO pasutijumi (pasutijuma_id, klienti_id, preces_id)
    VALUES (4, 3, 3)
""")

#Savienot tabulas






#Saņiemt datus no tabulam
cursor.execute ("""
    SELECT *
    FROM klienti
""")

klienti = cursor.fetchall()

print("\nKLIENTI")

for klients in klienti:
    print(klients)

#__________________________________________________
cursor.execute ("""
SELECT
    klienti.vards,
    preces.nosaukums,
    preces.cena

    FROM pasutijumi
                 
    JOIN klienti
        ON pasutijumi.klienti_id = klienti.klienti_id
         
    JOIN preces
        ON pasutijumi.preces_id = preces.preces_id
""")

pasutijumi = cursor.fetchall()

print("\nPASUTIJUMI")

for pasutijums in pasutijumi:
    klienta_vards = pasutijums[0]
    preces_nosaukums = pasutijums[1]
    cena = pasutijums[2]

    print(klienta_vards, preces_nosaukums,cena)



#Saglabat
database.commit()
