package P11286;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder stringBuilder=new StringBuilder();
        PriorityQueue<Integer> positiveQueue=new PriorityQueue<>(Comparator.naturalOrder());
        PriorityQueue<Integer> negativeQueue=new PriorityQueue<>(Comparator.reverseOrder());
        int n=Integer.parseInt(br.readLine());

        for(int i=0;i<n;i++){
            int x=Integer.parseInt(br.readLine());
            if(x==0){
                if(positiveQueue.isEmpty() && negativeQueue.isEmpty()){
                    stringBuilder.append(0).append("\n");
                }
                else if(!positiveQueue.isEmpty() && negativeQueue.isEmpty()){
                    stringBuilder.append(positiveQueue.poll()).append("\n");
                }
                else if(positiveQueue.isEmpty() && !negativeQueue.isEmpty()){
                    stringBuilder.append(negativeQueue.poll()).append("\n");
                }
                else{
                    int n1=positiveQueue.poll();
                    int n2=negativeQueue.poll();
                    if(Math.abs(n1)<Math.abs(n2)){
                        stringBuilder.append(n1).append("\n");
                        negativeQueue.offer(n2);
                    }
                    else{
                        stringBuilder.append(n2).append("\n");
                        positiveQueue.offer(n1);
                    }
                }
            }
            else{
                if(x>0){
                    positiveQueue.offer(x);
                }
                else{
                    negativeQueue.offer(x);
                }
            }
        }
        System.out.print(stringBuilder.toString());
    }
}
