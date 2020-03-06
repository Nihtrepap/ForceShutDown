""" I want to create a program that will force your computer to shutdown after x minutes """
import os, subprocess, tkinter
import tkinter.messagebox
class Window:
    def __init__(self):
        self.root = tkinter.Tk()
        self.paint = tkinter.Canvas(self.root, width=400, height=300, bg='grey')
        self.root.title('Shut it all down')
        self.adapt = 'green'

    def create_GUI(self):
        user_input = tkinter.Entry(self.paint,width=12,font='fixedsys')
        user_input.place(x=100,y=100)
        self.paint.create_text(50,110, text='Turn of in: ', font=("fixedsys",12))
        self.paint.create_text(270,110,text='minutes',font=("fixedsys",12))
        tkinter.Button(self.root, command=lambda: self.check_file(user_input),bg=f'{self.adapt}', text='Force shutdown', width=13).place(x=100,y=150)
        tkinter.Button(self.root, command= self.root.quit, text='Close this program', bg='red').place(x=280, y=250)
        self.paint.pack()
        self.root.mainloop()

    def check_file(self,user_input):
        self.adapt = 'orange'
        create_user_input = user_input.get()
        try:
            time_until_emptiness = int(create_user_input) *60
        except ValueError:
            tkinter.messagebox.showerror('Invalid','Invalid form of characters, Use numbers only')

        file_ = 'timeSD.bat'
        the_shutdown = open(file_, 'w')
        if os.path.exists(file_):
            print(os.path.exists(file_))
            the_shutdown.write(f'@ECHO OFF ECHO\nshutdown -s  -t {time_until_emptiness}')
            the_shutdown.close()
            subprocess.call([r'timeSD.bat'])
            tkinter.messagebox.showinfo('GOODBYE',f'You computer will shut down in {create_user_input} minutes\n Now use your minutes well')
            tkinter.Label(self.root, font=("fixedsys", 18), text = 'Shutdown in progress', bg='green').place(x=50,y=30)
Window().create_GUI()