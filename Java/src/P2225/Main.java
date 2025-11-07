package P2225;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        long [][] DP = new long[K+1][N+1];

        for (int i = 0; i<DP[0].length; i++) {
            DP[1][i] = 1;
        }

        for (int r = 2; r<DP.length; r++) {
            for (int c = 0; c<DP[r].length; c++) {
                long sum = 0;
                for (int k = 0; k <= c; k++) {
                    sum += DP[r-1][k];
                }
                DP[r][c] = sum % 1000000000;
            }
        }

        sb.append(DP[K][N] % 1000000000);
        System.out.println(sb.toString());
    }
}
