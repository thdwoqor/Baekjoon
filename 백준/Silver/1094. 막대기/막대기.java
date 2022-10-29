import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String a = Integer.toBinaryString(Integer.parseInt(br.readLine()));
        int aCount = a.length() - a.replace("1", "").length();
        System.out.println(aCount);
    }
}