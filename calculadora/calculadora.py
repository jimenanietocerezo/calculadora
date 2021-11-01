
from PyQt5 import QtCore, uic, QtWidgets
import sys, math
import locale 
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )


#vinculamos archivo ui
archivo = uic.loadUiType("calculadora.ui")[0]

        #reducimos a un solo operador
def num(self,s):
    self.calculo.insertPlainText(s)
    

            


def operador(self,op):
    div = self.calculo.toPlainText()
    if(validarExpresion(div)):
            nuevo = div + op
            pantalla(self,nuevo)  

def pantalla(self,a):
    self.calculo.clear()
    self.calculo.insertPlainText(a)



def validarExpresion(div):
    ultimo = div[len(div)-1]
    simbolos = "+-*/."
    encontro = True
    for i in range(len(simbolos)):
        if(simbolos[i] == ultimo):
         encontro = False
        break
    return encontro  

def calcular (self,div):
    if (len(div)>2):
        resultado = eval(str(div))
        pantalla(self,str(resultado))
    else:
        pantalla(self,"ingrese una expresión para calcular: ")
class MiVentana(QtWidgets.QMainWindow, archivo):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        #Listeners de Eventos de los botones de los números
        self.boton1.clicked.connect(self.click_1)
        self.boton2.clicked.connect(self.click_2)
        self.boton3.clicked.connect(self.click_3)
        self.boton4.clicked.connect(self.click_4)
        self.boton5.clicked.connect(self.click_5)
        self.boton6.clicked.connect(self.click_6)
        self.boton7.clicked.connect(self.click_7)
        self.boton8.clicked.connect(self.click_8)
        self.boton9.clicked.connect(self.click_9)
        self.boton0.clicked.connect(self.click_0)
        self.coma.clicked.connect(self.click_bcoma)
        #Listeners de Eventos de los botones de las operaciones
        self.suma.clicked.connect(self.sumar)
        self.resta.clicked.connect(self.restar)
        self.igual.clicked.connect(self.resultado)
        self.div.clicked.connect(self.division)
        self.producto.clicked.connect(self.multiplicacion)
        self.potencia.clicked.connect(self.potencia2)
        self.raiz.clicked.connect(self.raiz2)
        self.borrarop.clicked.connect(self.borrartodo)
        self.btdes.clicked.connect(self.borraruno)

        _translate = QtCore.QCoreApplication.translate
        self.boton0.setShortcut(_translate("MiVentana", "0"))
        self.boton1.setShortcut(_translate("MiVentana", "1"))
        self.boton2.setShortcut(_translate("MiVentana", "2"))
        self.boton3.setShortcut(_translate("MiVentana", "3"))
        self.boton4.setShortcut(_translate("MiVentana", "4"))
        self.boton5.setShortcut(_translate("MiVentana", "5"))
        self.boton6.setShortcut(_translate("MiVentana", "6"))
        self.boton7.setShortcut(_translate("MiVentana", "7"))
        self.boton8.setShortcut(_translate("MiVentana", "8"))
        self.boton9.setShortcut(_translate("MiVentana", "9"))
        self.coma.setShortcut(_translate("MiVentana", ","))
        self.suma.setShortcut(_translate("MiVentana", "+"))
        self.resta.setShortcut(_translate("MiVentana", "-"))
        self.igual.setShortcut(_translate("MiVentana", "Enter"))
        self.div.setShortcut(_translate("MiVentana", "/"))
        self.producto.setShortcut(_translate("MiVentana", "*"))
        self.btdes.setShortcut(_translate("MiVentana", "delete"))

    def borraruno(self):
       p = self.calculo.toPlainText()
       pa = ""
       for i in range(len(p)):
          if (i == (len(p)-1)):
           pa += ""
          else:
            pa += p[i]
          pantalla(self,str(pa))

    def borrartodo(self):
        self.calculo.clear()

    def click_bcoma(self):
        return operador(self,',')

    def sumar(self):
        return operador(self,'+')
    
    def restar(self):
        return operador(self,'-')
        
    def division(self):
        return operador(self,'/')

    def multiplicacion(self):
         return operador(self,'*')

        

    def potencia2(self):
        p = self.calculo.toPlainText()
        r = pow(float(p),2)
        pantalla(self,str(r))
        
    
    def raiz2(self):
        p = self.calculo.toPlainText()
        r = math.sqrt(float(p))
        pantalla(self,str(r))

             
    
    
    def resultado(self):
        div = self.calculo.toPlainText()
        calcular(self,div)
    
    
    


    #Eventos de asignación de valores al label
    def click_1(self):
        return num(self,"1")

    def click_2(self): 
        return num(self,"2")
    
    def click_3(self): 
        return num(self,"3")
    
    def click_4(self): 
        return num(self,"4")
    
    def click_5(self): 
        return num(self,"5")
    
    def click_6(self): 
        return num(self,"6")
    
    def click_7(self): 
        return num(self,"7")
    
    def click_8(self): 
        return num(self,"8")
    
    def click_9(self): 
        return num(self,"9")
    
    def click_0(self): 
        return num(self,"0")




        

app = QtWidgets.QApplication(sys.argv)
win = MiVentana()
win.show()
app.exec_()