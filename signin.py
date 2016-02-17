import db

def signin():
    db_obj = db.Database()
    
    print("Welcome to the TutorDB program.")
    while True:
        cwid = input("CWID: ")
        subject = input("Subject: ")
        db_obj.checkin(cwid, subject)
        db_obj.commit()
    db_obj.close()

if __name__ == "__main__":
    signin()
