from pydantic import BaseModel

class patients(BaseModel):
    name: str
    age: int

patient_info={'name':'Aasif',
              'age': 25}

patient=patients(**patient_info)

print(patient.age)
print(patient.name)