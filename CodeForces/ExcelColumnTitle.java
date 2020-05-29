/*// Java program to find Excel 
// column name from a given 
// column number 
  
public class ExcelColumnTitle { 
    // Function to print Excel column 
    // name for a given column number 
    private static void printString(int columnNumber) 
    { 
        // To store result (Excel column name) 
        StringBuilder columnName = new StringBuilder(); 
  
        while (columnNumber > 0) { 
            // Find remainder 
            int rem = columnNumber % 26; 
  
            // If remainder is 0, then a 
            // 'Z' must be there in output 
            if (rem == 0) { 
                columnName.append("Z"); 
                columnNumber = (columnNumber / 26) - 1; 
            } 
            else // If remainder is non-zero 
            { 
                columnName.append((char)((rem - 1) + 'A')); 
                columnNumber = columnNumber / 26; 
            } 
        } 
  
        // Reverse the string and print result 
        System.out.println(columnName.reverse()); 
    } 
  
    // Driver program to test above function 
    public static void main(String[] args) 
    { 
        printString(26); 
        printString(51); 
        printString(52); 
        printString(80); 
        printString(676); 
        printString(702); 
        printString(705); 
    } 
} 
*/

class ExcelColumnTitle{  
 public static void main(String args[]){  
  try{  
    try{  
     System.out.println("going to divide");  
     int b =39/0;  
    }catch(ArithmeticException e){System.out.println(e);}  
   
    try{  
    int a[]=new int[5];  
    a[5]=4;  
    }catch(ArrayIndexOutOfBoundsException e){System.out.println(e);}  
     
    System.out.println("other statement");  
  }catch(Exception e){System.out.println("handeled");}  
  
  System.out.println("normal flow..");  
 }  
}    

/*
public class ExcelColumnTitle{  
   static void validate(int age){  
     if(age<18)  
      throw new ArithmeticException("not valid");  
     else  
      System.out.println("welcome to vote");  
   }  
   public static void main(String args[]){  
      validate(13);  
      System.out.println("rest of the code...");  
  }  
}  
*/