package P7785;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();
        HashSet<String> hashSet=new HashSet<>();
        ArrayList<String> arrayList=new ArrayList<>();

        int n=Integer.parseInt(br.readLine());
        for(int i=0;i<n;i++){
            StringTokenizer st=new StringTokenizer(br.readLine());
            String name=st.nextToken();
            String status=st.nextToken();
            if(status.equals("enter")){
                hashSet.add(name);
            }
            else{
                hashSet.remove(name);
            }
        }

        Iterator<String> iterator = hashSet.iterator();
        while(iterator.hasNext()){
            String value=iterator.next();
            arrayList.add(value);
        }
        Collections.sort(arrayList,Collections.reverseOrder());

        for(int i=0;i<arrayList.size();i++){
            sb.append(arrayList.get(i)).append("\n");
        }
        System.out.print(sb.toString());
    }
}
