
# importing tkinter for gui
import tkinter as tk
  
# creating window
window = tk.Tk()

#gui = tk.Tk(className='Python Examples - Window Color')
# set window size
#gui.geometry("400x200")

#set window color
#gui.configure(bg='blue')
  
# setting attribute
window.attributes('-fullscreen', True)
window.configure(bg='black')
window.title("Geeks For Geeks")


  
# creating text label to display on window screen
label = tk.Label(window, text="""Hello Tkinter! Hello Tkinter!

Hello Tkinter! Hello Tkinter! Hello Tkinter!Hello Tkinter!Hello Tkinter!Hello Tkinter!Hello Tkinter!  


Hello Tkinter!Hello Tkinter!Hello Tkinter!
""" , fg='white' , bg = 'black')
label.pack()
  
window.mainloop()