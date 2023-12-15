from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector

app = Flask(__name__)

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



# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para o menu inicial (LOGIN)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('password')

        cursor = con.cursor()
        query_login = f'SELECT * FROM cliente WHERE login = "{email}" AND senha = "{senha}"'
        cursor.execute(query_login)
        resultado = cursor.fetchone()

        if resultado:
            return redirect("/main")
        else:
            return redirect("/login")

    if request.method == 'GET':
        return render_template('login.html')
    


#Rota Inicial (Registro)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('password')

        cursor = con.cursor()
        querycreate = f'INSERT INTO cliente (login, senha) VALUES ("{email}", "{senha}")'
        cursor.execute(querycreate)
        con.commit()
        return render_template('index.html')


    if request.method == 'GET':
        return render_template('register.html')

#Rota Inicial (Mudar Senha)
@app.route('/change', methods=['GET', 'PATCH'])
def change():

    if request.method == 'PATCH':
        email = request.form.get('email')
        senha = request.method('password')
        cursor = con.cursor()
        query_login = f'SELECT * FROM cliente WHERE CPF = "{email}" AND senha = "{senha}"'
        cursor.execute(query_login)
        resultado = cursor.fetchone()

        if resultado:
            key = input("Digite a sua nova senha: ")
            cursor = con.cursor()
            queryupdate = f'UPDATE cliente SET senha = "{key}" WHERE CPF = "{email}"'
            cursor.execute(queryupdate)
            con.commit()
            return render_template('index.html')
        else:
            return render_template('changepassword.html')

    if request.method == 'GET':
        return render_template('changepassword.html')    
        

@app.route("/main", methods=["GET"])
def main():
    try:
        cursor = con.cursor()
        cursor.execute('SELECT login FROM cliente')
        my_users = cursor.fetchall()

        users = list()
        for user in my_users:
            users.append(
                {
                    'email' : user[0]
                }
            )



        cursor.close()
    except Exception as e:
        print("Erro ao exibir as informações dos clientes:", e)
        
    #Exibir Locadoras
    try:
        cursor = con.cursor()
        cursor.execute('SELECT nome_locadora FROM locadoras')

        my_locs = cursor.fetchall()

        locadoras = list()
        for locadora in my_locs:
            locadoras.append(
                {
                    'locadora': locadora[0]
                }
            )

        cursor.close()
       # users = result
    except Exception as e:
        print("Erro ao exibir as informações das Locadora:", e)
        
    #Exibir Carros
    try:
        cursor = con.cursor()
        cursor.execute('SELECT CarroID, Modelo, Marca, Locadora FROM Carros')

        my_cars = cursor.fetchall()

        carros = list()
        for carro in my_cars:
            carros.append({
                    'id': str(carro[0]),
                    'modelo': carro[1],
                    'marca': carro[2],
                    'locadora': carro[3]
            })
        cursor.close()
        #users = result
    except Exception as e:
        print("Erro ao exibir as informações dos carros:", e)
    try: 
        cursor = con.cursor()
        cursor.execute('SELECT COUNT(*) FROM Carros')

        my_total = cursor.fetchone()


        total = my_total[0]

        cursor.close()
    except Exception as e:
        print("Erro ao exibir as informações do total de carros:", e)

    return render_template("main.html", results = carros, total = total)


@app.route("/cadastrar", methods=["POST","GET"])
def cadastrar():
    locadora = request.form["locadora"]
    marca = request.form["marca"]
    modelo = request.form["modelo"]
    
    cursor = con.cursor()
    queryinsert = f'INSERT INTO Carros (marca, modelo, locadora) VALUES ("{marca}", "{modelo}", "{locadora}")'
    cursor.execute(queryinsert)
    con.commit()
    return render_template('main.html')

@app.route("/atualizar/<string:id>", methods =['GET'])
def atualizar(id):
       try: 
            cursor = con.cursor()
            cursor.execute('SELECT * FROM Carros WHERE CarroID = %s', (id,))
            my_car = cursor.fetchall()
            carros = list()
            for carro in my_car:
                carros.append({
                    'id': str(carro[0]),
                    'modelo': carro[2],
                    'marca': carro[1],
                    'locadora': carro[4]
                })
            cursor.close()
            return render_template('update.html', carro = carros) 
       except Exception as e:
            print("Erro ao atualizar o carro:", e)
            return redirect('main')   


@app.route('/update/<string:id>', methods=["POST"])    
def update(id):
    try:
        marca = request.form["marca"]
        modelo = request.form["modelo"]
        locadora = request.form["locadora"]
        cursor = con.cursor()
        cursor.execute("""
               UPDATE Carros
               SET Marca=%s, Modelo=%s, Locadora=%s
               WHERE CarroID=%s
            """, (marca, modelo, locadora, id,))
        con.commit()
        return redirect(url_for('main'))    
    except Exception as e:
            print("Erro ao atualizar o carro:", e)
            return redirect(url_for('main')) 

@app.route("/deletar/<string:id>", methods=['GET'])
def deletar(id):
    try:
        cursor = con.cursor()
        cursor.execute("DELETE FROM Carros WHERE CarroID=%s", (id,))
        con.commit()
        return redirect(url_for('main'))
    except Exception as e:
        print("Erro ao deletar: ", e)
    return redirect("main")
if __name__=="__main__":
    app.run(debug=True)


# Desconectando do servidor
if con.is_connected():
    cursor.close()
    con.close()
    print(">>>>Conexão ao MySQL foi encerrada.")