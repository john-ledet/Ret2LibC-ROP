#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>

void vulnerable_function() {
    char buffer[64];
    printf("Enter your input: ");
    cin.get(buffer, sizeof(buffer));
}

int main() {
    vulnerable_function();
    printf("Exiting safely...\n");
    return 0;
}
