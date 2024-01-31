from flask import Flask, request, render_template,send_file,session,redirect,json , jsonify # Importa a biblioteca
import sqlite3
import time
import sqlite3
from waitress import serve
import pymysql
import credenciais
from datetime import date
import excel
import base64
# -*- coding: utf-8 -*-
import requests
import json
import base64
Host=''
User=''
Password=''
Db=''
Charset=''
Port=0
Host,User,Password,Db,Charset,Port=credenciais.credencialbanco()
db1 = pymysql.connect(host=Host, user=User, password=Password, db=Db, charset=Charset,port=Port)

cursor = db1.cursor()
#colocando as tabelas

sql=''' 
CREATE TABLE IF NOT EXISTS servicos_motor(item INT PRIMARY KEY AUTO_INCREMENT ,
potencia_cv varchar (6),
corrente varchar(10),
disjuntor_motor varchar(50),
tipo varchar(20),
suporte_conexao varchar(50),
contatora varchar(100),
contato_auxiliar_frontal varchar(200),
conector_saque varchar (50), 
seccionador_fusivel varchar (100),
soft_starter varchar (50) ,
contatora_de_comando varchar(50))

'''
cursor.execute(sql)

db1.commit()
db1.close()
from datetime import date
import json


app = Flask(__name__) # Inicializa a aplicação

import os
app.secret_key = "senha_secreta"
import webbrowser


@app.route('/download', methods=['GET','POST']) # Nova rota
def download():
    return send_file('relacao.xlsx')
@app.route('/inserir', methods=['POST']) # Nova rota
def inserir():
    senha=request.headers['Authentication']
    if senha!='Bearer 57027689-5':
        print("senha incorreta")
        return jsonify("senha incorreta")
    
    index=request.form['id']
    index=int(index)
    cv=request.form['potencia_cv']
    corrente=request.form['corrente']
    disjuntor_motor=request.form['disjuntor_motor']
    tipo=request.form['tipo']
    suporte_de_conexao=request.form['suporte_de_conexao']
    contatora=request.form['contatora']
    contato_auxiliar_frontal=request.form['contato_auxiliar_frontal']
    conector_saque=request.form['conector_saque']
    seccionador_fusivel=request.form['seccionador_fusivel']
    soft_starter=request.form['soft_starter']
    contatora_de_comando=request.form['contatora_de_comando']
    senha_mudanca=request.form['senha']
    senha_normal=''
    with open('senha.txt','r') as t:
        senha_normal=t.read()
        senha_normal=str(senha_normal)
    print("senhas:",senha_mudanca,"senha:",senha_normal)
    if senha_mudanca!=senha_normal:
        return jsonify("senha incorreta,por favor insira a senha correta para mudar os valores")
    if senha_mudanca==senha_normal:
        
        Host,User,Password,Db,Charser,Port=credenciais.credencialbanco()
        db1 = pymysql.connect(host=Host, user=User, password=Password, db=Db, charset=Charset,port=Port)
        cursor = db1.cursor()
        sql1= """INSERT INTO servicos_motor(
        potencia_cv,
        corrente,
        disjuntor_motor ,
        tipo,
        suporte_conexao,
        contatora,
        contato_auxiliar_frontal, 
        conector_saque,
        seccionador_fusivel,
        soft_starter,
        contatora_de_comando) 
        VALUES (%s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s  )"""
        cursor.execute(sql1, (cv,corrente,disjuntor_motor,tipo,suporte_de_conexao,contatora,contato_auxiliar_frontal,conector_saque,seccionador_fusivel,soft_starter,contatora_de_comando))
        db1.commit()
        db1.close()
        print("dados inseridos com sucesso")
        return jsonify("Dados inseridos com sucesso")
@app.route('/alterar', methods=['POST']) # Nova rota
def alterar():
    senha=request.headers['Authentication']
    if senha!='Bearer xxx':
        print("senha incorreta")
        return jsonify("senha incorreta")
    
    index=request.form['id']
    index=int(index)
    cv=request.form['potencia_cv']
    corrente=request.form['corrente']
    disjuntor_motor=request.form['disjuntor_motor']
    tipo=request.form['tipo']
    suporte_de_conexao=request.form['suporte_de_conexao']
    contatora=request.form['contatora']
    contato_auxiliar_frontal=request.form['contato_auxiliar_frontal']
    conector_saque=request.form['conector_saque']
    seccionador_fusivel=request.form['seccionador_fusivel']
    soft_starter=request.form['soft_starter']
    contatora_de_comando=request.form['contatora_de_comando']
    senha_mudanca=request.form['senha']
    senha_normal=''
    with open('senha.txt','r') as t:
        senha_normal=t.read()
        senha_normal=str(senha_normal)
    if senha_mudanca!=senha_normal:
        return jsonify("senha incorreta,por favor insira a senha correta para mudar os valores")
    if senha_mudanca==senha_normal:
        
        Host,User,Password,Db,Charser,Port=credenciais.credencialbanco()
        db1 = pymysql.connect(host=Host, user=User, password=Password, db=Db, charset=Charset,port=Port)
        cursor = db1.cursor()
        sql = """ UPDATE servicos_motor SET potencia_cv=%s, 
        corrente=%s, 
        disjuntor_motor=%s, 
        tipo=%s, 
        suporte_conexao=%s,
        contatora=%s, 
        contato_auxiliar_frontal=%s, 
        conector_saque=%s, 
        seccionador_fusivel=%s, 
        soft_starter=%s, 
        contatora_de_comando=%s
        WHERE item=%s"""
        cursor.execute(sql, (cv,corrente,disjuntor_motor,tipo,suporte_de_conexao,contatora,contato_auxiliar_frontal,conector_saque,seccionador_fusivel,soft_starter,contatora_de_comando,index,))
        db1.commit()
        db1.close()
        print("dados inseridos com sucesso")
        return jsonify("Dados alterados com sucesso")

@app.route('/historico', methods=['GET','POST']) # Nova rota
def historico():
    #print(request.args.get)
    senha=request.headers['Authentication']
    if senha!='Bearer xxx':
        print("senha incorreta")
        return jsonify("senha incorreta")
   
    if request.args.get('historico')=='sim':
        cv=request.args.get('cv')
        quantidade=request.args.get('qtd')
        filtro=request.args.get('filtro')
        print('entrou aqui')
        print (cv,quantidade,filtro)
        
        Host,User,Password,Db,Charser,Port=credenciais.credencialbanco()
        db1 = pymysql.connect(host=Host, user=User, password=Password, db=Db, charset=Charset,port=Port)
        cursor = db1.cursor()
        #fazer analise combinatoria
        if filtro=='total_download':
            #print('entrou no valor')
            sql1 = "SELECT * FROM servicos_motor"
            #cursor.execute(sql1,(f"%{cv}%",))
            cursor.execute(sql1)
            retorno = cursor.fetchall()
            print(retorno)
            quantidade='1'
            excel.geral(retorno,quantidade)
            return jsonify (retorno)
        if filtro=='total':
            #print('entrou no valor')
            sql1 = "SELECT * FROM servicos_motor WHERE potencia_cv LIKE %s"
            #cursor.execute(sql1,(f"%{cv}%",))
            cursor.execute(sql1,(cv,))
            retorno = cursor.fetchall()
            print(retorno)
            excel.geral(retorno,quantidade)
            return jsonify (retorno)
        if filtro=='pesquisa_id':
            print('entrou na pesquisa por id')
            
            sql1 = "SELECT * FROM servicos_motor WHERE item LIKE %s"
            cursor.execute(sql1,(cv,))
            retorno = cursor.fetchall()
            print(retorno)
            resposta=excel.geral(retorno,quantidade)
            if resposta=="feito":
                return jsonify (retorno)
                #return send_file('relacao.xlsx')
            return jsonify (retorno)
        
        
        
        retorno = cursor.fetchall()
        print(retorno)
            #excel.geral(retorno)
        return jsonify (retorno)
       
    

    
    return render_template('historico.html')
@app.route('/delete', methods=['GET','POST']) # Nova rota
def delete():
    if request.method=='POST':
        try:
            print(request.headers)
            senha=request.headers['Authentication']
        except:
            return jsonify('Acesso negado')
        if senha!='Bearer xxx':
            print("senha incorreta")
            return jsonify("senha incorreta")
        indexador=request.form['indexador']
        cpf=request.form['cpf']
        print("chegou  pra deletar")
        print("index:",indexador)
        
        Host,User,Password,Db,Charser,Port=credenciais.credencialbanco()
        db1 = pymysql.connect(host=Host, user=User, password=Password, db=Db, charset=Charset,port=Port)
        cursor = db1.cursor()
        #for index in indexador:
        cursor.execute('DELETE FROM relacao WHERE item=%s ',(indexador,))
        db1.commit()
        db1.close()
        Host,User,Password,Db,Charser,Port=credenciais.credencialbanco()
        db1 = pymysql.connect(host=Host, user=User, password=Password, db=Db, charset=Charset,port=Port)
        cursor = db1.cursor()
        print(request.form)
        filtro=request.form['filtro']
        inputar=request.form['inputar']
        cpf=request.form['cpf']
        #if filtro=='total':
            #print('entrou no valor')
        #sql1 = "SELECT * FROM relacao WHERE cpf LIKE %s order by data DESC"
        ##cursor.execute(sql1,(cpf,))
        #retorno = cursor.fetchall()
        #print(retorno)
            #excel.geral(retorno)
        #return jsonify (retorno)
        #sql1 = "SELECT * FROM relacao "
        ##.execute(sql1)
        #retorno = cursor.fetchall()
        #print(retorno)
        if filtro=='nome':
            print('entrou no nome')
            inputar='./static/txt/'+inputar
            sql1 = "SELECT * FROM relacao WHERE cpf LIKE %s AND caminho LIKE %s order by data DESC"
            cursor.execute(sql1,(cpf,f"%{inputar}%"))
            retorno = cursor.fetchall()
            print(retorno)
            #excel.geral(retorno)
            return jsonify (retorno)
        if filtro=='data':
            inputar=inputar.replace(' ','')
            print("entrou na averigacao da data")

            sql1 = "SELECT * FROM relacao WHERE data >= %s AND cpf LIKE %s order by data DESC"
            cursor.execute(sql1,(inputar,cpf))
            retorno = cursor.fetchall()
            print(retorno)
            #excel.geral(retorno)
            return jsonify (retorno)

       
        
        
       
    
    return jsonify ('vazio')

@app.route('/', methods=['GET']) # Nova rota
def index():
    
    
        
    return render_template('historico.html')
    


if __name__ == '__main__':
  #serve(app, host='xxx', port=5000)
  app.run(debug=True) # Executa a aplicação
  #app.run( host='xxx', port=5150)
