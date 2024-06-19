package P24416;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int[] fib;
    static int count1;
    static int count2;

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();

        int n=Integer.parseInt(br.readLine());
        fib=new int[n+1];
        int fib_n=fib1(n);
        fib_n=fib2(n);

        sb.append(count1 + " "+count2);
        System.out.print(sb.toString());
    }

    public static int fib2(int n){
        fib[1]=1;
        fib[2]=1;
        for(int i=3;i<=n;i++){
            count2++;
            fib[i]=fib[i-1]+fib[i-2];
        }
        return fib[n];
    }
    public static int fib1(int n){
        if(n==1 || n==2){
            count1++;
            return 1;
        }
        else{
            return fib1(n-1)+fib1(n-2);
        }
    }
}
