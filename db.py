import sqlite3
import datetime

DB_DEFAULT_NAME = 'logs.db'

class Database():
    def __init__(self, dbname=DB_DEFAULT_NAME):
        self.con = sqlite3.connect(dbname)
        self.con.execute("PRAGMA foreign_keys = ON;")
        self.cur = self.con.cursor()

    def init_db(self):
        self.cur.executescript("""
        CREATE TABLE users(
            cwid TEXT PRIMARY KEY,
            firstname TEXT,
            lastname TEXT,
            admin INTEGER
        );

        CREATE TABLE subjects(
            subject TEXT PRIMARY KEY
        );

        CREATE TABLE checkins(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cwid TEXT,
            subject TEXT,
            FOREIGN KEY (cwid) REFERENCES users(cwid),
            FOREIGN KEY (subject) REFERENCES subjects(subject)
        );

        CREATE TABLE sessions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cwid TEXT,
            subject TEXT,
            timein TIMESTAMP,
            timeout TIMESTAMP,
            totaltime TIMESTAMP,
            FOREIGN KEY (cwid) REFERENCES users(cwid)
        );
        """)     
        
    def insert_user(self, user):
        pass
        
    def record_session(self, session):
        session_data = (session.cwid, session.subject, session.timein, session.timeout, session.totaltime)
        self.cur.execute("INSERT INTO sessions (cwid, subject, timein, timeout, totaltime) VALUES (?, ?, ?, ?, ?)", session_data)

    def checkin(self, cwid, subject):
        checkin_data = (cwid, subject)
        try:
            self.cur.execute("INSERT INTO checkins (cwid, subject) VALUES (?, ?)", checkin_data)
        except sqlite3.IntegrityError:
            print("CWID or Subject does not exist.")

    def checkout(self, cwid):
        self.cur.execute("DELETE FROM checkins WHERE cwid=?", cwid)
        
    def get_checkins(self):
        self.cur.execute("SELECT * FROM checkins")
        return (self.cur.fetchall())

    def get_subjects(self):
        self.cur.execute("SELECT * FROM subjects")
        return (self.cur.fetchall())
        
    def commit(self):
        self.con.commit()
        
    def close(self):
        self.con.commit()
        self.con.close()
        
class User():
    def __init__(self):
        self.cwid = None
        self.firstname = None
        self.lastname = None
        self.admin = False

    def set_cwid(self, cwid):
        self.cwid = cwid

    def set_firstname(self, firstname):
        self.firstname = firstname

    def set_lastname(self, lastname):
        self.lastname = lastname

    def set_admin(self, admin):
        self.admin = admin
        
class Session(User):
    def __init__(self):
        self.subject = None
        self.timein = None
        self.timeout = None
        self.totaltime = None
             
    def set_subject(self, subject):
        self.subject = subject
        
    def start(self):
        self.timein = datetime.datetime.now()

    def stop(self):
        self.timeout = datetime.datetime.now()

    def set_totaltime(self):
        self.totaltime = self.timeout - self.timein
