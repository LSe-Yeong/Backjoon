import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        System.out.println("Hello world!");

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        while(st.hasMoreTokens()) {
            int n = Integer.parseInt(st.nextToken());
            if(n==-1) {
                break;
            }
            else {
                System.out.println(n);
            }
        }
    }
}
