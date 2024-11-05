package P1753;

import java.io.*;
import java.util.*;

public class Main {

    static ArrayList<ArrayList<int[]>> graph=new ArrayList<>();

    static int[] distance;
    public static void dij(int start){
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->Integer.compare(a[0],b[0]));
        distance[start]=0;
        pq.offer(new int[]{0,start});

        while(!pq.isEmpty()){
            int[] ele = pq.poll();
            int dist = ele[0];
            int node = ele[1];
            if(distance[ele[1]]<dist){
                continue;
            }

            for(int i=0;i<graph.get(node).size();i++){
                int v = (graph.get(node).get(i))[0];
                int w = (graph.get(node).get(i))[1];
                if(dist + w < distance[v]){
                    distance[v]=dist+w;
                    pq.offer(new int[]{dist+w,v});
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());

        distance= new int[V+1];
        for(int i=0;i<V+1;i++){
            graph.add(new ArrayList<int[]>());
            distance[i]=1000000000;
        }

        int start = Integer.parseInt(br.readLine());

        for(int i=0;i<E;i++){
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph.get(u).add(new int[]{v,w});
        }

        dij(start);

        for(int i=1;i< distance.length;i++){
            if(distance[i]==1000000000){
                sb.append("INF"+"\n");
            }
            else {
                sb.append(distance[i] + "\n");
            }
        }

        System.out.print(sb.toString());
    }
}
