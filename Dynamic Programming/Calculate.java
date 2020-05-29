import java.util.Scanner;
class task{
    public int Main1(int[] Memo,int n){
        if(Memo[n]==-1){
            if(n==0 || n==1){
                Memo[n]=n;
            }
            else{
                int res=Main1(Memo,n-1)+Main1(Memo,n-2);
                Memo[n]=res;
            }

        }
        return(Memo[n]);
    
    }
    
}

class Calculate{
    public static void main(String[] args){
        task obj=new task();
        int n=10;
        int[] Memo = new int[n];
        for(int i=0;i<n;i++){
            Memo[i]=-1;
        }
        obj.Main1(Memo,n-1);
        System.out.println(Memo[n-1]);

    }
}