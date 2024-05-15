package P11725;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static int[] parent;

    static int[] check;

    static ArrayList<ArrayList<Integer>> tree=new ArrayList<>();

    static Queue<Integer> queue = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder stringBuilder=new StringBuilder();

        int node = Integer.parseInt(br.readLine());

        parent=new int[node+1];
        check=new int[node+1];

        for(int i=0;i<node+1;i++){
            tree.add(new ArrayList<>());
        }

        for(int i=0;i<node-1;i++){
            StringTokenizer st=new StringTokenizer(br.readLine());
            int nodeA=Integer.parseInt(st.nextToken());
            int nodeB=Integer.parseInt(st.nextToken());

            tree.get(nodeA).add(nodeB);
            tree.get(nodeB).add(nodeA);
        }

        queue.offer(1);
        check[1]=1;
        while(!queue.isEmpty()){
            int treeNode=queue.poll();
            for(int i=0;i<tree.get(treeNode).size();i++){
                int adjNode=tree.get(treeNode).get(i);
                if(check[adjNode]==0){
                    queue.offer(adjNode);
                    check[adjNode]=1;
                    parent[adjNode]=treeNode;
                }
            }
        }

        for(int i=2;i< parent.length;i++){
            stringBuilder.append(parent[i]).append("\n");
        }
        System.out.print(stringBuilder.toString());
    }
}
