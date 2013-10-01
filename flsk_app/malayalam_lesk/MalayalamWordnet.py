import sys
sys.path.append('flsk_app/malayalam_lesk/classes/')
sys.path.append('classes/')
import mysqldaccess as _m_acc

class mysqldbwordnet:
    def __init__(self,HOST=None,USER=None,PASSWORD=None,DB=None):
        self._ml_access_obj = _m_acc.DbAccess()
    def getIdFromSense(self,sense):
            qr = "SELECT word_id FROM sense_table WHERE sense ='"+sense+"'"
            rows =self._ml_access_obj.selectDB(qr,"ERROR ON ID SELECTION")
            return rows[0]
            
    def getDefinitions(self,word):
        qr = "SELECT sense FROM sense_table WHERE word ='"+word+"'"
        rows=self._ml_access_obj.selectDB(qr,"ERROR ON SELECTION !@#")
        return rows
    
        