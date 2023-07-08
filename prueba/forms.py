from django import forms

class NombreMesForm(forms.Form):
    OPCIONES_CHOICES = [
        ('opcion0',' '),
        ('Anime', 'Anime'),
        ('Manga', 'Manga'),
        ('Comparacion1','C Manga->Anime'),
        ('Comparacion2', 'C Anime->Manga')
    ]
    OPCIONES_TYPOS = [
        ('opcion18', ' '),
        ('ona', 'ona'),
        ('movie', 'movie'),
        ('ova', 'ova'),
        ('music', 'music'),
        ('tv', 'tv'),
        ('special', 'special'),
        ('manhua', 'manhua'),
        ('light_novel', 'light_novel'),
        ('one_shot', 'one_shot'),
        ('novel', 'novel'),
        ('doujinshi', 'doujinshi'),
        ('manga', 'manga'),
        ('manhwa', 'manhwa'),
     
    ]
    OPCIONES_COMPARACION = [
        ('opcion26',' '),
        ('igual','igual'),
        ('mayor','mayor'),
        ('menor','menor'),
    ]
    OPCIONES_COMPARACION2 = [
        ('opcion25',' '),
        ('IGUAL','igual'),
        ('MAYOR','mayor'),
        ('MENOR','menor'),

    ]
    OPCIONES_GENEROS= [
        ('opcion25',' '),
        ('Action','Action'),
        ('Adventure','Adventure'),
        ('AvantGarde','AvantGarde'),
        ('AwardWinning','AwardWinning'),
        ('BoysLove','BoysLove'),
        ('Comedy','Comedy'),
        ('Drama','Drama'),
        ('Erotica','Erotica'),
        ('Fantasy','Fantasy'),
        ('GirlsLove','GirlsLove'),
        ('Gourmet','Gourmet'),
        ('Hentai','Hentai'),
        ('Horror','Horror'),
        ('Mystery','Mystery'),
        ('Romance','Romance'),
        ('Sci-Fi','Sci-Fi'),
        ('Fantasy','Fantasy'),
        ('SliceofLife','SliceofLife'),
        ('Sports','Sports'),
        ('Supernatural','Supernatural'),
        ('Suspense','Suspense'),
    ]

    campo3 = forms.ChoiceField(label='Eliga accion a buscar',choices=OPCIONES_CHOICES)
    campo4 = forms.ChoiceField(label='Eliga un tipo',choices=OPCIONES_TYPOS)
    nombre = forms.CharField(label='Nombre de la Entidad',max_length=100,required=False)
    campo5 = forms.ChoiceField(label='Score',choices=OPCIONES_COMPARACION)
    campo6 = forms.FloatField(label='que:',max_value=10,min_value=0,required=False)
    campo7 = forms.ChoiceField(label='StartYear',choices=OPCIONES_COMPARACION2)
    campo8 = forms.IntegerField(label='que',min_value=0,required=False)
    campo9 = forms.CharField(label='Author',max_length=100, required=False)
    campo10= forms.ChoiceField(label='Genre',choices=OPCIONES_GENEROS)

class otracosa(forms.Form):
    campo15 = forms.BooleanField(label='Marcar para hacer comparacion con su contraparte',required=False)

