class Checklist:
    def __init__(self, steps):
        self.steps = steps
        self.completed_tasks = {step: [] for step in steps}

    def mark_task_done(self, task_code):
        for step, tasks in self.steps.items():
            for task in tasks:
                if task.startswith(task_code):
                    self.completed_tasks[step].append(task)
                    return
        print(f"Tâche {task_code} non trouvée.")

    def mark_step_done(self, step_code):
        if step_code in self.steps:
            self.completed_tasks[step_code] = self.steps[step_code]
        else:
            print(f"Étape {step_code} non trouvée.")

    def notify_completion(self, step):
        total_tasks = len(self.steps[step])
        completed_tasks = len(self.completed_tasks[step])
        percentage_complete = (completed_tasks / total_tasks) * 100
        if percentage_complete == 100:
            print(f"{step} -> {percentage_complete:.2f}%\n")
        else:
            print(f"{step} -> {percentage_complete:.2f}%\n")
            for task in self.steps[step]:
                status = "DONE" if task in self.completed_tasks[step] else "PENDING"
                print(f"{task} -> {status}")

    def notify_global_completion(self):
        total_tasks = sum(len(tasks) for tasks in self.steps.values())
        completed_tasks = sum(len(tasks) for tasks in self.completed_tasks.values())
        global_percentage_complete = (completed_tasks / total_tasks) * 100
        print(f"[STX NOC] --- [MAINTENANCE PREVENTIVE GE3 : {global_percentage_complete:.2f}%]\n")
        
        for step in self.steps:
            if all(len(self.completed_tasks[prev_step]) == len(self.steps[prev_step]) for prev_step in self.steps if prev_step < step):
                self.notify_completion(step)
            else:
                break

# Etape et tâche du checklist
steps = {
    "0. PRECHECK SUR SITE TNR02 GALAXY" : [
        "0.1. Informer NOC pour DEBUT de l’opération",
        "0.2. Vérification visuelle du niveau carburant du GE1",
        "0.3. Vérification visuelle du niveau du liquide de refroidissement du radiateur du GE1",
        "0.4. Vérification de tous les paramètres (température, etc) du GE1",
        "0.5. Vérification des PDR disponible"
    ],
    "1. DEMARRAGE GROUPE ELECTROGENE": [
        "1.1. Démarrage à vide du GE1.",
        "1.2. Simulation du Coupure Jirama et basculement vers GE1.",
        "1.3. Démarrer en charge le GE1",
        "1.4. Basculement vers GE1"
    ],
    "2. MISE OFF DU GE3" : [
        "2.1.   Bloquer le site sous GE1.",
        "2.2.   Mise OFF du disjoncteur du GE3",
        "2.3.   Mise OFF du GE3"
    ],
    "3. MAINTENANCE GE3" : [
        "3.1.   Vidange GE",
        "3.2.   Remplacement filtre huile,",
        "3.3.   Remplacement filtre gasoil",
        "3.4.   Nettoyage filtre à air",
        "3.5.   Vérification courroies",
        "3.6.   Appoint liquide de refroidissement",
        "3.7.   Nettoyage.",
        "3.8.   Essai à vide ",
        "3.9.   Essai en charge"
    ],
    "4. POST-CHECK GE3" : [
        "4.1.   Vérification de fonctionnement en charge",
        "4.2.   Vérification fuite d’huile",
        "4.3.   Relevé heure de marche",
        "4.4.   Vérification charge du GE"
    ],
    
}
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Créer instance de Checklist
checklist = Checklist(steps)

# Liste étapes et tâches terminées
#checklist.mark_step_done("0. PRECHECK SUR SITE TNR02 GALAXY")
#checklist.mark_step_done("1. DEMARRAGE GROUPE ELECTROGENE")
#checklist.mark_step_done("2. MISE OFF DU GE3")
#checklist.mark_step_done("3. MAINTENANCE GE3")
#checklist.mark_step_done("4. POST-CHECK GE3")



#Check for 0.
checklist.mark_task_done("0.1")
checklist.mark_task_done("0.2")
checklist.mark_task_done("0.3")
checklist.mark_task_done("0.4")
checklist.mark_task_done("0.5")

#Check for 1.
checklist.mark_task_done("1.1")
checklist.mark_task_done("1.2")
checklist.mark_task_done("1.3")
checklist.mark_task_done("1.4")

#Check for 2.
checklist.mark_task_done("2.1")
checklist.mark_task_done("2.2")
checklist.mark_task_done("2.3")



#Check for 3.
checklist.mark_task_done("3.1")
checklist.mark_task_done("3.2")
checklist.mark_task_done("3.3")
checklist.mark_task_done("3.4")
checklist.mark_task_done("3.5")
checklist.mark_task_done("3.6")
checklist.mark_task_done("3.7")
checklist.mark_task_done("3.8")
checklist.mark_task_done("3.9")



#Check for 4.
checklist.mark_task_done("4.1")
checklist.mark_task_done("4.2")
checklist.mark_task_done("4.3")
#checklist.mark_task_done("4.4")




# Afficher uniquement le dernier résultat
checklist.notify_global_completion()