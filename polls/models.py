from django.db import models

# Create your models here.
class MyNodel(models.Model):
    property1 = models.CharField(max_length=100)  # Define property1 as a CharField
    property2 = models.IntegerField()  # Define property2 as an IntegerField

    def another_method(self):
        # Method code here
        return self.property1.upper()  # Example code, converting property1 to uppercase