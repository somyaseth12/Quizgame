import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("500x300")
        
        self.questions = [
            {
                "question": "What is the capital of India?",
                "options": ["Paris", "New Delhi", "London", "Berlin"],
                "correct_answer": "New Delhi"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                "correct_answer": "Mars"
            },
            {
                "question": "What is the currency of India??",
                "options": ["Dollar", "Paisa", "Rupee", "Euro"],
                "correct_answer": "Rupee"
            },    
            {
                "question": "What is the chemical symbol for carbon dioxide?",
                "options": ["H₂O", "CO₂", "O₂", "NaCl"],
                "correct_answer": "CO₂"
            },
            {
                "question": "What is the current value of 1 USD in INR?",
                "options": ["234", "100", "121", "82"],
                "correct_answer": "82"
            },
        ]
        
        self.current_question = 0
        self.score = 0

        self.create_widgets()
        self.show_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", wraplength=400, font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.root, text="", font=("Arial", 12), width=30, command=lambda i=i: self.check_answer(i))
            self.option_buttons.append(button)
            button.pack(pady=5)

        self.next_button = tk.Button(self.root, text="Next", font=("Arial", 14), command=self.next_question)
        self.next_button.pack(pady=10)
        self.next_button.config(state=tk.DISABLED)

        self.score_label = tk.Label(self.root, text="Score: 0", font=("Arial", 14))
        self.score_label.pack(pady=5)

    def show_question(self):
        if self.current_question < len(self.questions):
            question_info = self.questions[self.current_question]
            self.question_label.config(text=question_info["question"])
            for i, option in enumerate(question_info["options"]):
                self.option_buttons[i].config(text=option)
            self.next_button.config(state=tk.DISABLED)

    def check_answer(self, selected_option):
        question_info = self.questions[self.current_question]
        selected_answer = question_info["options"][selected_option]
        if selected_answer == question_info["correct_answer"]:
            self.score += 1
        self.score_label.config(text=f"Score: {self.score}")
        for button in self.option_buttons:
            button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            for button in self.option_buttons:
                button.config(state=tk.NORMAL)
            self.show_question()
        else:
            messagebox.showinfo("Quiz Over", f"YOUR FINAL SCORE IS: {self.score}")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    quiz_game = QuizGame(root)
    root.mainloop()
