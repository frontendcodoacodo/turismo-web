from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class GuiaTuristica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    provincia = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(255))
    actividades_permitidas = db.Column(db.String(255), nullable=False)

class Guia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    guia_turistica_id = db.Column(db.Integer, db.ForeignKey('guia_turistica.id'), nullable=False)
    guia_turistica = db.relationship('GuiaTuristica', backref=db.backref('guias', lazy=True))

class Lugar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    guia_turistica_id = db.Column(db.Integer, db.ForeignKey('guia_turistica.id'), nullable=False)
    guia_turistica = db.relationship('GuiaTuristica', backref=db.backref('lugares', lazy=True))

class Actividad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    lugar_id = db.Column(db.Integer, db.ForeignKey('lugar.id'), nullable=False)
    lugar = db.relationship('Lugar', backref=db.backref('actividades', lazy=True))