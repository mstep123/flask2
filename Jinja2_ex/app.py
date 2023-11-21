#"python.defaultInterpreterPath": "/home/user/.local/share/virtualenvs/Jinja2_ex--TRo7uIi/bin/python"
from flask import Flask, render_template, abort

app = Flask(__name__)
#--------------------------------------------
@app.route('/users/<username>')
def show_user_profile(username):
    humans = list()
    with open ("files/user_list.txt", encoding="utf-8") as f :
        for raw_line in f:
            data = raw_line.strip().split(';')
            if data[0] == username :
                humans.append(
                dict(zip(('login','last_name','name', 
                'surname','birth_date','phone'),data))
                )
                break
    if len(humans) == 0 :
        abort(404,f'user {username} not found')
    #return f'User {humans}'
    return render_template('user_list.html', **{'entities':humans})
#---------------------------------------------
@app.route('/posts/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'
#-------------------------------------------
@app.get('/user_list')
def user_list():
    humans = list()
    with open ("files/user_list.txt", encoding="utf-8") as f :
        for raw_line in f:
            data = raw_line.strip().split(';')
            humans.append(
                dict(zip(('login','last_name','name', 
                'surname','birth_date','phone'),data))
                )

    return render_template('user_list.html', **{'entities':humans})
#--------------------------------------------
@app.get('/humans')
def table():
    humans = list()
    with open ("files/humans.txt", encoding="utf-8") as f :
        for raw_line in f:
            data = raw_line.strip().split(';')
            keys = ['last_name', 'name', 'surname']
            humans.append({'last_name':data[0],'name':data[1], 'surname':data[2]})

    return render_template('humans.html', entities=humans)

#-----------------------------------------------
@app.get('/')
def home():
    return render_template("index.html")
#-----------------------------------------------
@app.get('/names')
def names():
    #name = 'Vladimir!!!!!'
    #return render_template("names.html",name=name)
    #return render_template("names.html",**{'name':name})
    names = list()
    with open ("files/names.txt", encoding="utf-8") as f :
        for raw_line in f:
            names.append(raw_line.strip())

    return render_template("names.html",names=names)
    #return "<br>".join(names)
#----------------------------------------------------
@app.route('/about')
def about():
    return 'about'

if __name__ == '__main__' :
    app.run(debug=True)