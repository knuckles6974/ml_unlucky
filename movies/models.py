from django.db import models



class MovieInfo(models.Model):
    name = models.TextField()
    original_name = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    genre = models.CharField(max_length=10)
    running_time = models.IntegerField()
    director = models.CharField(max_length=30)
    cast = models.TextField()
    synopsis = models.TextField()
    like = models.BooleanField(default=True)
    dislike = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'movieinfos'
    
     
class MovieVideo(models.Model):
    teaser = models.URLField()
    shorts = models.URLField()
    trailer = models.URLField()
    movieinfo = models.OneToOneField('Movieinfo', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'movievideos'
 
 
class MovieImage(models.Model):
    image_url = models.URLField(max_length=1000)
    movieinfo = models.ForeignKey('Movieinfo', on_delete=models.CASCADE)

    
    class Meta:
        db_table = 'movieimages'