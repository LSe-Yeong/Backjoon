package P1010;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();
        int t=Integer.parseInt(br.readLine());
        for(int i=0;i<t;i++){
            StringTokenizer st=new StringTokenizer(br.readLine());
            int N=Integer.parseInt(st.nextToken());
            int R=Integer.parseInt(st.nextToken());
            int[][] dp=new int[R+1][N+1];
            for(int n=0;n<=R;n++){
                dp[n][0]=1;
                dp[n][1]=n;
            }
            for(int n=1;n<=R;n++){
                for(int r=1;r<=N;r++){
                    dp[n][r]=dp[n-1][r]+dp[n-1][r-1];
                }
            }
            sb.append(dp[R][N]);
            sb.append("\n");
        }
        System.out.print(sb.toString());
    }
}
