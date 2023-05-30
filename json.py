# import json
#
# class Car:
#     def __init__(self, brand, model, year, body_type, doors, color):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.body_type = body_type
#         self.doors = doors
#         self.color = color
#
#     def to_json(self):
#         return json.dumps({
#             'brand': self.brand,
#             'model': self.model,
#             'year': self.year,
#             'body_type': self.body_type,
#             'doors': self.doors,
#             'color': self.color
#         })
#
# car = Car('BMW', 'X5', 2021, 'SUV', 5, 'black')
# json_string = car.to_json()
# print(json_string)