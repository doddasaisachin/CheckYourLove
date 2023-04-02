from flask import Flask,render_template,request
import pymongo
applicaton=Flask(__name__)
app=applicaton

@app.route('/',methods=['POST','GET'])
def home():
    if request.method=='GET':
        return render_template('home.html')
    else:
        name=request.form.get('Your Name')
        suspect=request.form.get('Her/Him Name')

        client = pymongo.MongoClient("mongodb+srv://saisachin1686863:ss1686863@cluster0.uubofh7.mongodb.net/?retryWrites=true&w=majority")
        db = client.test
        col=db['mycol']
        d={'name':name,"suspect":suspect}
        col.insert_one(d)
        import random
        temp=random.randint(60,99)

        return render_template('result.html',result=temp)
if __name__=='__main__':
    app.run(host='0.0.0.0')
