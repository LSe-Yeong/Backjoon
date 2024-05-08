package P2164;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        Queue<Integer> queue=new LinkedList<>();
        StringBuilder stringBuilder=new StringBuilder();

        for(int i=1;i<=n;i++){
            queue.offer(i);
        }

        while(queue.size()!=1){
            queue.poll();
            int element = queue.poll();
            queue.offer(element);
        }
        stringBuilder.append(queue.poll());
        System.out.print(stringBuilder.toString());
    }
}
