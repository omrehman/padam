import sys 
import MalayalamWordnet
import MalayalamStemmer
wordnet_object = MalayalamWordnet.mysqldbwordnet()
f = open('input.txt','r')
out_put_file = open('output.txt','w')
input_text = f.read().split('#');
root =  MalayalamStemmer.findstem(input_text[0])
row= wordnet_object.getDefinitions(root)
#row= wordnet_object.getDefinitions(input_text[0])
'''for item in input_text[1].split():
    print item.decode('UTF-8')[len(item.decode('UTF-8'))-4:len(item.decode('UTF-8'))]
    out_put_file.write(item.decode('UTF-8')+'\t')'''

for item in row:
    print item[0]


# sys.path.append('classes/')
# import mysqldaccess as  m_acc
# 
# 
# k = m_acc.DbAccess(password='user',user='root')
# rows = k.selectDB("SELECT * FROM  sense_table LIMIT 0,100", "hi")
# for item in rows:
#     print item[2]
#     
#k.insertDB("CREATE TABLE A (mm char(20))","error on selection")