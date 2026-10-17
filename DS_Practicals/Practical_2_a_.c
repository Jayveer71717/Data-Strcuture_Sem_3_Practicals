
#include <stdio.h>

int main() {
  int n, i;
  int arr[100];
  int *ptr;

  printf("Enter size of array: ");
  fflush(stdout);
  scanf("%d", &n);

  printf("Enter array elements:\n");
  for (i = 0; i < n; i++) {
    scanf("%d", &arr[i]);
  }

  ptr = arr;

  printf("\nArray in reverse order:\n");
  for (i = n - 1; i >= 0; i--) {
    printf("%d ", *(ptr + i));
  }
  printf("\n");

  return 0;
}
