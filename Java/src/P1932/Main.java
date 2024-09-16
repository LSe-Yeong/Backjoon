package P1932;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[][] triangle;
    static int[][] DP;

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();

        int N=Integer.parseInt(br.readLine());

        triangle=new int[N][N];
        DP=new int[N][N];
        for(int i=0;i<N;i++){
            StringTokenizer st=new StringTokenizer(br.readLine());
            for(int j=0;j<=i;j++){
                triangle[i][j]=Integer.parseInt(st.nextToken());
            }
        }

        DP[0][0]=triangle[0][0];

        for(int i=1;i<N;i++){
            for(int j=0;j<=i;j++){
                if(j==0){
                    DP[i][j]=DP[i-1][0]+triangle[i][j];
                }
                else if(j==i){
                    DP[i][j]=DP[i-1][j-1]+triangle[i][j];
                }
                else{
                    DP[i][j]=Math.max(DP[i-1][j-1],DP[i-1][j])+triangle[i][j];
                }
            }
        }

        int max=DP[N-1][0];
        for(int j=1;j<N;j++){
            if(DP[N-1][j]>max){
                max=DP[N-1][j];
            }
        }
        sb.append(max);
        System.out.print(sb.toString());
    }
}
