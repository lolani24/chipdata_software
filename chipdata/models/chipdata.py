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
    channel_1_note = db.Column(db.String)
    channel_2 = db.Column(db.String)
    channel_2_note = db.Column(db.String)
    channel_3 = db.Column(db.String)
    channel_3_note = db.Column(db.String)
    channel_4 = db.Column(db.String)
    channel_4_note = db.Column(db.String)
    channel_5 = db.Column(db.String)
    channel_5_note = db.Column(db.String)
    
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
    channel_1_dirac_voltage = db.Column(db.String)
    channel_1_slope = db.Column(db.String)
    channel_2_min = db.Column(db.String)
    channel_2_max = db.Column(db.String)
    channel_2_dirac_voltage = db.Column(db.String)
    channel_2_slope = db.Column(db.String)
    channel_3_min = db.Column(db.String)
    channel_3_max = db.Column(db.String)
    channel_3_dirac_voltage = db.Column(db.String)
    channel_3_slope = db.Column(db.String)
    channel_4_min = db.Column(db.String)
    channel_4_max = db.Column(db.String)
    channel_4_dirac_voltage = db.Column(db.String)
    channel_4_slope = db.Column(db.String)
    channel_5_min = db.Column(db.String)
    channel_5_max = db.Column(db.String)
    channel_5_dirac_voltage = db.Column(db.String)
    channel_5_slope = db.Column(db.String)

# ME Chip Tables 
class BatchME(db.Model):
    __tablename__ = 'batchME'
    id = db.Column(db.Integer, primary_key=True)
    batchME_number = db.Column(db.Integer)
    wafersME = db.relationship('WaferME', back_populates ='batchME') # wafer to batch

class WaferME(db.Model):
    __tablename__ = 'waferME'
    id = db.Column(db.Integer, primary_key=True)
    waferME_number = db.Column(db.Integer)
    batchME_id = db.Column(db.Integer, db.ForeignKey('batchME.id') )
    chipsME = db.relationship('ChipME', back_populates ='waferME') #chip to wafer
    batchME = db.relationship('BatchME', back_populates = 'wafersME')

class ChipME(db.Model):
    __tablename__ = 'chipME'
    id = db.Column(db.Integer, primary_key=True)
    chipME = db.Column(db.String(2))
    waferME_id = db.Column(db.Integer, db.ForeignKey('waferME.id') ) 
    waferME = db.relationship('WaferME', back_populates='chipsME')
    oqaME = db.relationship('OQAme', back_populates ='chipME') #oqa to chip 
    lqaME = db.relationship('LQAme', back_populates ='chipME') #lqa to chip
    eqaME = db.relationship('EQAme', back_populates ='chipME') #eqa to chip 

class OQAme(db.Model):
    __tablename__ = 'OQAme'
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    chipME_id = db.Column(db.Integer, db.ForeignKey('chipME.id') ) 
    chipME = db.relationship('ChipME', back_populates='oqaME')
    channel_1_ME = db.Column(db.String)
    channel_1_note_ME = db.Column(db.String)
    channel_2_ME = db.Column(db.String)
    channel_2_note_ME = db.Column(db.String)
    channel_3_ME = db.Column(db.String)
    channel_3_note_ME = db.Column(db.String)
    channel_4_ME = db.Column(db.String)
    channel_4_note_ME = db.Column(db.String)
    channel_5_ME = db.Column(db.String)
    channel_5_note_ME = db.Column(db.String)
    
class EQAme(db.Model):
    __tablename__ = 'EQAme'
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    chipME_id = db.Column(db.Integer, db.ForeignKey('chipME.id') ) 
    chipME = db.relationship('ChipME', back_populates='eqaME')
    Reschannel_1_ME = db.Column(db.String)
    Reschannel_2_ME = db.Column(db.String)
    Reschannel_3_ME = db.Column(db.String)
    Reschannel_4_ME = db.Column(db.String)
    Reschannel_5_ME = db.Column(db.String)

class LQAme(db.Model):
    __tablename__ = 'LQAme'
    id = db.Column(db.Integer, primary_key= True, nullable = False)
    chipME_id = db.Column(db.Integer, db.ForeignKey('chipME.id') )
    chipME = db.relationship('ChipME', back_populates='lqaME') 
    channel_1_min_ME = db.Column(db.String)
    channel_1_max_ME = db.Column(db.String)
    channel_1_dirac_voltage_ME = db.Column(db.String)
    channel_1_slope_ME = db.Column(db.String)
    channel_2_min_ME = db.Column(db.String)
    channel_2_max_ME = db.Column(db.String)
    channel_2_dirac_voltage_ME = db.Column(db.String)
    channel_2_slope_ME = db.Column(db.String)
    channel_3_min_ME = db.Column(db.String)
    channel_3_max_ME = db.Column(db.String)
    channel_3_dirac_voltage_ME = db.Column(db.String)
    channel_3_slope_ME = db.Column(db.String)
    channel_4_min_ME = db.Column(db.String)
    channel_4_max_ME = db.Column(db.String)
    channel_4_dirac_voltage_ME = db.Column(db.String)
    channel_4_slope_ME = db.Column(db.String)
    channel_5_min_ME = db.Column(db.String)
    channel_5_max_ME = db.Column(db.String)
    channel_5_dirac_voltage_ME = db.Column(db.String)
    channel_5_slope_ME = db.Column(db.String)