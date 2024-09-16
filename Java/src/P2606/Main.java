package P2606;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static ArrayList<ArrayList<Integer>> graph=new ArrayList<>();
    static Queue<Integer> queue=new LinkedList<>();
    static int[] check;

    static int count=0;

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder stringBuilder=new StringBuilder();
        int vertex=Integer.parseInt(br.readLine());
        int link=Integer.parseInt(br.readLine());

        check=new int[vertex+1];

        for(int i=0;i<=vertex+1;i++){
            graph.add(new ArrayList<>());
        }

        for(int i=0;i<link;i++){
            StringTokenizer st=new StringTokenizer(br.readLine());
            int u=Integer.parseInt(st.nextToken());
            int v=Integer.parseInt(st.nextToken());
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        BFS(1);
        stringBuilder.append(count).append("\n");
        System.out.println(stringBuilder.toString());
    }
    private static void BFS(int vertex){
        queue.offer(vertex);
        check[vertex]=1;
        while(!queue.isEmpty()){
            int element=queue.poll();
            for(int i=0;i<graph.get(element).size();i++){
                int n=graph.get(element).get(i);
                if(check[n]==0){
                    queue.offer(n);
                    check[n]=1;
                    count++;
                }
            }
        }
    }
}
