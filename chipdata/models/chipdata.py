from extensions import db



class Batch(db.Model):
    __tablename__ = 'batch'
    id = db.Column(db.Integer, primary_key=True)
    wafer = db.relationship('Wafer', backref ='batch') # wafer to batch

class Wafer(db.Model):
    __tablename__ = 'wafer'
    id = db.Column(db.Integer, primary_key=True)
    batch_id = db.Column(db.Integer, db.ForeignKey('batch.id') )
    chip = db.relationship('Chip', backref ='wafer') #chip to wafer


class Chip(db.Model):
    __tablename__ = 'chip'
    id = db.Column(db.Integer, primary_key=True)
    chips = db.Column(db.String(2))
    wafer_id = db.Column(db.Integer, db.ForeignKey('wafer.id') ) 
    oqa = db.relationship('OQA', backref ='chip') #oqa to chip 
    lqa = db.relationship('LQA', backref ='chip') #lqa to chip
    eqa = db.relationship('EQA', backref ='chip') #eqa to chip 

class OQA(db.Model):
    __tablename__ = 'OQA'
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    chip_id = db.Column(db.Integer, db.ForeignKey('chip.id') ) 
    channel_1 = db.Column(db.String)
    channel_2 = db.Column(db.String)
    channel_3 = db.Column(db.String)
    channel_4 = db.Column(db.String)
    channel_5 = db.Column(db.String)
    
class EQA(db.Model):
    __tablename__ = 'EQA'
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    chip_id = db.Column(db.Integer, db.ForeignKey('chip.id') ) 
    Reschannel_1 = db.Column(db.String)
    Reschannel_2 = db.Column(db.String)
    Reschannel_3 = db.Column(db.String)
    Reschannel_4 = db.Column(db.String)
    Reschannel_5 = db.Column(db.String)

class LQA(db.Model):
    __tablename__ = 'LQA'
    id = db.Column(db.Integer, primary_key= True, nullable = False)
    chip_id = db.Column(db.Integer, db.ForeignKey('chip.id') ) 
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