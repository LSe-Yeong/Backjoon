package P1912;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[] DP;
    static int[] array;
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();
        int N=Integer.parseInt(br.readLine());
        DP=new int[N];
        array=new int[N];
        StringTokenizer st=new StringTokenizer(br.readLine());
        for(int i=0;i<N;i++){
            array[i]=Integer.parseInt(st.nextToken());
        }

        DP[0]=array[0];
        for(int i=1;i<N;i++){
            if(DP[i-1]+array[i]>array[i]){
                DP[i]=DP[i-1]+array[i];
            }
            else{
                DP[i]=array[i];
            }
        }

        int max=DP[0];
        for(int i=1;i<N;i++){
            if(DP[i]>max){
                max=DP[i];
            }
        }
        sb.append(max);
        System.out.print(sb.toString());
    }
}
