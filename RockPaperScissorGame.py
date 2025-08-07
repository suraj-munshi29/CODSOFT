import tkinter as tk
import random

user_score = 0
computer_score = 0

choices = ["Rock","Paper","Scissors"]

def get_winner(user,computer):
    if user == computer :
        return "Tie"
    elif (user == "Rock" and computer == "Scissors") or \
        (user == "Scissors" and computer == "Paper") or \
        (user == "Paper" and computer == "Rock"):
        return "You"
    else:
        return "Computer"

def play(user_choice):
    global user_score,computer_score

    computer_choice = random.choice(choices)
    winner = get_winner(user_choice,computer_choice)

    result_text = f"You choose: {user_choice}\n Computer choose: {computer_choice}\n Result: {winner} win! " 
    result_label.config(text=result_text)

    if winner == "You":
        user_score += 1
    elif winner == "Computer":
        computer_score += 1

    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score , computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text = "Make your move!")
    score_label.config(text="Score - You: 0 | Computer: 0")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("800x700")
root.config(bg="#e3800e")

title = tk.Label(root, text ="Rock Paper Scissors Game", font = ("Algerian",40,"bold"),bg = "#c3e86c",fg = "#5f099c")
title.pack(pady=10)

result_label = tk.Label(root, text="Make your move",font=("Cascadia Code SemiBold",28),bg= "#f8ec0b", fg = "#4fba08")
result_label.pack(pady=20)

button_frame = tk.Frame(root,bg = "#422525")
button_frame.pack()

rock_button = tk.Button(button_frame, text = "Rock" , width = 10, font = ("Cascadia Code SemiBold",18),bg= "#e48df3", command = lambda: play("Rock"))
paper_button = tk.Button(button_frame, text = "Paper" , width = 10 , font = ("Cascadia Code SemiBold",18) ,bg="#e48df3", command = lambda: play("Paper"))
scissors_button = tk.Button(button_frame, text = "Scissors" , width = 10 , font = ("Cascadia Code SemiBold",18) ,bg="#e48df3", command = lambda: play("Scissors"))

rock_button.grid(row=0, column=0, padx=10, pady=10)
paper_button.grid(row=0, column=1, padx=10, pady=10)
scissors_button.grid(row=0, column=2, padx=10, pady=10)

score_label = tk.Label(root, text = "Score -You: 0 | Computer: 0",font=("Cascadia Code SemiBold", 18, ), bg= "#8cf7f7")
score_label.pack(pady=10)

reset_button  = tk.Button(root, text="Reset Game", font=("Cascadia Code SemiBold",16), bg = "#88efb5",command= reset_game)
reset_button.pack(pady=10)

root.mainloop()

    
