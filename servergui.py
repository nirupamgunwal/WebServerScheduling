try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk   
try:
    import tkinter.scrolledtext as tkscrolledtext
except ImportError:
    import ScrolledText as tkscrolledtext
try:
    import tkinter.filedialog as tkfiledialog
except ImportError:
    import tkFileDialog as tkfiledialog
try:
    import server as httpserver
except ImportError:
    import SimpleHTTPServer as httpserver
try:
    import socketserver as socketserver
except ImportError:
    import SocketServer as socketserver
try:
    import _thread as thread
except ImportError:
    import thread as thread

import os
import sys


def st_server():
    """Start server"""
    while True:
        httpd.handle_request()


class Application(tk.Frame):

    def verz(self):
        #select and change directory
        verzeichnis = tkfiledialog.askdirectory(
         title='Auswahl des Web-Rootverzeichnis')
        self.text.insert('end', verzeichnis)
        self.text.insert('end', "\n")
        if verzeichnis != '':
            os.chdir(verzeichnis)

    def start_server(self):
        thread.start_new_thread(st_server, ())
        self.start.config(state='disabled')
        self.text.insert('end', "Server gestartet mit PORT: {}\n".format(PORT))

    def createWidgets(self):
        """create GUI Tkinter"""
        #select directory
        self.verzeich = tk.Button(self)
        self.verzeich["text"] = "Change_Directory"
        self.verzeich["command"] = self.verz
        self.verzeich.pack({"side": "top", "fill": "x"})

        #start server
        self.start = tk.Button(self)
        self.start["text"] = "Start_Server"
        self.start["fg"] = "green"
        self.start["command"] = self.start_server
        self.start.pack({"side": "top", "fill": "x"})

        #I will write the logs here.
        # sys.stderr.write("HIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")

        #exit
        self.QUIT = tk.Button(self)
        self.QUIT["text"] = "Exit_Server"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.pack({"side": "top", "fill": "x"})

        #Information
        self.lab = tk.Label(self, text="Information Below")
        self.lab.pack({"side": "top"})

        self.text = tkscrolledtext.ScrolledText(self)
        self.text["width"] = 40
        self.text["height"] = 5
        self.text.pack({"side": "left"})

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack(expand='yes')
        self.createWidgets()

PORT = 8080
Handler = httpserver.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
root = tk.Tk()
root.title("Webserver mit Python")
app = Application(master=root)
app.mainloop()
#{code}
# servergui.py
# Displaying servergui.py.