import gui
import db

def checkin_main():
    db_obj = db.Database()
    subjects = db_obj.get_subjects()
    
    window = gui.CheckinWindow(subject_list=subjects)
    window.master.title("Tutoring Check-In")
    window.mainloop()

if __name__ == "__main__":
    checkin_main()
