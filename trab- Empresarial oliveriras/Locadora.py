from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para o menu inicial
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        cpf = request.form.get('cpf')
        password = request.form.get('password')

        print('cpf:', cpf, 'password:', password)
        return render_template('index.html')

    if request.method == 'GET':
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        cpf = request.form.get('cpf')
        address = request.form.get('address')
        password = request.form.get('password')
        phone = request.form.get('phone')
        email = request.form.get('email')

        return render_template('index.html')


    if request.method == 'GET':
        return render_template('register.html')


@app.route('/change', methods=['GET', 'PATCH'])
def change():

    if request.method == 'PATCH':
        cpf = request.form.get('cpf')
        password = request.method('password')

        return render_template('index.html')

    if request.method == 'GET':
        return render_template('changepassword.html')    
        
if __name__ == '__main__':
    app.run(debug=True)
con = mysql.connector.connect(host='localhost', database='empresarial_oliveiras', user='root', password='aluno')



if con.is_connected():
    db_info = con.get_server_info()
    print(">>>>Conectado ao servidor MySQL versão ", db_info)
    cursor = con.cursor()
    cursor.execute("SELECT DATABASE();")
    linha = cursor.fetchone()
    print(">>>>Conectado ao banco de dados ", linha)


cursor = con.cursor()
cursor.execute("SHOW DATABASES LIKE 'empresarial_oliveiras' ")

resultado = cursor.fetchone()

if resultado:
    print("O banco de dados já existe.")
else:
    print("O banco de dados não existe.")
    cursor.execute("CREATE DATABASE empresarial_oliveiras")

# Criar Tabela
cursor.execute("CREATE TABLE IF NOT EXISTS locadoras (codigo INT PRIMARY KEY,Nome_locadora VARCHAR(40),endereco VARCHAR(75)) ")
cursor.execute("CREATE TABLE IF NOT EXISTS Carros (CarroID INT NOT NULL,Marca VARCHAR(50) NOT NULL,Modelo VARCHAR(50) NOT NULL,Ano YEAR NOT NULL,Locadora VARCHAR(250) REFERENCES locadora(nome_locadora),Disponibilidade ENUM('disponivel', 'indisponivel') NOT NULL) ")
cursor.execute("CREATE TABLE IF NOT EXISTS cliente (codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(50) NOT NULL,CPF VARCHAR (14),endereco VARCHAR(30),telefone CHAR(15),email VARCHAR(30),senha VARCHAR(8)) ")

#Inserir registro
sql = "INSERT INTO locadoras"





'''# Menu inicial para escolher entre login, cadastro e alterar senha
def inicial():
    opcao = 0
    while opcao != 9:
        print("\n----------BEM-VINDO----------")
        print("\n[1] Efetuar Login\n[2] Cadastrar Conta\n[3] Alterar Senha\n[9] Encerrar")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            login()
        elif opcao == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            RegistrarConta()
        elif opcao == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            AlterarSenha()
        elif opcao == 9:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção inválida. Por favor, escolha uma opção válida.\n")

# Função para efetuar login
def login():
    print("\n----------LOGIN----------")
    CPF = input("Informe o CPF: ")
    senha = input("Senha: ")

    # Validando CPF e Senha
    try:
        cursor = con.cursor()
        query_login = f'SELECT * FROM cliente WHERE CPF = "{CPF}" AND senha = "{senha}"'
        cursor.execute(query_login)
        resultado = cursor.fetchone()

        if resultado:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(">>>>Login bem-sucedido!\n")
            main()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n>>>>CPF ou senha incorretos.")
            inicial()
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Erro ao efetuar login:", e)

# Função para alterar a senha da conta
def AlterarSenha():
    print("\n----------ALTERAR SENHA----------")
    CPF = input("Informe o CPF: ")
    senha = input("Senha: ")

    # Validando CPF e Senha
    try:
        cursor = con.cursor()
        query_login = f'SELECT * FROM cliente WHERE CPF = "{CPF}" AND senha = "{senha}"'
        cursor.execute(query_login)
        resultado = cursor.fetchone()

        if resultado:
            key = input("Digite a sua nova senha: ")
            cursor = con.cursor()
            queryupdate = f'UPDATE cliente SET senha = "{key}" WHERE CPF = "{CPF}"'
            cursor.execute(queryupdate)
            con.commit()
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Senha alterada com sucesso!\n")
            inicial()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n>>>>CPF ou senha incorretos.")
            inicial()
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Erro ao alterar a senha:", e)

# Função para cadastrar cliente
def RegistrarConta():
    print("\n----------CADASTRO----------")
    try:
        nome = input("Nome completo: ")
        CPF = input("CPF: ")
        endereco = input("Endereço: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        senha = input("Senha: ")

        cursor = con.cursor()
        querycreate = f'INSERT INTO cliente (nome, CPF, endereco, telefone, email, senha) VALUES ("{nome}", "{CPF}", "{endereco}", "{telefone}", "{email}", "{senha}")'
        cursor.execute(querycreate)
        con.commit()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Conta cadastrada com sucesso!\n")
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Erro ao cadastrar conta:", e)

# Função para consultar conta do cliente
def ConsultarConta():
    print("\n----------CONSULTAR CONTA----------")
    key = input("Digite seu CPF: ")
    
    try:
        cursor = con.cursor()
        queryconsulte = f'SELECT nome, CPF, endereco, telefone, email, senha FROM cliente WHERE CPF = "{key}"'
        cursor.execute(queryconsulte)
        resultado = cursor.fetchone()
        if resultado:
            nome, CPF, endereco, telefone, email, senha = resultado
            print("\n>>>>Dados do cliente:")
            print(f"Nome completo: {nome}")
            print(f"CPF: {CPF}")
            print(f"Endereço: {endereco}")
            print(f"Telefone: {telefone}")
            print(f"E-mail: {email}")
            print(f"Senha: {senha}")
            print("\n")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Cliente não localizado")
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Erro ao consultar conta:", e)

# Função para atualizar dados do cliente
def AtualizarConta():
    print("\n----------ATUALIZAR DADOS----------")
    key = input("Digite seu CPF: ")
    
    # Validando CPF
    cursor = con.cursor()
    query_login = f'SELECT * FROM cliente WHERE CPF = "{key}" '
    cursor.execute(query_login)
    resultado = cursor.fetchone()
    if resultado:
        try:
            nome = input("[Atualizando] Nome completo: ")
            endereco = input("[Atualizando] Endereço: ")
            telefone = input("[Atualizando] Telefone: ")
            email = input("[Atualizando] E-mail: ")
            senha = input("[Atualizando] Senha: ")

            # Atualizando os dados
            cursor = con.cursor()
            queryupdate = f'UPDATE cliente SET nome = "{nome}", endereco = "{endereco}", telefone = "{telefone}", email = "{email}", senha = "{senha}" WHERE CPF = "{key}"'
            cursor.execute(queryupdate)
            con.commit()
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Dados atualizados com sucesso!\n")
        except Exception as e:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Erro ao atualizar dados:", e)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n>>>>CPF incorreto.\n")
        main()

# Função para deletar conta do cliente
def DeletarConta():
    print("\n----------DELETAR CONTA----------")
    CPF = input("Informe o CPF: ")
    senha = input("Senha: ")

    # Validando CPF e Senha
    cursor = con.cursor()
    query_login = f'SELECT * FROM cliente WHERE CPF = "{CPF}" AND senha = "{senha}"'
    cursor.execute(query_login)
    resultado = cursor.fetchone()

    if resultado:
        try:
            # Deletando a conta
            cursor = con.cursor()
            querydelete = f'DELETE FROM cliente WHERE CPF = "{CPF}"'
            cursor.execute(querydelete)
            con.commit()
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Conta deletada com sucesso!\n")
        except Exception as e:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Não foi possível deletar a conta:", e)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n>>>>CPF ou senha incorretos.\n")
        main()

# Função para exibir toda as informações do database
def ExibeTodos():
    #Exibir clientes
    try:
        cursor = con.cursor()
        queryshow = f'SELECT nome, CPF, endereco, telefone, email FROM cliente'
        cursor.execute(queryshow)
        print(60*"-")
        print("Clientes na base de dados:")
        print(60*"-")
        for (nome, CPF, endereco, telefone, email) in cursor:
            print(f"Nome: {nome}\nCPF: {CPF}\nEndereço: {endereco}\nTelefone: {telefone}\nE-mail: {email}\n")
        cursor.close()
    except Exception as e:
        print("Erro ao exibir as informações dos clientes:", e)

    #Exibir Locadoras
    try:
        cursor = con.cursor()
        queryshow = f'SELECT nome_locadora, endereco FROM locadoras'
        cursor.execute(queryshow)
        print(60*"-")
        print("Locadoras da base de dados:")
        print(60*"-")
        for (nome_locadora, endereco) in cursor:
            print(f"Nome do Prédio: {nome_locadora}\nEndereço: {endereco}\n")
        cursor.close()
    except Exception as e:
        print("Erro ao exibir as informações das Locadora:", e)
        
    #Exibir Carros
    try:
        cursor = con.cursor()
        queryshow = f'SELECT CarroID, Modelo, Locadora, disponibilidade FROM Carros'
        cursor.execute(queryshow)
        print(60*"-")
        print("Carros da locadora:")
        print(60*"-")
        for ( CarroID, Modelo , Locadora, disponibilidade) in cursor:
            print(f"id do carro: {CarroID}\nModelo: {Modelo}\nLocalizada na locadora: {Locadora}\nStatus: {disponibilidade}\n")
        cursor.close()
    except Exception as e:
        print("Erro ao exibir as informações dos carros:", e)
   
# Função para checar informações de um único carro
def ChecarCarro():
    print("\n----------CONSULTAR CARROS----------")
    numero_carro = input("Informe o Modelo do carro: ")
    locadora = input("Informe qual o nome da Locadora: ")
    try:
        cursor = con.cursor()
        queryconsulte = f'SELECT CarroID, Modelo , Locadora, disponibilidade FROM Carros WHERE Modelo = "{numero_carro}" AND Locadora = "{locadora}"'
        cursor.execute(queryconsulte)
        resultado = cursor.fetchone()
        if resultado:
            CarroID, Modelo , Locadora, disponibilidade = resultado
            os.system('cls' if os.name == 'nt' else 'clear')
            print(60*"-")
            print("Informações da Carro selecionado:")
            print(60*"-")
            print("\n")
            print(f"id do carro: {CarroID}\nModelo: {Modelo}\nLocalizada na locadora: {Locadora}\nStatus: {disponibilidade}\n")
            cursor.close()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Carro não localizado")
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Erro ao exibir as informações do carro:", e)

# Função para exibir as informações todas os carros
def ExibirCarros():
    try:
        cursor = con.cursor()
        queryshow = f'SELECT CarroID, Modelo, Locadora, disponibilidade FROM Carros'
        cursor.execute(queryshow)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(60*"-")
        print("Carros da locadora:")
        print(60*"-")
        print("\n")
        for (CarroID, Modelo , Locadora, disponibilidade) in cursor:
            print(f"id do carro: {CarroID}\nModelo: {Modelo}\nLocalizada na locadora: {Locadora}\nStatus: {disponibilidade}\n")
        cursor.close()
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Erro ao exibir as informações dos carros:", e)

# Menu interativo adicional para carros
def ConsultarCarros():
    opcao = 0
    while opcao != 9:
        print("\n----------CONSULTAR CARROS ----------")
        print("\n[1] Consultar um carro \n[2] Consultar todos os carros\n[9] Sair")
        opcao = int(input("Escolha um opção: "))
        if opcao == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            ChecarCarro()
        elif opcao == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            ExibirCarros()
        elif opcao == 9:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção inválida. Por favor, escolha uma opção válida.\n")

# Menu interativo com Switch Case
def main():
    opcao = 0
    while opcao != 9:
        print("----------lOCADORA ----------")
        print("\n[1] Cadastar Conta\n[2] Consultar Conta\n[3] Atualizar Dados\n[4] Deletar Conta\n[5] Exibir todo o Banco de Dados\n[6] Consultar Carros\n[7] Alterar Senha\n[9] Sair")
        opcao = int(input("Escolha um opção: "))
        if opcao == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            RegistrarConta()
        elif opcao == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            ConsultarConta()
        elif opcao == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            AtualizarConta()
        elif opcao == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            DeletarConta()
        elif opcao == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            ExibeTodos()
        elif opcao == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            ConsultarCarros()
        elif opcao == 7:
            os.system('cls' if os.name == 'nt' else 'clear')
            AlterarSenha()
        elif opcao == 9:
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção inválida. Por favor, escolha uma opção válida.\n")
    print("\nAté logo...")'''

# Chamada para função inicial (login e cadastro)
inicial()


# Desconectando do servidor
if con.is_connected():
    cursor.close()
    con.close()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(">>>>Conexão ao MySQL foi encerrada.")