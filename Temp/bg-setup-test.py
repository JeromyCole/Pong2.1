# Import module 
from tkinter import *
  
# Create object 
root = Tk()
  
# Adjust size 
root.geometry("800x600")
  
# Add image file
bg = PhotoImage(file = "pexels-pixabay-2150.png")
  
# Create Canvas
canvas1 = Canvas( root, width = 800,
                 height = 600)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")
  
# Execute tkinter
root.mainloop()