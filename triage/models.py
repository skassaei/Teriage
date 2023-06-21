from django.utils.timezone import now
from django.db import models

# Create your models here.
class Triage(models.Model):
    first_name = models.CharField('نام', max_length=50, default='نامعلوم')  # type of the value
    last_name = models.CharField('نام خانوادگی' ,max_length=50, default='نامعلوم')
    admintion_date = models.DateField('تاریخ مراجعه' ,null=True,default=now)
    admintion_time = models.TimeField('ساعت مراجعه' ,null=True)
    age = models.PositiveSmallIntegerField('سن', default='نامعلوم')
    gender_choices = (
        ('1' ,'زن'),
        ('2' ,'مرد'),
        ('3' ,'باردار'),
    )
    gender = models.CharField('جنس' ,max_length=50, choices=gender_choices)
    transportion_choices =  (
        ('1' ,'آمبولانس خصوصی 115'),
        ('2' ,' آمبولانس خصوصی'),
        ('3' ,'وسیله شخصی'),
        ('3' ,'امداد هوایی'),
    )
    transportion = models.CharField('نحوه ارجاع' ,max_length=50, choices=transportion_choices ,null=True ,blank=True)
    other = models.CharField('other' ,max_length=200, blank=True)
    #
    visit_last24hour = models.BooleanField('مراجعه 24 ساعت قبل')


    pationt_main_complaint = models.CharField('شکایت اصلی بیمار' ,max_length=1000)
    Alergics = models.CharField('سابقه حساسیت دارویی و غذایی' ,max_length=1000, null=True)

    # -------------

    consciousness_choices =  (
        ('1' ,'A'),
        ('1' ,'V'),
        ('1' ,'P'),
        ('1' ,'U'),

    )
    level_of_consciousness = models.CharField('level_of_consciousness' ,max_length=200 ,choices=consciousness_choices)

    # ----Airway_hazard---
    respiratory_distress = models.BooleanField('دیسترس تنفس',default=False) #SP added default for migration
    airway_risk = models.BooleanField('مخاطره راه هوایی',default=False) #SP default added for migration
    cyanosis = models.BooleanField('سیانوز',default=False) #SP added default for migration
    shock_symptoms = models.BooleanField('علایم شوک',default=False) #SP added default for migration
    Spo2_90 = models.BooleanField('Spo2<90',default=False) #SP added default for migration

    # ---بیماران پرخطر (سطح 2)---
    # dangerous_conditions
    Lethargy_and_sleepiness = models.BooleanField('لتارژی و خواب آلودگی')
    Pain_with_severe_distress = models.BooleanField(' درد با دیسترس شدید')
    # ----------------------------------------------------------
    medical_record =models.CharField('سابقه پزشکی', max_length=200, null=True, blank=True)
    medication_history = models.CharField('سابقه دارویی', max_length=200, null=True, blank=True)

    # -------- vital_Signs-----------
    vital_Signs2_BP = models.CharField('vital_Signs2_BP', max_length=200, null=True, blank=True)
    vital_Signs2_RP = models.CharField('vital_Signs2_RP', max_length=200, null=True, blank=True)
    vital_Signs2_RR = models.CharField('vital_Signs2_RR', max_length=200, null=True, blank=True)
    vital_Signs2_T = models.CharField('vital_Signs2_T', max_length=200, null=True, blank=True)
    vital_Signs2_Spo2 = models.CharField('vital_Signs2_Spo2', max_length=200, null=True, blank=True)

    # ---بیماران پرخطر (سطح 3)---
    Facilities = models.BooleanField('تعداد تسهیلات مورد نظر بیمار اورژانس')
    vital_Signs3_BP = models.CharField('vital_Signs3_BP', max_length=200, null=True, blank=True)
    vital_Signs3_RP = models.CharField('vital_Signs3_RP', max_length=200, null=True, blank=True)
    vital_Signs3_RR = models.CharField('vital_Signs3_RR', max_length=200, null=True, blank=True)
    vital_Signs3_T = models.CharField('vital_Signs3_T', max_length=200, null=True, blank=True)
    vital_Signs3_Spo2 = models.CharField('vital_Signs3_Spo2', max_length=200, null=True, blank=True)

    Facility_Nums = (
        ('1', 'یک مورد'),
        ('2', 'هیچ')
    )
    faculties = models.CharField('تعداد تسهیلات مورد نیاز بیمار در اورژانس', max_length=25, choices=Facility_Nums)
    Triage_Levels = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    level_of_triage = models.CharField('سطح تریاژ بیمار', max_length=2, choices=Triage_Levels)

    emergency_department_choices = (
        ('1', 'بخش 1'),
        ('2', 'بخش 4'),
        ('3', '5 بخش'),
        ('4', 'بخش 6'),
        ('5', 'بخش 7'),
        ('6', 'بخش 8'),
        ('7', 'CCU'),
        ('8', 'اتاق عمل'),
        ('9', 'آنژیوگرافی'),
        ('10', 'زایمان'),
        ('11', 'NICU'),

    )
    emergency_department = models.CharField('ارجاع به کدام قسمت بخش اورژانس', max_length=25,
                                            choices=emergency_department_choices)

    # emergency_department = models.CharField(max_length=75)
    # referal_time = models.DateTimeField()
    triage_nurse_name = models.CharField('نام و امضای پرستار تریاژ', max_length=50, null=True)