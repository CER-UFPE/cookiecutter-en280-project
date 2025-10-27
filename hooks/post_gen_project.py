import subprocess
import sys

# Acessa a variável do template
project_slug = "{{ cookiecutter.project_slug }}"


def init_git():
    try:
        # Inicializa o repositório Git
        subprocess.run(["git", "init"], check=True)
        # Adiciona todos os arquivos
        subprocess.run(["git", "add", "."], check=True)
        # Faz o commit inicial
        subprocess.run(
            ["git", "commit", "-m", f"Commit inicial para {project_slug}"], check=True
        )
        print(f"Repositório Git inicializado para {project_slug}.")
    except subprocess.CalledProcessError:
        print("ERRO: Falha na inicialização do Git.")
        sys.exit(1)  # Para o processo e remove o projeto gerado se der erro


if __name__ == "__main__":
    init_git()
