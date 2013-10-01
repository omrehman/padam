from flask import render_template
from flsk_app import app
from flask import request
import sys
sys.path.append('flsk_app/malayalam_lesk')
import MalayalamStemmer as stemm 
import MalayalamWordnet as w_n
import lesk_algorithm as lesk

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Mujeeb' }
    return render_template('index.html',title="Welcome",user=user)


@app.route('/hello')
def hello():
    return "hello"

@app.route('/if_command')
def if_command():
    user = { 'nickname': 'Mujeeb' }
    k = render_template('if_cmd.html',usr=user,title="dddd")
    return k 
@app.route('/test_form',methods=['GET','POST'])
def test_form():
    if request.form:
        test=request.form['a']
        test = stemm.findstem(test.strip())
        return render_template('test_form.html',test=test)
    return render_template('test_form.html')

@app.route('/wordnet/get-definition',methods=['GET','POST'])
def get_definition():
    if request.form:
        mal_word =request.form["input_word"]
        mal_obj= w_n.mysqldbwordnet()
        definitions = mal_obj.getDefinitions(mal_word.encode('UTF-8'))
        return render_template('get_definitions.html',definition=definitions)
    return render_template('get_definitions.html')

@app.route('/lesk-algorithm',methods=['GET','POST'])
def lesk_algorithm():
    if request.form:
            context = request.form['context'].encode('UTF-8')
            word = request.form['word'].encode('UTF-8')
            if (word.strip()=="" or context.strip()==""):
                return render_template('lesk_algorithm.html',empty_flag=True,alert_msg="No field Should be empty!!")
                        
            row=lesk.lesk(context,word)
            if row == False:
                    return render_template('lesk_algorithm.html',empty_flag=True,alert_msg="Word not found in context!!")
            return render_template('lesk_algorithm.html',definition=row,empty_flag=False)
    return render_template('lesk_algorithm.html',empty_flag=False)