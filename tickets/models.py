from django.db import models


# Create your models here.
class Ticket(models.Model):
    STATUSES = (
        ("New", "New"),
        ("Assigned", "Assigned"),
        ("Work in Progress", "Work in Progress"),
        ("Completed", "Completed"),
        ("Closed", "Closed"),
        ("Re-Opened", "Re-Opened")
    )
    PRIORITIES = (
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High")
    )
    EMPLOYEES = (
        ("Ajay", "Ajay"),
        ("Akshay", "Akshay"),
        ("Amir", "Amir")
    )

    ticketId = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=500, null=False)
    description = models.CharField(max_length=2000, null=False)
    status = models.CharField(max_length=50, choices=STATUSES, null=False)
    priority = models.CharField(max_length=50, choices=PRIORITIES, null=False)
    createdOn = models.DateTimeField(null=False)
    employeeName = models.CharField(max_length=50, choices=EMPLOYEES, null=False)

    def __str__(self):
        return "{} - {} - {} - {} - {} - {} - {}" \
            .format(self.ticketId, self.subject, self.description, self.status, self.priority, self.createdOn,
                    self.employeeName)



