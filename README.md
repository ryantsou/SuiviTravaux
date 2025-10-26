This Python script helps track the progress of a preventive maintenance checklist for a generator (GE3), simulating the steps and tasks to be completed on-site.

## 📋 Description

The script implements a `Checklist` class that manages:

- Defining steps and associated tasks
- Marking tasks or steps as complete
- Displaying the progress status by step
- Tracking the overall progress of the maintenance

## 🚀 Features

- Mark a task as completed via its code (`mark_task_done`)
- Mark an entire step as completed (`mark_step_done`)
- Display the status of a step (`notify_completion`)
- Display the overall status of the checklist (`notify_global_completion`)

## 🛠️ Usage

### 1. Initialization

```python
checklist = Checklist(steps)
```

### 2. Mark tasks as completed

```python
checklist.mark_task_done("0.1")
checklist.mark_task_done("1.2")
```

### 3. Mark an entire step as completed

```python
checklist.mark_step_done("3. MAINTENANCE GE3")
```

### 4. Display the status of a step

```python
checklist.notify_completion("2. MISE OFF DU GE3")
```

### 5. Display the overall status

```python
checklist.notify_global_completion()
```

## 📦 Example Step Structure

```python
steps = {
    "0. PRECHECK SUR SITE TNR02 GALAXY": [
        "0.1. Inform NOC about the START of the operation",
        ...
    ],
    ...
}
```

## 📁 Files

- `checklist.py`: Contains the `Checklist` class and usage example.
- `README.md`: This file.

## 🧑‍🔧 Use Case

This script is especially useful for on-site maintenance technicians, NOC supervisors, or anyone involved in operational management of generators.

## 📜 License

This project is open-source. You are free to use, modify, and distribute it.

