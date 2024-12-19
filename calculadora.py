# Importar Módulos
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit
from PyQt5.QtGui import QFont

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.resize(350, 400)
        
        self.caixa_texto = QLineEdit()
        self.caixa_texto.setFont(QFont('Helvetica', 32))

        self.lista_botoes = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+'
        ]
        self.grid = QGridLayout()
        row = col = 0
        for texto_botao in self.lista_botoes:
            botao = QPushButton(texto_botao)
            botao.clicked.connect(self.clicar_botao)
            botao.setStyleSheet('QPushButton {font: 25px Comic Sans MS; padding: 10px; color: #1d0d35;}')
            self.grid.addWidget(botao,row,col)
            col += 1
            if col > 3:
                row += 1
                col = 0
            if row > 3:
                break

        self.limpar = QPushButton('C')
        self.deletar = QPushButton('<')

        # Criar todo o desing
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.caixa_texto)
        master_layout.addLayout(self.grid)

        linha_de_botoes = QHBoxLayout()
        linha_de_botoes.addWidget(self.limpar)
        linha_de_botoes.addWidget(self.deletar)
        self.limpar.clicked.connect(self.clicar_botao)
        self.deletar.clicked.connect(self.clicar_botao)
        self.limpar.setStyleSheet('QPushButton {font: 25px Comic Sans MS; padding: 10px; color: #1d0d35;}')
        self.deletar.setStyleSheet('QPushButton {font: 25px Comic Sans MS; padding: 10px; color: #1d0d35;}')

        master_layout.addLayout(linha_de_botoes)
        master_layout.setContentsMargins(25,25,25,25)

        self.setLayout(master_layout)

    # Eventos
    def clicar_botao(self):
        botao = app.sender()
        texto = botao.text()
        
        if texto == '=':
            simbolo = self.caixa_texto.text()
            try:
                res = eval(simbolo)
                self.caixa_texto.setText(str(res))
            except Exception as e:
                print("Error", e)
                self.caixa_texto.setText('ERRO')
        elif texto == 'C':
            self.caixa_texto.clear()
        elif texto == '<':
            valor_atual = self.caixa_texto.text()
            self.caixa_texto.setText(valor_atual[:-1])
        else:
            valor_atual = self.caixa_texto.text()
            self.caixa_texto.setText(valor_atual + texto)

    # Criar todos os objetos
    

# Mostrar/rodar app
app = QApplication([])
main_window = Calculadora()
main_window.setStyleSheet('QWidget {background-color: #c6b7db}')
main_window.show()
app.exec_()
