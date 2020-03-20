from os import path
import sqlite3 as sql

ROOT = path.dirname(path.relpath(__file__))
dbname = 'database.sqlite'

def create_post(user, post, location, item, tags, ats):
    con = sql.connect(path.join(ROOT, dbname))
    cur = con.cursor()
    cur.execute(
        """insert into post
                (user, post, location, item, tags, ats)
                values (?,?,?,?,?,?)
        """
        , (user, post, location, item, tags, ats)
        )
    con.commit()
    con.close()

def get_posts():
    con = sql.connect(path.join(ROOT, dbname))
    cur = con.cursor()
    posts = cur.execute('select * from post')
    con.commit()
    con.close()

    return posts

def make_db():
    schema = open(path.join(ROOT,'schema.sql')).read()
    con = sql.connect(path.join(ROOT, dbname))
    con.execute(schema)
    con.commit()
    con.close()
