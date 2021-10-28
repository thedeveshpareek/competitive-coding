import java.util.Scanner;

class FareCalculator{
public static void main(String arr[]){
    Scanner s = new Scanner(System.in);
    System.out.print("enter distance covered: ");
    int a = s.nextInt();
    int x=0,y=0;
    if(a<=5){
        System.out.println("fare for first 5KM : 50Rs");
        System.out.println("total distance: " +a+ " fare:50" );
    }   
    else if(a>5&&a<=20)
        {
        System.out.println("first 5 km fare : 50 Rs.");
        x = a-5;
        y=x*12;
        System.out.println("next " +x+ " KM fare @12 : " +y+ " Rs.");
        y=y+50;
        System.out.println("Total fare will be  : " +y+ " Rs.");
    }
    else if(a>20){
        System.out.println("first 5 km fare : 50 Rs.");
        x=20;
        y=20*12;
        System.out.println("next " +x+ " KM fare @12 : " +y+ " Rs.");
        int z = a-20;
        int b = z*14;
        System.out.println("next " +z+ " km  fare @14: " +b+ " Rs.");
        int c=y+b+50;
        System.out.println("Total fare will be  : " +c+ " Rs.");
    }
}   
}
