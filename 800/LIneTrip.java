import java.util.*;

public class java1 
{

    public static void main(String[] args) 
    {
       Scanner sc=new Scanner(System.in);
       int a=sc.nextInt();
       for(int i=0;i<a;i++)
       {
           int b=sc.nextInt();
           int c=sc.nextInt();
           int[] d=new int[b+2];
           d[0]=0;
           d[b+1]=c;
           for(int j=1;j<b+1;j++)
           {
               d[j]=sc.nextInt();
           }
          int  max=0;
           for(int k=0;k<b+1;k++)
           {
               if((d[k+1]-d[k])>max)
               {
                   max=(d[k+1]-d[k]);
               }
           }
           if(max>2*(d[b+1]-d[b]))
           {
               System.out.println(max);
           }
           else
           {
               System.out.println(2*(d[b+1]-d[b]));
           }
       }
       sc.close();
    }
}
