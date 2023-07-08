from django.shortcuts import render
from django.http import HttpResponse
from prueba.models import Mes
from prueba.models import Anime
from prueba.models import Manga
from prueba.models import Author
from prueba.models import Genre2
from prueba.models import Allmangas
from prueba.models import Filtroanime
from django.db import connection
from collections import namedtuple
from django.shortcuts import render
from .forms import NombreMesForm
from .forms import otracosa

# Create your views here.     
def index(request):
    return HttpResponse("Hola, soy una prueba.")

def mayo(request):
    return HttpResponse("El nmero del mes 'Mayo' es "+str(Mes.objects.filter(nombre='Mayo').get().numero))

def mayosql(request):
    return HttpResponse("El nmero del mes 'Mayo' es "+ str(consultar_mes('Mayo').numero))
    
def mes(request):
    # si es POST, tenemos una peticin del usuario
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NombreMesForm(request.POST)
        # verifica que sea valido:
        if form.is_valid():
            nombre_mes = form.cleaned_data['nombre'] if form.cleaned_data['nombre']!= None else ' '        
            sql_res = consultar_mes(nombre_mes)
            #sql_res = compracion_animes(data,tipo,scoreC,scoreN,yearC,yearN)
            if sql_res:
                num_mes = (consultar_mes(nombre_mes))
                #num_res= [data,tipo,scoreC,scoreN,yearC,yearN]
                #a=[str(i) for i in num_mes]
                #res='\n'.join(a)
                res = 'El nmero del mes '+nombre_mes+' es '+str(num_mes)
            else:
                #res=data,tipo,scoreC,scoreN,yearC,yearN
                res = 'El mes '+nombre_mes+' no est en la tabla'
            return render(request, 'mes_form.html', {'mes_form': form, 'resultados': res})
    # si es GET (o algo diferente) crearemos un formulario en blanco
    else:
        form = NombreMesForm()
        form2 =otracosa()
    return render(request, 'mes_form.html', {'mes_form': form,'mes_form2': form2})

def consultar_mes(nombre):	
    with connection.cursor() as cursor:
        results = Anime.objects.filter(name__icontains=nombre)
        #cursor.execute("SELECT * FROM allmangas WHERE name = %s", [nombre])
        #results = namedtuplefetchall(cursor)
    return results

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

#########################################################################################
def mesa(request):

    if request.method == 'POST':

        form = NombreMesForm(request.POST)

        if form.is_valid():
            nombre = form.cleaned_data['nombre'] if form.cleaned_data['nombre'] != None else ' '
            data   = form.cleaned_data['campo3'] if form.cleaned_data['campo3'] != None else ' '
            tipo   = form.cleaned_data['campo4'] if form.cleaned_data['campo4'] != None else ' '
            scoreC = form.cleaned_data['campo5'] if form.cleaned_data['campo5'] != None else ' '
            scoreN = form.cleaned_data['campo6'] if form.cleaned_data['campo6'] != None else ' '
            yearC  = form.cleaned_data['campo7'] if form.cleaned_data['campo7'] != None else ' '
            yearN  = form.cleaned_data['campo8'] if form.cleaned_data['campo8'] != None else ' '
            autor  = form.cleaned_data['campo9'] if form.cleaned_data['campo9'] != None else ' '   
            genero  = form.cleaned_data['campo10'] if form.cleaned_data['campo10'] != None else ' '
            anime_query=[]        
            if data=='Anime':
               anime_query =  Anime.objects.all()
               if nombre != ' ':
                 anime_query = Anime.objects.filter(name__icontains=nombre)


               if scoreN!=' ':
                  if scoreC == 'mayor':
                      anime_query = anime_query.filter(score__gt=scoreN)
                  elif scoreC == 'menor':
                      anime_query = anime_query.filter(score__lt=scoreN)
                  elif scoreC == 'igual':
                      anime_query = anime_query.filter(score=scoreN)
                  elif scoreC == 'opcion26':
                      pass
 
#               # Filtro de formato
               if tipo != 'opcion18':
                  anime_query = anime_query.filter(type=tipo)
 

               if yearN!=' ':
                  if yearC == 'MAYOR':
                     anime_query = anime_query.filter(startyear__gt=yearN)
                  elif yearC == 'MENOR':
                     anime_query = anime_query.filter(startyear__lt=yearN)
                  elif yearC == 'IGUAL':
                     anime_query = anime_query.filter(startyear=yearN)
                  elif yearC == 'opcion25':
                     pass

            elif data=='Manga':
#                 

              anime_query =  Manga.objects.all()
              if nombre != ' ':
                anime_query = Manga.objects.filter(name__icontains=nombre)
 
              if scoreN!=' ':
                 if scoreC == 'mayor':
                    anime_query = anime_query.filter(score__gt=scoreN)
                 elif scoreC == 'menor':
                    anime_query = anime_query.filter(score__lt=scoreN)
                 elif scoreC == 'igual':
                    anime_query = anime_query.filter(score=scoreN)
                 elif scoreC == 'opcion26':
                    pass
              # Filtro de formato
              if tipo!='opcion18':
                  anime_query = anime_query.filter(type=tipo)
              if yearN!=' ':
              # Filtro de ao de inicio
                 if yearC == 'MAYOR':
                    anime_query = anime_query.filter(startyear__gt=yearN)
                 elif yearC == 'MENOR':
                    anime_query = anime_query.filter(startyear__lt=yearN)
                 elif yearC == 'IGUAL':
                    anime_query = anime_query.filter(startyear=yearN)
                 elif yearC == 'opcion25':
                    pass
              if autor!= '':
                 mangasAutor = Author.objects.filter(lastname__icontains=autor)
                 if mangasAutor!=[]:
                    mangasAutor=Author.objects.filter(lastname__icontains=autor)[0].mangaid
                    anime_query=anime_query.filter(mangaid = mangasAutor)
              if genero!='opcion25':
                 mangasGenero = Genre2.objects.filter(genre__icontains = genero)
                 if len(mangasGenero)>0:
                    lista=[]
                    for i in mangasGenero:
                        lista.append(i.mangaid)
                    anime_query=anime_query.filter(mangaid__in=lista)
            elif data=='Comparacion1':
                if Manga.objects.filter(name__icontains=nombre)!=[] and Anime.objects.filter(name__icontains=nombre)!=[]:
                    anime_query =  Anime.objects.all()
                    if nombre != ' ':
                       anime_query = Anime.objects.filter(name__icontains=nombre)
                    if scoreC != 'opcion26':
                        score=Manga.objects.filter(name__icontains=nombre)[0].score
                        if scoreC == 'mayor':
                            anime_query = anime_query.filter(score__gt=score)
                        elif scoreC == 'menor':
                            anime_query = anime_query.filter(score__lt=score)
                        elif scoreC == 'igual':
                            anime_query = anime_query.filter(score=score)
                    if yearC != 'opcion25':
                        year=Manga.objects.filter(name__icontains=nombre)[0].startyear
                        if yearC == 'MAYOR':
                            anime_query = anime_query.filter(startyear__gt=year)
                        elif yearC == 'MENOR':
                            anime_query = anime_query.filter(startyear__lt=year)
                        elif yearC == 'IGUAL':
                            anime_query = anime_query.filter(startyear=year)
                            
            elif data=='Comparacion2':
                if Manga.objects.filter(name__icontains=nombre)!=[] and Anime.objects.filter(name__icontains=nombre)!=[]:
                    anime_query =  Manga.objects.all()
                    if nombre != ' ':
                       anime_query = Manga.objects.filter(name__icontains=nombre)
                    if scoreC != 'opcion26':
                        score=Anime.objects.filter(name__icontains=nombre)[0].score
                        if scoreC == 'mayor':
                            anime_query = anime_query.filter(score__gt=score)
                        elif scoreC == 'menor':
                            anime_query = anime_query.filter(score__lt=score)
                        elif scoreC == 'igual':
                            anime_query = anime_query.filter(score=score)
                    if yearC != 'opcion25':
                        year=Anime.objects.filter(name__icontains=nombre)[0].startyear
                        if yearC == 'MAYOR':
                            anime_query = anime_query.filter(startyear__gt=year)
                        elif yearC == 'MENOR':
                            anime_query = anime_query.filter(startyear__lt=year)
                        elif yearC == 'IGUAL':
                            anime_query = anime_query.filter(startyear=year)  
              
                 
            resultado="" # ("%s",Genre2.objects.filter(genre__icontains = genero)[0].mangaid)
            if anime_query!=[]:
                anime_query=anime_query[:30]
                for objeto in anime_query:
                    if data=='Anime' or data=='Comparacion2' :
                       resultado += f"Nombre: {objeto.name},Tipo: {objeto.type},Score:{objeto.score},Startyear:{objeto.startyear}\n"
                    elif data=='Manga' or data=='Comparacion1':
                       resultado += f"Nombre: {objeto.name},Tipo: {objeto.type},Score:{objeto.score},Startyear:{objeto.startyear}\n"
            return render(request, 'mes_form.html', {'mes_form': form, 'resultados': resultado})
    # si es GET (o algo diferente) crearemos un formulario en blanco
    else: 
        form = NombreMesForm()
    return render(request, 'mes_form.html', {'mes_form': form})