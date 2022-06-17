from extensions import db

class Chip(db.Model):
    id = db.Column(db.String, primary_key=True)
    batch = db.Column(db.String(500), nullable = False)   
    wafer = db.Column(db.String(500), nullable = False)