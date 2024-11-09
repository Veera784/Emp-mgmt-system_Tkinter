import sqlite3

class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql="""
        CREATE TABLE IF NOT EXISTS employees(
            id Integer primary key,
            name text,
            age text,
            DOB text,
            email text,
            gender text,
            mail text,
            phone text,
            DOJ text,
            address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

o=Database("Empdet.db")