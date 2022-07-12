from extensions import db
from datetime import datetime

    
class Chip(db.Model):
    id = db.Column(db.String, primary_key=True)
    batch = db.Column(db.String(500), nullable = False)   
    wafer = db.Column(db.String(500), nullable = False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

class QA(db.Model):
    __tablename__ = 'QA'
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    channel_1 = db.Column(db.String)
    channel_2 = db.Column(db.String)
    channel_3 = db.Column(db.String)
    channel_4 = db.Column(db.String)
    channel_5 = db.Column(db.String)
    
class EQA(db.Model):
    __tablename__ = 'EQA'
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    Reschannel_1 = db.Column(db.String)
    Reschannel_2 = db.Column(db.String)
    Reschannel_3 = db.Column(db.String)
    Reschannel_4 = db.Column(db.String)
    Reschannel_5 = db.Column(db.String)

class LQA(db.Model):
    __tablename__ = 'LQA'
    id = db.Column(db.Integer, primary_key= True, nullable = False)
    channel_1_min = db.Column(db.String)
    channel_1_max = db.Column(db.String)
    channel_1_slope = db.Column(db.String)
    channel_2_min = db.Column(db.String)
    channel_2_max = db.Column(db.String)
    channel_2_slope = db.Column(db.String)
    channel_3_min = db.Column(db.String)
    channel_3_max = db.Column(db.String)
    channel_3_slope = db.Column(db.String)
    channel_4_min = db.Column(db.String)
    channel_4_max = db.Column(db.String)
    channel_4_slope = db.Column(db.String)
    channel_5_min = db.Column(db.String)
    channel_5_max = db.Column(db.String)
    channel_5_slope = db.Column(db.String)