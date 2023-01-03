package newtest;

import java.io.*;
import java.util.Scanner;

public class makefasta {

    public static void main(String[] args) throws IOException {


        String file = "/home/pratikcu/Documents/out95newcut15_trim";

        File f1 = new File("/home/pratikcu/Documents/out95newcut15_trim.fa");

        Scanner scanner = new Scanner(new File(file));
        int cn=0;
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            String id=">trans_"+cn;
            System.out.println("line is : "+id);

            FileOutputStream fos = new FileOutputStream(f1,true);
            fos.write(id.getBytes());
            String newl ="\n";
            fos.write(newl.getBytes());
            fos.write(line.getBytes());
            fos.write(newl.getBytes());
//            FileWriter bw = new FileWriter("/home/pratikcu/Documents/newout95trancriptK15_100to700.fa"),true);
//                    //BufferedWriter bw = new BufferedWriter(fw);
//                    bw.write(id);
//                    bw.write("\n");
//                    bw.write(line);
//                    bw.write("\n");
                    cn++;
        }
    }
}
