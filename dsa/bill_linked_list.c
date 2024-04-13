#include <stdio.h>
#include <stdlib.h>
#include <string.h>


struct Item {
    char name[50];
    float price;
    int quantity;
    struct Item *next;
};

// Function to add an item to the bill
void addItem(struct Item **head_ref, char *name, float price, int quantity) {
    struct Item *new_item = (struct Item *)malloc(sizeof(struct Item));
    if (new_item == NULL) {
        printf("Memory allocation failed.\n");
        return;
    }
    strcpy(new_item->name, name);
    new_item->price = price;
    new_item->quantity = quantity;
    new_item->next = *head_ref;
    *head_ref = new_item;
}


float calculateTotal(struct Item *head) {
    float total = 0;
    struct Item * ptr = head;
    while (ptr != NULL) {
        total += (ptr->price) * (ptr->quantity);
        ptr = ptr->next;
    }
    return total;
}


// Function to print the bill
void printBill(struct Item *head) {
    struct Item * ptr = head;
    printf("Item\t\tPrice\t\tQuantity\tTotal\n");
    printf("------------------------------------------------\n");
    while (ptr != NULL) {
        printf("%s\t\t%.2f\t\t%d\t\t%.2f\n", ptr->name, ptr->price, ptr->quantity, ptr->price * ptr->quantity);
        ptr = ptr->next;
    }
    printf("\nTotal: %.2f\n", calculateTotal(head)); 
}


int main() {
    struct Item *bill = NULL;
    int choice;
    char name[50];
    float price;
    int quantity;

    do {
        printf("\n1. Add item\n");
        printf("2. Print bill\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter item name: ");
                scanf("%s", name);
                printf("Enter item price: ");
                scanf("%f", &price);
                printf("Enter item quantity: ");
                scanf("%d", &quantity);
                addItem(&bill, name, price, quantity);
                break;
            case 2:
                if (bill == NULL) {
                    printf("No items added to the bill.\n");
                } else {
                    printBill(bill);
                }
                break;
            case 3:
                printf("Exiting...\n");
                break;
            default:
                printf("Invalid choice. Please enter a valid option.\n");
        }
    } while (choice != 3);

    // Free memory
    struct Item *temp;
    while (bill != NULL) {
        temp = bill;
        bill = bill->next;
        free(temp);
    }

    return 0;
}
