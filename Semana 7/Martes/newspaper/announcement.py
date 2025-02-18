class CommercialAnnouncement:
    def __init__(self, name, dni, section, title, body):
        self.name = name
        self.dni = dni
        self.section = section
        self.title = title
        self.body = body

class ClassifiedAnnouncement:
    def __init__(self, price, publish_date, days, type):
        self.price = price
        self.publish_date = publish_date
        self.days = days
        self.type = type

class VehicleAnnouncement(ClassifiedAnnouncement):
    def __init__(self, price, publish_date, days, brand, model, color, km, year):
        super().__init__(price, publish_date, days, "Vehicle")
        self.brand = brand
        self.model = model
        self.color = color
        self.km = km
        self.year = year

class HomeAnnouncement(ClassifiedAnnouncement):
    def __init__(self, price, publish_date, days, m2, rooms, bathrooms, parking_lot, apply_policy):
        super().__init__(price, publish_date, days, "Home")
        self.m2 = m2
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.parking_lot = parking_lot
        self.apply_policy = apply_policy
