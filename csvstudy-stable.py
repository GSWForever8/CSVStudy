#Python study software by Aidan Hong

import csv
import random
import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
termbank = []
defbank = []
window=tk.Tk()
window.geometry('500x500')
sets = []
roundnum = 1
difficulty=3
defonly=-1
termonly=-1
correct=0
picker=1
settings=None
ans=None
gamepause=False
def fileselection():
    global instructions, yes_header, no_header, hardmode, mediummode, easymode, difficulty,askheaders,askdifficulty, roundnum,sets,termbank,defbank,settings,tonly,donly,both,askmode,start_game,correct,clearset,answer,ans,submit,rng,status,resume,question,refill,file_button
    filename=fd.askopenfilename()
    with open(filename,"r") as file:
        csvreader = csv.reader(file)
        for column in csvreader: 
            sets.append(column)
        for x in sets:
            termbank.append(x[0])
            defbank.append(x[1])
        askheaders=tk.Label(settings, text="Does your file contain headers?")
        askheaders.pack()
        yes_header=tk.Button(settings, text="Yes",command=yesheader)
        yes_header.place(relx=0.4,rely=0.5,anchor=CENTER)
        no_header=tk.Button(settings,text="No",command=noheader)
        no_header.place(relx=0.6,rely=0.5,anchor=CENTER)
def yesheader():
    global instructions, yes_header, no_header, hardmode, mediummode, easymode, difficulty,askheaders,askdifficulty, roundnum,sets,termbank,defbank,settings,tonly,donly,both,askmode,start_game,correct,clearset,answer,ans,submit,rng,status,resume,question,header
    termbank.pop(0)
    defbank.pop(0)
    sets.pop(0)
    yes_header.place_forget()
    no_header.place_forget()
    askheaders.pack_forget()
    askdifficulty=tk.Label(settings,text="Select your difficulty!")
    askdifficulty.pack()
    hardmode=tk.Button(settings, text="Hard mode",command=sethard)
    hardmode.place(relx=0.7,rely=0.5,anchor=CENTER)
    mediummode=tk.Button(settings, text="Medium mode",command=setmed)
    mediummode.place(relx=0.5,rely=0.5,anchor=CENTER)
    easymode=tk.Button(settings, text="Easy mode",command=setez)
    easymode.place(relx=0.3,rely=0.5,anchor=CENTER)
def noheader():
    global instructions, yes_header, no_header, hardmode, mediummode, easymode, difficulty,askheaders,askdifficulty, roundnum,sets,termbank,defbank,settings,tonly,donly,both,askmode,start_game,correct,clearset,answer,ans,submit,rng,status,resume,question
    yes_header.place_forget()
    no_header.place_forget()
    askheaders.pack_forget()
    askdifficulty=tk.Label(settings,text="Select your difficulty!")
    askdifficulty.pack()
    hardmode=tk.Button(settings, text="Hard mode",command=sethard)
    hardmode.place(relx=0.7,rely=0.5,anchor=CENTER)
    mediummode=tk.Button(settings, text="Medium mode",command=setmed)
    mediummode.place(relx=0.5,rely=0.5,anchor=CENTER)
    easymode=tk.Button(settings, text="Easy mode",command=setez)
    easymode.place(relx=0.3,rely=0.5,anchor=CENTER)
def sethard():
    global instructions, yes_header, no_header, hardmode, mediummode, easymode, difficulty,askheaders,askdifficulty, roundnum,sets,termbank,defbank,settings,tonly,donly,both,askmode,start_game,correct,clearset,answer,ans,submit,rng,status,resume,question
    difficulty=1
    askdifficulty.pack_forget()
    hardmode.place_forget()
    mediummode.place_forget()
    easymode.place_forget()
    askmode=tk.Label(settings, text="Choose your mode")
    askmode.pack()
    both=tk.Button(settings, text="Both",command=termdef)
    both.place(relx=0.7,rely=0.5,anchor=CENTER)
    tonly=tk.Button(settings, text="Term Only",command=termonly)
    tonly.place(relx=0.5,rely=0.5,anchor=CENTER)
    donly=tk.Button(settings, text="Definition Only",command=defonly)
    donly.place(relx=0.3,rely=0.5,anchor=CENTER)
def setmed():
    global instructions, yes_header, no_header, hardmode, mediummode, easymode, difficulty,askheaders,askdifficulty, roundnum,sets,termbank,defbank,settings,tonly,donly,both,askmode,start_game,correct,clearset,answer,ans,submit,rng,status,resume,question
    difficulty=2
    askdifficulty.pack_forget()
    hardmode.place_forget()
    mediummode.place_forget()
    easymode.place_forget()
    askmode=tk.Label(settings, text="Choose your mode")
    askmode.pack()
    both=tk.Button(settings, text="Both",command=termdef)
    both.place(relx=0.7,rely=0.5,anchor=CENTER)
    tonly=tk.Button(settings, text="Term Only",command=termonly)
    tonly.place(relx=0.5,rely=0.5,anchor=CENTER)
    donly=tk.Button(settings, text="Definition Only",command=defonly)
    donly.place(relx=0.3,rely=0.5,anchor=CENTER)
def setez():
    global instructions, yes_header, no_header, hardmode, mediummode, easymode, difficulty,askheaders,askdifficulty, roundnum,sets,termbank,defbank,settings,tonly,donly,both,askmode,start_game,correct,clearset,answer,ans,submit,rng,status,resume,question
    difficulty=3
    askdifficulty.pack_forget()
    hardmode.place_forget()
    mediummode.place_forget()
    easymode.place_forget()
    askmode=tk.Label(settings, text="Choose your mode")
    askmode.pack()
    both=tk.Button(settings, text="Both",command=termdef)
    both.place(relx=0.7,rely=0.5,anchor=CENTER)
    tonly=tk.Button(settings, text="Term Only",command=termonly)
    tonly.place(relx=0.5,rely=0.5,anchor=CENTER)
    donly=tk.Button(settings, text="Definition Only",command=defonly)
    donly.place(relx=0.3,rely=0.5,anchor=CENTER)
def submit():
    global instructions, yes_header, no_header, hardmode, mediummode, easymode, difficulty,askheaders,askdifficulty, roundnum,sets,termbank,defbank,settings,tonly,donly,both,askmode,start_game,correct,clearset,answer,ans,submit,rng,status,resume,question,refill,gamepause
    if gamepause:
        return
    answer=ans.get()
    if(answer.lower()==termbank[rng].lower() or answer.lower()==defbank[rng].lower()):
        correct+=1
        status.config(text=("Correct! You are {} for {}".format(correct,roundnum)))
        del termbank[rng]
        del defbank[rng]
    else:
        status.config(text=("Wrong! Definition: {}, Term: {}. You are {} for {}".format(defbank[rng],termbank[rng],correct,roundnum)))
    if len(termbank)==0:
        question.config(text="You finished the game! Go to settings to refill.")
    roundnum=roundnum+1
    gamepause=True
def refill():
    global instructions, yes_header, no_header, hardmode, mediummode, easymode, difficulty,askheaders,askdifficulty, roundnum,sets,termbank,defbank,settings,tonly,donly,both,askmode,start_game,correct,clearset,answer,ans,submit,rng,status,resume,question,refill
    for x in sets:
        termbank.append(x[0])
        defbank.append(x[1])
def game():
    global instructions, yes_header, no_header, hardmode, mediummode, easymode, difficulty,askheaders,askdifficulty, roundnum,sets,termbank,defbank,settings,tonly,donly,both,askmode,start_game,correct,clearset,answer,ans,submit,rng,status,resume,question,picker,termonly,defonly,gamepause
    if roundnum==1:
        question=tk.Label(window,text="",wraplength=300, justify=CENTER)
        question.pack()
        ans=tk.Entry()
        ans.pack()
        submitbutton=tk.Button(window,text="Submit",command=submit)
        submitbutton.pack()
        settingsbutton=tk.Button(window,text="Settings",command=open_settings)
        settingsbutton.pack()
        status=tk.Label(window,text="",wraplength=300,justify=CENTER)
        status.pack()
        resume=tk.Button(window,text="Resume",command=game)
        resume.pack()
        showmain()
        close_settings()
    try:
        start_game.pack_forget()
    except:
        pass
    try:
        ans.delete(0,tk.END)
    except:
        pass
    gamepause=False
    if(picker==0):
        termonly=0
        defonly=0
        choice=random.randint(0,1)
        if(choice==0):
            termonly=1
        else:
            defonly=1
    if roundnum>0:
        rng=random.randint(0,len(termbank)-1)
    if(termonly==1):
        question.config(text=("Respond with the term given the definition: {}".format(defbank[rng])))
    else:
        question.config(text=("Respond with the definition given the term: {}".format(termbank[rng])))
    ans.bind('<Return>',enter)
    window.bind('<Command-r>',resumegame)
    window.bind('<Control-r>',resumegame)
    window.bind('<Command-comma>',setting)
    window.bind('<Control-comma>',setting)
def termonly():
    global instructions, yes_header, no_header, hardmode, mediummode, easymode, difficulty,askheaders,askdifficulty, roundnum,sets,termbank,defbank,settings,tonly,donly,both,askmode,start_game,correct,clearset,answer,ans,submit,rng,status,resume,question,termonly,defonly
    termonly=1
    askmode.pack_forget()
    both.place_forget()
    tonly.place_forget()
    donly.place_forget()
    start_game=tk.Button(settings, text="Start Game",command=game)
    start_game.pack()
def defonly():
    global instructions, yes_header, no_header, hardmode, mediummode, easymode, difficulty,askheaders,askdifficulty, roundnum,sets,termbank,defbank,settings,tonly,donly,both,askmode,start_game,correct,clearset,answer,ans,submit,rng,status,resume,question,termonly,defonly
    defonly=1
    askmode.pack_forget()
    both.place_forget()
    tonly.place_forget()
    donly.place_forget()
    start_game=tk.Button(settings, text="Start Game",command=game)
    start_game.pack()
def termdef():
    global instructions, yes_header, no_header, hardmode, mediummode, easymode, difficulty,askheaders,askdifficulty, roundnum,sets,termbank,defbank,settings,tonly,donly,both,askmode,start_game,correct,clearset,answer,ans,submit,rng,status,resume,question,picker,termonly,defonly
    askmode.pack_forget()
    picker=0
    both.place_forget()
    tonly.place_forget()
    donly.place_forget()
    start_game=tk.Button(settings, text="Start Game",command=game)
    start_game.pack()
def clearsets():
    global instructions, yes_header, no_header, hardmode, mediummode, easymode, difficulty,askheaders,askdifficulty, roundnum,sets,termbank,defbank,settings,tonly,donly,both,askmode,start_game,correct,clearset,answer,ans,submit,rng,status,resume,question
    sets.clear()
    termbank.clear()
    defbank.clear()
def open_settings():
    global instructions, yes_header, no_header, hardmode, mediummode, easymode, difficulty,askheaders,askdifficulty, roundnum,sets,termbank,defbank,settings,tonly,donly,both,askmode,start_game,correct,clearset,answer,ans,submit,rng,status,resume,question,refill,file_button,settings
    if settings is None:
        settings=tk.Toplevel()
        settings.title("Settings")
        settings.geometry('500x500')
        settings.protocol("WM_DELETE_WINDOW", close_settings)
        clearset=tk.Button(settings,text="Clear Sets",command=clearsets)
        clearset.pack()
        file_button=tk.Button(settings,text="Add New File",command=fileselection)
        file_button.pack()
        refill=tk.Button(settings,text="Refill",command=refill)
        refill.pack()
        settings.attributes("-fullscreen",False)
    else:
        settings.deiconify()
def close_settings():
    global settings
    if settings is not None:
        settings.withdraw()
def enter(event):
    submit()
def resumegame(event):
    game()
def setting(event):
    open_settings()
def hidemain():
    window.withdraw()
def showmain():
    window.deiconify()
window.attributes("-fullscreen",False)
window.withdraw()
open_settings()
window.title("Csvstudy")
window.mainloop()