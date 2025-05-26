from github import Github
import os

# 🔒 Use uma variável de ambiente para armazenar seu token com segurança
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# 📝 Nome do repositório no formato "usuario/repositorio"
REPO_NAME = "GreisonMontenari/MontenariLabs"

# 🎯 Labels que serão criadas (nome, cor hexadecimal, descrição)
LABELS = [
    ("enhancement", "84b6eb", "Nova funcionalidade ou melhoria"),
    ("bug", "d73a4a", "Algo está quebrado"),
    ("help wanted", "008672", "Ajuda é bem-vinda nesta tarefa"),
    ("good first issue", "7057ff", "Boa para iniciantes"),
    ("question", "d876e3", "Questões ou dúvidas"),
    ("documentation", "0075ca", "Melhoria ou adição de documentação"),
]

# 🎯 Milestones (opcional)
MILESTONES = [
    "MVP",
    "Versão 1.0",
    "Refatoração",
]

def main():
    if not GITHUB_TOKEN:
        print("Erro: variável de ambiente GITHUB_TOKEN não encontrada.")
        return

    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)

    # Criar labels
    print("🔖 Criando labels...")
    for name, color, description in LABELS:
        try:
            repo.create_label(name=name, color=color, description=description)
            print(f"✅ Label '{name}' criada.")
        except Exception as e:
            print(f"⚠️ Label '{name}' não pôde ser criada: {e}")

    # Criar milestones
    print("\n📅 Criando milestones...")
    for milestone in MILESTONES:
        try:
            repo.create_milestone(title=milestone)
            print(f"✅ Milestone '{milestone}' criada.")
        except Exception as e:
            print(f"⚠️ Milestone '{milestone}' não pôde ser criada: {e}")

if __name__ == "__main__":
    main()
