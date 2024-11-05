package P1715;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();

        int N = Integer.parseInt(br.readLine());
        int[] array= new int[N];

        for(int i=0;i<N;i++){
            array[i]=Integer.parseInt(br.readLine());
            pq.offer(array[i]);
        }

        int sum=0;
        while(pq.size()!=1){
            int ele1=pq.poll();
            int ele2=pq.poll();
            sum=sum+ele1+ele2;
            pq.offer(ele1+ele2);
        }

        sb.append(sum);
        System.out.print(sb.toString());
    }
}
