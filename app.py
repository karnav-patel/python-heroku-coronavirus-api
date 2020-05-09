from flask import Flask ,request,jsonify

app = Flask(__name__)

@app.route('/api',methods=['GET'])
def hello_world():
    d={}
    a={}
    b={}
    f={}
    s={}

    d['name'] = str(request.args['name'])
    if d['name'] == 'karnav':
        a['see'] = 'Your father name is Sharadkumar'
        return jsonify(a)

    elif d['name'] == 'vrushik':
        b['see'] = 'Your father name is Sudhirkumar'
        return jsonify(b)
        
    elif d['name'] == 'simreen':
        s['see'] = 'Your father name is InderSingh and mother name is SatinderKaur. IMP: Simreen is Fool'
        return jsonify(s)
        
    else:
        f['see'] = 'Your father name is something else'
        return jsonify(f)
    


if __name__ == '_main_':
    app.run()
