class Zoo:

    def __init__(self, name, number_of_animals, attendance_per_year):
        self.name = name
        self.number_of_animals = number_of_animals
        self.attendance_per_year = attendance_per_year

    def __str__(self):
        return f"Zoo:\t name: {self.name}, number of animals: {self.number_of_animals}, attendance per year: {self.attendance_per_year}"




