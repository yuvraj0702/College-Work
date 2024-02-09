#include <stdio.h>

int main() {
    int n;

    // Read the value of n
    printf("Enter the value of n: ");
    scanf("%d", &n);

    if (n <= 0) {
        printf("Please enter a positive integer for n.\n");
        return 1;  // Exit with an error code
    }

    // Declare an array to store numbers
    float numbers[n];

    // Read n numbers from the user
    for (int i = 0; i < n; i++) {
        printf("Enter number %d: ", i + 1);
        scanf("%f", &numbers[i]);
    }

    // Display the entered numbers
    printf("Numbers entered: ");
    for (int i = 0; i < n; i++) {
        printf("%f ", numbers[i]);
    }

    return 0;  // Exit successfully
}
