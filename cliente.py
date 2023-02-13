# COLETAR DIRETORIO DE APENAS UM ARQUIVO

from tkinter import filedialog as fd

filename = fd.askopenfilename(title='Selecione o arquivo', )
print(filename)
