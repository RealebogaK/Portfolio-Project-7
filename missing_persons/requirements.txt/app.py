from flask import Flask, request, jsonify
from db_helper import init_db, db
from models import Person

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///missing_wanted.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

@app.route('/persons', methods=['POST'])
def add_person():
    data = request.get_json()
    new_person = Person(
            name=data['name'],
            date_of_birth=data['date_of_birth'],
            description=data.get('description'),
            status=data['status']
            )
    db.session.add(new_person)
    db.session.commit()
    return jsonify({'message': 'Person added successfully!'}), 201

@app.route('/persons', methods=['GET'])
def get_persons():
    persons = Person.query.all()
    results = [
            {
                "id": person.id,
                "name": person.name,
                "date_of_birth": person.date_of_birth.isoformat(),
                "description": person.description,
                "status": person.status,
                "date_reported": person.date_reported.isoformat()
            } for person in persons
]
return jsonify(results)
@app.route('/persons/<int:id>', methods=['GET'])
def get_person(id):
    person = Person.query.get_or_404(id)
    result = {
            "id": person.id,
            "name": person.name,
            "date_of_birth": person.date_of_birth.isoformat(),
            "description": person.description,
            "status": person.status,
            "date_reported": person.date_reported.isoformat()
        }
    return jsonify(result)

@app.route('/persons/<int:id>', methods=['PUT'])
def update_person(id):
    data = request.get_json()
    person = Person.query.get_or_404(id)
    person.name = data.get('name', person.name)
    person.date_of_birth = data.get('date_of_birth', person.date_of_birth)
    person.description = data.get('description', person.description)
    person.status = data.get('status', person.status)
    db.session.commit()
    return jsonify({'message': 'Person updated successfully!'})

@app.route('/persons/<int:id>', methods=['DELETE'])
def delete_person(id):
    person = Person.query.get_or_404(id)
    db.session.delete(person)
    db.session.commit()
    return jsonify({'message': 'Person deleted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)
