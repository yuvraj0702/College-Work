#include <stdio.h>
#include <string.h>
#define MAX_TASKS 100

typedef struct {
    int id;
    char title[50];
    char dueDate[11];
    char priority[10];
    int isCompleted;
} Task;

void addTask(Task tasks[], int *count);
void viewTasks(Task tasks[], int count);
void saveToFile(Task tasks[], int count);
void loadFromFile(Task tasks[], int *count);

int main() {
    Task tasks[MAX_TASKS];
    int count = 0;
    int choice;

    loadFromFile(tasks, &count);

    do {
        printf("\n--- To-Do List ---\n");
        printf("1. Add Task\n");
        printf("2. View Tasks\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addTask(tasks, &count);
                break;
            case 2:
                viewTasks(tasks, count);
                break;
            case 3:
                saveToFile(tasks, count);
                printf("Goodbye!\n");
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    } while (choice != 3);

    return 0;
}

void addTask(Task tasks[], int *count) {
    if (*count >= MAX_TASKS) {
        printf("Task limit reached!\n");
        return;
    }
    tasks[*count].id = *count + 1;
    printf("Enter task title: ");
    scanf(" %[^\n]", tasks[*count].title);
    printf("Enter due date (YYYY-MM-DD): ");
    scanf("%s", tasks[*count].dueDate);
    printf("Enter priority (High/Medium/Low): ");
    scanf("%s", tasks[*count].priority);
    tasks[*count].isCompleted = 0;
    (*count)++;
    printf("Task added successfully!\n");
}

void viewTasks(Task tasks[], int count) {
    printf("\n--- Task List ---\n");
    for (int i = 0; i < count; i++) {
        printf("ID: %d, Title: %s, Due: %s, Priority: %s, Completed: %s\n",
               tasks[i].id, tasks[i].title, tasks[i].dueDate,
               tasks[i].priority, tasks[i].isCompleted ? "Yes" : "No");
    }
}

void saveToFile(Task tasks[], int count) {
    FILE *file = fopen("tasks.txt", "w");
    if (file == NULL) {
        printf("Error saving tasks!\n");
        return;
    }
    for (int i = 0; i < count; i++) {
        fprintf(file, "%d|%s|%s|%s|%d\n", tasks[i].id, tasks[i].title, tasks[i].dueDate,
                tasks[i].priority, tasks[i].isCompleted);
    }
    fclose(file);
    printf("Tasks saved successfully!\n");
}

void loadFromFile(Task tasks[], int *count) {
    FILE *file = fopen("tasks.txt", "r");
    if (file == NULL) {
        printf("No previous tasks found.\n");
        return;
    }
    while (fscanf(file, "%d|%[^|]|%[^|]|%[^|]|%d\n", &tasks[*count].id,
                  tasks[*count].title, tasks[*count].dueDate,
                  tasks[*count].priority, &tasks[*count].isCompleted) != EOF) {
        (*count)++;
    }
    fclose(file);
    printf("Tasks loaded successfully!\n");
}
