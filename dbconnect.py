import sqlite3

def connection():
    conn= sqlite3.connect('students.db')
    c = conn.cursor()
    return c, conn
