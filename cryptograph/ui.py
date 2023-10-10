from tkinter import Tk
from tkinter import Label
from tkinter import Canvas
from tkinter import Entry
from tkinter import Button
from tkinter import Frame

from abc import ABC 
from abc import abstractstaticmethod

from typing import Any

from cryptograph import algorithms

class Cryptograph(Tk):

	FONT = lambda size: ("OCR A Extended", size)

	class OperationWindow(Tk):
		def __init__(self, operation: str, inclKeying: bool=True, **kwargs: dict[str, Any]) -> None:
			for key in kwargs.keys():
				setattr(self, key, kwargs[key])

			Tk.__init__(self)
			self.title("Cryptograph: " + operation)
			self.config(bg="black")

			self.targetFile = None
			self.keyFile = None

			self.titleLabel = Label(
				self,
				text=operation,
				bg="black",
				fg="white",
				font=Cryptograph.FONT(16)
			)
			self.titleLabel.grid(row=1, column=1, columnspan=2)

			if inclKeying:
				self.keyFileLabel = Label(
					self,
					text="Key file",
					bg="black",
					fg="white",
					font=Cryptograph.FONT(12)
				)
				self.keyFileLabel.grid(row=2, column=1)
				self.targetFileLabel = Label(
					self,
					text="Target file",
					bg="black",
					fg="white",
					font=Cryptograph.FONT(12)
				)
				
			self.targetFileLabel.grid(row=2, column=2)
			self.keyFileSelect = Button(
				self,
				text="None selected",
				bg="black",
				fg="white",
				font=Cryptograph.FONT(12),
				command=self.findKeyFile
			)
			self.keyFileSelect.grid(row=3, column=1)
			self.targetFileSelect = Button(
				self,
				text="None selected",
				bg="black",
				fg="white",
				font=Cryptograph.FONT(12),
				command=self.findTargetFile
			)
			self.targetFileSelect.grid(row=3, column=2)
			self.runButton = Button(
				self,
				text="Go",
				bg="black",
				fg="white",
				font=Cryptograph.FONT(12),
				command=lambda: self.run(self.targetFile, self.keyFile)
			)

		@abstractstaticmethod
		def run(targetFile: str, keyFile: str) -> None:
			pass

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

		self.algorithmFrame = Frame(self, bg="black")
		self.algorithmFrame.grid(row=3, column=1, columspan=2)

		self.