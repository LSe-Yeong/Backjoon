package P4779;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();

        String str;
        while((str=br.readLine())!=null){
            int n=Integer.parseInt(str);
            int count= (int) Math.pow(3,n);
            char[] shape=new char[count];
            for(int i=0;i<count;i++){
                shape[i]='-';
            }
            divide(shape,0,count);
            for(int i=0;i< shape.length;i++){
                sb.append(shape[i]);
            }
            sb.append("\n");
            System.out.print(sb.toString());
            sb.setLength(0);
        }
    }
    public static void divide(char[] shape,int start,int size){
        int newSize=size/3;
        if(size==1){
            return;
        }
        for(int i=start+newSize;i<start+2*newSize;i++){
            shape[i]=' ';
        }
        divide(shape,start,newSize);
        divide(shape,start+2*newSize,newSize);
    }
}
