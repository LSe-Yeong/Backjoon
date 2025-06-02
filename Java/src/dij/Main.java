package dij;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static ArrayList<ArrayList<int[]>> graph = new ArrayList<>();
    static PriorityQueue<int []> pq = new PriorityQueue<>(Comparator.comparing((int[] a) -> (Integer) (a[0])));

    static int[] distance;
    static void dij(int start) {
        distance[start] = 0;
        pq.offer(new int[]{0,start});
        while(!pq.isEmpty()) {
            int[] ele = pq.poll();
            int dist = ele[0];
            int dot = ele[1];
            if(distance[dot]<dist) {
                continue;
            }
            ArrayList<int[]> target = graph.get(dot);
            for(int i=0;i<target.size();i++) {
                int cost = (target.get(i))[1];
                int v = (target.get(i))[0];
                if(distance[v]>dist+cost) {
                    distance[v] = dist+cost;
                    pq.offer(new int[]{dist+cost,v});
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int V = Integer.parseInt(st.nextToken());
        int start = Integer.parseInt(br.readLine());
        final int INF = 100000000;

        distance = new int[N+1];
        for (int i=0;i<N+1;i++) {
            graph.add(new ArrayList<>());
            distance[i] = INF;
        }

        for(int i=0;i<V;i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph.get(u).add(new int[]{v,w});
        }

        dij(start);

        for(int i=1;i< distance.length;i++) {
            int dist = distance[i];
            if(dist==INF) {
                sb.append("INF");
            }
            else {
                sb.append(dist);
            }
            sb.append("\n");
        }

        System.out.print(sb.toString());
    }
}
