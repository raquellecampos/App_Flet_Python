from flet import *
import sqlite3

# conectando banco
conexao = sqlite3.connect('dados.db', check_same_thread=False)
cursor = conexao.cursor()

#Criar Tabela no banco de dados
def tabela_base():
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)

        '''
    )

# UserControl responsabilidade Flet
class App(UserControl):
    def __init__(self):
        super().__init__()  # inicializar a classe responsabilidade Flet
        self.todos_os_dados = Column(auto_scroll=True)
        self.adcionar_dados = TextField(label='Nome do dado de entrada: ')
        self.editar_dados = TextField(label='Editar')

    # função para abrir a ação
    def abrir_acoes(self, e):
        pass


   # READ - Mostrar todos os daods do banco de dados(select)
    def renderizar_todos(self):
        cursor.execute('SELECT * FROM clientes')
        conexao.commit()

        meus_dados = cursor.fetchall()

        for dado in meus_dados:
            self.todos_os_dados.controls.append(
                ListTile(
                    subtitle=Text(dado[0]),
                    title=Text(dado[1]),
                    on_click=self.abrir_acoes
                )
            )

    # Criar um dado dentro do banco de dados (CREATE)
    def adicionar_novo_dado(self, e):
        cursor.execute('INSERT INTO clientes (nome) VALUES (?)', [self.adcionar_dados.value])
        self.todos_os_dados.controls.clear()
        self.renderizar_todos()
        self.page.update()


#Definir uma função build
    def build(self):
        return Column([
            # Visualização da aplicação
            Text("CRUD com sqlite", text_align='center', size=20, weight='bold'),
            self.adcionar_dados,
            ElevatedButton(
            'Adicionar',
            on_click=self.adicionar_novo_dado,
            ),
            self.todos_os_dados
        ])    

# no terminal digitar: flet - r e o nome do arquivo para rodar a aplicação nesse caso app.py
def main(page:Page):
    minha_aplicação = App()
    page.add(
        minha_aplicação
    )

app(target=main)