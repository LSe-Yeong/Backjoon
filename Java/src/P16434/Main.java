package P16434;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int[][] roomInfos;
    static int N;
    static int ATTACK;

    static boolean isClear(long hp) {
        long curHp = hp;
        long curAttack = ATTACK;

        for (int[] roomInfo : roomInfos) {
            if (roomInfo[0]==1) {
                int monsterHp = roomInfo[2];
                int monsterAttack = roomInfo[1];
                long attackCount = (monsterAttack % curAttack == 0) ? (monsterHp / curAttack) - 1 : (monsterHp / curAttack);
                curHp -= monsterAttack * attackCount;
                if (curHp <= 0) {
                    return false;
                }
            } else {
                curAttack += roomInfo[1];
                curHp += roomInfo[2];
                if (curHp >= hp) {
                    curHp = hp;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        long result = 0L;

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        ATTACK = Integer.parseInt(st.nextToken());

        roomInfos = new int[N][3];

        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            roomInfos[i][0] = Integer.parseInt(st.nextToken());
            roomInfos[i][1] = Integer.parseInt(st.nextToken());
            roomInfos[i][2] = Integer.parseInt(st.nextToken());
        }

        long left = 1L;
        long right = Long.MAX_VALUE - 1L;

        while (left <= right) {
            long mid = (left + right) / 2;
            if (isClear(mid)) {
                result = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        sb.append(result);
        System.out.println(sb.toString());
    }
}
