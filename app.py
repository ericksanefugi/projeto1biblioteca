from flask import Flask
import mysql.connector
from config import DB_CONFIG


app = Flask(__name__)


def conectar():
   return mysql.connector.connect(**DB_CONFIG)


@app.route("/")
def index():
   return """
   <h1>Sistema Biblioteca Escolar</h1>
   <p>Projeto iniciado com Python, Flask e MySQL.</p>
   <ul>
       <li><a href="/alunos">Ver alunos cadastrados</a></li>
       <li><a href="/livros">Ver livros cadastrados</a></li>
       <li><a href="/bibliotecarios">Ver bibliotecários cadastrados</a></li>
       <li><a href="/professores">Ver professores cadastrados</a></li>
   </ul>
   """


@app.route("/alunos")
def listar_alunos():
   try:
       conexao = conectar()
       cursor = conexao.cursor(dictionary=True)
       cursor.execute("SELECT * FROM alunos")
       alunos = cursor.fetchall()
       cursor.close()
       conexao.close()


       html = """
       <h1>Alunos Cadastrados</h1>
       <a href="/">Voltar ao Menu</a>
       <br><br>
       <table border="1" cellpadding="8">
       <tr>
           <th>ID</th>
           <th>Nome</th>
           <th>Turma</th>
           <th>E-mail</th>
       </tr>
       """
       for aluno in alunos:
           html += f"""
           <tr>
               <td>{aluno['id_aluno']}</td>
               <td>{aluno['nome']}</td>
               <td>{aluno['turma']}</td>
               <td>{aluno['email']}</td>
           </tr>
           """
       html += "</table>"
       return html
   except Exception as erro:
       return f"Erro ao listar alunos: {erro}"


@app.route("/livros")
def listar_livros():
   try:
       conexao = conectar()
       cursor = conexao.cursor(dictionary=True)
       cursor.execute("SELECT * FROM livros")
       livros = cursor.fetchall()
       cursor.close()
       conexao.close()


       html = """
       <h1>Livros Cadastrados</h1>
       <a href="/">Voltar ao Menu</a>
       <br><br>
       <table border="1" cellpadding="8">
       <tr>
           <th>ID</th>
           <th>Título</th>
           <th>Autor</th>
           <th>Editora</th>
           <th>Ano</th>
           <th>Quantidade</th>
       </tr>
       """
       for livro in livros:
           html += f"""
           <tr>
               <td>{livro['id_livro']}</td>
               <td>{livro['titulo']}</td>
               <td>{livro['autor']}</td>
               <td>{livro['editora']}</td>
               <td>{livro['ano_publicacao']}</td>
               <td>{livro['quantidade']}</td>
           </tr>
           """
       html += "</table>"
       return html
   except Exception as erro:
       return f"Erro ao listar livros: {erro}"


@app.route("/bibliotecarios")
def listar_bibliotecarios():
   try:
       conexao = conectar()
       cursor = conexao.cursor(dictionary=True)
       cursor.execute("SELECT * FROM bibliotecario")
       bibliotecarios = cursor.fetchall()
       cursor.close()
       conexao.close()


       html = """
       <h1>Bibliotecários Cadastrados</h1>
       <a href="/">Voltar ao Menu</a>
       <br><br>
       <table border="1" cellpadding="8">
       <tr>
           <th>ID</th>
           <th>Nome</th>
           <th>Telefone</th>
           <th>E-mail</th>
       </tr>
       """
       for bib in bibliotecarios:
           html += f"""
           <tr>
               <td>{bib['id_bibliotecario']}</td>
               <td>{bib['nome']}</td>
               <td>{bib['telefone']}</td>
               <td>{bib['email']}</td>
           </tr>
           """
       html += "</table>"
       return html
   except Exception as erro:
       return f"Erro ao listar bibliotecários: {erro}"


@app.route("/professores")
def listar_professores():
   try:
       conexao = conectar()
       cursor = conexao.cursor(dictionary=True)
       cursor.execute("SELECT * FROM professor")
       professores = cursor.fetchall()
       cursor.close()
       conexao.close()


       html = """
       <h1>Professores Cadastrados</h1>
       <a href="/">Voltar ao Menu</a>
       <br><br>
       <table border="1" cellpadding="8">
       <tr>
           <th>ID</th>
           <th>Nome</th>
           <th>Telefone</th>
           <th>E-mail</th>
       </tr>
       """
       for prof in professores:
           html += f"""
           <tr>
               <td>{prof['id_professor']}</td>
               <td>{prof['nome']}</td>
               <td>{prof['telefone']}</td>
               <td>{prof['email']}</td>
           </tr>
           """
       html += "</table>"
       return html
   except Exception as erro:
       return f"Erro ao listar professores: {erro}"


if __name__ == "__main__":
   app.run(debug=True)
