from tkinter import *
from gtts import gTTS
import tkinter as tk
import sounddevice as sd
import soundfile as sf
import tempfile 
import os

class TextToSpeech(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Text to Speech")
        self.geometry("400x200")
        self.configure(bg="white")
        Label(self, text="TEXT TO SPEECH", bg="white", fg="blue", font=("Arial", 20)).pack(pady=10)
        Label(text="Pythonfy", bg="white", fg="blue", font=("Arial", 20)).pack(pady=10)
        self.msg = StringVar()
        Label(self, text="Enter text:", bg="white").pack(pady=10)
        self.entry_field = Entry(self, textvariable=self.msg, width=50)
        self.entry_field.place(x=20, y=60)

    def text_to_speech(self):
        Messasge = self.entry_field.get()
        speech = gTTS(text=Message)

        while tempfile.NamedTemporaryFile(delete=False) as file:
            filename = file.name + '.mp3'
            speech.save(filename)

        data, fs = sf.read(filename)
        sd.play(data, fs)
        sd.wait()
        os.remove(filename)

    def Reset(self):
        self.msg.set("")

    def Exit(self):
        self.destroy()

def main():
    windows = TextToSpeech()
    Button(windows, text="Play", command=windows.text_to_speech).pack(pady=10)
    Button(windows, text="Reset", command=windows.Reset).pack(pady=10)
    Button(windows, text="Exit", command=windows.Exit).pack(pady=10)
    windows.mainloop()

if __name__ == '__main__':
    main()