import tkinter

from tkinter import ttk

from data.Services.CountryService import CountryService
from GuessDataGenerator import GuessDataGenerator


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

        self.username_confirm_button = ttk.Button(st_frm, text="Confirm", style="confirm_username.TButton", command=self.__start_guessing)
        self.username_confirm_button.pack(fill="x")

        self.username.trace("w", self.__on_username_entry_trace)
        self.username.set("")


    def __create_guess_frame(self):
        self.guess_frame = ttk.Frame(self)
        gu_frm = self.guess_frame

        self.answers = []

        self.index = tkinter.IntVar()
        self.index.set(-1)

        self.guess_capital_label = ttk.Label(gu_frm, text="What is the capital city of", style="question.TLabel", anchor="center")
        self.guess_capital_label.pack(expand=True, fill="x")

        self.guess_options = []
        for i in range(4):
            self.guess_options.append(ttk.Radiobutton(gu_frm, text="test", style="guess.TRadiobutton", variable=self.index, value=i))
            self.guess_options[i].pack(fill="x")

        self.guess_data = self.__generate_guess_data()
        guess_frame_courutine = self.__create_guess_frame_courutine(self.guess_data)

        self.guess_button = ttk.Button(gu_frm, text="confirm", style="confirm_username.TButton", command=lambda: self.next_guess_frame(guess_frame_courutine))
        self.guess_button.pack(fill="x")
        guess_frame_courutine.send(None)


    def next_guess_frame(self, guess_frame_courutine):
        self.answers.append(self.index.get())
        try:
            guess_frame_courutine.send(None)
        except StopIteration as si:
            self.guess_frame.pack_forget()
            self.__create_results_frame()
            self.results_frame.pack()


    def __create_results_frame(self):
        self.results_frame = ttk.Frame(self)
        correct = [i for i in range(len(self.guess_data)) if self.guess_data[i][1] == self.answers[i]]
        result_label = ttk.Label(self.results_frame, text=f"You have got {len(correct)} correct answer(s):", style="result.TLabel", anchor="center")
        result_label.pack(expand=True, fill="x")
        for i in range(len(self.guess_data)):
            countries, correct_index = self.guess_data[i]
            correct_country = countries[correct_index]
            if i in correct:
                ttk.Label(self.results_frame, text=f"Capital city of {correct_country.name} is {correct_country.capital_city} (correct)", style="correct.TLabel").pack(fill="x")
            else:
                ttk.Label(self.results_frame, text=f"Capital city of {correct_country.name} is {correct_country.capital_city} (not {countries[self.answers[i]].capital_city})", style="correct.TLabel").pack(fill="x")



    def __create_guess_frame_courutine(self, guess_data):
        index = 0
        while index < len(guess_data):
            countries, correct = guess_data[index]
            correct_country = countries[correct]

            self.guess_capital_label.config(text = f"What is the capital city of {correct_country.name}")
            for i in range(len(countries)):
                self.guess_options[i].config(text = f"{countries[i].capital_city}")

            index += 1
            next_frame = yield


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
        self.ttk_style.configure("result.TLabel", font=("Helvetica", 24))
        self.ttk_style.configure("correct.TLabel", font=("Times New Roman", 12))


    def __start_guessing(self):
        self.startup_frame.pack_forget()
        self.__create_guess_frame()
        self.pack_guess_frame()


    def __generate_guess_data(self):
        country_service = CountryService()
        guess_data_generator = GuessDataGenerator(country_service)
        return guess_data_generator.generate_guess_data(5, 4)
