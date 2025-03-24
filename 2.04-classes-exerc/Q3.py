import datetime as dt

class Evento:
    total_eventos = 0

    def __init__(self, titulo, data_hora, descrição):
        self.titulo = titulo
        self.data_hora = data_hora
        self.descrição = descrição
        self.is_concluido = False
        Evento.total_eventos += 1

    def isConcluido(self):
        if self.data_hora < dt.datetime.now():
            self.is_concluido = True
        else:
            self.is_concluido = False

    @classmethod
    def num_eventos(cls):
        return cls.total_eventos

    @staticmethod
    def valida_evento(titulo, data_hora, descrição):
        return (
            isinstance(titulo, str) and
            isinstance(data_hora, dt.datetime) and
            isinstance(descrição, str)
        )

    def __str__(self):
        return f"Evento: {self.titulo}, Data: {self.data_hora}, Descrição: {self.descrição}, Concluído: {self.is_concluido}"

    def __eq__(self, other):
        if isinstance(other, Evento):
            return self.data_hora == other.data_hora
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Evento):
            return self.data_hora < other.data_hora
        return False

    def __le__(self, other):
        if isinstance(other, Evento):
            return self.data_hora <= other.data_hora
        return False

    def __gt__(self, other):
        if isinstance(other, Evento):
            return self.data_hora > other.data_hora
        return False

    def __ge__(self, other):
        if isinstance(other, Evento):
            return self.data_hora >= other.data_hora
        return False


evento1 = Evento("Reunião de Equipe", dt.datetime(2023, 10, 15, 14, 30), "Discutir próximos passos do projeto.")
evento2 = Evento("Aniversário", dt.datetime(2023, 11, 20, 18, 0), "Festa de aniversário de 30 anos.")

print(evento1)
print(evento2)

print(f"Evento1 == Evento2? {evento1 == evento2}")
print(f"Evento1 != Evento2? {evento1 != evento2}")
print(f"Evento1 < Evento2? {evento1 < evento2}")
print(f"Evento1 <= Evento2? {evento1 <= evento2}")
print(f"Evento1 > Evento2? {evento1 > evento2}")
print(f"Evento1 >= Evento2? {evento1 >= evento2}")
