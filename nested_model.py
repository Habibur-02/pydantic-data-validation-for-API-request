from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address  # Nested model

# Create address instance
address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}
address1 = Address(**address_dict)


patient_dict = {
    'name': 'nitish',
    'gender': 'male', 
    'age': 35,
    'address': address1
}
patient1 = Patient(**patient_dict)

# Correct usage of model_dump() with include/exclude
temp = patient1.model_dump()  # Serialize entire model
print(temp)
print(type(temp))  # <class 'dict'>

# Example with include/exclude
partial_data = patient1.model_dump(include={'name', 'age'})
print("\nPartial data (name and age only):")
print(partial_data)

nested_data = patient1.model_dump(include={'name', 'address'})
print("\nNested selective data:")
print(nested_data)






















# Better organization of related data (e.g., vitals, address, insurance)

# Reusability: Use Vitals in multiple models (e.g., Patient, MedicalRecord)

# Readability: Easier for developers and API consumers to understand

# Validation: Nested models are validated automatically—no extra work needed