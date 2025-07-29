from pydantic import BaseModel
from typing import List, Dict
class patients(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: list[str]
    contact: Dict[str,str]



def print_patient_info(patient: patients):
    print(patient.age)
    print(patient.name)

patient_info={'name':'Aasif',
              'age': '25',
              'weight': '33.33',
              'married': True,
              'allergies':['pollen','dust'],
              'contact':{'email':'abc@gmail.com',
                         'phone':'+8801748150901'}}

patient=patients(**patient_info)

print_patient_info(patient)

print(patient.age)
print(patient.name)

