package P1991;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static Node head=new Node('A',null,null);

    static StringBuilder stringBuilder=new StringBuilder();

    static class Node{
        char value;
        Node left;
        Node right;

        public Node(char value, Node left, Node right){
            this.value=value;
            this.left=left;
            this.right=right;
        }
    }

    public static void insertNode(Node node,char root,char left, char right){
        if(node.value==root){
            if(left!='.') {
                node.left = new Node(left, null, null);
            }
            if (right != '.') {
                node.right=new Node(right,null,null);
            }
        }
        else{
            if(node.left!=null){
                insertNode(node.left,root,left,right);
            }
            if(node.right!=null){
                insertNode(node.right,root,left,right);
            }
        }
    }

    public static void preOrder(Node tree){
        if(tree == null){
            return ;
        }
        stringBuilder.append(tree.value);
        preOrder(tree.left);
        preOrder(tree.right);
    }

    public static void inOrder(Node tree){
        if(tree==null){
            return;
        }
        inOrder(tree.left);
        stringBuilder.append(tree.value);
        inOrder(tree.right);
    }

    public static void postOrder(Node tree){
        if(tree==null){
            return;
        }
        postOrder(tree.left);
        postOrder(tree.right);
        stringBuilder.append(tree.value);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());

        for(int i=0;i<n;i++){
            StringTokenizer st=new StringTokenizer(br.readLine());
            char root=st.nextToken().charAt(0);
            char left=st.nextToken().charAt(0);
            char right=st.nextToken().charAt(0);

            insertNode(head,root,left,right);
        }

        preOrder(head);
        System.out.println(stringBuilder.toString());
        stringBuilder.setLength(0);

        inOrder(head);
        System.out.println(stringBuilder.toString());
        stringBuilder.setLength(0);

        postOrder(head);
        System.out.println(stringBuilder.toString());
        stringBuilder.setLength(0);
    }
}
