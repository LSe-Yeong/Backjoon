package P1339;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br =new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        int[] char_int_value = new int[26];
        String[] target=new String[N];
        int[][] w = new int[26][2];
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->Integer.compare(b[1],a[1]));

        for(int i=0;i<N;i++){
            String str = br.readLine();
            target[i]=str;
            for(int j=0;j<str.length();j++){
                char ele = str.charAt(j);
                int idx = ele-'A';
                w[idx][0]=idx;
                w[idx][1]+=Math.pow(10,str.length()-1-j);
            }
        }

        for(int i=0;i<w.length;i++){
            if(w[i][1]!=0){
                pq.offer(w[i]);
            }
        }

        int value=9;
        while(!pq.isEmpty()){
            int[] ele = pq.poll();
            char_int_value[ele[0]]=value;
            value--;
        }


        int sum=0;
        for(int i=0;i<target.length;i++){
            String str = target[i];
            for(int j=0;j<str.length();j++){
                char ele = str.charAt(j);
                sum=sum+char_int_value[ele-'A']*(int) Math.pow(10,str.length()-1-j);
            }
        }

        sb.append(sum);

        System.out.print(sb.toString());

    }
}
