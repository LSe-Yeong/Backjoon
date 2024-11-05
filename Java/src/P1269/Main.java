package P1269;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        HashSet<Integer> hashSet1 = new HashSet<>();
        HashSet<Integer> hashSet2 = new HashSet<>();
        ArrayList<Integer> A = new ArrayList<>();
        ArrayList<Integer> B = new ArrayList<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for(int i=0;i<N;i++){
            hashSet1.add(Integer.parseInt(st.nextToken()));
        }

        st = new StringTokenizer(br.readLine());
        for(int i=0;i<M;i++){
            hashSet2.add(Integer.parseInt(st.nextToken()));
        }

        Iterator itor = hashSet2.iterator();
        while(itor.hasNext()){
            int element = (int) itor.next();
            if(!hashSet1.contains(element)){
               B.add(element);
            }
        }

        itor = hashSet1.iterator();
        while(itor.hasNext()){
            int element = (int) itor.next();
            if(!hashSet2.contains(element)){
                A.add(element);
            }
        }

        sb.append(A.size()+B.size());
        System.out.print(sb.toString());
    }
}
