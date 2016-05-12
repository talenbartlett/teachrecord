import db
import pathlib

def main():
    print("Welcome to the TeachRecord program.")
    
    dbpath = pathlib.Path(db.DB_DEFAULT_NAME)
    if (not dbpath.exists()):
        print("No database found! Creating one for you.")
        db_obj = db.Database(db.DB_DEFAULT_NAME)
        db_obj.init_db()
    else:
        db_obj = db.Database(db.DB_DEFAULT_NAME)

    while True:
        print("""
Select one of the following options to continue:
[1] Start new tutoring session
[2] View current check-ins
[3] Create new user
""")

        selection = int(input("Selection: "))
        if (selection == 1):
            session = new_session()
            if session is not None:
                db_obj.insert_session(session)
        elif (selection == 2):
            print(db_obj.get_checkins())
        elif (selection == 3):
            user = new_user()
            db_obj.insert_user(user)
        else:
            pass

    db_obj.close()

def new_session():
    session = db.Session()
    session.start()
    while True:
        print("""
Select one of the following options to continue:
[1] Stop tutoring session and save
[2] Stop tutoring session and do not save
""")

        selection = int(input("Selection: "))
        if (selection == 1):
            session.stop()
            return session
        elif (selection == 2):
            return None
        else:
            pass
                
def new_user():
    user = db.User()
    user.set_cwid(input("User's campus-wide ID (CWID): "))
    user.set_firstname(input("User's first name: "))
    user.set_lastname(input("User's last name: "))

    admin_setting = False
    user.set_admin(admin)
    return user

if __name__ == "__main__":
    main()
