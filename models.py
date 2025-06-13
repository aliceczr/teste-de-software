from flask_sqlalchemy import SQLAlchemy
import os


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    data_adicao = db.Column(db.String(30), nullable=False)
    adicionado_por = db.Column(db.String(80), nullable=False)
    cargo = db.Column(db.String(80), nullable=False)

