
    #include <stdio.h>

#define MAX_SIZE 100

void deleteElement(int arr[], int *size, int position) {
    if (*size <= 0 || position < 0 || position >= *size) {
        printf("Invalid position. Cannot delete element.\n");
        return;
    }

    
    for (int i = position; i < *size - 1; i++) {
        arr[i] = arr[i + 1];
    }

    
    (*size)--;
}

int main() {
    int arr[MAX_SIZE] = {1, 2, 3, 4, 5};
    int size = 5; 
    int position = 2; 

    printf("Original array:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    deleteElement(arr, &size, position);

    printf("Array after deleting element at position %d:\n", position);
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}

