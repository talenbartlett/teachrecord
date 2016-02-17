import tkinter as tk

class TutorSignin (tk.Frame):
    def __init__(self, root=None):
        self.root = root
        self.root.geometry("200x100")
        tk.Frame.__init__(self, root)
        
        tk.Label(text = "ID:").grid(row = 0)
        self.user = tk.Entry().grid(row = 1)
        tk.Button(text = "Connect").grid(row = 1, column = 1)

class TutorWindow (tk.Frame):
    def __init__(self, root=tk.Tk()):
        self.root = root        
        tk.Frame.__init__(self, self.root)
        self.root.geometry("800x600")
        tk.Label(text = "Current Session: ").grid(sticky = tk.W, row = 0)
        
        self.checkin_list = tk.Listbox(height = 25, width = 50)
        self.checkin_list.grid(sticky = tk.W, row = 1)

        tk.Button(text = "Start Session").grid(sticky = tk.W, row = 2)
        tk.Button(text = "End Session").grid(sticky = tk.E, row = 2)

        self.poll_checkins()
        
    def poll_checkins(self):
        self.root.after(10000, self.poll_checkins)
        
class CheckinWindow (tk.Frame):
    def __init__(self, root=None, subject_list=["No subjects"]):
        tk.Frame.__init__(self, root)
        tk.Label(text = "CWID:").grid(row = 0)

        self.subject_list = subject_list
        
        self.cwid = tk.Entry()
        self.cwid.grid(row = 0, column = 1)

        tk.Label(text = "Subject: ").grid(row = 1)
        
        self.selection = tk.StringVar(root)
        self.subjects = tk.OptionMenu(root, self.selection, *(self.subject_list))
        self.subjects.grid(row=1, column = 1, sticky="we")
        
        #send the form in
        tk.Button(text="Check-In").grid(row = 2, column = 0)
