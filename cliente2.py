# COLETAR DIRETORIO DE VARIOS ARQUIVOS

from tkinter import *
import tkinter.filedialog as fd

win = Tk()
win.withdraw()
file = fd.askopenfilenames(title='Selecione o(s) arquivo(s)...')
print(win.splitlist(file))
