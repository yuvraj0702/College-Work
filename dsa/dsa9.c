#include <stdio.h>

#define MAX_SIZE 100

void insertElement(int arr[], int *size, int element, int position) {
    if (*size >= MAX_SIZE) {
        printf("Array is full. Cannot insert element.\n");
        return;
    }

    if (position < 0 || position > *size) {
        printf("Invalid position. Cannot insert element.\n");
        return;
    }

    
    for (int i = *size; i > position; i--) {
        arr[i] = arr[i - 1];
    }

    
    arr[position] = element;
    
    (*size)++;
}

int main() {
    int arr[MAX_SIZE] = {1, 2, 3, 4, 5};
    int size = 5; 
    int element = 10; 
    int position = 2; 

    printf("Original array:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    insertElement(arr, &size, element, position);

    printf("Array after inserting %d at position %d:\n", element, position);
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
