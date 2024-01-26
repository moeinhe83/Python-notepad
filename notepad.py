# Create Notepad

# Calling packages
from tkinter import Tk
import pygments.lexers
from chlorophyll import CodeView

# Value 
root = Tk()

# Work With CodeView
codeview = CodeView(root, lexer=pygments.lexers.PythonLexer, color_scheme='dracula')
codeview.pack(fill='both', expand=True)

# Mainloop 
root.mainloop()

# Create By Moein Heshmati