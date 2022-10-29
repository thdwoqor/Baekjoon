import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String a = br.readLine();
        List<String> l = new ArrayList<>();

        for(int i=1;i<a.length();i++){
            for(int j=i+1;j<a.length();j++){
                String merge = "";
                StringBuffer b = new StringBuffer(a.substring(0,i));
                StringBuffer c = new StringBuffer(a.substring(i,j));
                StringBuffer d = new StringBuffer(a.substring(j,a.length()));
                merge = b.reverse().toString()+c.reverse().toString()+d.reverse().toString();
                l.add(merge);
            }
        }
        l.sort(Comparator.naturalOrder());
        System.out.println(l.get(0));
    }
}