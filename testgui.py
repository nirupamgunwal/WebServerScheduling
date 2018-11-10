from tkinter import *

root = Tk()
S = Scrollbar(root)
T = Text(root, height=4, width=50)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)


# import time
# def follow(thefile):
#     thefile.seek(0,2)
#     while True:
#         line = thefile.readline()
#         if not line:
#             time.sleep(0.1)
#             continue
#         yield line



def follow2(thefile):
	thefile.seek(0,2)
	while True:
		line = thefile.readline()
		if not line:
			T.after(1,follow2)
			continue
		yield line	        

logfile = open("logs.txt","r")
loglines = follow2(logfile)

T.insert(END, "Hiiiii")

for line in loglines:
    T.insert(END, line)





mainloop()



# import Tkinter as tk

# counter = 0 
# def counter_label(label):
#   counter = 0
#   def count():
#     global counter
#     counter += 1
#     label.config(text=str(counter))
#     label.after(1000, count)
#   count()
 
 
# root = tk.Tk()
# root.title("Counting Seconds")
# label = tk.Label(root, fg="dark green")
# label.pack()
# counter_label(label)
# button = tk.Button(root, text='Stop', width=25, command=root.destroy)
# button.pack()
# root.mainloop()