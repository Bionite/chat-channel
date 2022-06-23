import tkinter as tk
from tkinter import *
import requests

# Input
class textBox(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.entry1 = tk.Entry(self, width=25, font=("Helvetica"))
        self.entry2 = tk.Entry(self, width=35, font=("Helvetica"))
        button = tk.Button(self, text="Send", command=self.on_button)
        button.pack(pady=20, ipadx=20, ipady=5)
        self.entry1.pack()
        self.entry2.pack(pady=20)

    def on_button(self):
        content = self.entry2.get()
        username = self.entry1.get()

        url = "https://ptb.discord.com/api/webhooks/989548552671866962/T8-7DYc5FNKZhu7FzzGKAqIttSxq8Q1FpdVfivrSyS3lQNY_ck8kDS-Rmf_YlGunOXFt"

        data = {
             "content": content,
              "username": username,
         }


        result = requests.post(url, json=data)

root = textBox()
root.geometry("370x200")
root.title('The simulation')
root.mainloop()





