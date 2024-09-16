package P24479;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static ArrayList<ArrayList<Integer>> graph=new ArrayList<>();
    static int[] check;
    static int count;

    public static void main(String[] args) throws IOException {
        StringBuilder stringBuilder=new StringBuilder();
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n=Integer.parseInt(st.nextToken());
        int m=Integer.parseInt(st.nextToken());
        int r=Integer.parseInt(st.nextToken());

        check=new int[n+1];

        for(int i=1;i<=n+1;i++){
            graph.add(new ArrayList<>());
        }

        for(int i=0;i<m;i++){
            st=new StringTokenizer(br.readLine());
            int u=Integer.parseInt(st.nextToken());
            int v=Integer.parseInt(st.nextToken());

            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        for (int i = 1; i <= n; i++) {
            Collections.sort(graph.get(i));
        }

        count = 1;
        DFS(r);

        for(int i = 1; i < check.length; i++) {
            stringBuilder.append(check[i]).append("\n");
        }
        System.out.println(stringBuilder.toString());
    }
    private static void DFS(int r){
        check[r] = count;
        for(int i = 0; i < graph.get(r).size(); i++) {
            int n = graph.get(r).get(i);

            //다음 갈 정점을 방문했었는지 체크(0일 경우 방문 X)
            if(check[n] == 0){
                count++;
                DFS(n);
            }
        }
    }
}
