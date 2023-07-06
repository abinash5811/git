employees = [
    {"name": "John Doe", "id": "00123"},
    {"name": "Jane Mary Smith", "id": "04567"},
    {"name": "Alice Bob Carol", "id": "00089"},
]
def generate_email(name,emp_id):
    emp_id=emp_id.lstrip('0')
    name=name.split()
    print(name)
    email_id=name[0]+ '.' +name[-1]
    email = f"{email_id}@company.com"
    return email,emp_id
for employee in employees:
    email,emp_id = generate_email(employee["name"], employee["id"])
    print(f"Employee ID: {emp_id}, Email: {email}")    
