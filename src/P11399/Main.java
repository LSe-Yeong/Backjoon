package P11399;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();
        ArrayList<Integer> time=new ArrayList<>();
        int total=0;

        int N=Integer.parseInt(br.readLine());
        StringTokenizer st=new StringTokenizer(br.readLine());
        for(int i=0;i<N;i++){
            time.add(Integer.parseInt(st.nextToken()));
        }
        Collections.sort(time);

        for(int i=0;i<N;i++){
            for(int j=0;j<N-i;j++){
                total=total+time.get(j);
            }
        }
        sb.append(total);
        System.out.print(sb.toString());
    }
}
