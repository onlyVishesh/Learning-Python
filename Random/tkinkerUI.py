from tkinter import *

window = Tk() # Creating a window of gui
window.title('Hi I m Vishesh') #giving title
window.config(background='cyan') #giving colour also use hex value

def click():
   print('why u click me')
   
label = Label(
      window #telling window on which we work
     ,text='Hi hii I love my self' #adding text in window
     ,font=('Arial',19,'bold') #formating text
     ,fg='yellow' # giving text colour
     ,bg='orange' #giving colour to text bg
     ,relief = RAISED
     ,bd =10)
button = Button(
      window, 
      text='Please do not click me',
      command = click,
      font= ('Comic Sana',16),
      fg ='pink',
      bg ='black',
      activeforeground='blue',
      activebackground='violet')
label.pack()
button.pack()
window.mainloop() #showing window
#slider = Scale(window)
#slider.pack()