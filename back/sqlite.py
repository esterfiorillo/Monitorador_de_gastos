import sqlite3
import json

def creat_db():

	banco = sqlite3.connect('my_test.db')
	cursor = banco.cursor()
	#cursor.execute('CREATE TABLE TRANSACOES (time_stamp integer, descricao text, valor integer, categoria text)')
	banco.commit()

	return banco

def insert_db(banco, time_stamp, descricao, valor, categoria):

	cursor = banco.cursor()
	cursor.execute('INSERT INTO TRANSACOES VALUES (?, ?, ?, ?)', (time_stamp, descricao, valor, categoria))
	banco.commit()

def return_transacoes(banco):
	cursor = banco.cursor()
	cursor.execute('SELECT * FROM TRANSACOES')
	rows = cursor.fetchall()
	return rows


def write_json(banco):
	linhas = return_transacoes(banco)

	data = {}
	data['transacoes'] = []
	for i in linhas:
		data['transacoes'].append({'time_stamp': i[0], 'descricao': i[1], 'valor' : i[2], 'categoria' : i[3]})

	with open('data.json', 'w') as f:
		json.dump(data, f)


def __main__():
	banco = creat_db()
	insert_db(banco, 12334, 'pizza', 12, 'alimentacao')
	insert_db(banco, 3333, 'festa', 45, 'entrenimento')
	print(return_transacoes(banco))
	write_json(banco)

__main__()

