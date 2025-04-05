# Copyleft 🄯 2025, Germano Castanho;
# Software livre licenciado sob a GPL-3.0;
# Cada linha, um manifesto pela liberdade!


import json
import time
from pathlib import Path

TASKS = Path(__file__).parent / "tasks"
TASKS.mkdir(exist_ok=True)
JSON = TASKS / "tasks.json"
JSON.touch(exist_ok=True)
if JSON.stat().st_size == 0:
    with open(JSON, "w") as f:
        json.dump({"tasks": []}, f, indent=2)


OPTS = {
    "1": "Mostrar tarefas",
    "2": "Adicionar tarefa",
    "3": "Excluir tarefa",
    "q": "Sair do programa",
}


def user_options():
    print("\n✨✨ TASKFLOW ME ✨✨\n")
    for key, value in OPTS.items():
        print(f"{key}: {value}")

    chosen = input("\nEscolha uma opção: ")
    return chosen


def invalid_option(chosen):
    if chosen not in OPTS.keys():
        print("Opção inválida! 😅")
        time.sleep(1)
    return None


def show_todo_list(chosen):
    if chosen == "1":
        print("\n📋 TAREFAS:\n")
        with open(JSON, "r") as f:
            tasks = json.load(f)
            for task in tasks["tasks"]:
                print(task)
        input("\nENTER para continuar: ")
    return None


def add_new_task(chosen):
    if chosen == "2":
        task = input("Digite a tarefa: ")
        with open(JSON, "r") as f:
            tasks = json.load(f)
            tasks["tasks"].append(task)
        with open(JSON, "w") as f:
            json.dump(tasks, f, indent=2)
        print("Tarefa adicionada! 🚀")
        input("\nENTER para continuar: ")
    return None


def delete_done_task(chosen):
    if chosen == "3":
        print("\n🎯 OPÇÕES\n")
        with open(JSON, "r") as f:
            tasks = json.load(f)
        for task in tasks["tasks"]:
            print(task)
        task = input("\nQual deseja excluir? ")
        with open(JSON, "r") as f:
            tasks = json.load(f)
            tasks["tasks"].remove(task)
        with open(JSON, "w") as f:
            json.dump(tasks, f, indent=2)
        print("Tarefa excluída! 🗑️")
        input("\nENTER para continuar: ")
    return None


def quit_program(chosen):
    if chosen == "q":
        print("Saindo do programa... 👋")
        time.sleep(1)
        exit()
    return None


def main():
    while True:
        chosen = user_options()
        invalid_option(chosen)
        show_todo_list(chosen)
        add_new_task(chosen)
        delete_done_task(chosen)
        quit_program(chosen)
    return None


if __name__ == "__main__":
    main()
