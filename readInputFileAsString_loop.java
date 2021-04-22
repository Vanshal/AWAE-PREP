//  
import java.util.Base64;
import java.io.*;
import java.util.Scanner;
import java.nio.file.*;

public class loop {

    public static String readFileAsString(String fileName)throws Exception
    {
        String data = "";
        data = new String(Files.readAllBytes(Paths.get(fileName)));
        return data;
    }
 
    public static void main(String args[]) throws Exception
    {
        String data = readFileAsString("/usr/share/wordlists/all.txt");
        
        Scanner scanner = new Scanner(data);
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            // process the line
            System.out.println(SOMEFUNCTION(line));
        }
        scanner.close();
    }
}
