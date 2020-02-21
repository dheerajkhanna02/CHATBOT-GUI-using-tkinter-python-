#Creating GUI with tkinter
import tkinter
from tkinter import *
import time
time_string = time.strftime('%H:%M:%S')
msg="hii"
time1 = ''





def send(event=None):
    global msg
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(selectforeground="Blue", font=("Verdana", 12 ))



base = Tk()
base.title("CHATBOT")
label=Label(base,text="WELCOME TO CHATBOT",compound=CENTER,fg="Red",font = "Helvetica 16 bold italic")
label.grid(row=0,column=0)
clock=Label(base, font="Times") 
clock.grid(row=1,column=0)
def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
clock.config(text="CLOCK:" + str(tick()))


#button_image=PhotoImage(file="send-button.png")

#Create Chat window
ChatLog = Text(base,bd=0, bg="White", width="50", font="Arial",fg="Blue")
ChatLog.config(state=DISABLED)
ChatLog.grid(row=2, column=0)



#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, orient="vertical", command=ChatLog.yview)
scrollbar.grid(row=2, column=1, sticky="ns")

scroll_x = Scrollbar(base, orient="horizontal", command=ChatLog.xview)
scroll_x.grid(row=3, column=0, sticky="ew")

ChatLog.configure(yscrollcommand=scrollbar.set, xscrollcommand=scroll_x.set)

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="White",width="50", height="2", font="Arial",fg="Blue")
EntryBox.grid(row=4, column=0)

#Create Button to send message
SendButton = tkinter.Button(base, font=("Verdana",12,'bold'), text="Send", width="10", height="2",
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',command=send)
SendButton.grid(row=5, column=0)
#SendButton.bind("<Return>", send)


base.mainloop()
