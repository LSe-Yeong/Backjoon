package P1920;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();
        ArrayList<Integer> arrayList=new ArrayList<>();

        int n=Integer.parseInt(br.readLine());
        StringTokenizer st=new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++){
            arrayList.add(Integer.parseInt(st.nextToken()));
        }
        Collections.sort(arrayList);

        int m=Integer.parseInt(br.readLine());
        st=new StringTokenizer(br.readLine());
        for(int i=0;i<m;i++){
            int key=Integer.parseInt(st.nextToken());
            boolean isInclude = binarySearch(arrayList,key);
            if(isInclude){
                sb.append("1").append("\n");
            }
            else{
                sb.append("0").append("\n");
            }
        }
        System.out.print(sb.toString());
    }
    public static boolean binarySearch(ArrayList<Integer> arrayList,int key){
        int left=0;
        int right= arrayList.size()-1;
        int mid;
        while(left<=right){
            mid=(left+right)/2;
            if(arrayList.get(mid)<key){
                left=mid+1;
            }
            else if(arrayList.get(mid)>key){
                right=mid-1;
            }
            else{
                return true;
            }
        }
        return false;
    }
}
