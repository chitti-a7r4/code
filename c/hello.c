#include <stdio.h>

int main() {
    int arr[10] = {10, 14, 19, 26, 27, 31, 33, 35, 45, 55};
    int low = 0, high = 9, mid, N = 31; 

    while (low <= high) { 
        mid = (low + high) / 2;

        if (N == arr[mid]) { 
            printf("The no %d is found in %d index\n", N, mid); 
            return 0; 
        } else if (N < arr[mid]) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    printf("The no %d is not present in the array\n", N); 

    return 0; 
}
