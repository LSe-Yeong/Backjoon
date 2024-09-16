package P11866;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder stringBuilder=new StringBuilder();

        String[] input = br.readLine().split(" ");

        int n=Integer.parseInt(input[0]);
        int k=Integer.parseInt(input[1]);

        int count=1;
        Queue<Integer> queue=new LinkedList<>();

        stringBuilder.append("<");

        for(int i=1;i<=n;i++){
            queue.offer(i);
        }

        while(!(queue.isEmpty())){
            if(count!=k){
                int e =queue.poll();
                queue.offer(e);
                count++;
            }
            else{
                int e=queue.poll();
                if((queue.isEmpty())){
                    stringBuilder.append(e+">");
                    break;
                }
                stringBuilder.append(e+", ");
                count=1;
            }
        }
        System.out.print(stringBuilder.toString());
    }
}
