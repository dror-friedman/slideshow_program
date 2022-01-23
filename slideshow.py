from itertools import cycle
import tkinter as tk
#using "self" allows me to access the object from within the class#
class App(tk.Tk):
    def __init__(self,image_files,x,y,delay):
        tk.Tk.__init__(self)
        self.geometry('+{}+{}'.format(x, y))
        self.delay = delay
        self.pictures = cycle((tk.PhotoImage(file=image), image)
                              for image in image_files)
        #Tk window/Label adjusts to size of imqage
        self.picture_display = tk.Label(self)
        self.picture_display.pack()
        #defying a function to cycle through images and display them
    def show_slides(self):
        img_object, img_name = next(self.pictures)
        self.picture_display.config(image=img_object)
        self.title(img_name)
        self.after(self.delay,self.show_slides)

    def run(self):
        self.mainloop()
#setting millisecods between objects
delay = 3500
#option:type the full path of the pics or set directory to their location
image_files = [
'1.GIF',
'2.GIF',
'3.GIF',
'4.GIF',
'5.GIF',
'6.GIF',
'7.GIF']
x = 100
y = 50
app = App(image_files, x, y, delay)
app.show_slides()
app.run()
