from flask  import Flask,request,render_template
from flask_cors import CORS,cross_origin
from page_type1 import page1
app=Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
@cross_origin()
def homepage():
    return render_template('index.html')



@app.route('/scrap',methods=['GET','POST'])
def index():
    if request.method=='POST':
        searchstring=request.form['content'].replace(" ","+")
        try:
            results_page,reviews,searchstring=page1(searchstring)
            return render_template(results_page, reviews=reviews, searchstring=searchstring)
        except:
            return "something is wrong"


if __name__ == '__main__':
    app.run(port=8000,debug=True)