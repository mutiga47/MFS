from django.db import models

class PointsConnector(models.Model):
    points_list = models.CharField(max_length=60)
    closest_points_pair = models.CharField(max_length=60)  
    
    #Unit test case
    def __str__(self):
        return self.points_list # + ' ' + self.closest_points_pair