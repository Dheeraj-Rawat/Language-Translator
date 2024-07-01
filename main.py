from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    trans = Translator()
    try:
        trans1 = trans.translate(text, src=src, dest=dest)
        return trans1.text
    except AttributeError as e:
        return "Translation failed: Please check the language codes and try again."
    except Exception as e:
        return f"Error: {e}"

def data():
    s = comb_source.get()
    d = comb_destination.get()
    msg = source_text.get(1.0, END)
    textget = change(text = msg, src = s, dest = d)
    destination_text.delete(1.0, END)
    destination_text.insert(END, textget)



root = Tk()
root.title("Language Translator")
root.geometry("500x700")
root.config(bg= "green")

lab_text = Label(root, text = "Language Translator", font = ("Times New Roman",30, "bold"), bg = "green", foreground = "white")
lab_text.place(x = 100, y = 30, height = 50, width = 380)

frame = Frame(root).pack(side = BOTTOM)

lab_text = Label(root, text = "Enter text here", font = ("Times New Roman",18, "bold"), bg = "green", foreground = "black")
lab_text.place(x = 90, y = 90, height = 40, width = 310)

source_text = Text(frame,font = ("Times New Roman",20, "bold"), wrap = WORD)
source_text.place(x = 10, y = 130, height = 70, width = 480)

list_text = list(LANGUAGES.values())
comb_source = ttk.Combobox(frame,value= list_text)
comb_source.place(x = 10, y = 210, height = 30, width = 150)
comb_source.set("English")

button_change = Button(frame,text = "Translate", relief = RAISED, command = data)
button_change.place(x = 170, y = 210, height = 30, width = 150)

comb_destination = ttk.Combobox(frame,value= list_text)
comb_destination.place(x = 330, y = 210, height = 30, width = 150)
comb_destination.set("English")



lab_text = Label(root, text = "Translation", font = ("Times New Roman",18, "bold"), bg = "green", foreground = "black")
lab_text.place(x = 100, y = 270, height = 40, width = 300)
destination_text = Text(frame,font = ("Times New Roman",20, "bold"), wrap = WORD)
destination_text.place(x = 10, y = 310, height = 70, width = 480)




root.mainloop()