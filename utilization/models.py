# -*- coding: utf8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Unicode

Base = declarative_base()
  
class Department(Base):
    __tablename__ = 'xxsm_departments_v'
    department_code = Column(String(30),primary_key=True)
    department      = Column(String(100))
    
    user = relationship('User',backref='xxsm_departments_v')
    
    def __init__(self,department_code, department):
        self.department_code = department_code
        self.department      = department
        
    def __repr__(self):
        return '<Department : %s, %s>' % (self.department_code, self.department)

class Location(Base):
    __tablename__ = 'xxsm_locations_v'
    
    location_code = Column(String(30),primary_key=True)
    location      = Column(String(100))
    
    def __init__(self,location_code, location):
        self.location_code = location_code
        self.location      = location
        
    def __repr__(self):
        return '<Location : %s, %s>' %(self.location_code, self.location)

class User(Base):
    __tablename__ = 'xxsm_users_v'
    
    id = Column(Integer,primary_key=True)
    user_name = Column(String(100))
    description = Column(Unicode(250))
    department_code = Column('department_code_id',String(30),ForeignKey('xxsm_departments_v.department_code'))
    location_code   = Column('location_code_id',String(30),ForeignKey('xxsm_locations_v.location_code'))
    enable          = Column(String(1))
    inactive_date   = Column(Date)  
    password        = Column(String(100))
    
    #department = relationship('Department',backref('xxsm_users_v'))
    #location   = relationship('Location',backref('xxsm_users_v'))   
    
    department = relationship('Department',backref = backref('xxsm_users_v',order_by=id))
    location   = relationship('Location')
    
    def __repr__(self):
        return '<User : %s, %s>' %(self.user_name, self.description)



class UserLogin(Base):
    __tablename__ = 'xxsm_user_logins'
    id = Column(Integer, primary_key=True)
    user_id =  Column(Integer, ForeignKey('xxsm_users_v.id'))
    year    = Column(Integer)
    month   = Column(Integer)
    day     = Column(Integer)
    counts  = Column(Integer)
    
    user = relationship('User',backref=backref('xxsm_user_logins',order_by=id))
                                               
       
class Month(Base):
    __tablename__ = 'xxsm_months'
    month = Column(Integer, primary_key=True)
                                                      
class Computer(Base):
    __tablename__ = 'computer'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(200))
    
    def __repr__(self):
        return '<Computer %s>' %self.name
    
"""    
class UserLogin(models.Model):
    '''
    일별 사용자 Login 횟수
    '''
    
    # composite Key가 지원되지 않음.
    user_id = models.ForeignKey(User,db_column='user_id')
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    counts = models.IntegerField()
    
    def __unicode(self):
        return self.user_id
    
    class Meta:
        db_table = 'xxsm_user_logins'
        verbose_name_plural = 'userlogins'
        
class Responsibility(models.Model):
    '''
    ERP 권한
    '''
    responsibility_id   = models.IntegerField(primary_key=True)
    responsibility_key  = models.CharField(max_length =30)
    responsibility_name = models.CharField(max_length =100)
    active_date         = models.DateField()
    end_date            = models.DateField()
    
    def __unicode(self):
        return self.responsibility_name
    
    class Meta:
        verbose_name_plural = 'responsibilities'
        db_table = 'xxsm_responsibilities_v'
        
class Program(models.Model):
    '''
    ERP에 등록된 프로그램(Form, Concurrent)
    '''
    program_id   = models.IntegerField(primary_key=True)
    responsibility_id = models.ManyToManyField(Responsibility, db_table='xxsm_resp_prog_v')
    program_name = models.CharField(max_length=100)
    description  = models.CharField(max_length=250)
    type         = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.program_name
    
    class Meta:
        db_table = 'xxsm_programs_v'
        verbose_name_plural = 'programs'



class ProgramCount(models.Model):
    '''
    프로그램 사용 횟수
    '''
    program_id        = models.ForeignKey(Program)
    responsibility_id = models.ForeignKey(Responsibility)
    year              = models.IntegerField()
    month             = models.IntegerField()
    day               = models.IntegerField()
    counts            = models.IntegerField()
    
    def __unicode__(self):
        return self.counts
    class Meta:
        db_table = 'xxsm_prog_counts'
        verbose_name_plural = 'programCounts'
        
class ProgramCountDetail(models.Model):
    '''
    프로그램 사용자 정보
    '''
    user_id = models.ForeignKey(User)
    responsibility_id = models.ForeignKey(Responsibility)
    program_id        = models.ForeignKey(Program)
    start_date        = models.DateTimeField()
    end_date          = models.DateTimeField()
    
    def __unicode__(self):
        return self.user_id
    
    class Meta:
        db_table = 'xxsm_prog_count_detail'
        verbose_name_plural = 'programCountDetails'
"""