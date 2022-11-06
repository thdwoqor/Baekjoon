import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] m = new int[n];

        for (int j=0;j<n;j++){
            m[j]=Integer.parseInt((st.nextToken()));
        }

        int[] l = new int[1001];
        l[1]=1;


        IntStream.range(2, 1001).forEach(e->{
            for(int i=2*e;i<1001;i+=e){
                l[i]=1;
            }
        });

        int sum=0;
        for(int k : m){
            if (l[k]!=1) {
                sum += 1;
            }
        }
        System.out.println(sum);
    }
}
