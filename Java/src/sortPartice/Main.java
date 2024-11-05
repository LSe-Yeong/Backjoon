package sortPartice;

import java.util.*;

public class Main {
    public static void main(String[] args){
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int[] list = {6,5,9,1,6,3,10,5,8};
        int[][] list2 = {
                {3, 5},
                {1, 2},
                {2, 8},
                {2, 7}
        };

        Map<String,Integer> map = new HashMap<>();
        map.put("A",10);
        map.put("B",2);
        map.put("C",15);
        map.put("D",5);
        map.put("E",9);
        map.put("F",12);

        ArrayList<Map<String, Object>> listOfMaps = new ArrayList<>();

        // 각 Map 생성
        listOfMaps.add(createMap("Alice", 30));
        listOfMaps.add(createMap("Bob", 25));
        listOfMaps.add(createMap("Charlie", 35));

        for(int i = 0;i<list.length;i++){
            pq.offer(list[i]);
        }
        for(int i = 0;i<list.length;i++){
            System.out.print(pq.poll()+" ");
        }
        System.out.println();

        pq = new PriorityQueue<>(Collections.reverseOrder());
        for(int i = 0;i<list.length;i++){
            pq.offer(list[i]);
        }
        for(int i = 0;i<list.length;i++){
            System.out.print(pq.poll()+" ");
        }
        System.out.println();

        PriorityQueue<String> pq1 = new PriorityQueue<>(Comparator.comparing(map::get)); //String을 입력받아 value를 반환

        pq1.addAll(map.keySet());

        for(int i = 0;i<map.size();i++){
            System.out.print(map.get(pq1.poll())+" ");
        }

        System.out.println();

        pq1 = new PriorityQueue<>(Comparator.comparing(map::get).reversed());

        pq1.addAll(map.keySet());

        for(int i = 0;i<map.size();i++){
            System.out.print(map.get(pq1.poll())+" ");
        }

        System.out.println();

        PriorityQueue<Map<String,Object>> pq2 = new PriorityQueue<>(Comparator.comparing((Map<String,Object> map1)-> (Integer) map1.get("age")));

        // 리스트의 Map을 PriorityQueue에 추가
        pq2.addAll(listOfMaps);

        // PriorityQueue에서 값 출력
        while (!pq2.isEmpty()) {
            Map<String, Object> element = pq2.poll();
            System.out.println("Name: " + element.get("name") + ", Age: " + element.get("age"));
        }

        pq2 = new PriorityQueue<>(Comparator.comparing((Map<String,Object> map1)-> (Integer) map1.get("age")).reversed());

        pq2.addAll(listOfMaps);

        // PriorityQueue에서 값 출력
        while (!pq2.isEmpty()) {
            Map<String, Object> element = pq2.poll();
            System.out.println("Name: " + element.get("name") + ", Age: " + element.get("age"));
        }

        //여기서 부터 정렬
        Arrays.sort(list);
        for(int i=0;i<list.length;i++){
            System.out.print(list[i]+" ");
        }
        System.out.println();

        Arrays.sort(list2,Comparator.comparing((int[] row)-> (Integer) (row[0])).reversed().thenComparing(row -> row[1]).reversed());
        for(int i=0;i<list2.length;i++){
            for(int j=0;j<list2[i].length;j++) {
                System.out.print(list2[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();


    }

    // Map을 생성하는 헬퍼 메서드
    private static Map<String, Object> createMap(String name, int age) {
        Map<String, Object> map = new HashMap<>();
        map.put("name", name);
        map.put("age", age);
        return map;
    }
}
