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
        st_frm = self.startup_frame

        _ = ttk.Button(st_frm, text="Show leaderboard", style="leaderboard.TButton").pack(expand=True, fill="both")
        _ = ttk.Label(st_frm, text="Enter your name:", style="username.TLabel").pack(fill="x")

        self.username = tkinter.StringVar()
        self.username_entry = ttk.Entry(st_frm, textvariable=self.username)
        self.username_entry.pack(fill="x")

        self.username_confirm_button = ttk.Button(st_frm, text="Confirm", style="confirm_username.TButton", command=self.__get_user_name)
        self.username_confirm_button.pack(fill="x")

        self.username.trace("w", self.__on_username_entry_trace)
        self.username.set("")


    def __on_username_entry_trace(self, *args):
        new_state = "disabled" if self.username.get() == "" else "normal"
        self.username_confirm_button.config(state=new_state)


    def __style_configuration(self):
        self.ttk_style = ttk.Style()
        self.ttk_style.configure("leaderboard.TButton", font=("Helvetica", 36))
        self.ttk_style.configure("username.TLabel", font=("Times New Roman", 18))
        self.ttk_style.configure("confirm_username.TButton", font=("Helvetica", 18))


    def __get_user_name(self):
        self.startup_frame.pack_forget()
        return self.username.get()
