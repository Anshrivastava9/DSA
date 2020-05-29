class myapplet{
public static synchronized void main(String[] args) throws  
InterruptedException {  
     Thread f = new Thread();  
      f.start();  
      System.out.print("A");  
      f.wait(1000);  
      System.out.print("B");  
}  
}