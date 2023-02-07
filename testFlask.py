from flask import Flask, request, jsonify, json

app = Flask(__name__)
app.config["DEBUG"] = True

employees = json.load(open("employees.json"))

@app.route('/')
def index():
 return "<h1>hello my app</h1>"

@app.route('/api/v1/employees',  methods=['GET'])
def get():
    return jsonify(employees)

@app.route('/api/v1/post/employees',  methods=['POST'])
def post():
    data = request.form
    new_employee = employees.copy()
    new_employee.append(data)
    return jsonify(new_employee)
#Récupérer dernier ID, ajouter 1 et ajouter autres valeurs

@app.route("/api/v1/delete/employee/<id>", methods=["DELETE"])
def delete(id):
    #On copie la liste originale pour ne pas l'altérer
    deleted_employee = employees.copy()
    
    #On parcours chaque employé de la liste d'employés
    for i in range(len(deleted_employee)) :
        #Si c'est l'id de l'employé qu'on recherche
        if deleted_employee[i]["id"] == int(id) :
           #On retient sa position/index
           to_delete_index = i
    deleted_employee.pop(to_delete_index)
    return jsonify(deleted_employee)
   

@app.route("/api/V1/put/employee/<id>", methods=["PUT"])
def put(id):
    #On copie la liste originale pour ne pas l'altérer
    modified_employee = employees.copy()
    #On récupère les données du formulaire
    data = request.form
    #On prépare une variable qui va enregistrer l'index à modifier
    to_modify_index = 0
    
    #On parcours chaque employé de la liste d'employés
    for i in range(len(modified_employee)) :
        #Si c'est l'id de l'employé qu'on recherche
        if modified_employee[i]["id"] == int(id) :
           #On retient sa position/index
           to_modify_index = i
    
    #Modification de l'élément dans la liste par les données du formulaire récupéré dans la variable data
    modified_employee[to_modify_index] = data
    return jsonify(modified_employee)
            

if __name__ == '__main__':
    app.run(port=8080, debug=True)
