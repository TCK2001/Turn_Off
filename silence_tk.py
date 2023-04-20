import tkinter as tk
import random
import time
from tkinter import messagebox


def run_tk():
    global x
    check = 1
    x = random.randint(2,10)

    def toggle_label():
        global check, x
        if label["text"] == "ON":
            label.config(text="OFF", bg="green")
            check = 0
            button.after(x*1000, show_who)
        else:
            label.config(text="ON", bg="red")
            check = 1
            button.after(x*1000, show_who)
                
    def show_who():
        global x
        if label["text"] == "ON":
            # 텍스트 생성
            text = "Who is it ?"
            color = "black"
            canvas.delete("text")
            canvas.create_text(150, 20, text=text, fill=color, font=("Helvetica", 24), tags="text")
            if check == 1:
                button.after(0, game_over)
        else:
            button.after(0, game_clear)
                
    def game_clear():
        messagebox.showinfo("Game Clear", "You have completed the meeting with ease.")
        root.destroy()
        
    def game_over():
        messagebox.showerror("Game Over", "You are fired by the boss")
        root.destroy()
        
    # tkinter 윈도우 생성
    root = tk.Tk()
    root.title("Phone")
    root.geometry("400x600")

    time_label = tk.Label(root, font=("Helvetica", 16), bg="black", fg="white")
    time_label.pack(pady=10)

    def update_time():
        current_time = time.strftime("%H:%M:%S")
        time_label.config(text=current_time)
        time_label.after(1000, update_time)
        
    update_time()

    # 레이블 생성
    label = tk.Label(root, text="ON", bg="red", fg="white", font=("Helvetica", 24), width=10, height=5)
    label.pack(pady=50)

    # 버튼 생성
    button = tk.Button(root, text="Press", font=("Helvetica", 16), width=10, height=2, command=toggle_label)
    button.pack(pady=10)

    canvas = tk.Canvas(root, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)

    if label["text"] == "ON":
        button.after(x*1000, show_who)
    # 메인 루프 시작
    root.mainloop()