import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#Exercício 1:
#cursor.execute('CREATE TABLE alunos(id int, nome varchar(100), idade int, curso varchar(250));')

#Exercício 2:
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Julia", 27, "Sistemas de Informação")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Luana", 30, "Engenharia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Bruna", 18, "Engenharia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Gabi", 25, "ADS")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Camila", 24, "Ciência da Computação")')

#Exercício 3:
#a)
#dados =  cursor.execute('SELECT * FROM alunos')
#for alunos in dados:
#    print(alunos)

#b)
#dados =  cursor.execute('select nome, idade from alunos where idade > 20')
#for alunos in dados:
#    print(alunos)

#c)
#dados = cursor.execute("SELECT * FROM alunos WHERE curso = 'Engenharia' ORDER BY nome")
#for alunos in dados:
#    print(alunos)

#d)
#dados = cursor.execute("SELECT COUNT(*) FROM alunos")
#for alunos in dados:
#    print(alunos)

#Exercício 4:
#a)
#cursor.execute('update alunos set idade = 40 where id = 5')

#b)
#cursor.execute('DELETE from alunos where id = 2')

#Exercício 5:
#cursor.execute('create table clientes (id int, nome varchar (150), idade int, saldo float)')

#cursor.execute('insert into clientes (id, nome, idade, saldo) values (1, "Joana", 38, 10.000 )')
#cursor.execute('insert into clientes (id, nome, idade, saldo) values (2, "Bruna", 29, 8000 )')
#cursor.execute('insert into clientes (id, nome, idade, saldo) values (3, "Maria", 55, 7542 )')

#Exercício 6:
#a)
#dados = cursor.execute('select nome, idade from clientes where idade>30')
#for clientes in dados:
#    print(clientes)

#b)
#dados = cursor.execute("SELECT AVG(saldo) FROM clientes")
#for clientes in dados:
#    print("A média do saldo dos clientes é:", clientes)

#cursor.execute("SELECT * FROM clientes ORDER BY saldo DESC LIMIT 1")
#cliente_maior_saldo = cursor.fetchone()

#print("Cliente com o maior saldo:")
#print("ID:", cliente_maior_saldo[0])
#print("Nome:", cliente_maior_saldo[1])
#print("Idade:", cliente_maior_saldo[2])
#print("Saldo:", cliente_maior_saldo[3])

#d)

#cursor.execute("SELECT COUNT(*) FROM clientes WHERE saldo > 1000")
#clientes_saldo_acima_de_1000 = cursor.fetchone()[0]
#print("Quantos clientes tem saldo acima de 1000:", clientes_saldo_acima_de_1000)

#Exercício 7:
#a)
#cursor.execute('update clientes set saldo = 12000 where id = 2')

#b)
#cursor.execute('DELETE from clientes where id = 1')

#Exercício 8:

cursor.execute('''CREATE TABLE compras (
                    id int,
                    cliente_id int,
                    produto varchar(50),
                    valor REAL,
                    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
                )''')

compras = [
    (1, 'Produto A', 50.0),
    (2, 'Produto B', 100.0),
    (3, 'Produto C', 150.0),
    (1, 'Produto D', 200.0),
    (3, 'Produto E', 80.0)
]

cursor.executemany('INSERT INTO compras (cliente_id, produto, valor) VALUES (?, ?, ?)', compras)

conexao.commit()

cursor.execute('''SELECT c.nome, co.produto, co.valor 
                  FROM clientes c 
                  INNER JOIN compras co ON c.id = co.cliente_id''')

print("Nome do Cliente | Produto | Valor da Compra")
for row in cursor.fetchall():
    print(row[0], "|", row[1], "|", row[2])

conexao.commit()
conexao.close