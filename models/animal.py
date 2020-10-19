
class Animal:
    def __init__(self, id, name, breed, status, locationId, customerId):
        self.id = id
        self.name = name
        self.breed = breed
        self.status = status
        self.location_id = locationId
        self.customer_id = customerId
        self.location = None