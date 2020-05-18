from Film import Film


class Animate(Film):
    def __init__(self, titlu, durata, sala, varsta_minima, audio_dublat, limba_dublare, categorie):
        super().__init__(titlu, durata, sala)
        self.varsta_minima = varsta_minima
        self.audio_dublat = audio_dublat
        self.limba_dublare = limba_dublare
        self.categorie = categorie

    def __call__(self, *args, **kwargs):
        return self


animata = Animate(input('Adauga titlul animatiei: '),
                  input('Adauga durata filmului: '),
                  int(input('Adauga sala in cifre: ')),
                  int(input('Adauga varsta minima pentru vizionare in cifre: ')),
                  input("Adauga 'NU' daca filmul nu este dublat si 'DA' daca este dublat"),
                  input("Adauga 'NU' daca filmul are limba dublare sau limba in care este dublat: "),
                  input('Adauga categoria din care face parte acest film: '))
