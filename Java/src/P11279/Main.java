package P11279;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder stringBuilder=new StringBuilder();
        int n=Integer.parseInt(br.readLine());
        PriorityQueue<Integer> priorityQueue=new PriorityQueue<>(Comparator.reverseOrder());

        for(int i=0;i<n;i++){
            int x=Integer.parseInt(br.readLine());
            if(x==0){
                if(priorityQueue.isEmpty()){
                    stringBuilder.append(0).append("\n");
                }
                else {
                    stringBuilder.append(priorityQueue.poll()).append("\n");
                }
            }
            else{
                priorityQueue.offer(x);
            }
        }
        System.out.print(stringBuilder.toString());
    }
}
