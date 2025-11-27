package P17135;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    static Stack<Integer> arr = new Stack<>();
    static int[][] array;
    static int[][] copyArray;
    static List<Integer> result = new ArrayList<>();
    static int M;
    static int N;
    static int D;

    public static boolean isGameOver() {
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                if (copyArray[r][c] != 0) {
                    return false;
                }
            }
        }
        return true;
    }

    public static int playGame() {
        int[][] thisTarget = new int[arr.size()][2];
        copyArray = new int[N+1][M];

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                copyArray[r][c] = array[r][c];
            }
        }

        int count = 0;
        while (!isGameOver()) {
            for (int i = 0; i < arr.size(); i++) {
                int distance = 1000000000;
                int[] spot = {-1, -1};
                for (int r = 0; r < N; r++) {
                    for (int c = 0; c < M; c++) {
                        if (copyArray[r][c] == 1) {
                            if (distance > Math.abs(N - r) + Math.abs(arr.get(i) - c) && Math.abs(N - r) + Math.abs(arr.get(i) - c) <= D) {
                                distance = Math.abs(N - r) + Math.abs(arr.get(i) - c);
                                spot[0] = r;
                                spot[1] = c;
                            } else if (Math.abs(N - r) + Math.abs(arr.get(i) - c) == distance && c < spot[1]) {
                                distance = Math.abs(N - r) + Math.abs(arr.get(i) - c);
                                spot[0] = r;
                                spot[1] = c;
                            }
                        }
                    }
                }
                thisTarget[i][0] = spot[0];
                thisTarget[i][1] = spot[1];
            }

            for (int i = 0; i < thisTarget.length; i++) {
                if (thisTarget[i][0] != -1 && copyArray[thisTarget[i][0]][thisTarget[i][1]] == 1) {
                    copyArray[thisTarget[i][0]][thisTarget[i][1]] = 0;
                    count += 1;
                }
            }

            for (int r = N - 1; r > 0; r--) {
                for (int c = 0; c < M; c++) {
                    copyArray[r][c] = copyArray[r - 1][c];
                }
            }

            for (int c = 0; c < M; c++) {
                copyArray[0][c] = 0;
            }
        }

        return count;
    }

    public static void backT(int idx, int start) {
        if (idx == 3) {
            result.add(playGame());
        }

        for (int i = start; i < M; i++) {
            arr.push(i);
            backT(idx+1,i+1);
            arr.pop();
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());

        array = new int[N+1][M];

        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < M; j++) {
                array[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        backT(0,0);

        sb.append(Collections.max(result));
        System.out.println(sb.toString());
    }
}
