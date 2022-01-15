from flask import Flask , jsonify , request

app = Flask(__name__)

tasks=[
    {
        'id':1,
        'Name':'Nagalakshmi',
        'Contact':'1234567890',
        'done':False
    },
    {
        'id':2,
        'Name':'Jawahar',
        'Contact':'0987654321', 
        'done':False
    }
]


@app.route("/")

def hello_world():
    return " Hi *_*"

@app.route("/add-data" , methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
    task = {
        'id':tasks[-1]['id']+1,
        'Name':request.json['Name'],
        'Contact':request.json.get('Contact',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"task added successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })

    
if __name__ == '__main__':
    app.run()