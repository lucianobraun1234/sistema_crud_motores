import pymysql
import credenciais
Host,User,Password,Db,Charser,Port=credenciais.credencialbanco()
db1 = pymysql.connect(host=Host, user=User, password=Password, db=Db, charset=Charser,port=Port)
cursor = db1.cursor()
sql1 = "SELECT * FROM servicos_motor"
cursor.execute(sql1)
retorno = cursor.fetchall()
print(retorno)
if retorno==():
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
#sql1= """INSERT INTO servicos_motor(potencia_cv,corrente,disjuntor_motor ,tipo,suporte_conexao,contatora) 
#VALUES (%s,%s,%s,%s,%s,%s)"""
    cursor.execute(sql1, ('1',#cv
                      '1,73',#corrente
                      '3RV2311-1BC10',#disjuntor_motor
                      'parafuso',#tipo
                      '3RA2921-1BA00',#suporte_conexao
                      '3RT2015-1BB41 para tensão 24vcc ou 3RT2015-1AP01 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      ' 8WA1011-1DF11',# conector saque
                      'menos de 15 cv nao vai seccionador fusivel',#seccionador fusível
                      'menos de 15 cv nao vai soft starter',#soft starter
                      'menos de 15 cv nao vai contatora de comando'))#contatora de comando
    cursor.execute(sql1, ('1',#cv
                      '1,73',#corrente
                      '3RV2311-1BC20',#disjuntor_motor
                      'mola',#tipo
                      '3RA2921-2GA00',#suporte_conexao
                      '3RT2015-2BB42 para tensão 24vcc ou 3RT2015-2AP02 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      ' 8WA1011-1DF11',#conector saque
                      'menos de 15 cv nao vai seccionador fusivel',#seccionador fusivel
                      'menos de 15 cv nao vai soft starter',#soft starter
                      'menos de 15 cv nao vai contatora de comando'))# contatora de comando
    cursor.execute(sql1, ('1,5',#cv
                      '2,56',#corrente
                      '3RV2311-1DC10',#disjuntor_motor
                      'parafuso',#tipo
                      '3RA2921-1BA00',#suporte_conexao
                      '3RT2015-1BB41 para tensão 24vcc ou 3RT2015-1AP01 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      ' 8WA1011-1DF11',#conector saque
                      'menos de 15 cv nao vai seccionador fusivel',#seccionador fusivel
                      'menos de 15 cv nao vai soft starter',#soft -starter
                      'menos de 15 cv nao vai contatora de comando'))#contatora de comando
    cursor.execute(sql1, ('1,5',#cv
                      '2,56',#corrente
                      '3RV2311-1DC20',#disjuntor_motor
                      'mola',#tipo
                      '3RA2911-2GA00',#suporte_conexao
                      '3RT2015-2BB42 para tensão 24vcc ou 3RT2015-2AP02 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA1011-1DF11',#conector saque
                      'menos de 15 cv nao vai seccionador fusivel',#seccionador fusivel
                      'menos de 15 cv nao vai soft starter',#soft -starter
                      'menos de 15 cv nao vai contatora de comando'))#contatora de comando
    cursor.execute(sql1, ('2',#cv
                      '3,56',#corrente
                      '3RV2311-1EC10',#disjuntor_motor
                      'parafuso',#tipo
                      '3RA2921-1BA00',#suporte_conexao
                      '3RT2015-1BB41 para tensão 24vcc ou 3RT2015-1AP01 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA1011-1DF11',#conector saque
                      'menos de 15 cv nao vai seccionador fusivel',#seccionador fusivel
                      'menos de 15 cv nao vai soft starter',#soft -starter
                      'menos de 15 cv nao vai contatora de comando'))#contatora de comando
    cursor.execute(sql1, ('2',#cv
                      '3,56',#corrente
                      '3RV2311-1EC20',#disjuntor_motor
                      'mola',#tipo
                      '3RA2911-2GA00',#suporte_conexao
                      '3RT2015-2BB42 para tensão 24vcc ou 3RT2015-2AP02 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA1011-1DF11',#conector saque
                      'menos de 15 cv nao vai seccionador fusivel',#seccionador fusivel
                      'menos de 15 cv nao vai soft starter',#soft -starter
                      'menos de 15 cv nao vai contatora de comando'))#contatora de comando
    
    cursor.execute(sql1, ('3',#cv
                      '4,79',#corrente
                      '3RV2311-1FC10',#disjuntor_motor
                      'parafuso',#tipo
                      '3RA2921-1BA00',#suporte_conexao
                      '3RT2015-1BB41 para tensão 24vcc ou 3RT2015-1AP01 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA1011-1DF11',#conector saque
                      'menos de 15 cv nao vai seccionador fusivel',#seccionador fusivel
                      'menos de 15 cv nao vai soft starter',#soft -starter
                      'menos de 15 cv nao vai contatora de comando'))#contatora de comando
    cursor.execute(sql1, ('3',#cv
                      '4,79',#corrente
                      '3RV2311-1FC20',#disjuntor_motor
                      'mola',#tipo
                      '3RA2911-2GA00',#suporte_conexao
                      '3RT2015-2BB42 para tensão 24vcc ou 3RT2015-2AP02 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA1011-1DF11',#conector saque
                      'menos de 15 cv nao vai seccionador fusivel',#seccionador fusivel
                      'menos de 15 cv nao vai soft starter',#soft -starter
                      'menos de 15 cv nao vai contatora de comando'))#contatora de comando
    cursor.execute(sql1, ('4',#cv
                      '6,43',#corrente
                      '3RV2311-1HC10',#disjuntor_motor
                      'parafuso',#tipo
                      '3RA2921-1BA00',#suporte_conexao
                      '3RT2015-1BB41 para tensão 24vcc ou 3RT2015-1AP01 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA1011-1DF11',#conector saque
                      'menos de 15 cv nao vai seccionador fusivel',#seccionador fusivel
                      'menos de 15 cv nao vai soft starter',#soft -starter
                      'menos de 15 cv nao vai contatora de comando'))#contatora de comando
    cursor.execute(sql1, ('4',#cv
                      '6,43',#corrente
                      '3RV2311-1HC20',#disjuntor_motor
                      'mola',#tipo
                      '3RA2911-2GA00',#suporte_conexao
                      '3RT2015-2BB42 para tensão 24vcc ou 3RT2015-2AP02 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA1011-1DF11',#conector saque
                      'menos de 15 cv nao vai seccionador fusivel',#seccionador fusivel
                      'menos de 15 cv nao vai soft starter',#soft -starter
                      'menos de 15 cv nao vai contatora de comando'))#contatora de comando
    cursor.execute(sql1, ('5',#cv
                      '8',#corrente
                      '3RV2311-1HC10',#disjuntor_motor
                      'parafuso',#tipo
                      '3RA2921-1BA00',#suporte_conexao
                      '3RT2016-1BB41 para tensão 24vcc ou 3RT2016-1AP01 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA1011-1DF11',#conector saque
                      'menos de 15 cv nao vai seccionador fusivel',#seccionador fusivel
                      'menos de 15 cv nao vai soft starter',#soft -starter
                      'menos de 15 cv nao vai contatora de comando'))#contatora de comando
    cursor.execute(sql1, ('5',#cv
                      '8',#corrente
                      '3RV2311-1HC20',#disjuntor_motor
                      'mola',#tipo
                      '3RA2911-2GA00',#suporte_conexao
                      '3RT2016-2BB42 para tensão 24vcc ou 3RT2016-2AP02 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA1011-1DF11',#conector saque
                      'menos de 15 cv nao vai seccionador fusivel',#seccionador fusivel
                      'menos de 15 cv nao vai soft starter',#soft -starter
                      'menos de 15 cv nao vai contatora de comando'))#contatora de comando
    cursor.execute(sql1, ('6',#cv
                      '9,5',#corrente
                      '3RV2311-1JC10',#disjuntor_motor
                      'parafuso',#tipo
                      '3RA2921-1BA00',#suporte_conexao
                      '3RT2017-1BB41 para tensão 24vcc ou 3RT2017-1AP01 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA1011-1DF11',#conector saque
                      'menos de 15 cv nao vai seccionador fusivel',#seccionador fusivel
                      'menos de 15 cv nao vai soft starter',#soft -starter
                      'menos de 15 cv nao vai contatora de comando'))#contatora de comando
    cursor.execute(sql1, ('6',#cv
                      '9,5',#corrente
                      '3RV2311-1JC20',#disjuntor_motor
                      'mola',#tipo
                      '3RA2911-2GA00',#suporte_conexao
                      '3RT2017-2BB42 para tensão 24vcc ou 3RT2017-2AP02 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA1011-1DF11',#conector saque
                      'menos de 15 cv nao vai seccionador fusivel',#seccionador fusivel
                      'menos de 15 cv nao vai soft starter',#soft -starter
                      'menos de 15 cv nao vai contatora de comando'))#contatora de comando
    cursor.execute(sql1, ('7,5',#cv
                      '11,6',#corrente
                      '3RV2311-1KC10',#disjuntor_motor
                      'parafuso',#tipo
                      '3RA2921-1BA00',#suporte_conexao
                      '3RT2017-1BB41 para tensão 24vcc ou 3RT2017-1AP01 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA1011-1DF11',#conector saque
                      'menos de 15 cv nao vai seccionador fusivel',#seccionador fusivel
                      'menos de 15 cv nao vai soft starter',#soft -starter
                      'menos de 15 cv nao vai contatora de comando'))#contatora de comando
    cursor.execute(sql1, ('7,5',#cv
                      '11,6',#corrente
                      '3RV2311-1KC20',#disjuntor_motor
                      'mola',#tipo
                      '3RA2911-2GA00',#suporte_conexao
                      '3RT2017-2BB42 para tensão 24vcc ou 3RT2017-2AP02 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA1011-1DF11',#conector saque
                      'menos de 15 cv nao vai seccionador fusivel',#seccionador fusivel
                      'menos de 15 cv nao vai soft starter',#soft -starter
                      'menos de 15 cv nao vai contatora de comando'))#contatora de comando
    cursor.execute(sql1, ('10',#cv
                      '15,3',#corrente
                      '3RV2321-4AC10',#disjuntor_motor
                      'parafuso',#tipo
                      '3RA2921-1BA00',#suporte_conexao
                      '3RT2018-1BB41 para tensão 24vcc ou 3RT2018-1AP01 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA1011-1DF11',#conector saque
                      'menos de 15 cv nao vai seccionador fusivel',#seccionador fusivel
                      'menos de 15 cv nao vai soft starter',#soft -starter
                      'menos de 15 cv nao vai contatora de comando'))#contatora de comando
    cursor.execute(sql1, ('10',#cv
                      '15,3',#corrente
                      '3RV2321-4AC20',#disjuntor_motor
                      'mola',#tipo
                      '3RA2911-2GA00',#suporte_conexao
                      '3RT2018-2BB42 para tensão 24vcc ou 3RT2018-2AP02 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA1011-1DF11',#conector saque
                      'menos de 15 cv nao vai seccionador fusivel',#seccionador fusivel
                      'menos de 15 cv nao vai soft starter',#soft -starter
                      'menos de 15 cv nao vai contatora de comando'))#contatora de comando
    cursor.execute(sql1, ('12,5',#cv
                      '18,6',#corrente
                      '3RV2321-4BC10',#disjuntor_motor
                      'parafuso',#tipo
                      '3RA2921-1BA00',#suporte_conexao
                      '3RT2026-1BB40 para tensão 24vcc ou 3RT2026-1AP00 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA1011-1DF11',#conector saque
                      'menos de 15 cv nao vai seccionador fusivel',#seccionador fusivel
                      'menos de 15 cv nao vai soft starter',#soft -starter
                      'menos de 15 cv nao vai contatora de comando'))#contatora de comando
    cursor.execute(sql1, ('12,5',#cv
                      '18,6',#corrente
                      '3RV2321-4BC20',#disjuntor_motor
                      'mola',#tipo
                      '3RA2911-2GA00',#suporte_conexao
                      '3RT2026-2BB40 para tensão 24vcc ou 3RT2026-2AP00 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA1011-1DF11',#conector saque
                      'menos de 15 cv nao vai seccionador fusivel',#seccionador fusivel
                      'menos de 15 cv nao vai soft starter',#soft -starter
                      'menos de 15 cv nao vai contatora de comando'))#contatora de comando
    cursor.execute(sql1, ('15',#cv
                      '22,4',#corrente
                      '3RV2321-4DC10',#disjuntor_motor
                      'parafuso',#tipo
                      '3RA2921-1BA00',#suporte_conexao
                      '3RT2026-1BB40 para tensão 24vcc ou 3RT2026-1AP00 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA1011-1DG11',#conector saque
                      '3NP1143-1DA10 para parafuso ou 3NP1143-1DA20 para CABO',#seccionador fusivel 250 AMPERES
                      'menos de 15 cv nao vai soft starter',#soft -starter
                      'menos de 15 cv nao vai contatora de comando'))#contatora de comando
    cursor.execute(sql1, ('15',#cv
                      '22,4',#corrente
                      '3RV2321-4DC20',#disjuntor_motor
                      'mola',#tipo
                      '3RA2911-2GA00',#suporte_conexao
                      '3RT2026-2BB40 para tensão 24vcc ou 3RT2026-2AP00 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA1011-1DG11',#conector saque
                      '3NP1133-1CA10 para parafuso ou 3NP1133-1CA20  para CABO',#seccionador fusivel
                      '3RW3028-1BB04',#soft -starter
                      '3RT2016-1BB41 contato por parafuso'))#contatora de comando
    cursor.execute(sql1, ('20',#cv
                      '31',#corrente
                      '3RV2321-4PC10',#disjuntor_motor
                      'parafuso',#tipo
                      '3RA2921-1BA00',#suporte_conexao
                      '3RT2028-1BB40 para tensão 24vcc ou 3RT2028-1AP00 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA1011-1DG11',#conector saque
                      '3NP1133-1CA10 para parafuso ou 3NP1133-1CA20  para CABO',#seccionador fusivel
                      '3RW3028-1BB04',#soft -starter
                      '3RT2016-1BB41 contato por parafuso'))#contatora de comando
    cursor.execute(sql1, ('25',#cv
                      '38',#corrente
                      '3RV2321-4FC10',#disjuntor_motor
                      'parafuso',#tipo
                      '3RA2921-1BA00',#suporte_conexao
                      '3RT2035-1AP00 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA12 04',#conector saque
                      '3NP1133-1CA10 para parafuso ou 3NP1133-1CA20  para CABO',#seccionador fusivel
                      '3RW3036-1BB04',#soft -starter
                      '3RT2016-1BB41 contato por parafuso'))#contatora de comando
    cursor.execute(sql1, ('30',#cv
                      '43',#corrente
                      '3RV2331-4WC10',#disjuntor_motor
                      'parafuso',#tipo
                      '3RA2921-1BA00',#suporte_conexao
                      '3RT2036-1AP00 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA12 04',#conector saque
                       '3NP1133-1CA10 para parafuso ou 3NP1133-1CA20  para CABO',#seccionador fusivel
                      '3RW3037-1BB04',#soft -starter
                      '3RT2016-1BB41 contato por parafuso'))#contatora de comando
    cursor.execute(sql1, ('40',#cv
                      '58',#corrente
                      '3RV2331-4JC10',#disjuntor_motor
                      'parafuso',#tipo
                      '3RA2921-1BA00',#suporte_conexao
                      '3RT2037-1AP00 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA12 04',#conector saque
                      '3NP1133-1CA10 para parafuso ou 3NP1133-1CA20  para CABO',#seccionador fusivel
                      '3RW3037-1BB04',#soft -starter
                      '3RT2016-1BB41 contato por parafuso'))#contatora de comando
    cursor.execute(sql1, ('50',#cv
                      '72',#corrente
                      '3RV2331-4RC10',#disjuntor_motor
                      'parafuso',#tipo
                      '3RA2921-1BA00',#suporte_conexao
                      '3RT2038-1AP00 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA12 05',#conector saque
                      '3NP1143-1DA10 para parafuso ou 3NP1143-1DA20  para cabo',#seccionador fusivel
                      '3RW3038-1BB04',#soft -starter
                      '3RT2016-1BB41 contato por parafuso'))#contatora de comando
    cursor.execute(sql1, ('60',#cv
                      '85',#corrente
                      '3RV2341-4MC10',#disjuntor_motor
                      'parafuso',#tipo
                      '3RA2921-1BA00',#suporte_conexao
                      '3RT2046-3AN20 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA12 05',#conector saque
                      '3NP1143-1DA10 para parafuso ou 3NP1143-1DA20  para cabo',#seccionador fusivel
                      '3RW3047-1BB14',#soft -starter
                      '3RT2016-1BB41 contato por parafuso'))#contatora de comando
    cursor.execute(sql1, ('75',#cv
                      '101',#corrente
                      '3RV2041-4MA10',#disjuntor_motor
                      'parafuso',#tipo
                      '3RA2921-1BA00',#suporte_conexao
                      '3RT1054-1AP36 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA12 05',#conector saque
                      '3NP1143-1DA10 para parafuso ou 3NP1143-1DA20  para cabo',#seccionador fusivel
                      '3RW3047-1BB14',#soft -starter
                      '3RT2016-1BB41 contato por parafuso'))#contatora de comando
    cursor.execute(sql1, ('100',#cv
                      '141',#corrente
                      '3RV2341-4MC10',#disjuntor_motor
                      'parafuso',#tipo
                      '3RA2921-1BA00',#suporte_conexao
                      '3RT1056-6AP36 para 230 VAC',#contatora
                      '3RV2901-1D 1NAF-comutador ou 3RV2901-2E 1NA + 1NFpy',#contato auxiliar frontal
                      '8WA1206',#conector saque
                      '3NP1153-1DA10  para parafuso ou 3NP1153-1DA20  para cabo',#seccionador fusivel
                      '3RW5056-2AB14',#soft -starter
                      '3RT2016-1BB41 contato por parafuso'))#contatora de comando
    
    db1.commit()
    print("dados inseridos com sucesso")
db1.close()
print("fechando o banco de dados")
        
