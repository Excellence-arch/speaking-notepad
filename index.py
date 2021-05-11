import pyttsx3
from tkinter import *
from tkinter import filedialog
# from tkinter.messagebox import *

class note():

	def __init__(self):
		self.root = Tk()
		self.root.iconbitmap('icons8_Add_User_Male.ico')
		self.root.geometry('800x450')
		self.root.title('Notepad')
		self.mainframe = Frame(self.root)
		self.mainframe.pack()
		self.pad = Text(self.mainframe, width=95)
		self.pad.grid(row=0, column=0, columnspan=3)
		Button(self.mainframe, command=self.speak, text='Speak').grid(row=1, column=0)
		Button(self.mainframe, command=self.open, text='Open').grid(row=1, column=1)
		Button(self.mainframe, command=self.save, text='Save').grid(row=1, column=2)
		self.root.mainloop()

	def speak(self):
		self.text = self.pad.get(0.0, END)
		if self.text == '':
			messagebox.showinfo('Error Message', 'You must type something')
		else:
			self.engine = pyttsx3.init()
			self.engine.say(self.text)
			self.engine.runAndWait()

	def save(self):
		self.smart = filedialog.asksaveasfile(mode='w', defaultextension='.mike', filetypes=[('Mike File', '*.mike')])
		if self.smart is None:
			return
		self.text = str(self.pad.get(0.0, END))
		self.smart.write(self.text)
		self.smart.close()

	def open(self):
		self.openFile = filedialog.askopenfile(mode='r', defaultextension='.mike')
		if self.openFile is None:
			return
		self.pad.delete(0.0, END)
		self.me = self.openFile.read()
		self.pad.insert(0.0, self.me)
		self.openFile.close()

me = note()

