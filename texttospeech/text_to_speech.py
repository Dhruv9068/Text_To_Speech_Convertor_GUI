import tkinter as tk
from tkinter import *
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak the entered text
def speak_now():
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()

# Create the main application window
root = Tk()
root.title("Text to Speech")
root.geometry("400x200")

# Create a LabelFrame for the text-to-speech section
obj = LabelFrame(root, text="Text to Speech", font=("Arial", 14, "bold"), bd=2, relief="groove", padx=10, pady=10)
obj.pack(fill="both", expand="yes", padx=20, pady=20)

# Create a label for the text entry field
lbl = Label(obj, text="Enter Text:", font=("Arial", 12))
lbl.grid(row=0, column=0, padx=5, pady=5, sticky="w")

# Create an entry field for the user to input text
textv = StringVar()
text = Entry(obj, textvariable=textv, font=("Arial", 12), bd=3)
text.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

# Create a button to trigger the text-to-speech conversion
btn = Button(obj, text="Speak", font=("Arial", 12), bg="#4CAF50", fg="white", command=speak_now)
btn.grid(row=0, column=2, padx=10, pady=5, sticky="e")

# Run the Tkinter event loop
root.mainloop()
