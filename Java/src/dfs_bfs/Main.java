package dfs_bfs;

import java.util.*;
import java.io.*;

public class Main {
    static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();

    static boolean[] dfsCheck;

    static int dfsCount = -1;
    static int bfs(int start,int n) {
        boolean[] isVisited = new boolean[n+1];
        Queue<Integer> q = new LinkedList<>();
        q.offer(start);
        isVisited[start] = true;
        int count = 0;
        while(!q.isEmpty()) {
            int ele = q.poll();
            ArrayList<Integer> targetGraph = graph.get(ele);
            for(int i=0;i<targetGraph.size();i++) {
                int v = targetGraph.get(i);
                if (!isVisited[v]) {
                    count++;
                    isVisited[v] = true;
                    q.offer(v);
                }
            }
        }
        return count;
    }

    static void dfs(int start) {
        dfsCheck[start] = true;
        dfsCount++;
        ArrayList<Integer> target = graph.get(start);
        for(int i=0;i<target.size();i++) {
            if(!dfsCheck[target.get(i)]) {
                dfs(target.get(i));
            }
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int v = Integer.parseInt(br.readLine());

        for(int i=0; i<n+1; i++) {
            graph.add(new ArrayList<>());
        }
        dfsCheck = new boolean[n+1];

        for (int i=0; i<v ;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        int start = 1;
//        sb.append(bfs(start,n));
        dfs(start);
        sb.append(dfsCount);
        System.out.println(sb.toString());
    }
}
