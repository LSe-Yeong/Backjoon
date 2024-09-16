package P11047;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();
        StringTokenizer st=new StringTokenizer(br.readLine());
        ArrayList<Integer> money=new ArrayList<>();

        int N=Integer.parseInt(st.nextToken());
        int K=Integer.parseInt(st.nextToken());
        int count=0;

        for(int i=0;i<N;i++){
            money.add(Integer.parseInt(br.readLine()));
        }

        for(int i=money.size()-1;i>=0;i--){
            int thisMoney=money.get(i);
            count=count+K/ thisMoney;
            K=K% thisMoney;
        }

        sb.append(count);
        System.out.print(sb.toString());
    }
}
