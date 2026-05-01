#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int GpuID = 1; // Allows specification of your gpu.

// Usually, 0 is your cpu's iGpu, and 1 is your main gpu, aka your 'discrete' one.
// Why do they call it a discrete GPU? it's bloody huge.


char *readfile(char *FilePath, int ReadLength) { // File Reading function.
  FILE *fptr;
  fptr = fopen(FilePath, "r");
  char *out = malloc(ReadLength);
  fgets(out, ReadLength, fptr);
  fclose(fptr);
  return out;
}

int main(void) {

  printf("GPU.C Started.\n");
  printf("Reading GPU:");
  printf("%d\n", GpuID);

  char directory[100];
  snprintf(directory,sizeof(directory), "/sys/class/drm/card%i/device/gpu_busy_percent",GpuID);
  
  while (1) {
    sleep(0.1);

    printf(readfile(directory, 4));
  }

  return 1;
}