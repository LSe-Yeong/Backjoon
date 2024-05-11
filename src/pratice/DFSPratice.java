package pratice;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.LinkedList;

class Graph{
    int V;
    LinkedList<Integer>[] adj;
    boolean[] visited;
    ArrayList<Integer> dfs_array;
    public Graph(int v){
        V=v;
        adj=new LinkedList[v+1];
        for(int i=0;i<v+1;i++){
            adj[i] = new LinkedList<>();
        }
        visited=new boolean[v+1];
        dfs_array=new ArrayList<>();
    }

    public void sortGraph(){
        for(int i=0;i<V+1;i++){
            Collections.sort(adj[i]);
        }
    }
    public void addGraph(int v, int w){
        adj[v].add(w);
        adj[w].add(v);
    }

    public ArrayList<Integer> DFS(int v){
        visited[v]=true;
        dfs_array.add(v);

        Iterator<Integer> i = adj[v].listIterator();
        while (i.hasNext()) {
            int n = i.next();
            if (!visited[n])
                DFS(n); // 순환 호출
        }
        return dfs_array;
    }
}

public class DFSPratice {
    public static void main(String[] args) throws IOException {
        StringBuilder stringBuilder=new StringBuilder();
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        int n=Integer.parseInt(inputs[0]);
        int m=Integer.parseInt(inputs[1]);
        int r=Integer.parseInt(inputs[2]);

        Graph graph=new Graph(n);
        for(int i=0;i<m;i++) {
            String[] vertexInputs = br.readLine().split(" ");
            int u=Integer.parseInt(vertexInputs[0]);
            int v=Integer.parseInt(vertexInputs[1]);
            graph.addGraph(u,v);
        }

        graph.sortGraph();

        ArrayList<Integer> dfs_set = graph.DFS(r);

        for(int i=1;i<n+1;i++){
            int idx = dfs_set.indexOf(i);
            if(idx==-1){
                stringBuilder.append(0).append("\n");
            }
            else{
                stringBuilder.append(idx+1).append("\n");
            }
        }
        System.out.print(stringBuilder.toString());
    }
}
