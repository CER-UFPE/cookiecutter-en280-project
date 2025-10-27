import subprocess
import sys


def print_banner():
    """Exibe um banner com arte ASCII para CER Model Factory com cores."""
    banner = r"""
░▒▓████████▓▒░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░
░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░░▒▓██████▓▒░░▒▓████████▓▒░
    """
    print("\033[1;32m" + banner + "\033[0m")  # Verde
    print("\033[1;34m" + "Welcome to EN 280 Project Factory!" + "\033[0m")  # Azul
    print("\033[1;33m" + "Initializing your project..." + "\033[0m")  # Amarelo


# Acessa a variável do template
project_slug = "{{ cookiecutter.project_slug }}"


def is_uv_installed():
    """Verifica se o uv está instalado."""
    try:
        subprocess.run(
            "uv --version", shell=True, capture_output=True, text=True, check=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


if __name__ == "__main__":
    print_banner()
    if not is_uv_installed():
        print("\033[1;31m" + "[[ERROR]]" + "\033[0m")
        print(
            "uv não está instalado. Considere instalá-lo para gerenciar dependências Python."
        )
        print("Instruções: https://docs.astral.sh/uv/getting-started/installation/")
        sys.exit(1)
