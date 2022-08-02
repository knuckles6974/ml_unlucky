import json

from django.shortcuts import redirect
from django.views     import View
from django.http      import JsonResponse
from .models          import MovieInfo, MovieVideo, MovieImage

        
    
class MovieInfoView(View):
    def post(self,request):
      try:
          data = json.loads(request.body)
          
          MovieInfo.objects.create(
              
              name = data['name'],
              original_name = data['original_name'],
              rating = data['rating'],
              genre = data['genre'],
              running_time = data['running_time'],
              director = data['director'],
              cast = data['cast'],
              synopsis = data['synopsis'],
              like = 'True',
              dislike = 'False',
              
          )  
          return JsonResponse({"message": "영화정보 등록완료"}, status=201)
      except KeyError:
          return JsonResponse({"message":"KEY_ERROR"}, status=400)
      


class MovieImageView(View):
    def post(self,request):
      try:  
        data = json.loads(request.body)
        
        movieimage = MovieImage(
            image_url = data['image_url'],
            movieinfo_id = data['movieinfo_id']
            
        )
        movieimage.save()
    
        return JsonResponse({"message": "영화이미지 등록완료"}, status=201)
      except KeyError:
          return JsonResponse({"message":"KEY_ERROR"}, status=400)
              
      

class MovieVideoView(View):
    def post(self,request):
      try:
        data = json.loads(request.body)
        
        MovieVideo.objects.create(
            teaser = data['teaser'],
            shorts = data['shorts'],
            trailer = data['trailer'],
            movieinfo_id = data['movieinfo_id']
            
        )
        
        return JsonResponse({"message": "영화예고편 등록완료"}, status=201)
      except KeyError:
        return JsonResponse({"message":"KEY_ERROR"}, status=400) 
      
      
      
class InformationView(View):
    def get(self, request, movieinfo_id):
        if not MovieInfo.objects.filter(id=movieinfo_id).exists():
           return JsonResponse({"message":"INVALID_INFO"}, status=400)
        
        
        movieinfo  = MovieInfo.objects.get(id=movieinfo_id)
        
        data = {}
        
        data["movieimage"] =  [movieimage.image_url 
             for movieimage in movieinfo.movieimage_set.all()],
        data["name"] = movieinfo.name,
        data["original_name"] = movieinfo.original_name,
        data["rating"] = movieinfo.rating,
        data["genre"] = movieinfo.genre,
        data["running_time"] = movieinfo.running_time,
        data["director"] = movieinfo.director,
        data["cast"] = movieinfo.cast,
        data["synopsis"] = movieinfo.synopsis,
        data["like"] = movieinfo.like,
        data["dislike"] = movieinfo.dislike,
        data["teaser"] = movieinfo.movievideo.teaser,
        data["shorts"] = movieinfo.movievideo.shorts,
        data["trailer"] = movieinfo.movievideo.trailer
        
        
        # results = {
        # 'movieimage' : [movieimage.image_url 
        #     for movieimage in movieinfo.movieimage_set.all()],
        # 'name' : movieinfo.name,             
        # 'original_name' : movieinfo.original_name,
        # 'rating' : movieinfo.rating,
        # 'genre' : movieinfo.genre,
        # 'running_time' : movieinfo.running_time,
        # 'director' : movieinfo.director,
        # 'cast' : movieinfo.cast,
        # 'synopsis' : movieinfo.synopsis,
        # 'like' : movieinfo.like,
        # 'dislike' : movieinfo.dislike,
        # 'teaser' : movieinfo.movievideo.teaser,
        # 'shorts' : movieinfo.movievideo.shorts,
        # 'trailer' : movieinfo.movievideo.trailer
        # }    
        return JsonResponse({"movieinfo" : data}, status=200)    
    



class MovieRepairView(View):
    def delete(self,request, movieinfo_id):
        try:
            MovieInfo.objects.get(id=movieinfo_id).delete()
            
            return JsonResponse({"message" : "삭제완료"}, status=204)

        except MovieInfo.DoesNotExist:
            return JsonResponse({"message" : "DOES_NOT_EXIST"}, status=404) 
        
        
        
    def patch(self, request, movieinfo_id):
        try:                
           movieinfos = MovieInfo.objects.get(id=movieinfo_id)
           data = json.loads(request.body)
           movieinfos.running_time = data['running_time']

           movieinfos.save()
           return JsonResponse({"messeage": "수정완료"}, status=201)
        except movieinfos.DoesNotExist: 
           return JsonResponse({"message" : "DOES_NOT_EXIST"}, status=404) 