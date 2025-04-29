from django.db import models

class Vehicle(models.Model):
    license_plate = models.CharField(max_length=20, unique=True)
    owner_name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.license_plate} - {self.model}"

class Maintenance(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='maintenances')
    description = models.TextField()
    date = models.DateField()
    is_future = models.BooleanField(default=False)  # True if future maintenance

    def __str__(self):
        return f"Maintenance for {self.vehicle.license_plate} on {self.date}"

class Repair(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='repairs')
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"Repair for {self.vehicle.license_plate} on {self.date}"
