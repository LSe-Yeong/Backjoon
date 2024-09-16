package P1149;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.StringTokenizer;

public class Main {
    static int[][] RGB;
    static int[][] DP;

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();

        int N=Integer.parseInt(br.readLine());

        RGB=new int[N][3];
        DP=new int[N][3];
        for(int i=0;i<N;i++){
            StringTokenizer st=new StringTokenizer(br.readLine());
            for(int j=0;j<3;j++){
                RGB[i][j]=Integer.parseInt(st.nextToken());
            }
        }

        DP[0][0]=RGB[0][0];
        DP[0][1]=RGB[0][1];
        DP[0][2]=RGB[0][2];

        for(int i=1;i<N;i++){
            DP[i][0]=Math.min(DP[i-1][1],DP[i-1][2])+RGB[i][0];
            DP[i][1]=Math.min(DP[i-1][0],DP[i-1][2])+RGB[i][1];
            DP[i][2]=Math.min(DP[i-1][0],DP[i-1][1])+RGB[i][2];
        }

        int min=DP[N-1][0];
        min=Math.min(min,DP[N-1][1]);
        min=Math.min(min,DP[N-1][2]);

        sb.append(min);
        System.out.print(sb.toString());
    }
}
