import java.awt.*;  
public class AwtFrame  
{  
    AwtFrame(){  
        Frame f= new Frame("Aastha Shrivastava");    
            Label l1=new Label("Information Technology");
            Checkbox checkbox1 = new Checkbox("B.Tech");  
        checkbox1.setBounds(50,100,100,50);  
        Checkbox checkbox2 = new Checkbox("M.Tech");  
        checkbox2.setBounds(50,300,100,50);
        
        TextArea area=new TextArea("The School of Information Technology at RGTU was established in 2002-03. School of Information Technology offers M. Tech. in Computer Technology & Applications as well as in Information Technology. These courses prepare young graduates to take state of art challenges as required by the industry and R & D organizations Information Technology is a field that continues to evolve at a rate faster than other disciplines. Advances in the field have resulted in significant developments in Information and Communication Technologies, which in turn, has had a tremendous impact on the way research, is conducted. As a result the school has increased its emphasis on research during the last few years.");

        l1.setBounds(200,50,500,50);  
        area.setBounds(200,100,300,400);  
        Choice c=new Choice();
        c.setBounds(50,150, 100,100);  
        c.add("Sem-1");  
        c.add("Sem-2");  
        c.add("Sem-3");  
        c.add("Sem-4");  
        c.add("Sem-5");
        c.add("Sem-6");
        c.add("Sem-7");
        c.add("Sem-8");  
        f.add(c);
        Choice c12=new Choice();
        c12.setBounds(50,350, 100,100);  
        c12.add("Sem-1");  
        c12.add("Sem-2");  
        c12.add("Sem-3");  
        c12.add("Sem-4");  
        f.add(c12);    
        f.add(checkbox1);  
        f.add(checkbox2);  
                         
        f.add(l1); 
        f.add(area);  
        f.setSize(600,600);  
        f.setLayout(null);  
        f.setVisible(true);  
     }  
public static void main(String args[])  
{  
   new AwtFrame();  
}  
}  