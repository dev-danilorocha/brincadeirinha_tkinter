from tkinter import Tk, Label, Button

janelinha = Tk()
janelinha.title('Minha janelinha')
janelinha.geometry('400x350')
janelinha.resizable(width=None,height=None)
janelinha['bg'] = 'black'

def funcaosinha():
    labelsinha['text'] = 'Segue a gente no \nInstagram!\n@dev.junin'

labelsinha = Label(janelinha, bg='black', text='', font=('Verdana' , 25, 'bold'), foreground='white')
labelsinha.place(x=20,y=20, width=360, height=150)

botaosinho = Button(janelinha, text='Aperta aqui, vai!', font=('Verdana' , 20, 'bold'), command=funcaosinha)
botaosinho.place(x=50, y=200, width=300, height=100)

janelinha.mainloop()