from django.db import models
from utills.uuid import CustomUUIDField
from app.base.models import BaseModel
from django.utils.timezone import now
from app.authentication.models import BracHChoice
from safedelete.models import SOFT_DELETE_CASCADE, HARD_DELETE

class Discount(BaseModel):
  name = models.CharField("insurance name", max_length=50)
  is_rate = models.BooleanField("is_rate", default=True)
  discount_rate = models.FloatField("discount_rate")
  discount_amount = models.PositiveIntegerField("discount_amount")

  class Meta:    
    verbose_name = 'Discount'
    verbose_name_plural = verbose_name

  def __str__(self):
      return f'{self.name}'


class Patient(BaseModel):    
  discount_set = models.ManyToManyField("patient.Discount", verbose_name="discount reason", blank= True)
  name = models.CharField("name", max_length=50)
  BLOOD_TYPE_CHOICES=[
  ('A','A'), 
  ('B', 'B'),
  ('AB','AB'),
  ('O', 'O'),
  ]
  blood_type = models.CharField(
    max_length=50,
    choices=BLOOD_TYPE_CHOICES,
    default=None
  )
  GENDER_CHOICES=[
    ('Perempuan', "Perempuan"),
    ('Laki-laki', 'Laki-laki')
  ]
  gender = models.CharField(
    max_length=50,
    choices= GENDER_CHOICES,
    default=None
  )
  address = models.CharField("Address", max_length=250)

  branch = models.CharField(
    max_length=10,
    choices=BracHChoice.choices,
    default=None,
    null=True
  )
  birth_date = models.DateField('date of birth', null=True, blank=True)
  birth_place = models.CharField('place of birth', max_length=50,null=True, blank=True)
  occupation= models.CharField('occupation', max_length=50,null=True, blank=True)
  mobile = models.CharField('mobile', max_length=50, null=True, blank=True)
  odontogram = models.ForeignKey("patient.Odontogram", verbose_name="odontogram", on_delete=models.CASCADE, null=True, blank=True)
  uuid = CustomUUIDField()
  last_scaling_date = models.DateField('last scaling date', null=True, blank=True)
  last_visit_date = models.DateField('last visit date', null=True, blank=True)
  updated_date = models.DateTimeField("last modified", auto_now=True)


  class Meta:    
      verbose_name = 'Patient'
      verbose_name_plural = verbose_name
      ordering = ['-updated_date']

  def __str__(self):
      return f'{self.name}'


class Odontogram(BaseModel):

  MOUTH_CHOICES = (
    ('C', 'C'),
    ('D', 'D'),
    ('M', 'M'),
    ('F', 'F'),
    ('I', 'I'),
    ('K', 'K'),
    ('G', 'G'),
    ('T', 'T'),
    ('I', 'I'),
    ('Ab', 'Ab'),
    ('At', 'At'),
    ('Fr', 'Fr'),
    ('MP', 'Mp'),
    )
  t_11_1 = models.CharField(verbose_name="11_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_11_2 = models.CharField(verbose_name="11_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_11_3 = models.CharField(verbose_name="11_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_12_1 = models.CharField(verbose_name="12_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_12_2 = models.CharField(verbose_name="12_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_12_3 = models.CharField(verbose_name="12_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_13_1 = models.CharField(verbose_name="13_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_13_2 = models.CharField(verbose_name="13_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_13_3 = models.CharField(verbose_name="13_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_14_1 = models.CharField(verbose_name="14_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_14_2 = models.CharField(verbose_name="14_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_14_3 = models.CharField(verbose_name="14_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_15_1 = models.CharField(verbose_name="15_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_15_2 = models.CharField(verbose_name="15_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_15_3 = models.CharField(verbose_name="15_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_16_1 = models.CharField(verbose_name="16_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_16_2 = models.CharField(verbose_name="16_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_16_3 = models.CharField(verbose_name="16_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_17_1 = models.CharField(verbose_name="17_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_17_2 = models.CharField(verbose_name="17_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_17_3 = models.CharField(verbose_name="17_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_18_1 = models.CharField(verbose_name="18_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_18_2 = models.CharField(verbose_name="18_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_18_3 = models.CharField(verbose_name="18_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_21_1 = models.CharField(verbose_name="21_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_21_2 = models.CharField(verbose_name="21_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_21_3 = models.CharField(verbose_name="21_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_22_1 = models.CharField(verbose_name="22_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_22_2 = models.CharField(verbose_name="22_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_22_3 = models.CharField(verbose_name="22_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_23_1 = models.CharField(verbose_name="23_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_23_2 = models.CharField(verbose_name="23_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_23_3 = models.CharField(verbose_name="23_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_24_1 = models.CharField(verbose_name="24_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_24_2 = models.CharField(verbose_name="24_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_24_3 = models.CharField(verbose_name="24_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_25_1 = models.CharField(verbose_name="25_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_25_2 = models.CharField(verbose_name="25_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_25_3 = models.CharField(verbose_name="25_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_26_1 = models.CharField(verbose_name="26_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_26_2 = models.CharField(verbose_name="26_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_26_3 = models.CharField(verbose_name="26_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_27_1 = models.CharField(verbose_name="27_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_27_2 = models.CharField(verbose_name="27_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_27_3 = models.CharField(verbose_name="27_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_28_1 = models.CharField(verbose_name="28_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_28_2 = models.CharField(verbose_name="28_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_28_3 = models.CharField(verbose_name="28_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_31_1 = models.CharField(verbose_name="31_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_31_2 = models.CharField(verbose_name="31_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_31_3 = models.CharField(verbose_name="31_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_32_1 = models.CharField(verbose_name="32_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_32_2 = models.CharField(verbose_name="32_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_32_3 = models.CharField(verbose_name="32_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_33_1 = models.CharField(verbose_name="33_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_33_2 = models.CharField(verbose_name="33_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_33_3 = models.CharField(verbose_name="33_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_34_1 = models.CharField(verbose_name="34_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_34_2 = models.CharField(verbose_name="34_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_34_3 = models.CharField(verbose_name="34_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_35_1 = models.CharField(verbose_name="35_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_35_2 = models.CharField(verbose_name="35_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_35_3 = models.CharField(verbose_name="35_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_36_1 = models.CharField(verbose_name="36_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_36_2 = models.CharField(verbose_name="36_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_36_3 = models.CharField(verbose_name="36_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_37_1 = models.CharField(verbose_name="37_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_37_2 = models.CharField(verbose_name="37_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_37_3 = models.CharField(verbose_name="37_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_38_1 = models.CharField(verbose_name="38_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_38_2 = models.CharField(verbose_name="38_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_38_3 = models.CharField(verbose_name="38_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_41_1 = models.CharField(verbose_name="41_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_41_2 = models.CharField(verbose_name="41_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_41_3 = models.CharField(verbose_name="41_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_42_1 = models.CharField(verbose_name="42_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_42_2 = models.CharField(verbose_name="42_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_42_3 = models.CharField(verbose_name="42_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_43_1 = models.CharField(verbose_name="43_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_43_2 = models.CharField(verbose_name="43_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_43_3 = models.CharField(verbose_name="43_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_44_1 = models.CharField(verbose_name="44_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_44_2 = models.CharField(verbose_name="44_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_44_3 = models.CharField(verbose_name="44_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_45_1 = models.CharField(verbose_name="45_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_45_2 = models.CharField(verbose_name="45_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_45_3 = models.CharField(verbose_name="45_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_46_1 = models.CharField(verbose_name="46_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_46_2 = models.CharField(verbose_name="46_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_46_3 = models.CharField(verbose_name="46_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_47_1 = models.CharField(verbose_name="47_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_47_2 = models.CharField(verbose_name="47_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_47_3 = models.CharField(verbose_name="47_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_48_1 = models.CharField(verbose_name="48_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_48_2 = models.CharField(verbose_name="48_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_48_3 = models.CharField(verbose_name="48_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_51_1 = models.CharField(verbose_name="51_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_51_2 = models.CharField(verbose_name="51_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_51_3 = models.CharField(verbose_name="51_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_52_1 = models.CharField(verbose_name="52_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_52_2 = models.CharField(verbose_name="52_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_52_3 = models.CharField(verbose_name="52_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_53_1 = models.CharField(verbose_name="53_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_53_2 = models.CharField(verbose_name="53_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_53_3 = models.CharField(verbose_name="53_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_54_1 = models.CharField(verbose_name="54_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_54_2 = models.CharField(verbose_name="54_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_54_3 = models.CharField(verbose_name="54_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_55_1 = models.CharField(verbose_name="55_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_55_2 = models.CharField(verbose_name="55_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_55_3 = models.CharField(verbose_name="55_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_61_1 = models.CharField(verbose_name="61_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_61_2 = models.CharField(verbose_name="61_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_61_3 = models.CharField(verbose_name="61_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_62_1 = models.CharField(verbose_name="62_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_62_2 = models.CharField(verbose_name="62_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_62_3 = models.CharField(verbose_name="62_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_63_1 = models.CharField(verbose_name="63_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_63_2 = models.CharField(verbose_name="63_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_63_3 = models.CharField(verbose_name="63_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_64_1 = models.CharField(verbose_name="64_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_64_2 = models.CharField(verbose_name="64_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_64_3 = models.CharField(verbose_name="64_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_65_1 = models.CharField(verbose_name="65_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_65_2 = models.CharField(verbose_name="65_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_65_3 = models.CharField(verbose_name="65_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_71_1 = models.CharField(verbose_name="71_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_71_2 = models.CharField(verbose_name="71_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_71_3 = models.CharField(verbose_name="71_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_72_1 = models.CharField(verbose_name="72_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_72_2 = models.CharField(verbose_name="72_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_72_3 = models.CharField(verbose_name="72_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_73_1 = models.CharField(verbose_name="73_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_73_2 = models.CharField(verbose_name="73_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_73_3 = models.CharField(verbose_name="73_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_74_1 = models.CharField(verbose_name="74_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_74_2 = models.CharField(verbose_name="74_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_74_3 = models.CharField(verbose_name="74_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_75_1 = models.CharField(verbose_name="75_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_75_2 = models.CharField(verbose_name="75_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_75_3 = models.CharField(verbose_name="75_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_81_1 = models.CharField(verbose_name="81_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_81_2 = models.CharField(verbose_name="81_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_81_3 = models.CharField(verbose_name="81_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_82_1 = models.CharField(verbose_name="82_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_82_2 = models.CharField(verbose_name="82_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_82_3 = models.CharField(verbose_name="82_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_83_1 = models.CharField(verbose_name="83_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_83_2 = models.CharField(verbose_name="83_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_83_3 = models.CharField(verbose_name="83_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_84_1 = models.CharField(verbose_name="84_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_84_2 = models.CharField(verbose_name="84_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_84_3 = models.CharField(verbose_name="84_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)

  t_85_1 = models.CharField(verbose_name="85_1",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_85_2 = models.CharField(verbose_name="85_2",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)
  t_85_3 = models.CharField(verbose_name="85_3",max_length=90, choices=MOUTH_CHOICES, default=None, blank=True, null=True)



  class Meta:    
    verbose_name = 'Odontogram'
    verbose_name_plural = verbose_name

