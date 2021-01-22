import tkinter as tk
from tkinter import BOTH, CENTER, WORD, INSERT, DISABLED, NORMAL
from random import sample
import time

# how many words to type
num_words = 20

# define fonts and colors
root_color = "#191b25"
bg_color = "#232533"
text_bg_color = "#232533"
correct_color = "#32cb8b"
wrong_color = "#fe494e"
button_color = "#32cb8b"
text_color = "#fafafa"
text_entry_color = "#2c2e40"
stats_color = "#ff9552"
word_count_color = "#ffd751"
font = "Lucida Console"

word_list = ["the", "be", "of", "and", "a", "to", "in", "he", "have", "it", "that", "for", "they", "I", "with", "as",
             "not", "on", "she", "at", "by", "this", "we", "you", "do", "but", "from", "or", "which", "one", "would",
             "all", "will", "there", "say", "who", "make", "when", "can", "more", "if", "no", "man", "out", "other",
             "so", "what", "time", "up", "go", "about", "than", "into", "could", "state", "only", "new", "year", "some",
             "take", "come", "these", "know", "see", "use", "get", "like", "then", "first", "any", "work", "now", "may",
             "such", "give", "over", "think", "most", "even", "find", "day", "also", "after", "way", "many", "must",
             "look", "before", "great", "back", "through", "long", "where", "much", "should", "well", "people", "down",
             "own", "just", "because", "good", "each", "those", "feel", "seem", "how", "high", "too", "place", "little",
             "world", "very", "still", "nation", "hand", "old", "life", "tell", "write", "become", "here", "show",
             "house", "both", "between", "need", "mean", "call", "develop", "under", "last", "right", "move", "thing",
             "general", "school", "never", "same", "another", "begin", "while", "number", "part", "turn", "real",
             "leave", "might", "want", "point", "form", "off", "child", "few", "small", "since", "against", "ask",
             "late", "home", "interest", "large", "person", "end", "open", "public", "follow", "during", "present",
             "without", "again", "hold", "govern", "around", "possible", "head", "consider", "word", "program",
             "problem", "however", "lead", "system", "set", "order", "eye", "plan", "run", "keep", "face", "fact",
             "group", "play", "stand", "increase", "early", "course", "change", "help", "line"]

# define window
root = tk.Tk()
root.title("Typing Test")
root.geometry("1100x800")
root.resizable(0, 0)
root.iconbitmap("icon.ico")

# list of words to use
words = sample(word_list, num_words)

# initializes test
correct_words = []
current_word = 0
ok = 2
wpm = "---"
accuracy = "---"
start = True
index = 0
starting_time = 0


# functions will change word count
def word_50():
    global num_words
    num_words = 50
    redo_button()


def word_25():
    global num_words
    num_words = 25
    redo_button()


def word_10():
    global num_words
    num_words = 10
    redo_button()


# checks if a word is right or wrong after every space
def check_word(event):
    global current_word, wpm, accuracy, start, stats, index, starting_time
    # if the word is right, it becomes green
    if text_entry.get().replace(" ", "") == words[current_word]:
        correct_words.append(words[current_word])
        text_box.tag_add("correct words", f"1.{index} wordstart", f"1.{index} wordend")
        text_box.tag_config("correct words", foreground=correct_color, background=text_bg_color)
    # if wrong, word becomes red
    else:
        text_box.tag_add("wrong words", f"1.{index} wordstart", f"1.{index} wordend")
        text_box.tag_config("wrong words", foreground=wrong_color, background=text_bg_color)

    index += len(words[current_word]) + 1
    current_word += 1
    # if it is the first time checking a word, it starts the counter
    if start:
        starting_time = time.perf_counter()
        start = False
    # checks if the user is done, then calculates wpm and accuracy
    if current_word == num_words:
        end_time = time.perf_counter()
        wpm = round(len(correct_words) / ((end_time - starting_time) / 60))
        accuracy = (len(correct_words) / num_words) * 100
        stats = tk.Label(root, bd=0, font=(font, 15), bg=root_color, fg=stats_color,
                         text=f"WPM: {wpm} Accuracy: {accuracy}%")
        stats.place(relx=0.5, rely=0.2, relwidth=0.6, relheight=0.1, anchor=CENTER)

    # clears text entry box
    text_entry.delete(first=0, last=1000)


# resets test
def redo_button():
    global current_word, correct_words, text_box, words, wpm, accuracy, start, index, starting_time
    wpm = "---"
    accuracy = "---"
    start = True
    index = 0
    current_word = 0
    starting_time = 0
    words = sample(word_list, num_words)
    correct_words = []
    text_entry.delete(first=0, last=1000)
    text_entry.insert(0, " ")
    text_box.config(state=NORMAL)
    text_box = tk.Text(text_bg, bd=0, font=(font, 14), wrap=WORD, spacing2=5, bg=text_bg_color, fg=text_color, padx=5,
                       pady=5)
    text_box.place(relx=0.5, rely=0.42, relwidth=0.9, relheight=0.7, anchor=CENTER)
    text_box.insert(INSERT, " ".join(words))
    text_box.config(state=DISABLED)


root.config(bg=root_color)

# define frames
background = tk.LabelFrame(root, bg=bg_color, bd=0)
text_bg = tk.LabelFrame(root, bg=text_bg_color, bd=0)
background.pack(pady=150)
text_bg.pack(padx=250, pady=(0, 250), fil=BOTH, expand=True)

# redo button
button = tk.Button(text_bg, text="redo", bg=button_color, fg=text_color, bd=0, activebackground=button_color,
                   activeforeground=text_color, font=(font, 15), command=redo_button)
button.place(relx=0.92, rely=0.87, relwidth=0.12, relheight=0.16, anchor=CENTER)

# entry box
text_entry = tk.Entry(text_bg, bd=0, bg=text_entry_color, fg=text_color, font=(font, 15), insertbackground=text_color)
text_entry.bind("<space>", check_word)
text_entry.place(relx=0.425, rely=0.87, relwidth=0.8, relheight=0.16, anchor=CENTER)
text_entry.insert(0, " ")

# text box to show words
text_box = tk.Text(text_bg, bd=0, font=(font, 14), wrap=WORD, spacing2=5, bg=text_bg_color, fg=text_color, padx=5,
                   pady=5)
text_box.place(relx=0.5, rely=0.42, relwidth=0.9, relheight=0.7, anchor=CENTER)
text_box.config(state=NORMAL)
text_box.insert(INSERT, " ".join(words))
text_box.config(state=DISABLED)

# menu to select word count

word_count = tk.Menubutton(root, bd=0, font=(font, 12), bg=root_color, fg=word_count_color,
                           activebackground=text_bg_color, activeforeground=word_count_color, text="Word Count")
word_count.place(relx=0.17, rely=0.34, relwidth=0.115, relheight=0.06, anchor=CENTER)
options = tk.Menu(word_count, bd=0, activeborderwidth=15, font=(font, 14), bg=root_color, fg=word_count_color,
                  tearoff=0)
word_count.config(menu=options)
options.add_command(label="10", command=word_10)
options.add_command(label="25", command=word_25)
options.add_command(label="50", command=word_50)

# wpm and acc label
stats = tk.Label(root, bd=0, font=(font, 15), bg=root_color, fg=stats_color,
                 text=f"WPM: {wpm} Accuracy: {accuracy}")
stats.place(relx=0.5, rely=0.2, relwidth=0.6, relheight=0.1, anchor=CENTER)

# run root windows main loop
root.mainloop()
