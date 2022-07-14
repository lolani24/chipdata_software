from extensions import db



class Batch(db.Model):
    __tablename__ = 'batch'
    id = db.Column(db.Integer, primary_key=True)
    batch_number = db.Column(db.Integer)
    wafers = db.relationship('Wafer', back_populates ='batch') # wafer to batch

class Wafer(db.Model):
    __tablename__ = 'wafer'
    id = db.Column(db.Integer, primary_key=True)
    wafer_number = db.Column(db.Integer)
    batch_id = db.Column(db.Integer, db.ForeignKey('batch.id') )
    chips = db.relationship('Chip', back_populates ='wafer') #chip to wafer
    batch = db.relationship('Batch', back_populates = 'wafers')

class Chip(db.Model):
    __tablename__ = 'chip'
    id = db.Column(db.Integer, primary_key=True)
    chip = db.Column(db.String(2))
    wafer_id = db.Column(db.Integer, db.ForeignKey('wafer.id') ) 
    wafer = db.relationship('Wafer', back_populates='chips')
    oqa = db.relationship('OQA', back_populates ='chip') #oqa to chip 
    lqa = db.relationship('LQA', back_populates ='chip') #lqa to chip
    eqa = db.relationship('EQA', back_populates ='chip') #eqa to chip 

class OQA(db.Model):
    __tablename__ = 'OQA'
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    chip_id = db.Column(db.Integer, db.ForeignKey('chip.id') ) 
    chip = db.relationship('Chip', back_populates='oqa')
    channel_1 = db.Column(db.String)
    channel_2 = db.Column(db.String)
    channel_3 = db.Column(db.String)
    channel_4 = db.Column(db.String)
    channel_5 = db.Column(db.String)
    
class EQA(db.Model):
    __tablename__ = 'EQA'
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    chip_id = db.Column(db.Integer, db.ForeignKey('chip.id') ) 
    chip = db.relationship('Chip', back_populates='eqa')
    Reschannel_1 = db.Column(db.String)
    Reschannel_2 = db.Column(db.String)
    Reschannel_3 = db.Column(db.String)
    Reschannel_4 = db.Column(db.String)
    Reschannel_5 = db.Column(db.String)

class LQA(db.Model):
    __tablename__ = 'LQA'
    id = db.Column(db.Integer, primary_key= True, nullable = False)
    chip_id = db.Column(db.Integer, db.ForeignKey('chip.id') )
    chip = db.relationship('Chip', back_populates='lqa') 
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