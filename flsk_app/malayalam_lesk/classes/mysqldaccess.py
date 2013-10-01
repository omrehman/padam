import mysql_config as conf

import MySQLdb as mysql
import sys

class DbAccess:
    def __init__(self,host=conf._HOST_,user=conf._USER_,password=conf._PASSWORD_,db=conf._DATABASE_):
           
            self.conn =mysql.Connect(host,user,password,db)
            self.cur = self.conn.cursor()
            
    #SELECT A DATABASE         
    def selectDB(self, qr,msg):
        try:
            self.cur.execute(qr)
            row = self.cur.fetchall()
            return row
        except self.conn.Error, e:
                print  msg+"\nERROR %d: %s"%(e.args[0],e.args[1])
                sys.exit(1)
                
#INSERT INTO DATABASE  
               
    def insertDB(self,qr,msg):
        try:
            self.cur.execute(qr)
            self.conn.commit()
        except self.conn.Error,e:
            print  msg+"\nERROR %d: %s"%(e.args[0],e.args[1])
            sys.exit(1)

#UPDATE INTO DATABASE            
    def updadateDB(self,qr,msg):
        try:
            self.cur.execute(qr)
            self.conn.commit()
        except self.conn.Error, e:
            print  msg+"\nERROR %d: %s"%(e.args[0],e.args[1])
            sys.exit(1) 
