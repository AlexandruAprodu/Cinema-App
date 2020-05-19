from Film import Film


class Animate(Film):
    def __init__(self, titlu, durata, sala, varsta_minima, audio_dublat, limba_dublare, categorie):
        super().__init__(titlu, durata, sala)
        self.varsta_minima = varsta_minima
        self.audio_dublat = audio_dublat
        self.limba_dublare = limba_dublare
        self.categorie = categorie

    # def __call__(self, *args, **kwargs):
    #     return self

