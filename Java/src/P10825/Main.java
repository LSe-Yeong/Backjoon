package P10825;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        List<Map<String, Object>> students = new ArrayList<>();

        for (int i = 0 ; i < n ; i++) {
            Map<String,Object> map = new HashMap<>();
            StringTokenizer st = new StringTokenizer(br.readLine());
            map.put("name",st.nextToken());
            map.put("kor",Integer.parseInt(st.nextToken()));
            map.put("eng",Integer.parseInt(st.nextToken()));
            map.put("math",Integer.parseInt(st.nextToken()));
            students.add(map);
        }

        students.sort(Comparator.comparing((Map<String,Object> m) -> (Integer) (m.get("kor")),Comparator.reverseOrder())
                .thenComparing((m) -> (Integer) (m.get("eng")))
                .thenComparing((m) -> (Integer) (m.get("math")),Comparator.reverseOrder())
                .thenComparing((m)->(String) (m.get("name"))));

        printName(students,sb);
    }

    private static void printName(List<Map<String,Object>> list, StringBuilder sb) {
        for(int i=0;i<list.size();i++) {
            Map<String,Object> map = list.get(i);
            sb.append(map.get("name"));
            sb.append("\n");
        }
        System.out.println(sb.toString());
    }
}
