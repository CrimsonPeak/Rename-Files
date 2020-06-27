# tkinter als gui modul
import tkinter
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

# os modul um die Datei umzubenennen
import os 

# Zeitstempel um das Datum zu bekommen
import datetime

# Das (gui) Fenster wird erstellt
window = tkinter.Tk()
window.title("Rename")
window.geometry("571x361")

#------------------------ Choose Directory ------------------------#
# das derzeitige Verzeichniss wird angezeigt
currdir = os.getcwd()
txt1 = tkinter.Text(window, height = 1, width = 571)
txt1.pack()
txt1.insert(END, currdir)

# die Verzeichnissauswahl wird durch einen Buttonklick durchgeführt
def find_path():
    currdir = os.getcwd()
    window.filename =  filedialog.askdirectory(parent=window, initialdir=currdir, title='Wählen Sie Ihr Verzeichniss')
    txt1.delete('1.0', END)
    txt1.insert(END, window.filename)
# Button: Verzeichnissauswahl
btn1 = tkinter.Button(window, text = "Ordner Auswählen", command = find_path, width = 571)
btn1.pack()

# Trennlinie
ttk.Separator(window, orient='horizontal').pack(side='top', fill='x')

#----------------------- Rename Adjustments -----------------------#
# Die Trennart zwichen den titeln wird ausgewählt
lbl1 = tkinter.Label(window, text = "Wählen Sie eine Trennart", width = 571)
lbl1.pack()
OptionList = [" - ", "-", "_", ".", " "]
sep = tkinter.StringVar(window)
sep.set(OptionList[0])
opt = tkinter.OptionMenu(window, sep, *OptionList)
opt.pack()

# Trennlinie
ttk.Separator(window, orient='horizontal').pack(side='top', fill='x')

# Trennlinie
ttk.Separator(window, orient='horizontal').pack(side='top', fill='x')

lbl3 = tkinter.Label(window, text = "Geben Sie Ihren gewünschten Titel ein", width = 571)
lbl3.pack()

txt2 = tkinter.Text(window, height = 1, width = 571)
txt2.pack()
dt = datetime.datetime.now()
dateStamp = datetime.date(dt.year, dt.month, dt.day)
txt2.insert(END, dateStamp)

# Trennlinie
ttk.Separator(window, orient='horizontal').pack(side='top', fill='x')

lbl3 = tkinter.Label(window, text = "Geben Sie Ihren gewünschten zweiten Titel ein (optional)", width = 571)
lbl3.pack()

txt3 = tkinter.Text(window, height = 1, width = 571)
txt3.pack()

# Trennlinie
ttk.Separator(window, orient='horizontal').pack(side='top', fill='x')

lbl4 = tkinter.Label(window, text = "Geben Sie den Dateityp ein (mp3/png/jpg/...)", width = 571)
lbl4.pack()

txt4 = tkinter.Text(window, height = 1, width = 571)
txt4.pack()
txt4.insert(END, "mp3")

#------------------------- Rename Process -------------------------#
def rename_files():
    # Erhält den eingegebenen Text (Ordnerpfad)
    inputTxt = txt1.get("1.0", 'end-1c')

    # Erhält die eingegebenen Texte
    input1 = txt2.get("1.0", 'end-1c')
    input2 = txt3.get("1.0", 'end-1c')
    input3 = txt4.get("1.0", 'end-1c')

    # Warnhinweis
    canvas1 = tkinter.Canvas(window, width = 300, height = 300)
    canvas1.pack()

    # Nachdem der Benutzer auf 'ja' klickt, bennent es die Dateien um
    MsgBox = tkinter.messagebox.askquestion("Rename", "Sind Sie sich sicher alle Dateien in diesem Ordner umzubenennen '" + inputTxt + "'?", icon='warning')
    if MsgBox == 'yes':
        # Funktion zum Umbenennen mehreren Dateien
        def main():
            if(input2 == ""):
                for count, filename in enumerate(os.listdir(inputTxt)): 
                    dst = input1 + sep.get() + str(count) + "." + input3
                    src = inputTxt + "/" + filename 
                    dst = inputTxt + "/" + dst 
                    os.rename(src, dst)
            else:
                for count, filename in enumerate(os.listdir(inputTxt)): 
                    dst = input1 + sep.get() + input2 + sep.get() + str(count) + "." + input3
                    src = inputTxt + "/" + filename 
                    dst = inputTxt + "/" + dst 
                    os.rename(src, dst)
        # Driver Code 
        if __name__ == '__main__': 
            main()
        
    else:
        canvas1.destroy()
btn2 = tkinter.Button(window, text = "Dateien Umbenennen", command = rename_files, width = 571)
btn2.pack(side = "bottom")

window.mainloop()