#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main() {
   FILE *fp = fopen("input.txt", "r");
   char line[4096];
   long sum = 0;
   while (fgets(line, sizeof(line), fp) != NULL) {
      // Read input
      char *p = line;
      
      long target = strtol(p, &p, 10);
      while (!isdigit(*p) && *p != 0) p++;
      
      long elem[1000];
      int nrElem = 0;
      while (isdigit(*p)) {
         elem[nrElem++] = strtol(p, &p, 10);
         while (!isdigit(*p) && *p != 0) p++;
      }
      
      // Try all combinations
      int nrCombinations = 3;
      for (int i = 0; i < nrElem-1; i++) {
         nrCombinations *= 3;
      }
      for (int i = 0; i < nrCombinations; i++) {
         long out = elem[0];
         int mask = i;
         for (int j = 0; j < nrElem-1; j++) {
            int oper = mask % 3;
            mask = mask / 3;
            
            switch (oper) {
               case 0:
                  out += elem[j+1];
                  break;
               case 1:
                  out *= elem[j+1];
                  break;
               case 2: {
                  long shift = 1;
                  while (elem[j+1] >= shift) {
                     shift *= 10;
                  }
                  out = out*shift + elem[j+1];
                  break;
               }
            }
         }
      
         if (target == out) {
            sum += target;
            break;
         }
      }
   }
   fclose(fp);

   printf("%ld\n", sum);

   return 0;
}
