/**
 * To compile and run:
 *    $ javac part2.java
 *    $ java part2
 */
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class part2 {

   /**
    * @param args the command line arguments
    */
   public static void main(String[] args) throws FileNotFoundException, IOException {
      BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
      String line;
      long sum = 0;
      while ((line = reader.readLine()) != null) {
         // Read input
         String parts[] = line.split(":");

         long target = Long.valueOf(parts[0]);
         
         String elemStr[] = parts[1].split(" ");
         ArrayList<Long> elem = new ArrayList<>();
         for (int i = 0; i < elemStr.length; i++) {
            if (elemStr[i].isBlank()) continue;
            elem.add(Long.valueOf(elemStr[i]));
         }

         // Try all combinations
         int nrCombinations = 3;
         for (int i = 0; i < elem.size() - 1; i++) {
            nrCombinations *= 3;
         }
         for (int i = 0; i < nrCombinations; i++) {
            long out = elem.get(0);
            int mask = i;
            for (int j = 0; j < elem.size() - 1; j++) {
               int oper = mask % 3;
               mask = mask / 3;

               switch (oper) {
                  case 0:
                     out += elem.get(j + 1);
                     break;
                  case 1:
                     out *= elem.get(j + 1);
                     break;
                  case 2:
                     long shift = 1;
                     while (elem.get(j + 1) >= shift) {
                        shift *= 10;
                     }
                     out = out*shift + elem.get(j + 1);
                     break;
               }
            }

            if (target == out) {
               sum += target;
               break;
            }
         }
      }
      System.out.printf("%d\n", sum);
   }
}
