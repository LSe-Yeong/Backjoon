package hyundaeTest;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int[][] my_map;

    static int N;
    static boolean[][] isVisited;

    public static int bfs(int[] start) {
        Queue<int[]> queue = new LinkedList<>();
        int[] dRow={0,0,1,-1};
        int[] dCol={1,-1,0,0};
        int count=1;
        queue.offer(start);
        isVisited[start[0]][start[1]]=true;

        while(!queue.isEmpty()) {
            int[] ele = queue.poll();
            for(int i=0;i<dRow.length;i++){
                int nRow = ele[0]+dRow[i];
                int nCol = ele[1]+dCol[i];
                if(nRow<0 || nRow>N-1 || nCol<0 || nCol>N-1)
                    continue;
                if(!isVisited[nRow][nCol] && my_map[nRow][nCol]==1){
                    count++;
                    queue.offer(new int[]{nRow,nCol});
                    isVisited[nRow][nCol]=true;
                }
            }
        }
        return count;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        my_map = new int[N][N];
        isVisited = new boolean[N][N];
        ArrayList<Integer> result = new ArrayList<>();

        for(int i=0;i<N;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0;j<N;j++){
                my_map[i][j]=Integer.parseInt(st.nextToken());
            }
        }

        for(int r=0;r<N;r++){
            for(int c=0;c<N;c++){
                if(!isVisited[r][c] && my_map[r][c]==1){
                    int count = bfs(new int[]{r,c});
                    result.add(count);
                }
            }
        }

        Collections.sort(result);

        for(int i=0;i<result.size();i++) {
            System.out.print(result.get(i)+" ");
        }

    }
}

