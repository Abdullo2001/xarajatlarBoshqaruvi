  
from tkinter import * 
  
window = Tk()
window.geometry('100x150')
  

list = Listbox(window, selectmode = "multiple")

list.pack(expand = YES, fill = "both")
  

x = ["C", "C++", "Java", "Python", "R",
     "Go", "Ruby", "JavaScript", "Swift"]
  
for each_item in range(len(x)):
      
    list.insert(END, x[each_item])
      
    
    list.itemconfig(each_item,
             bg = "yellow" if each_item % 2 == 0 else "cyan")
      
window.mainloop()




