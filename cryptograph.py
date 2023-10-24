from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button

from hashlib import sha3_512

from typing import Union

from os.path import exists

class CommonCipher:
	def __init__(self, key: Union[str, bytes]) -> None:
		if type(key) == str:
			key = sha3_512(key.encode("utf-8")).digest()
		self.key = key

	def encrypt(self, data: bytes) -> bytes:
		transient = self.key
		keystream = b""
		while len(keystream) < len(data):
			keystream += bytes([a ^ b for a, b in zip(self.key, sha3_512(transient).digest())])
			transient = sha3_512(transient).digest()
		if len(keystream) > len(data):
			keystream = keystream[:len(data)]
		return bytes([a ^ b for a, b in zip(data, keystream)])

	def decrypt(self, data: bytes) -> bytes:
		transient = self.key
		keystream = b""
		while len(keystream) < len(data):
			keystream += bytes([a ^ b for a, b in zip(self.key, sha3_512(transient).digest())])
			transient = sha3_512(transient).digest()
		if len(keystream) > len(data):
			keystream = keystream[:len(data)]
		return bytes([a ^ b for a, b in zip(data, keystream)])

class Cryptograph(Tk):

	class Encryptor(Tk):
		def __init__(self) -> None:
			Tk.__init__(self)
			self.title("Cryptograph - Encryption")

			self.explanation1 = Label(self, text="Encryption is used to protect data, both while it is being sent and when it is in a file.")
			self.explanation1.grid(row=1, column=1, columnspan=2)
			self.explanation2 = Label(self, text="Enter a filename and a key, and the app will encrypt the file using its encryption algorithm.")
			self.explanation2.grid(row=2, column=1, columnspan=2)
			self.explanation3 = Label(self, text="You will need the key to decrypt the file later so keep track of it!")
			self.explanation3.grid(row=3, column=1, columnspan=2)
			self.explanation4 = Label(self, text="However, anyone with the key can decrypt the file, so make sure not to share it with anyone.")
			self.explanation4.grid(row=4, column=1, columnspan=2)

			self.keyInputLabel = Label(self, text="Input any text as a key")
			self.keyInputLabel.grid(row=5, column=1)
			self.keyInput = Entry(self)
			self.keyInput.grid(row=5, column=2)

			self.fileInputLabel = Label(self, text="Input a file name")
			self.fileInputLabel.grid(row=6, column=1)
			self.fileInput = Entry(self)
			self.fileInput.grid(row=6, column=2)

			self.runButton = Button(self, text="Encrypt", command=lambda: self.run())

		def run(self) -> None:
			k = self.keyInput.get()
			f = self.fileInput.get()
			if not exists(f):
				self.destroy()
				return
			with open(f, "rb") as tf:
				plaintext = tf.read()
			cipher = CommonCipher(k)
			ciphertext = cipher.encrypt(plaintext)
			with open(f, "wb") as tf:
				tf.write(ciphertext)
			self.destroy()

	class Decryptor(Tk):
		def __init__(self) -> None:
			Tk.__init__(self)
			self.title("Cryptograph - Encryption")

			self.explanation1 = Label(self, text="Decryption is used to access encrypted data so that it can be used again.")
			self.explanation1.grid(row=1, column=1, columnspan=2)
			self.explanation2 = Label(self, text="Enter a filename and a key, and the app will decrypt the file using its encryption algorithm.")
			self.explanation2.grid(row=2, column=1, columnspan=2)
			self.explanation3 = Label(self, text="You must use the same key you used to encrypt the file to decrypt it.")
			self.explanation3.grid(row=3, column=1, columnspan=2)
			self.explanation4 = Label(self, text="Using another key might result in corrupting the file, so be careful!")
			self.explanation4.grid(row=4, column=1, columnspan=2)

			self.keyInputLabel = Label(self, text="Input any text as a key")
			self.keyInputLabel.grid(row=5, column=1)
			self.keyInput = Entry(self)
			self.keyInput.grid(row=5, column=2)

			self.fileInputLabel = Label(self, text="Input a file name")
			self.fileInputLabel.grid(row=6, column=1)
			self.fileInput = Entry(self)
			self.fileInput.grid(row=6, column=2)

			self.runButton = Button(self, text="Decrypt", command=lambda: self.run())

		def run(self) -> None:
			k = self.keyInput.get()
			f = self.fileInput.get()
			if not exists(f):
				self.destroy()
				return
			with open(f, "rb") as tf:
				ciphertext = tf.read()
			cipher = CommonCipher(k)
			plaintext = cipher.decrypt(plaintext)
			with open(f, "wb") as tf:
				tf.write(plaintext)
			self.destroy()

	def __init__(self) -> None:
		Tk.__init__(self)
		self.title("Cryptograph")

		self.title = Label(self, text="Cryptograph")
		self.title.grid(row=1, column=1)

		self.encryptButton = Button(self, text="Encrypt a file", command=lambda: self.encryptAFile())
		self.encryptButton.grid(row=2, column=1)

		self.decryptButton = Button(self, text="Decrypt a file", command=lambda: self.decryptAFile())
		self.decryptButton.grid(row=3, column=1)

	def encryptAFile(self) -> None:
		self.Encryptor().mainloop()

	def decryptAFile(self) -> None:
		self.Decryptor().mainloop()

if __name__ == "__main__":
	Cryptograph().mainloop()
