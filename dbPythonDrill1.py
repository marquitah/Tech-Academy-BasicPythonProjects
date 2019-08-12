import sqlite3

conn = sqlite3.connect('dbPythonDrill.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileList TEXT)")

conn.commit()
conn.close()


conn = sqlite3.connect('dbPythonDrill.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_fileList (col_fileList) VALUES ('information.docx')")
    cur.execute("INSERT INTO tbl_fileList (col_fileList) VALUES ('Hello.txt')")
    cur.execute("INSERT INTO tbl_fileList (col_fileList) VALUES ('myImage.png')")
    cur.execute("INSERT INTO tbl_fileList (col_fileList) VALUES ('myMovie.mgp')")
    cur.execute("INSERT INTO tbl_fileList (col_fileList) VALUES ('World.txt')")
    cur.execute("INSERT INTO tbl_fileList (col_fileList) VALUES ('data.pdf')")
    cur.execute("INSERT INTO tbl_fileList (col_fileList) VALUES ('myPhoto.jpg')")
    conn.commit()
conn.close()

conn = sqlite3.connect('dbPythonDrill.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fileList FROM tbl_fileList WHERE col_fileList LIKE '%txt'")
    varFiles = cur.fetchall()
    print(varFiles)
    



