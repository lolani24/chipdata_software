from extensions import db
from datetime import datetime

class Chip(db.Model):
    id = db.Column(db.String, primary_key=True)
    batch = db.Column(db.String(500), nullable = False)   
    wafer = db.Column(db.String(500), nullable = False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

class QA(db.Model):
    channel_1 = db.Column(db.String, primary_key=True)
    channel_2 = db.Column(db.String)
    channel_3 = db.Column(db.String)
    channel_4 = db.Column(db.String)
    channel_5 = db.Column(db.String)
    
class EQA(db.Model):
    channel_1 = db.Column(db.String, primary_key=True)
    channel_2 = db.Column(db.String)
    channel_3 = db.Column(db.String)
    channel_4 = db.Column(db.String)
    channel_5 = db.Column(db.String)

class LQA(db.Model):
    channel_1 = db.Column(db.String, primary_key=True)
    channel_2 = db.Column(db.String)
    channel_3 = db.Column(db.String)
    channel_4 = db.Column(db.String)
    channel_5 = db.Column(db.String)