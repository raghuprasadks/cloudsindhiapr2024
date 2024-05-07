from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/register',methods = ['POST', 'GET'])
def register():
   if request.method == 'POST':
      user = request.form['name']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('name')
      return redirect(url_for('success',name = user))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)