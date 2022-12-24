# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 10:58:56 2022

@author: KIIT
"""
car1_model={'mercedez':1966}
car2_model={'Audi':1977}
car3_model={'Bmw':1988}
car4_model={'Nexon':1999}
car_type={'car1':car1_model,'car2':car2_model,'car3':car3_model,'car4':car4_model}
print(car_type)

print(car_type['car2'])
print(car_type['car3']['Bmw'])