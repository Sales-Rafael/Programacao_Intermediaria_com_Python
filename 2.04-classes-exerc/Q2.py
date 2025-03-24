import datetime as dt

class Evento:
    # Atributo de classe
    total_eventos = 0

    def __init__(self, titulo, data_hora, descrição):
        # Atributos de instância
        self.titulo = titulo
        self.data_hora = data_hora
        self.descrição = descrição
        self.is_concluido = False  # Inicializado como False

        # Incrementa o total de eventos
        Evento.total_eventos += 1

    def isConcluido(self):
        """
        Verifica se o evento já ocorreu (data/hora do evento é menor que a data/hora atual).
        Atualiza o atributo `is_concluido` para True caso o evento já tenha ocorrido.
        """
        if self.data_hora < dt.datetime.now():
            self.is_concluido = True
        else:
            self.is_concluido = False

    @classmethod
    def num_eventos(cls):
        """
        Retorna o número total de eventos criados.
        """
        return cls.total_eventos

    @staticmethod
    def valida_evento(titulo, data_hora, descrição):
        """
        Valida os tipos dos atributos de um evento.
        Retorna True se todos os tipos estiverem corretos, caso contrário, retorna False.
        """
        return (
            isinstance(titulo, str) and
            isinstance(data_hora, dt.datetime) and
            isinstance(descrição, str)
        )
        
        # Criando uma instância de Evento
evento1 = Evento(
    titulo="Reunião de Equipe",
    data_hora=dt.datetime(2023, 10, 15, 14, 30),
    descrição="Reunião para discutir os próximos passos do projeto."
)

# Testando o método isConcluido
evento1.isConcluido()
print(f"O evento '{evento1.titulo}' está concluído? {evento1.is_concluido}")

# Testando o método de classe num_eventos
print(f"Total de eventos criados: {Evento.num_eventos()}")

# Testando o método estático valida_evento
# Caso 1: Valores corretos
valido = Evento.valida_evento(
    titulo="Aniversário",
    data_hora=dt.datetime(2023, 11, 20, 18, 0),
    descrição="Festa de aniversário de 30 anos."
)
print(f"Validação do evento 1: {valido}")

# Caso 2: Valores incorretos (data_hora não é um objeto datetime)
invalido = Evento.valida_evento(
    titulo="Evento Inválido",
    data_hora="2026-11-20 18:00:00",  # String em vez de datetime
    descrição="Este evento não é válido."
)
print(f"Validação do evento 2: {invalido}")