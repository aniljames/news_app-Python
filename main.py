from cProfile import label
import io
from turtle import heading, left
from matplotlib.pyplot import title
from regex import F
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image
import webbrowser 



class News_app:
    #construtor
    def __init__(self):
    #fetch data
        self.data=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=c451f7534a754f72a4b0e077ad3b7ac6').json()
        # print(data)
    #GUI
        self.loadgui()
     
    #load news item 
        self.load_newsitems(0) #1st load item= index value
    
    
    def loadgui(self):
        self.root=Tk()
        self.root.geometry('350x700')
        self.root.resizable(0,0)
        self.root.title("My News App")
        self.root.configure(background='black')
        
    def clr(self):
        for i in self.root.pack_slaves():
            i.destroy()
            
    
    def load_newsitems(self,index):
        #clear news item for next one
        self.clr()
        #image
        try:
            img_url=self.data['articles'][index]['urlToImage']
            raw_data=urlopen(img_url).read()
            img=Image.open(io.BytesIO(raw_data)).resize((350,350))
            photo=ImageTk.PhotoImage(img)
            label=Label(self.root,image=photo)
            label.pack()
        except:
            img_url='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQYAAADACAMAAADRLT0TAAAATlBMVEX///+ysrLLy8uvr6/5+fm4uLj8/PzExMTn5+fBwcG7u7vX19f19fXj4+Pc3NyXl5fR0dGmpqbKysrr6+uSkpLv7++enp6Li4uioqKAgIAhIPmjAAAEJUlEQVR4nO3ci3KjIBQGYBBUEFE0Mem+/4vuORhNvOylM7sl1f+baVI1yXBOEBBshQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAeGOmrMpL6kIk1ysllQqpi5FYpiRTLnVBkjJjFigPQ+qipJTLSZW6KAk1ak6D8qkLk0zxzAJJXZpkwmsaTttK1ovKIKVOXaA0ymUaVJa6QElcVpXhpJ2mles0lKmLlICfR05q/s2kLtSXKx4jJ2VN7adR1PnGUO5RBfKCNuqzjqH0FPh4bdlP50XiYn21x5XlNGiaN891xT2PnNa1QZ1qDGXnsPtxWy63z+Fl5GR5u6hOOYZ6Rj32FPq5rWzqwn2Zl2mGsTF4vcg6zRiqeM45UdQ8K+1fLy/OMoZyi2mGZnfP8dXyVewxs8XFZn6KTnMZc7ystNvMHN2wmmaoVo0F56FOXcj/z65nW6i/XO06wRjKbOacis2k5AnGUKv6H0PepObwnWaziVj5/Z1HVqzjjcMEt0mDzFOX9L8K24BlOWwmZw++eLNpC8eQ93YeefGm34tY7efmuGOozQJNjLd0m6FE3H/YMdReuPFb36slh1288btfOl9ob3vM6cgBVTuxjrMs+2k45jzUbssgpdWi3k3QQVuHnUFSDDbfT8JR51/2hk6/dcwhFNIQba8j/5SGY15ul5/Lw1FvAiqC+gR53NF03YTs74TmkL0lAAAAAAAAfIYp87+eRPzlC5vxMrsp/kGBkrCt86r7w4v6Mf6i/VWYYVysuWphv+Uav2n5kdeiCs+TaLXQvBKhRWFiyDU/6TyL0wlzGvTjoI8LuNoLN6ah1VoGfunAazeFLgwf/QZVRMbvmUJ316qTFEgp82stcttVd4pB3qqrE67tYphTGiraS4mTH/ZK331G7ywfaSjopVYUneIPcYo+y3T5/f2nZLppyS1QhN0gWkenQCmqnCpKR4FQ7FTTy8VJ4fkcumvNVagVA9endrwLrNWiopfaEN/d3ChH9BPefz1rToO4uNBeOBDhpeBWs+5EvJmHHuw49/5IA0cad3mX3YXjILPppIgHP0LT+B/CVdRo0lH//vfCjCcFNQlSBt8ZwYE+0jB0ouN2gn5fpiH2LKWrb6Uz97F1DIs03PoQgosJ4jQ0758Gf+NH29cf9HRb1AZKQ891va2faYhPgW98a4eMDtZ3rv1UYxZpiOu9w3dKg8hv/lJdKYLsYlvDXd6cBsrMPRhFQYQ2/rlAcXWkppbA5J0wV9/kdzqvcmPV3GGGmxHDvfEffTwp4onxDdIgfBVv3dClHTy17gX3g4I7T811v48NgXDjWkzo+57/wU2ouHqYKhP81pD7evyrCn6340pSVtSqDC8/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAb+cnJPojNOxxqCEAAAAASUVORK5CYII='
            raw_data=urlopen(img_url).read()
            img=Image.open(io.BytesIO(raw_data)).resize((250,250))
            photo=ImageTk.PhotoImage(img)
            label=Label(self.root,image=photo)
            label.pack()
        
        
        
        heading=Label(self.root,text=self.data['articles'][index]['title'],bg='black',fg='white',wraplength=350,justify='left')
        heading.pack(pady=(20,20))
        heading.config(font=('poppins',14))
        
        details=Label(self.root,text=self.data['articles'][index]['description'],bg='black',fg='white',wraplength=350,justify='left')
        details.pack(pady=(20,20))
        details.config(font=('verdana',10))
        
        
        
        #butttons
        frame=Frame(self.root,bg='black')
        frame.pack(expand=True,fill=BOTH)
        if index!=0:
            prev=Button(frame,text="Previous",width=16, height=5,command=lambda:self.load_newsitems(index-1))
            prev.pack(side=LEFT)
        read=Button(frame,text="Read More",width=16, height=5,command=lambda:self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)
        
        if index!=len(self.data['articles'])-1:
            Next_n=Button(frame,text="Next",width=16, height=5,command=lambda:self.load_newsitems(index+1))
            Next_n.pack(side=LEFT)
            self.root.mainloop()
    def open_link(self,url):
        webbrowser.open(url)
obj =News_app()  