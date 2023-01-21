import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x550')
        self.resizable(0,0)
        self.title('Calculadora by Ivan Fibiger')
        self.iconbitmap('calcuchiquita.ico')
        #atributos de clase
        self.expresion = ''
        #caja de texto
        self.entrada = None
        #stringVar para obtener el valor del imput
        self.entrada_texto = tk.StringVar()
        #creamos los componentes
        self._creacion_componentes()


    #metodos de clase
    #metodo para crear componentes
    def _creacion_componentes(self):
        entrada_frame = tk.Frame(self, width=700, height=150, bg='YellowGreen')
        entrada_frame.pack(side=tk.TOP)
        #caja de texto
        entrada = tk.Entry(entrada_frame, font=('arial', 25, 'bold'),
                           textvariable=self.entrada_texto, width=26, justify=tk.RIGHT)
        entrada.grid(row=0, column=0,padx=15, pady=5,ipady=35)
        #agregamos otro frame para la parte inferior
        botones_frame = tk.Frame(self, width=500, height=300, bg='lightblue')
        botones_frame.pack()

        #primer renglon
        boton_limpiar = tk.Button(botones_frame, text='C', width=50, height=5,
                                  bd=0, bg='#eee', cursor='hand2',
                                  command=self._evento_limpiar, font=("Arial",9)).grid(row=0, column=0, columnspan=3, padx=1, pady=1)


        boton_dividir = tk.Button(botones_frame, text='/', width=13, height=3,
                                  bd=0, bg='#eee', cursor='hand2',
                                  command=lambda: self._evento_click('/'),font=("Arial",15)).grid(row=0, column=3, padx=1, pady=1)

        #segundo renglon
        boton_siete = tk.Button(botones_frame, text='7', width=16, height=5,
                                  bd=0, bg='#fff', cursor='hand2',
                                  command=lambda: self._evento_click('7')).grid(row=1, column=0, padx=1, pady=1)

        boton_ocho = tk.Button(botones_frame, text='8', width=16, height=5,
                                bd=0, bg='#fff', cursor='hand2',
                                command=lambda: self._evento_click('8')).grid(row=1, column=1, padx=1, pady=1)

        boton_nueve = tk.Button(botones_frame, text='9', width=16, height=5,
                                bd=0, bg='#fff', cursor='hand2',
                                command=lambda: self._evento_click('9')).grid(row=1, column=2, padx=1, pady=1)

        boton_multiplicar = tk.Button(botones_frame, text='*', width=13, height=3,
                                bd=0, bg='#eee', cursor='hand2',
                                command=lambda: self._evento_click('*'),font=("Arial",15)).grid(row=1, column=3, padx=1, pady=1)

        #tercer renglon
        boton_cuatro = tk.Button(botones_frame, text='4', width=16, height=5,
                                bd=0, bg='#fff', cursor='hand2',
                                command=lambda: self._evento_click('4')).grid(row=2, column=0, padx=1, pady=1)

        boton_cinco = tk.Button(botones_frame, text='5', width=16, height=5,
                               bd=0, bg='#fff', cursor='hand2',
                               command=lambda: self._evento_click('5')).grid(row=2, column=1, padx=1, pady=1)

        boton_seis = tk.Button(botones_frame, text='6', width=16, height=5,
                                bd=0, bg='#fff', cursor='hand2',
                                command=lambda: self._evento_click('6')).grid(row=2, column=2, padx=1, pady=1)

        boton_restar = tk.Button(botones_frame, text='-', width=13, height=3,
                                      bd=0, bg='#eee', cursor='hand2',
                                      command=lambda: self._evento_click('-'),font=("Arial",15)).grid(row=2, column=3, padx=1, pady=1)

        #cuarto renglon

        boton_uno = tk.Button(botones_frame, text='1', width=16, height=5,
                                 bd=0, bg='#fff', cursor='hand2',
                                 command=lambda: self._evento_click('1')).grid(row=3, column=0, padx=1, pady=1)

        boton_dos = tk.Button(botones_frame, text='2', width=16, height=5,
                                bd=0, bg='#fff', cursor='hand2',
                                command=lambda: self._evento_click('2')).grid(row=3, column=1, padx=1, pady=1)

        boton_tres = tk.Button(botones_frame, text='3', width=16, height=5,
                               bd=0, bg='#fff', cursor='hand2',
                               command=lambda: self._evento_click('3')).grid(row=3, column=2, padx=1, pady=1)

        boton_sumar = tk.Button(botones_frame, text='+', width=13, height=3,
                                 bd=0, bg='#eee', cursor='hand2',
                                 command=lambda: self._evento_click('+'),font=("Arial",15)).grid(row=3, column=3, padx=1, pady=1)


        #quinto renglon

        boton_cero = tk.Button(botones_frame, text='0', width=33, height=5,
                                 bd=0, bg='#fff', cursor='hand2',
                                 command=lambda: self._evento_click('0')).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

        boton_punto = tk.Button(botones_frame, text='.', width=10, height=3,
                                bd=0, bg='#eee', cursor='hand2',
                                command=lambda: self._evento_click('.'),font=("Arial",15)).grid(row=4, column=2, padx=1, pady=1)



        boton_igual = tk.Button(botones_frame, text='=', width=13, height=3,
                                 bd=0, bg='#eee', cursor='hand2',
                                 command=self._evento_igualdad,font=("Arial",15)).grid(row=4, column=3, padx=1, pady=1)


    def _evento_igualdad(self):
        #eval evalua la expresion de tipo str como una expresion aritmetica
        try:
            if self.expresion:
                resultado = str(eval(self.expresion))
                self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showerror('Error', f'Ocurrio un error {e}')
            self.entrada_texto.set('')
        finally:
            self.expresion = ''


    def _evento_limpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)

    def _evento_click(self, elemento):
        #concatenamos el nuevo elemento a la expresion ya existente
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)





if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()