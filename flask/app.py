#coding:utf-8
from flask import Flask, request, render_template, redirect, url_for, session, make_response
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, TextField
from wtforms.validators import Required
from lib.dbcomm import *
import json
import re


app = Flask(__name__)
bootstrap = Bootstrap(app)


app.config['SECRET_KEY'] = 'helloasldjasldjoasidjoijfoiadsjfhas'
app.config.from_object(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True




class contentForm(FlaskForm):
    commandInConfig = StringField(u'内置命令')
    commandInWrite = TextAreaField(u'写入Python代码', default=u"写入Python代码")
    userName = StringField(u'用户名', validators=[Required()])
    passWord = StringField(u'密码', validators=[Required()])
    sendCommand = SubmitField(u'发送命令')
    clearCommand = SubmitField(u'清空命令')




class NameForm(FlaskForm):  
    id = StringField('id')
    name = StringField('name', validators=[Required()])
    info = StringField('info')
    level = StringField('level')
    type = StringField('type')
    data = TextAreaField('data', validators=[Required()])




@app.route('/e0df5f3dfd2650ae5be9993434e2b2c0/', methods=['GET'])  
def index():  
    form = NameForm()  
    #如果提交的数据验证通过，则返回True  
    if form.validate_on_submit():  
        name = form.name.data  
        form.name.data = ''  
    return render_template('insert.html', form=form)



@app.route('/e0df5f3dfd2650ae5be9993434e2b2c0/', methods=['POST']) 
def insert():
    form = NameForm()
    name = request.form['name']
    info = request.form['info']
    level = request.form['level']
    type = request.form['type']
    data = request.form['data']
    


    r = "^\w+$"
    try:
        n = re.search(r, name).group()
        i = re.search(r, info).group()
        l = re.search(r, level).group()
        t = re.search(r, type).group()
    except:
        render_template('insert.html', form=form)
    
    try:
        j = json.loads(data.replace('\\','\\\\').replace('\\\\"', '\\\\\\"'))
    except:
        render_template('insert.html', form=form)


    if info.strip() == "":
        db_update(db_payload, name, json.dumps(j))
    else:
        db_insert(db_payload, name, info, level, type, json.dumps(j))
    return render_template('insert.html', form=form)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
