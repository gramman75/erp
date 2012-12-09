# -*- coding: utf8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Unicode, Sequence

Base = declarative_base()
  
class Application(Base):
    __tablename__ = 'xxsm_applications_v'
    
    application_id  = Column(Integer,primary_key=True)
    application_short_name = Column(String(50))
    application_name = Column(String(240))
    description   = Column(String(240))
        
    program = relationship('Program',backref='xxsm_applications_v')
    
    def __init__(self,application_id, application_short_name, application_name, description):
        self.application_id         = application_id
        self.application_short_name = application_short_name
        self.application_name       = application_name
        self.description            = description
        
    def __repr__(self):
        return '<Application : %s, %s>' % (self.application_short_name, self.application_name)

class Program(Base):
    __tablename__ = 'xxsm_programs_v'
    
    program_id = Column(Integer, primary_key = True)
    #type       = Column(String(30), primary_key = True)
    application_id  = Column('application_id',Integer,ForeignKey('xxsm_applications_v.application_id'))
    program_short_name = Column(String(50))
    program_name = Column(String(240))
    description   = Column(String(240))
    
    application = relationship('Application', backref=backref('xxsm_programs_v'))

        
    def __repr__(self):
        return '<Program : %s, %s>' % (self.program_short_name, self.program_name)  


class OperationUnit(Base):
    __tablename__ = 'xxsm_operation_units_v'
    operation_unit_id = Column(Integer,primary_key=True)
    name              = Column(Unicode(250))  
    
    def __repr__(self):
        return '<Operation Unit : %s>' % (self.name)
    
class Division(Base):
    __tablename__='xxsm_divisions_v'
    
    division_code = Column(String(30),primary_key=True)
    name = Column(Unicode(250))
    
    def __repr__(self):
        return '<Division : %s, %s>' % (self.division_code, self.name)    
    
    
class Notice(Base):
    __tablename__ = 'xxsm_notices'
    
    notice_id = Column(Integer, Sequence('notice_id_seq'),primary_key= True)
    program_id = Column(Integer,ForeignKey('xxsm_programs_v.program_id'))
    from_date  = Column(Date)
    to_date    = Column(Date)
    title      = Column(Unicode(250))
    body       = Column(Unicode(4000))
    
    target = relationship('Target', backref = backref('xxsm_notices'))
    
    def __init__(self,program_id, from_date, to_date, title, body):
        self.program_id = program_id
        self.from_date = from_date
        self.to_date = to_date
        self.title = title
        self.body = body
    def __repr__(self):
        return '<Notice : %s >' %self.title
    
    
class Target(Base):
    __tablename__ ='xxsm_notice_targets'
    
    target_id = Column(Integer,Sequence('target_id_seq'), primary_key=True)
    notice_id = Column(Integer, ForeignKey('xxsm_notices.notice_id'))
    type      = Column(String(30))
    value     = Column(Unicode(100))
    
    notice = relationship('Notice', backref = backref('xxsm_notice_targets'))
    
    def init(self,notice_id, source, value):
        self.notice_id = notice_id
        self.type = source
        self.value = value
        
    def repr(self):
        return '<Target : %s, %s>' %(self.type, self.value)