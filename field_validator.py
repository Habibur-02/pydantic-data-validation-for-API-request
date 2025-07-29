from pydantic import BaseModel , EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict,Optional,Annotated

#Field function custom data banate help kore
#Annotade metadata banate help kore
#Field Annotade er moddho o kaj kore, default o banate help kore data k



class patients(BaseModel):
    name: str = Annotated[str,Field(max_length=10,description="Hii",title="write your name",example=["Habibur","Rahman"])]
    age: int
    email: EmailStr
    url: AnyUrl
    weight: Annotated[float, Field(gt=0,lt=120,strict=True)]
    married: bool = False
    allergies: Annotated[Optional[list[str]],Field(default=None,max_length=2)]
    contact: Dict[str,str]
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_mail=["sonali.com","rupali.com.bd","ruet.ac.bd"]
        extract_mail=value.split('@')[-1]
        if extract_mail not in valid_mail:
            raise ValueError(404,"Not a corrected mail")
        return value
    @field_validator('name')
    @classmethod
    def name_transform(cls, value):
        return value.upper()
    #eta field function a gt,lt diyeo kora jai.
    @field_validator('age',mode='before')
    @classmethod
    def Age(cls, value):
        if 0<value<100:
            return value
        else:
            return ValueError(404,"Hoga mara sara")






def print_patient_info(patient: patients):
    print(patient.age)
    print(patient.name)
    print(patient.married)
    print(patient.allergies)
    print(patient.email)
    print(patient.url)

patient_info={'name':'Aasif',
              'age': 25,
              'email':'abc@sonali.com',
              'url':'https://asif.com',
              'weight': 18,
              'married': True,
              'allergies':['pollen','dust'],
              'contact':{'email':'abc@gmail.com',
                         'phone':'+8801748150901'}}

patient=patients(**patient_info)

print_patient_info(patient)


