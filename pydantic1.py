from pydantic import BaseModel , EmailStr, AnyUrl
from typing import List, Dict,Optional
class patients(BaseModel):
    name: str
    age: int
    email: EmailStr
    url: AnyUrl
    weight: float
    married: bool = False
    allergies: Optional[list[str]]=None
    contact: Dict[str,str]



def print_patient_info(patient: patients):
    print(patient.age)
    print(patient.name)
    print(patient.married)
    print(patient.allergies)
    print(patient.email)
    print(patient.url)

patient_info={'name':'Aasif',
              'age': '25',
              'email':'abc@gmail.com',
              'url':'https://asif.com',
              'weight': '33.33',
              'married': True,
              'allergies':['pollen','dust'],
              'contact':{'email':'abc@gmail.com',
                         'phone':'+8801748150901'}}

patient=patients(**patient_info)

print_patient_info(patient)

# print(patient.age)
# print(patient.name)

