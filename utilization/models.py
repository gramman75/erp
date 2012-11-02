# -*- encoding:utf-8 -*-
from django.db import models

class Department(models.Model):
    '''
    ERP 부서 정보 
    '''
    department_code = models.CharField(primary_key=True, max_length=30)
    department      = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.department
    
    class Meta:
        verbose_name_plural = 'departments'
        db_table = 'xxsm_departments_v'

class Location(models.Model):
    '''
    사업장 위치
    '''
    location_code = models.CharField(primary_key = True, max_length=30)
    location      = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.location
    
    class Meta:
        verbose_name_plural = 'locations'
        db_table = 'xxsm_locations_v'
             
class User(models.Model):

    '''
    ERP사용자 정보 Class
    '''
    user_name       = models.CharField(max_length=100)
    description     = models.CharField(max_length=250)
    department_code = models.ForeignKey(Department) # CharField(max_length=30)
    #department      = models.CharField(max_length=100)
    location_code   = models.ForeignKey(Location) #CharField(max_length=30)
    #location        = models.CharField(max_length=30)
    enable          = models.CharField(max_length=1)
    inactive_date   = models.DateField(null=True,blank=True )
    
    def __unicode__(self):
        return self.user_name
        
    class Meta:
        verbose_name_plural = 'users'
        db_table = 'xxsm_users_v'

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