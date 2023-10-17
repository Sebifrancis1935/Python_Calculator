import tkinter as tk


def on_button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)


root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font=("Arial", 20), bd=10, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

button_texts = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row = 1
col = 0

for button_text in button_texts:
    button = tk.Button(root, text=button_text, font=(
        "Arial", 18), padx=20, pady=20, bd=5, relief="ridge", bg="lightgray")
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

    button.bind("<Button-1>", on_button_click)

root.mainloop()
