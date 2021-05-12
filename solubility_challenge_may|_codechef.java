import java.util.Scanner;

class codechef
{
    public static void find () 
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0)
        {
            int x = sc.nextInt();
            int a = sc.nextInt();
            int b = sc.nextInt();
            System.out.println((a + (100 - x ) *b) * 10);
        }
    }
        public static void main(String[] args)
        {
            find();
        
        }
}
