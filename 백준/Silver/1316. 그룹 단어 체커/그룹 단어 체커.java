import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        List<String> l = new ArrayList<>();

        for(int i=0;i<n;i++){
            l.add(br.readLine());
        }
        int count =0;
        for(int i=0;i<l.size();i++){
            HashSet<String> set = new HashSet<>();
            List<String> words = Arrays.asList(l.get(i).split(""));
            set.add(words.get(0));
            for(int j=1;j<words.size();j++){
                if(words.get(j).equals(words.get(j-1))){
                    continue;
                }else{
                    if(set.contains(words.get(j))){
                        count+=1;
                        break;
                    }else{
                        set.add(words.get(j));
                    }
                }
            }
        }

        System.out.println(l.size()-count);
    }
}