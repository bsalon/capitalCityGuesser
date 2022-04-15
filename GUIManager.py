import tkinter

from tkinter import ttk


class GUIManager(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        super(GUIManager, self).__init__(*args, **kwargs)
        self.geometry("640x480")
        self.title("Capital city guesser")


    def run(self):
        self.__style_configuration()
        self.pack_startup_frame()
        self.mainloop()


    def pack_startup_frame(self):
        self.startup_frame = ttk.Frame(self)
        self.__create_startup_frame()
        self.startup_frame.pack(expand=True, fill=tkinter.BOTH)


    def __create_startup_frame(self):
        stFrm = self.startup_frame

        _ = ttk.Button(stFrm, text="Show leaderboard", style="leaderboard.TButton").pack(expand=True, fill="both")
        _ = ttk.Label(stFrm, text="Enter your name:", style="name.TLabel").pack(fill="x")

        self.startup_frameNameEntry = ttk.Entry(stFrm)
        self.startup_frameNameEntry.pack(fill="x")

        _ = ttk.Button(stFrm, text="Confirm", style="confirm_name.TButton", command=self.__getUserName).pack(fill="x")


    def __style_configuration(self):
        self.ttk_style = ttk.Style()
        self.ttk_style.configure("leaderboard.TButton", font=("Helvetica", 36))
        self.ttk_style.configure("name.TLabel", font=("Times New Roman", 18))
        self.ttk_style.configure("confirm_name.TButton", font=("Helvetica", 18))


    def __getUserName(self):
        return self.startup_frameNameEntry.get()
