



from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")
#   date='20200819'
 #  text='2'   
  # return render_template("test.html",date=date,text=text)

if __name__ == '__main__':
   #app.run(host='107.172.206.163', debug = True)
   app.run(host='107.172.206.163')
