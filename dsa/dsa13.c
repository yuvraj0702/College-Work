#include <stdio.h>

#define SALESMEN 5
#define PRODUCTS 3

void printSalesmanTotal(int sales[SALESMEN][PRODUCTS]) {
    printf("Total sales by each salesman:\n");
    for (int i = 0; i < SALESMEN; i++) {
        int total = 0;
        for (int j = 0; j < PRODUCTS; j++) {
            total += sales[i][j];
        }
        printf("Salesman %d: %d\n", i + 1, total);
    }
}

void printProductTotal(int sales[SALESMEN][PRODUCTS]) {
    printf("Total sales of each product:\n");
    for (int j = 0; j < PRODUCTS; j++) {
        int total = 0;
        for (int i = 0; i < SALESMEN; i++) {
            total += sales[i][j];
        }
        printf("Product %d: %d\n", j + 1, total);
    }
}

int main() {
    int sales[SALESMEN][PRODUCTS];

    printf("Enter the sales figures for each salesman and product:\n");
    for (int i = 0; i < SALESMEN; i++) {
        printf("Salesman %d:\n", i + 1);
        for (int j = 0; j < PRODUCTS; j++) {
            printf("Enter sales of product %d: ", j + 1);
            scanf("%d", &sales[i][j]);
        }
    }

    printSalesmanTotal(sales);
    printProductTotal(sales);

    return 0;
}
