package P24444;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static ArrayList<ArrayList<Integer>> graph=new ArrayList<>();
    static int[] check;
    static int count;

    static Queue<Integer> queue=new LinkedList<>();

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

        BFS(r);

        for(int i = 1; i < check.length; i++) {
            stringBuilder.append(check[i]).append("\n");
        }
        System.out.println(stringBuilder.toString());
    }
    private static void BFS(int start){
        queue.offer(start);
        check[start]=count;
        count++;

        while(!queue.isEmpty()) {
            int element = queue.poll();
            for (int i = 0; i < graph.get(element).size(); i++) {
                int n=graph.get(element).get(i);
                if(check[n]==0){
                    queue.offer(n);
                    check[n]=count;
                    count++;
                }
            }
        }
    }
}
