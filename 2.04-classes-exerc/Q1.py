import datetime as dt

class Evento:
    # Atributo de classe
    total_eventos = 0;
    
    def __init__(self, titulo, data_hora, descrição):  # Removi os valores padrão
        # Atributos de instância
        self.titulo = titulo
        self.data_hora = data_hora
        self.descrição = descrição
        self.is_concluido = False  # Sempre inicializado como False

        # Incrementa o total de eventos
        Evento.total_eventos += 1
        
# Criando instâncias de Evento
evento1 = Evento(
    titulo="Reunião de Equipe",
    data_hora=dt.datetime(2023, 10, 15, 14, 30),
    descrição="Reunião para discutir os próximos passos do projeto."
)

evento2 = Evento(
    titulo="Aniversário",
    data_hora=dt.datetime(2023, 11, 20, 18, 0),
    descrição="Festa de aniversário de 30 anos."
)

# Imprimindo os atributos das instâncias
print("Evento 1:")
print(f"Título: {evento1.titulo}")
print(f"Data e Hora: {evento1.data_hora}")
print(f"Descrição: {evento1.descrição}")
print(f"Concluído: {evento1.is_concluido}")
print()

print("Evento 2:")
print(f"Título: {evento2.titulo}")
print(f"Data e Hora: {evento2.data_hora}")
print(f"Descrição: {evento2.descrição}")
print(f"Concluído: {evento2.is_concluido}")
print()

# Imprimindo o total de eventos
print(f"Total de eventos criados: {Evento.total_eventos}")
