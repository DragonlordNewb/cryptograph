from tkinter import Tk
from tkinter import Label
from tkinter import Canvas
from tkinter import Entry
from tkinter import Button
from tkinter import Frame

from cryptograph import algorithms

class Cryptograph(Tk):

	FONT = lambda size: ("OCR A Extended", size)

	def __init__(self) -> None:
		Tk.__init__(self)
		self.title("Cryptograph")
		self.config(bg="black")

		self.titleLabel = Label(
			self, 
			text="Cryptograph", 
			bg="black", 
			fg="white", 
			font=self.FONT(24)
		)
		self.titleLabel.grid(row=1, column=1, columnspan=2)

		self.keyManagementFrame = Frame(self, bg="black")
		self.keyManagementFrame.grid(row=2, column=1)

		self.keyManagementLabel = Label(
			self.keyManagementFrame, 
			text="Keys", 
			bg="black", 
			fg="white", 
			font=self.FONT(16)
		)
		self.keyManagementLabel.grid(row=1, column=1)
		self.generateKeysButton = Button(
			self.keyManagementFrame, 
			text="Generate keys", 
			bg="black", 
			fg="white", 
			font=self.FONT(12),
			command=lambda: self.generateKeys()
		)
		self.generateKeysButton.grid(row=2, column=1)

		self.encryptionFrame = Frame(self, bg="black")
		self.encryptionFrame.grid(row=2, column=2)

		self.encryptionLabel = Label(
			self.encryptionFrame,
			text="Encryption",
			bg="black",
			fg="white",
			font=self.FONT(16)
		)
		self.encryptionLabel.grid(row=1, column=1)
		self.encryptFileButton = Button(
			self.encryptionFrame,
			text="Encrypt a file",
			bg="black",
			fg="white",
			font=self.FONT(12),
			command=lambda: self.encryptFile()
		)
		self.encryptFileButton.grid(row=2, column=1)
		self.decryptFileButton = Button(
			self.encryptionFrame,
			text="Decrypt a file",
			bg="black", 
			fg="white",
			font=self.FONT(12)
			command=lambda: self.decryptFile()
		)
		self.decryptFileButton.grid(row=3, column=1)