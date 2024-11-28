def lister_todos():
   print()

def crer_todo():
    tasks = []
    while True :
        print("\n==== Créer une tâche ====")
        print("1. Ajouter une tâche")
        print("2. Supprimer une tâche")
        print("3. Quitter")

        choice = input("Entrez votre choix : ")
        if choice == '1':
            print()
            n_tasks = int(input("Combien de tâches souhaitez-vous ajouter :"))

            for i in range(n_tasks):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done": False})
                print("Task added !")

        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")



def modifier_statut_todo():
    print()

def supprimer_todo():
    print()


# Menu principal

choix = ''
while choix != 'q' :
    print()
    print()
    print()
    print()
    print()
    print()
    print()

    choix = input('=> Choix :')


