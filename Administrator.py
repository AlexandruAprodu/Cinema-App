
class Administrator:

    def __init__(self, nume, prenume, email_address):
        self.nume = nume
        self.prenume = prenume
        self.email_address = email_address

    def __call__(self, *args, **kwargs):
        return self



administrator = Administrator(
    input('Scrie numele administratorului: '),
    input('Scrie prenumele administratorului: '),
    input('Scrie adresa de email: ')
)