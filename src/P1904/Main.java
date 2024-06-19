package P1904;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int[] fib;
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();

        int n=Integer.parseInt(br.readLine());
        int count;
        fib=new int[n+2];
        fib[1]=1;
        fib[2]=2;

        for(int i=3;i<n+1;i++){
            fib[i]=(fib[i-1]+fib[i-2])%15746;
        }
        count=fib[n];
        sb.append(count);
        System.out.print(sb.toString());
    }
}
