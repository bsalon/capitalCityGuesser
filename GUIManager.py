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


    def pack_guess_frame(self):
        self.guess_frame.pack(expand=True, fill=tkinter.BOTH)


    def __create_startup_frame(self):
        self.startup_frame = ttk.Frame(self)
        st_frm = self.startup_frame

        _ = ttk.Button(st_frm, text="Show leaderboard", style="leaderboard.TButton").pack(expand=True, fill="both")
        _ = ttk.Label(st_frm, text="Enter your name:", style="username.TLabel").pack(fill="x")

        self.username = tkinter.StringVar()
        self.username_entry = ttk.Entry(st_frm, textvariable=self.username)
        self.username_entry.pack(fill="x")

        self.username_confirm_button = ttk.Button(st_frm, text="Confirm", style="confirm_username.TButton", command=self.__get_username)
        self.username_confirm_button.pack(fill="x")

        self.username.trace("w", self.__on_username_entry_trace)
        self.username.set("")


    def __create_guess_frame(self):
        self.guess_frame = ttk.Frame(self)
        gu_frm = self.guess_frame

        index = tkinter.IntVar()
        index.set(-1)

        _ = ttk.Label(gu_frm, text=f"What is the capital city of", style="question.TLabel", anchor="center").pack(expand=True, fill="x")
        _ = ttk.Radiobutton(gu_frm, text="test", style="guess.TRadiobutton", variable=index, value=0).pack(fill="x")
        _ = ttk.Radiobutton(gu_frm, text="test", style="guess.TRadiobutton", variable=index, value=1).pack(fill="x")
        _ = ttk.Radiobutton(gu_frm, text="test", style="guess.TRadiobutton", variable=index, value=2).pack(fill="x")
        _ = ttk.Radiobutton(gu_frm, text="test", style="guess.TRadiobutton", variable=index, value=3).pack(fill="x")
        _ = ttk.Button(gu_frm, text="confirm", style="confirm_username.TButton").pack(fill="x")


    def __on_username_entry_trace(self, *args):
        new_state = "disabled" if self.username.get() == "" else "normal"
        self.username_confirm_button.config(state=new_state)


    def __style_configuration(self):
        self.ttk_style = ttk.Style()
        self.ttk_style.configure("leaderboard.TButton", font=("Helvetica", 36))
        self.ttk_style.configure("username.TLabel", font=("Times New Roman", 18))
        self.ttk_style.configure("question.TLabel", font=("Times New Roman", 24))
        self.ttk_style.configure("confirm_username.TButton", font=("Helvetica", 18))
        self.ttk_style.configure("guess.TRadiobutton", font=("Helvetica", 18),
                                                       indicatorrelief=tkinter.FLAT,
                                                       indicatormargin=-1,
                                                       indicatordiameter=-1,
                                                       relief=tkinter.RAISED,
                                                       focusthickness=5,
                                                       padding=5)
        self.ttk_style.map("guess.TRadiobutton",
                           background=[("selected", "white"), ("active", "#ececec")])


    def __get_username(self):
        self.startup_frame.pack_forget()
        self.__create_guess_frame()
        self.pack_guess_frame()
        return self.username.get()
