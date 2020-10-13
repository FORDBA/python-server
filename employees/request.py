EMPLOYEES = [
    {
        "id": 1,
        "name": "Emily Lemmon",
        "locationId": 1
    },
    {
        "id": 2,
        "name": "Jordan Castelloe",
        "locationId": 2
    },
    {
        "id": 3,
        "name": "Ryan Tanay",
        "locationId": 2
    },
    {
        "id": 4,
        "name": "Jenna Solis",
        "locationId": 1
    }
]


def get_all_employees():
    return EMPLOYEES


def get_single_employee(id):
    
    requested_employee = None

   
    for employee in EMPLOYEES:
        
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    
    max_id = EMPLOYEES[-1]["id"]

    
    new_id = max_id + 1

    
    employee["id"] = new_id

    
    EMPLOYEES.append(employee)

    
    return employee

def delete_employee(id):
    
    employee_index = None

   
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            
            employee_index = index
            break

    
    if employee_index is not None:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            
            EMPLOYEES[index] = new_employee
            break