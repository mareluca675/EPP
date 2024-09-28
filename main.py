import preposition_data as pd
import random as rand
import sys
import time
import tkinter as tk

class EPP():
    def __init__(self):
        # Screen settings
        self.screen = tk.Tk()
        self.screen.geometry('1280x780')
        self.screen.title('English Preposition Practice')

        # Title
        self.title = tk.Label(self.screen, text='Welcome to EPP!', font=('Arial', 40))
        self.title.pack(pady=10)
        
        # Start label
        self.start_label = tk.Label(self.screen, text='Ready to practice?', font=('Arial', 40))
        self.start_label.pack(pady=20)
        
        # Choosing a random phrase from data
        self.index = 0
        
        # Phrase display
        self.phrase_display = tk.Label(self.screen, text='', font=('Arial', 40))
        self.phrase_display.pack(pady=10)

        # Start button
        self.start_button = tk.Button(self.screen, text='START', command=lambda: [self.practice(), self.start_game()], font=('Arial', 40), width=10)
        self.start_button.pack(pady=30)
            
        # Answer input
        self.answer_input = tk.Entry(self.screen, font=('Arial', 40))
        
        # Binding the Enter key to the check_answer method
        self.answer_input.bind('<Return>', self.check_answer)
        
        # Result label
        self.result_label = tk.Label(self.screen, font=('Arial', 40), text='')
        self.result_label.pack(pady=40)
        
        # Exit button
        self.exit_button = tk.Button(self.screen, text='EXIT', command=sys.exit, font=('Arial', 30), width=5)
        self.exit_button.place(x=575, y=600)
    
    def start_game(self):
        # Remvoing unwanted elements
        self.start_button.pack_forget()
        self.start_label.pack_forget()
        self.title.pack_forget()
    
    def practice(self):
        # Resetting the screen elements
        self.result_label.config(text='')
        self.phrase_display.config(text='')
        self.answer_input.pack(pady=10)
        
        # Choosing a random phrase from data
        self.index = rand.randint(0, len(pd.phrases.keys()) - 1)
        
        # Phrase display
        self.phrase_display.config(text=list(pd.phrases.keys())[self.index])
        
        
    def check_answer(self, event=None):
        answer = self.answer_input.get().lower()
        
        if answer == list(pd.phrases.values())[self.index]:
            self.result_label.config(text='Correct!')
        else:
            self.result_label.config(text=f'Wrong. The answer was \"{list(pd.phrases.values())[self.index]}\".')
        self.screen.after(1500, self.practice)
            
            
EPP().screen.mainloop()