package P1260;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int count;
    static int[] check;

    static StringBuilder stringBuilder=new StringBuilder();
    static Queue<Integer> queue=new LinkedList<>();
    static  ArrayList<ArrayList<Integer>> graph=new ArrayList<>();

    public static void main(String[] agrs) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st=new StringTokenizer(br.readLine());
        int node=Integer.parseInt(st.nextToken());
        int link=Integer.parseInt(st.nextToken());
        int start=Integer.parseInt(st.nextToken());

        check=new int[node+1];

        for(int i=0;i<node+1;i++){
            graph.add(new ArrayList<>());
        }

        for(int i=0;i<link;i++){
            st=new StringTokenizer(br.readLine());
            int u=Integer.parseInt(st.nextToken());
            int v=Integer.parseInt(st.nextToken());
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        for(int i=1;i<=node;i++){
            Collections.sort(graph.get(i));
        }

        DFS(start);
        stringBuilder.append("\n");

        check=new int[node+1];

        BFS(start);
        System.out.print(stringBuilder.toString());
    }
    private static void DFS(int start){
        check[start]=1;
        stringBuilder.append(start).append(" ");

        for(int i=0;i<graph.get(start).size();i++){
            int n=graph.get(start).get(i);
            if(check[n]==0){
                DFS(n);
            }
        }
    }

    private static void BFS(int start){
        queue.offer(start);
        check[start]=1;
        stringBuilder.append(start).append(" ");

        while(!queue.isEmpty()){
            int n=queue.poll();
            for(int i=0;i<graph.get(n).size();i++){
                int element=graph.get(n).get(i);
                if(check[element]==0){
                    queue.offer(element);
                    stringBuilder.append(element).append(" ");
                    check[element]=1;
                }
            }
        }
    }
}
