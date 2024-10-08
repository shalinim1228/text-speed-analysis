import tkinter as tk
import random
import time
class Typingtester:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing tester")
        self.generated_text = self.generate_random_text()
        self.typed_text = tk.StringVar()
        self.start_time = None
        self.create_widgets()
    def create_widgets(self):
        self.text_label = tk.Label(self.root, text="Type the following:")
        self.text_label.pack()
        self.generated_label = tk.Label(self.root, text=self.generated_text, font=("Helvetica", 12), wraplength=400)
        self.generated_label.pack()
        self.entry_label = tk.Label(self.root, text="Your typing:")
        self.entry_label.pack()
        self.entry = tk.Entry(self.root, textvariable=self.typed_text)
        self.entry.pack()
        self.start_button = tk.Button(self.root, text="Start Typing", command=self.start_typing)
        self.start_button.pack()
        self.speed_label = tk.Label(self.root, text="Typing Speed: 0 WPM")
        self.speed_label.pack()
        self.accuracy_label = tk.Label(self.root, text="Accuracy: 0%")
        self.accuracy_label.pack()
    def generate_random_text(self):
        words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
        return ' '.join(random.sample(words, k=5))
    def start_typing(self):
        self.start_time = time.time()
        self.start_button.config(state=tk.DISABLED)
        self.entry.bind("<KeyRelease>", self.check_typing)
    def check_typing(self, event):
        typed_text = self.typed_text.get()
        generated_text = self.generated_text
        if typed_text == generated_text:
            elapsed_time = time.time() - self.start_time
            words_per_minute = int((len(generated_text.split()) / elapsed_time) * 60)
            accuracy = self.calculate_accuracy(typed_text, generated_text)
            self.speed_label.config(text=f"Typing Speed: {words_per_minute} WPM")
            self.accuracy_label.config(text=f"Accuracy: {accuracy}%")
            self.entry.unbind("<KeyRelease>")
            self.start_button.config(state=tk.NORMAL)
    def calculate_accuracy(self, typed_text, generated_text):
        correct_characters = sum(c1 == c2 for c1, c2 in zip(typed_text, generated_text))
        accuracy_percentage = (correct_characters / len(generated_text)) * 100
        return round(accuracy_percentage, 2)
if __name__ == "__main__":
    root = tk.Tk()
    app = Typingtester(root)
    root.mainloop()