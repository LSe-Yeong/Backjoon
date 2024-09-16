package P14425;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();
        HashSet<String> hashSet=new HashSet<>();

        int count =0 ;

        StringTokenizer st=new StringTokenizer(br.readLine());
        int N=Integer.parseInt(st.nextToken());
        int M=Integer.parseInt(st.nextToken());

        for(int i=0;i<N;i++){
            String str = br.readLine();
            hashSet.add(str);
        }
        for(int i=0;i<M;i++){
            String str = br.readLine();
            if(hashSet.contains(str)){
                count++;
            }
        }
        sb.append(count);
        System.out.print(sb.toString());
    }
}
