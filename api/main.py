from flask import Flask,request,jsonify
app = Flask(__name__)


@app.route('/')
def hello():
    name = "Hello World"
    return "Congratulations!　You finally found me！"


@app.route('/IoT',methods=['POST'])
def iot():
    #get data
    headers= request.headers.get("Chikuzenni-token",None)
    json=request.get_json()
    #check json data
    if json == None:
        if request.headers['Content-Type'] != 'application/json':
            return_data={"success":False,"message":"Kindly use the Content-Type as application/json."}
        else:
            return_data={"success":False,"message":"We can only process JSON data."}
        return jsonify(return_data)

    #parse json data
    data1 = json.get('token',None)
    data2 = json.get('status',None)

    #check requirements
    if (headers==None or data1==None or data2==None):
        return_data={"success":False,"message":"The required information is incomplete."}
    else:
        return_data = {
            "success":True,
            "data":{
            "header-token":headers,
            "body-token":data1,
            "body-status":data2
            }
            }

    return jsonify(return_data)

if __name__ == "__main__":
    app.run(debug=True)
