import sqlite3
import json

def creat_db():

	banco = sqlite3.connect('my_test.db')
	cursor = banco.cursor()
	cursor.execute('CREATE TABLE IF NOT EXISTS TRANSACOES (idx integer, time_stamp integer, descricao text, valor integer, categoria text)')
	banco.commit()

	return banco

def insert_db(banco, idx, time_stamp, descricao, valor, categoria):

	cursor = banco.cursor()
	cursor.execute('INSERT INTO TRANSACOES VALUES (?, ?, ?, ?, ?)', (idx, time_stamp, descricao, valor, categoria))
	banco.commit()


def delete_db (banco, idx):
	cursor = banco.cursor()
	cursor.execute('DELETE from TRANSACOES where idx = ?', (idx,))
	banco.commit()


def update_db (banco, idx, time_stamp, descricao, valor, categoria):
	cursor = banco.cursor()
	cursor.execute('UPDATE TRANSACOES set time_stamp = ? where idx = ?', (time_stamp, idx))
	cursor.execute('UPDATE TRANSACOES set descricao = ? where idx = ?', (descricao, idx))
	cursor.execute('UPDATE TRANSACOES set valor = ? where idx = ?', (valor, idx))
	cursor.execute('UPDATE TRANSACOES set categoria = ? where idx = ?', (categoria, idx))
	banco.commit()


def return_transacoes(banco):
	cursor = banco.cursor()
	cursor.execute('SELECT * FROM TRANSACOES')
	rows = cursor.fetchall()
	return rows


def __main__():
	banco = creat_db()
	#insert_db(banco, 0, 12334, 'pizza', 12, 'alimentacao')
	#insert_db(banco, 1, 3333, 'festa', 45, 'entrenimento')
	#delete_db(banco, 1)
	#update_db(banco, 0, 12334, 'pizza', 15, 'alimentacao')
	print(return_transacoes(banco))

__main__()

