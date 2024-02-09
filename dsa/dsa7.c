#include <stdio.h>

int containsDuplicate(int nums[], int numsSize) 
{
    for (int i = 0; i < numsSize; i++) 
    {
        for (int j = i + 1; j < numsSize; j++) 
        {
            if (nums[i] == nums[j]) {
                return 1; // Duplicate found
            }
        }
    }
    return 0; // No duplicate found
}

int main() {
    int array1[] = {1, 2, 3, 4, 5};
    int array2[] = {1, 2, 3, 4, 1};
    int array3[] = {1, 1, 2, 3, 4};

    int size1 = sizeof(array1) / sizeof(array1[0]);
    int size2 = sizeof(array2) / sizeof(array2[0]);
    int size3 = sizeof(array3) / sizeof(array3[0]);

    printf("Array 1 contains duplicate: %s\n", containsDuplicate(array1, size1) ? "true" : "false");
    printf("Array 2 contains duplicate: %s\n", containsDuplicate(array2, size2) ? "true" : "false");
    printf("Array 3 contains duplicate: %s\n", containsDuplicate(array3, size3) ? "true" : "false");

    return 0;
}
