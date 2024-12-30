import tkinter as tk

def say_hello():
    print("Hallo von deinem Raspberry Pi!")

root = tk.Tk()
root.title("Test-GUI")

button = tk.Button(root, text="Klick mich!", command=say_hello)
button.pack(pady=20)

root.mainloop()
