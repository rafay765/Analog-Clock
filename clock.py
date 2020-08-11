from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import *

class clock():
    def __init__(self,root):
        self.root = root
        self.root.iconbitmap("C:/Users/MUHAMMAD RAFAY/Downloads/333333333333 (1).ico")
        self.root.title("Clock")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="indigo")
        
        title = Label(self.root,text = "BMS ANALOG CLOCK",font=("Monotype Corsiva",50,"bold"),
                     bg="black",fg="white",bd=4)
        title.place(x=0,y=50,relwidth=1)
        
        self.lbl = Label(self.root,bg="white",bd = 20 , relief = RAISED)
        self.lbl.place(x=450,y=160,height=400,width=400)
#         self.clock_image()
        self.working()
        
    def clock_image(self,hr,minute,sec):
        clock=Image.new("RGB",(400,400),(255,255,255))
        draw = ImageDraw.Draw(clock)
        #------------CLOCK IMAGE---------------
        bg = Image.open("C:/Users/MUHAMMAD RAFAY/Desktop/PROGRAMMING FUNDAMENTAL/PROGRAMMING FUNDAMENTAL/Projects/Analog Clock/clock1.jpg")
        bg = bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        
        #--------------FORUMULA TO ROTATE THE CLOCK------------------
        
#         angle_in_radians = angle_in_degrees * math.pi / 180
#         line_length = 100
#         center_x = 250
#         center_y = 250
#         end_x = center_x + line_length * math.cos(angle_in_radians)
#         end_y = center_y - line_length * math.cos(angle_in_radians)
        origin = 200,200
        
        #------------Hour Line IMAGE---------------
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),
                  fill="black",width=4)
        #------------Minute Line IMAGE---------------
        draw.line((origin,200+80*sin(radians(minute)),200-80*cos(radians(minute))),
                  fill="blue",width=3)
        #------------Sec Line IMAGE---------------
        draw.line((origin,200+80*sin(radians(sec)),200-100*cos(radians(sec))),
                  fill="green",width=4)
        draw.ellipse((195,195,210,210),fill="black")
        clock.save("new_clock.png")
        
    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second
        
        hr = (h/12)*360
        minute = (m/60)*360
        sec = (s/60)*360
#         print(h,m,s)
#         print(hr,minute,sec)
        self.clock_image(hr,minute,sec)
        self.img=ImageTk.PhotoImage(file="new_clock.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)
        
        
    
    
    
        
        
  
  
































root=Tk()
# root.mainloop()
obj = clock(root)
