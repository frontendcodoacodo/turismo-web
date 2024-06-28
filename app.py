from flask import Flask, request, jsonify, render_template, request, redirect, url_for
from models import db, GuiaTuristica, Guia, Lugar, Actividad
from flask_sqlalchemy import SQLAlchemy



"""app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'turismo_db1'
mysql = MySQL(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///turismo_db1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)"""


app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/turismodb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guias')
def view_guides():
    guias = GuiaTuristica.query.all()
    return render_template('view_guides.html', guias=guias)
    
@app.route('/lugares')
def view_places():
    lugares = Lugar.query.all()
    return render_template('view_places.html', lugares=lugares)

@app.route('/actividades')
def view_activities():
    actividades = Actividad.query.all()
    return render_template('view_activities.html', actividades=actividades)

@app.route('/add_guia', methods=['GET', 'POST'])
def add_guide():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        provincia = request.form['provincia']
        actividades = request.form.getlist('actividades')
        
        # Validaciones según la provincia
        if provincia == 'Corrientes' and ('turismo de nieve' in actividades or 'trekking de alta montaña' in actividades):
            return "En Corrientes no se puede ofrecer turismo de nieve ni trekking de alta montaña."
        elif provincia == 'San Juan' and 'turismo de pesca' in actividades:
            return "En San Juan no se puede ofrecer turismo de pesca."
        elif provincia == 'Tucuman' and 'turismo de nieve' in actividades:
            return "En Tucuman no se puede ofrecer turismo de nieve."
        elif provincia == 'Mendoza' and 'turismo de pesca' in actividades:
            return "En Mendoza no se puede ofrecer turismo de pesca."

        actividades_permitidas = ', '.join(actividades)
        descripcion = request.form['descripcion']
        new_guia_turistica = GuiaTuristica(nombre=nombre, apellido=apellido, provincia=provincia, actividades_permitidas=actividades_permitidas, descripcion=descripcion)
        db.session.add(new_guia_turistica)
        db.session.commit()
        return redirect(url_for('view_guides'))
    
    return render_template('add_guide.html')

if __name__ == '__main__':
    app.run(debug=True)