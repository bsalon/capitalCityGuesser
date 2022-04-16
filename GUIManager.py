import tkinter

from tkinter import ttk


class GUIManager(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        super(GUIManager, self).__init__(*args, **kwargs)
        self.geometry("640x480")
        self.title("Capital city guesser")


    def run(self):
        self.__style_configuration()
        self.__create_startup_frame()
        self.pack_startup_frame()
        self.mainloop()


    def pack_startup_frame(self):
        self.startup_frame.pack(expand=True, fill=tkinter.BOTH)


    def __create_startup_frame(self):
        self.startup_frame = ttk.Frame(self)
        stFrm = self.startup_frame

        _ = ttk.Button(stFrm, text="Show leaderboard", style="leaderboard.TButton").pack(expand=True, fill="both")
        _ = ttk.Label(stFrm, text="Enter your name:", style="name.TLabel").pack(fill="x")

        self.name = tkinter.StringVar()
        self.startup_frameNameEntry = ttk.Entry(stFrm, textvariable=self.name)
        self.startup_frameNameEntry.pack(fill="x")

        self.name_confirm_button = ttk.Button(stFrm, text="Confirm", style="confirm_name.TButton", command=self.__getUserName)
        self.name_confirm_button.pack(fill="x")

        self.name.trace("w", self.__on_name_entry_trace)
        self.name.set("")


    def __on_name_entry_trace(self, *args):
        new_state = "disabled" if self.name.get() == "" else "normal"
        self.name_confirm_button.config(state=new_state)


    def __style_configuration(self):
        self.ttk_style = ttk.Style()
        self.ttk_style.configure("leaderboard.TButton", font=("Helvetica", 36))
        self.ttk_style.configure("name.TLabel", font=("Times New Roman", 18))
        self.ttk_style.configure("confirm_name.TButton", font=("Helvetica", 18))


    def __getUserName(self):
        self.startup_frame.pack_forget()
        return self.name.get()
