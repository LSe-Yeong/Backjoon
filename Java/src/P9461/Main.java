package P9461;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static long[] wave;
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();

        long t=Integer.parseInt(br.readLine());
        for(long i=0;i<t;i++){
            int n=Integer.parseInt(br.readLine());
            wave=new long[n+6];
            wave[1]=1;
            wave[2]=1;
            wave[3]=1;
            wave[4]=2;
            wave[5]=2;
            for(int j=6;j<=n;j++){
                wave[j]=wave[j-1]+wave[j-5];
            }
            sb.append(wave[n]).append("\n");
        }
        System.out.print(sb.toString());
    }
}
