import pymysql
#porta 3307
import credenciais
Host,User,Password,Db,Charset,Port=credenciais.credencialbanco()
db1 = pymysql.connect(host=Host, user=User, password=Password, db=Db, charset=Charset,port=Port)

cursor = db1.cursor()
sql=''' 
DROP TABLE IF EXISTS servicos_motor


'''

           
cursor.execute(sql)
#cursor.execute('DELETE FROM relacao WHERE item=%s ',(9,))
db1.commit()
db1.close()
print("tabela deletada")
#print("index deletado")