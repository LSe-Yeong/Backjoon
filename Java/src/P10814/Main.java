package P10814;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        ArrayList<Map<String,Object>> list=new ArrayList<>();

        int N = Integer.parseInt(br.readLine());

        for(int i=0;i<N;i++) {
            Map<String, Object> map = new HashMap<String, Object>();
            StringTokenizer st = new StringTokenizer(br.readLine());
            int age = Integer.parseInt(st.nextToken());
            String name = st.nextToken();
            map.put("id",i);
            map.put("age",age);
            map.put("name",name);
            list.add(map);
        }

        list.sort(Comparator.comparing((Map<String,Object> m) -> (int) m.get("age"))
                .thenComparing(m -> (int) m.get("id")));

        for(int i=0;i<list.size();i++){
            sb.append(list.get(i).get("age")+" "+list.get(i).get("name"));
            sb.append("\n");
        }

        System.out.print(sb.toString());
    }
}
