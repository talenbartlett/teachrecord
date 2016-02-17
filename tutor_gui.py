import gui

def signin_main():
    window = gui.TutorSignin()
    window.master.title("Tutor Sign-In")
    window.mainloop()

def tutor_panel():
    panel = gui.TutorWindow()
    panel.master.title("Tutor Panel")
    panel.mainloop()
    
if __name__ == "__main__":
    tutor_panel()
