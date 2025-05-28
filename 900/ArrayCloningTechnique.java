import java.util.*;
public class c2 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        for(int i=0;i<a;i++)
        {
            int z=sc.nextInt();
            Map<Integer, Integer> b=new HashMap<>();
            for (int j=0;j<z;j++) {
                int c=sc.nextInt();
                b.put(c,b.getOrDefault(c,0)+1);
            }
            int m=0;
            for (Map.Entry<Integer,Integer> entry:b.entrySet()) {
                m=Math.max(m,entry.getValue());
            }
            int f=0;
            while (m<z) {
                int d=Math.min(z-m,m);
                f=f+1+d;
                m=m+d;
            }
            System.out.println(f);
        }
    }
}
