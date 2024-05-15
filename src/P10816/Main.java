package P10816;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();
        HashMap<String,Integer> hashMap=new HashMap<>();

        int n=Integer.parseInt(br.readLine());
        StringTokenizer st=new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++){
            String num=st.nextToken();
            if(hashMap.get(num)==null){
                hashMap.put(num,1);
            }
            else{
                int count = hashMap.get(num);
                count++;
                hashMap.put(num,count);
            }
        }

        int m=Integer.parseInt(br.readLine());
        st =new StringTokenizer(br.readLine());
        for(int i=0;i<m;i++){
            String num= st.nextToken();
            if(hashMap.get(num)!=null){
                sb.append(hashMap.get(num)).append(" ");
            }
            else{
                sb.append("0 ");
            }
        }
        System.out.print(sb.toString());
    }
}
