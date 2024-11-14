package P14235;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.Collections;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        PriorityQueue<Integer> present_value = new PriorityQueue<>(Collections.reverseOrder());
        int N = Integer.parseInt(br.readLine());

        for(int i=0;i<N;i++){
            StringTokenizer st =new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            if(a==0){
                if(!present_value.isEmpty()){
                    sb.append(present_value.poll()+"\n");
                }
                else{
                    sb.append(-1+"\n");
                }
            }
            else {
                for(int j=0;j<a;j++){
                    present_value.offer(Integer.parseInt(st.nextToken()));
                }
            }
        }

        System.out.print(sb.toString());
    }
}
