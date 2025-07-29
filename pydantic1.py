from pydantic import BaseModel

class patients(BaseModel):
    name: str
    age: int

def print_patient_info(patient: patients):
    print(patient.age)
    print(patient.name)

patient_info={'name':'Aasif',
              'age': 25}

patient=patients(**patient_info)

print_patient_info(patient)

print(patient.age)
print(patient.name)

