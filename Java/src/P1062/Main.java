package P1062;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Deque;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.Stack;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {
    static int N;
    static int K;
    static List<Character> chList = new ArrayList<>();
    static List<Character> alphaList = List.of('b','d','e','f','g','h','j','k','l','m',
            'o','p','q',
            'r','s','u','v','w','x','y','z');
    static List<Integer> result = new ArrayList<>();
    static List<Set<String>> usedAlpha = new ArrayList<>();

    public static void backT(int cnt, int idx) {
        if(cnt == K-5) {
            int count = 0;
            for (Set<String> set : usedAlpha) {
                boolean flag = true;
                for (String s : set) {
                    if(!chList.contains(s.charAt(0))) {
                        flag = false;
                    }
                }
                if (flag) {
                    count++;
                }
            }
            result.add(count);
        }

        for(int i = idx; i <alphaList.size(); i++) {
            chList.add(alphaList.get(i));
            backT(cnt+1,i+1);
            chList.remove(chList.size()-1);
        }
    }

    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<String> strList = new ArrayList<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());


        for(int i = 0; i<N; i++) {
            String str = br.readLine();
            strList.add(str);
            List<String> list = Arrays.asList(str.split(""));
            Set<String> set = new HashSet<>();
            for (String s : list) {
                if (s.charAt(0) != 'a' && s.charAt(0) != 'n' && s.charAt(0) != 't' && s.charAt(0) != 'i'  && s.charAt(0) != 'c' ){
                    set.add(s);
                }
            }
            usedAlpha.add(set);
        }

        if(K < 5) {
            sb.append(0);
        } else {
            backT(0,0);
            Integer max = Collections.max(result);
            sb.append(max);
        }

        System.out.println(sb.toString());

    }
}
