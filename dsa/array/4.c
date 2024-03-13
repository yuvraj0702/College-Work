<<<<<<< HEAD
#include <stdio.h>

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void reverseArray(int arr[], int size) {
    for (int i = size - 1; i >= 0; i--) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int sumOfElements(int arr[], int size) {
    int sum = 0;
    for (int i = 0; i < size; i++)
        sum += arr[i];
    return sum;
}

int findMaximum(int arr[], int size) {
    int max = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > max)
            max = arr[i];
    }
    return max;
}

int findMinimum(int arr[], int size) {
    int min = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] < min)
            min = arr[i];
    }
    return min;
}

float calculateAverage(int arr[], int size) {
    int sum = sumOfElements(arr, size);
    float avg = (float)sum / size;
    return avg;
}

int searchElement(int arr[], int size, int key) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == key)
            return i;
    }
    return -1;
}

int countOccurrences(int arr[], int size, int key) {
    int count = 0;
    for (int i = 0; i < size; i++) {
        if (arr[i] == key)
            count++;
    }
    return count;
}

void bubbleSortAscending(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
} 

void bubbleSortDescending(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] < arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void insertElement(int arr[], int *size, int element, int position) {
    if (position < 0 || position > *size) {
        printf("Invalid position!\n");
        return;
    }
    for (int i = *size; i > position; i--)
        arr[i] = arr[i - 1];
    arr[position] = element;
    (*size)++;
    printf("Element inserted successfully.\n");
}

void deleteElement(int arr[], int *size, int position) {
    if (position < 0 || position >= *size) {
        printf("Invalid position!\n");
        return;
    }
    for (int i = position; i < *size - 1; i++)
        arr[i] = arr[i + 1];
    (*size)--;
    printf("Element deleted successfully.\n");
}

int main() {
    int choice;
    int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = 10;

    do {
        printf("\n1. Print the array\n");
        printf("2. Reverse the array\n");
        printf("3. Print the sum of elements\n");
        printf("4. Find the maximum element\n");
        printf("5. Find the minimum element\n");
        printf("6. Calculate average of elements\n");
        printf("7. Search for an element\n");
        printf("8. Count occurrences of an element\n");
        printf("9. Sort the array in ascending order\n");
        printf("10. Sort the array in descending order\n");
        printf("11. Insert an element at a specific position\n");
        printf("12. Delete an element at a specific position\n");
        printf("13. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Array: ");
                printArray(arr, size);
                break;
            case 2:
                printf("Reversed Array: ");
                reverseArray(arr, size);
                break;
            case 3:
                printf("Sum of elements: %d\n", sumOfElements(arr, size));
                break;
            case 4:
                printf("Maximum element: %d\n", findMaximum(arr, size));
                break;
            case 5:
                printf("Minimum element: %d\n", findMinimum(arr, size));
                break;
            case 6:
                printf("Average of elements: %.2f\n", calculateAverage(arr, size));
                break;
            case 7:
                {
                    int key;
                    printf("Enter element to search: ");
                    scanf("%d", &key);
                    int index = searchElement(arr, size, key);
                    if (index != -1)
                        printf("Element found at index %d.\n", index);
                    else
                        printf("Element not found in the array.\n");
                }
                break;
            case 8:
                {
                    int key;
                    printf("Enter element to count occurrences: ");
                    scanf("%d", &key);
                    printf("Occurrences of %d: %d\n", key, countOccurrences(arr, size, key));
                }
                break;
            case 9:
                {
                    bubbleSortAscending(arr, size);
                    printf("Array sorted in ascending order.\n");
                }
                break;
            case 10:
                {
                    bubbleSortDescending(arr, size);
                    printf("Array sorted in descending order.\n");
                }
                break;
            case 11:
                {
                    int element, position;
                    printf("Enter the element to insert: ");
                    scanf("%d", &element);
                    printf("Enter the position to insert: ");
                    scanf("%d", &position);
                    insertElement(arr, &size, element, position);
                }
                break;
            case 12:
                {
                    int position;
                    printf("Enter the position to delete: ");
                    scanf("%d", &position);
                    deleteElement(arr, &size, position);
                }
                break;
            case 13:
                printf("Exiting...\n");
                break;
            default:
                printf("Invalid choice! Please enter a number between 1 and 13.\n");
        }
    } while (choice != 13);

    return 0;
=======
#include <stdio.h>

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void reverseArray(int arr[], int size) {
    for (int i = size - 1; i >= 0; i--) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int sumOfElements(int arr[], int size) {
    int sum = 0;
    for (int i = 0; i < size; i++)
        sum += arr[i];
    return sum;
}

int findMaximum(int arr[], int size) {
    int max = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > max)
            max = arr[i];
    }
    return max;
}

int findMinimum(int arr[], int size) {
    int min = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] < min)
            min = arr[i];
    }
    return min;
}

float calculateAverage(int arr[], int size) {
    int sum = sumOfElements(arr, size);
    float avg = (float)sum / size;
    return avg;
}

int searchElement(int arr[], int size, int key) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == key)
            return i;
    }
    return -1;
}

int countOccurrences(int arr[], int size, int key) {
    int count = 0;
    for (int i = 0; i < size; i++) {
        if (arr[i] == key)
            count++;
    }
    return count;
}

void bubbleSortAscending(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
} 

void bubbleSortDescending(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] < arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void insertElement(int arr[], int *size, int element, int position) {
    if (position < 0 || position > *size) {
        printf("Invalid position!\n");
        return;
    }
    for (int i = *size; i > position; i--)
        arr[i] = arr[i - 1];
    arr[position] = element;
    (*size)++;
    printf("Element inserted successfully.\n");
}

void deleteElement(int arr[], int *size, int position) {
    if (position < 0 || position >= *size) {
        printf("Invalid position!\n");
        return;
    }
    for (int i = position; i < *size - 1; i++)
        arr[i] = arr[i + 1];
    (*size)--;
    printf("Element deleted successfully.\n");
}

int main() {
    int choice;
    int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = 10;

    do {
        printf("\n1. Print the array\n");
        printf("2. Reverse the array\n");
        printf("3. Print the sum of elements\n");
        printf("4. Find the maximum element\n");
        printf("5. Find the minimum element\n");
        printf("6. Calculate average of elements\n");
        printf("7. Search for an element\n");
        printf("8. Count occurrences of an element\n");
        printf("9. Sort the array in ascending order\n");
        printf("10. Sort the array in descending order\n");
        printf("11. Insert an element at a specific position\n");
        printf("12. Delete an element at a specific position\n");
        printf("13. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Array: ");
                printArray(arr, size);
                break;
            case 2:
                printf("Reversed Array: ");
                reverseArray(arr, size);
                break;
            case 3:
                printf("Sum of elements: %d\n", sumOfElements(arr, size));
                break;
            case 4:
                printf("Maximum element: %d\n", findMaximum(arr, size));
                break;
            case 5:
                printf("Minimum element: %d\n", findMinimum(arr, size));
                break;
            case 6:
                printf("Average of elements: %.2f\n", calculateAverage(arr, size));
                break;
            case 7:
                {
                    int key;
                    printf("Enter element to search: ");
                    scanf("%d", &key);
                    int index = searchElement(arr, size, key);
                    if (index != -1)
                        printf("Element found at index %d.\n", index);
                    else
                        printf("Element not found in the array.\n");
                }
                break;
            case 8:
                {
                    int key;
                    printf("Enter element to count occurrences: ");
                    scanf("%d", &key);
                    printf("Occurrences of %d: %d\n", key, countOccurrences(arr, size, key));
                }
                break;
            case 9:
                {
                    bubbleSortAscending(arr, size);
                    printf("Array sorted in ascending order.\n");
                }
                break;
            case 10:
                {
                    bubbleSortDescending(arr, size);
                    printf("Array sorted in descending order.\n");
                }
                break;
            case 11:
                {
                    int element, position;
                    printf("Enter the element to insert: ");
                    scanf("%d", &element);
                    printf("Enter the position to insert: ");
                    scanf("%d", &position);
                    insertElement(arr, &size, element, position);
                }
                break;
            case 12:
                {
                    int position;
                    printf("Enter the position to delete: ");
                    scanf("%d", &position);
                    deleteElement(arr, &size, position);
                }
                break;
            case 13:
                printf("Exiting...\n");
                break;
            default:
                printf("Invalid choice! Please enter a number between 1 and 13.\n");
        }
    } while (choice != 13);

    return 0;
>>>>>>> 9d7a52511b127bbcc3be0333be01401cbb37a239
}