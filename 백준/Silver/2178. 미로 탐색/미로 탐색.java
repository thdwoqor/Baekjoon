import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int map[][];
    static boolean visited[][];
    static int dx[] = { -1, 1, 0, 0 };
    static int dy[] = { 0, 0, -1, 1 };
    static int n;
    static int m;
    static int min = 100000000;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt((st.nextToken()));
        m = Integer.parseInt((st.nextToken()));

        map = new int[n+1][m+1];
        visited = new boolean[n+1][m+1];
        for(int i=0; i<n; i++) {
            String s = br.readLine(); // 101111
            for (int j=0; j<m; j++){
                    map[i][j] = s.charAt(j)- '0'; // 1 0 1 1 1 1
            }
        }

        bfs(0, 0);

        System.out.println(min);
    }

    private static void bfs(int x, int y) {
        Queue<point> q  = new LinkedList<>();
        q.add(new point(x, y,1));
        visited[x][y]=true;

        while(!q.isEmpty()) {
            point temp = q.poll();
            for (int k = 0; k < 4; k++) {
                int xx = temp.x + dx[k];
                int yy = temp.y + dy[k];
                int dd = temp.depth+1;

                if (xx==n-1&&yy==m-1){
                    min = Math.min(min,dd);
                    break;
                }

                if(xx>=0 && yy>=0 && xx<n && yy<m &&!visited[xx][yy] && map[xx][yy]==1) {
                    visited[xx][yy]=true;
                    q.add(new point(xx, yy,dd));
                }
            }
        }
    }

    static class point{
        int x;
        int y;
        int depth;
        public point(int x, int y,int depth) {
            super();
            this.x = x;
            this.y = y;
            this.depth= depth;
        }

    }



}
