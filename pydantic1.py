from pydantic import BaseModel , EmailStr, AnyUrl, Field
from typing import List, Dict,Optional,Annotated
#Field function custom data banate help kore
#Annotade metadata banate help kore
#Field Annotade er moddho o kaj kore, default o banate help kore data k


class patients(BaseModel):
    name: str = Annotated[str,Field(max_length=10,description="Hii",title="write your name",example=["Habibur","Rahman"])]
    age: int
    email: EmailStr
    url: AnyUrl
    weight: float = Field(gt=0,lt=120)
    married: bool = False
    allergies: Annotated[Optional[list[str]],Field(default=None,max_length=2)]
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
              'weight': '12',
              'married': True,
              'allergies':['pollen','dust'],
              'contact':{'email':'abc@gmail.com',
                         'phone':'+8801748150901'}}

patient=patients(**patient_info)

print_patient_info(patient)

# print(patient.age)
# print(patient.name)

