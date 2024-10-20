# Importar bibliotecas necessárias
import os
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq

# Definindo variáveis de ambiente, caso necessário (por exemplo, chaves de API)
os.environ["SERPER_API_KEY"] = "7a37c4b75d3db13570f57fbdee7998d4fc122fad"
os.environ["GROQ_API_KEY"] = "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"  # Adicione sua chave de API aqui

# Função de geração de respostas utilizando a biblioteca CrewAI
def completion(prompt_text):
    response = ChatGroq().invoke(prompt_text)  # Passar a string diretamente
    return response.content  # Ajustar para acessar o conteúdo corretamente

# Criando uma função para executar tarefas
def perform_task(agent, task_description):
    if "buscar voos" in task_description:
        query = input("Digite os detalhes da busca de voos: ")
        return completion(f"Buscar voos para {query}")
    elif "reservar hotel" in task_description:
        query = input("Digite os detalhes da reserva do hotel: ")
        return completion(f"Reservar hotel para {query}")
    elif "alugar carro" in task_description:
        query = input("Digite os detalhes do aluguel do carro: ")
        return completion(f"Alugar carro para {query}")
    else:
        return "Tarefa desconhecida"

# Criando os agentes com os campos obrigatórios
agent1 = Agent(
    name="Agente de Voos",
    role="Pesquisar voos",
    goal="Encontrar os melhores voos",
    backstory="Especialista em encontrar as melhores opções de voos"
)
agent2 = Agent(
    name="Agente de Hotel",
    role="Pesquisar hotéis",
    goal="Encontrar os melhores hotéis",
    backstory="Especialista em encontrar acomodações confortáveis"
)
agent3 = Agent(
    name="Agente de Aluguel de Carro",
    role="Alugar carros",
    goal="Encontrar as melhores opções de aluguel de carros",
    backstory="Especialista em aluguel de veículos"
)

# Função principal para executar o programa
def main():
    task_description = input("Escolha uma tarefa (buscar voos, reservar hotel, alugar carro): ").lower()
    if task_description not in ["buscar voos", "reservar hotel", "alugar carro"]:
        print("Tarefa desconhecida")
        return

    if "buscar voos" in task_description:
        result = perform_task(agent1, task_description)
    elif "reservar hotel" in task_description:
        result = perform_task(agent2, task_description)
    elif "alugar carro" in task_description:
        result = perform_task(agent3, task_description)
    
    # Imprimindo os resultados
    print(f"Resultado da tarefa ({task_description}): {result}")

    # Salvando a saída em um arquivo
    with open("resultado_agentes.txt", "w") as f:
        f.write(f"Resultado da tarefa ({task_description}): {result}\n")

if __name__ == "__main__":
    main()
