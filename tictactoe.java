import java.util.Scanner;

public class TicTacToe{    

    private static Scanner scanner;
	private static Scanner scanner2;
	private static Scanner scanner3;

	public static void main(String[] args){
		
	if(args.length== 0){
	    twoHumanPlayers();
	}
        else if(args.length ==1 && args[0].equals("-c")){
	    twoComputers();  
	}
        else if(args.length == 2 && args[0].equals("-c") && args[1].equals("2")){
	    playerComputer(); 
	}
        else if(args.length == 2 && args[0].equals("-c") && args[1].equals("1")){
	    computerPlayer(); 
	}
	// Add a command line option "-a", which stands for "advanced". 
	// This option, if used, makes any computer players take their turns with more advanced logic,
	// such as using a minimax algorithm to determine the best move.
	else if(args.length == 3 && args[0].equals("-c") && args[1].equals("1") && args[2].equals("-a")){
	    playerComputerAdvanced(); 
	}

	
	else{
	  System.out.println("Usage: java TicTacToe [-c [1|2]]");
	  }		      	
    }
    private static void playerComputerAdvanced() {
		  
	    Computer p1= new Computer();
	    Computer p2= new Computer();
	    char c1= 'X'; 
	    char c2= 'O';
	    int a =0;
	    boolean flag= false;
	    System.out.println("Current Board");
	    p1.printBoard();
	    do{
		a = p1.makeMove('O','X');
		System.out.println(" ");
		System.out.printf("Player 1 (computer) chooses position  %d", a );
		System.out.println("");
		p1.changeBoard(a,c1);
		p2.changeBoard(a,c1);
		p1.printBoard();
		if(p1.checkWinner(c1)){
 		    System.out.println("Player 1 you win!");
		    flag= true;
		    System.exit(0);
		}
		if(p1.isaTie()){
		    System.out.println("It's a tie :(");
		    flag=true;
		    System.exit(0);
		}

		a = p2.makeMove('X','O');
		System.out.printf("Player 2 (computer) chooses position  %d", a );
		System.out.println("");
		p2.changeBoard(a,c2);
		p1.changeBoard(a,c2);
		p2.printBoard();
		if(p2.checkWinner(c2)){
		    System.out.println("Player 2 you win!");
		    flag= true;
		    System.exit(0);
		  }
		if(p2.isaTie()){
		    System.out.println("It's a tie :(");
		    flag=true;
		    System.exit(0);
		}
	    }while(flag==false);
    }	
	
	static void twoHumanPlayers(){
       	    scanner = new Scanner(System.in);    
	    Human p1= new Human();	    
	    Human p2= new Human();
	    char c1= 'X'; 
	    char c2= 'O';

	    System.out.println("Game Board:");
	    p1.printBoard();
	    
	    boolean flag= false;
	    do{ 
	    System.out.println(" ");
	    System.out.print("Player 1, please enter a move (1-9):");	    
	    System.out.println(" ");
	    System.out.println(" ");
	    int number = scanner.nextInt();

	    while(p1.isAvailable(number)==false){
	     System.out.print("That position is unavailable, please enter a new one: ");
	     number = scanner.nextInt();
	    }
		    
	    //First player**
	    if(p1.isAvailable(number)){
		p1.changeBoard(number, c1);
		p2.changeBoard(number, c1);
		System.out.println("Game Board:");
		p1.printBoard();
		System.out.println(" ");
		if(p1.checkWinner(c1)){
		    System.out.println("Player 1 you win!");
		    flag= true;
		    System.exit(0);
		}
		if(p1.isaTie()){
		    System.out.println("It's a tie :(");
		    flag=true;
		    System.exit(0); 
		}

		//end 2nd if 
	    }// end first if
	    
	    //Second player **
	    System.out.print("Player 2, please enter a move (1-9):");
	    System.out.println(" ");
	    System.out.println(" ");
	    number = scanner.nextInt();

	   while(p1.isAvailable(number)==false){
	     System.out.print("That position is unavailable, please enter a new one: ");
	     number = scanner.nextInt();
	    }
	
	    if(p2.isAvailable(number)){
		p2.changeBoard(number,c2);
		p1.changeBoard(number,c2);
		System.out.println("Game Board:");
		p2.printBoard();
		System.out.println(" ");
		System.out.println(" ");
		if(p2.checkWinner(c2)){
		    System.out.println("Player 2 you win!");
		    flag= true;
		    System.exit(0);
		}//end 2nd if
		if(p2.isaTie()){
		    System.out.println("It's a tie :(");
		    flag=true;
		    System.exit(0);
		}
	    }
	    
	    }while(flag== false);
    }
    static void twoComputers(){
	    
	    Computer p1= new Computer();
	    Computer p2= new Computer();
	    char c1= 'X'; 
	    char c2= 'O';
	    int a =0;
	    boolean flag= false;
	    System.out.println("Current Board");
	    p1.printBoard();
	    do{
		a = p1.makeMove('O','X');
		System.out.println(" ");
		System.out.printf("Player 1 (computer) chooses position  %d", a );
		System.out.println("");
		p1.changeBoard(a,c1);
		p2.changeBoard(a,c1);
		p1.printBoard();
		if(p1.checkWinner(c1)){
 		    System.out.println("Player 1 you win!");
		    flag= true;
		    System.exit(0);
		}
		if(p1.isaTie()){
		    System.out.println("It's a tie :(");
		    flag=true;
		    System.exit(0);
		}

		a = p2.makeMove('X','O');
		System.out.printf("Player 2 (computer) chooses position  %d", a );
		System.out.println("");
		p2.changeBoard(a,c2);
		p1.changeBoard(a,c2);
		p2.printBoard();
		if(p2.checkWinner(c2)){
		    System.out.println("Player 2 you win!");
		    flag= true;
		    System.exit(0);
		  }
		if(p2.isaTie()){
		    System.out.println("It's a tie :(");
		    flag=true;
		    System.exit(0);
		}
	    }while(flag==false);
    }	
    
    static void computerPlayer(){
	 int a=0; 
	 scanner2 = new Scanner(System.in); 
	 Computer p1= new Computer();
       	 Player p2  = new Player();
	 char c1= 'X'; 
	 char c2= 'O';
	 boolean flag= false;

	 System.out.println("Current Board");
	 p1.printBoard();
	 
         do{
	 a = p1.makeMove('O','X');
	 
	 System.out.println(" ");
	 System.out.printf("Player 1 (computer) chooses position  %d", a );
	 System.out.println("");
	 p1.changeBoard(a,c1);
	 p2.changeBoard(a,c1);
	 System.out.println("Game Board:");
	 System.out.println(" ");
	 p1.printBoard();
	 if(p1.checkWinner(c1)){
	     System.out.println("Player 1 you win!");
	     flag= true;
	     System.exit(0);	     
	 }
	 if(p1.isaTie()){
	     System.out.println("It's a tie :(");
	     flag=true;
	     System.exit(0);
	 }
	 //**Player 2 
	 System.out.print("Player 2, please enter a move (1-9) : ");	 
	 int number = scanner2.nextInt();
	 while(p2.isAvailable(number)==false){
	     System.out.print("That position is unavailable, enter a new position: ");
	     number = scanner2.nextInt();
	 }	 
	 if(p2.isAvailable(number)){
	     p2.changeBoard(number, c2);
	     p1.changeBoard(number, c2);
	     System.out.println("Game Board:");
	     System.out.println(" ");
	     p2.printBoard();
	     System.out.println(" ");
	   
	     if(p2.checkWinner(c1)){
		 System.out.println("Player 2 you win!");
		 flag= true;
		 System.exit(0);
	     }//end 2nd if
	     if(p2.isaTie()){
		 System.out.println("It's a tie :(");
		 flag=true;
		 System.exit(0);
	     }// end 3rd if 
	 }// end first if   
	 

	 }while(flag==false);

     }

     static void playerComputer(){
	 scanner3 = new Scanner(System.in); 
	    Player p1=   new Player();
	    Computer p2= new Computer();
	    char c1= 'X'; 
	    char c2= 'O';
	    boolean flag= false;
	    int a=0; 
	   
	    System.out.println("Game Board:");
	    p1.printBoard();
	    do{
	    System.out.println(" ");	
	    System.out.println("Player 1, please enter a move (1-9) : ");
	    
	    int number = scanner3.nextInt();

	    while(p1.isAvailable(number)==false){
		System.out.print("That position is unavailable, enter a new position: ");
	     number = scanner3.nextInt();
	    }
		    
	    //First player**
	    if(p1.isAvailable(number)){
		p1.changeBoard(number, c1);
		p2.changeBoard(number, c1);
		System.out.println("Game Board:");
		System.out.println(" ");
		p1.printBoard();
		System.out.println(" "); 
		//p2.printBoard();
		
		if(p1.checkWinner(c1)){
		    System.out.println("Player 1 you win!");
		    flag= true;
		    System.exit(0);
		}//end 2nd if
		if(p1.isaTie()){
		    System.out.println("It's a tie :(");
		    flag=true;
		    System.exit(0);
		}// end 3rd if 
	    }// end first if

	    
	   a = p2.makeMove('X','O');
	   System.out.printf("Player 2 (computer) chooses position  %d", a );
	   System.out.println("");
	   p2.changeBoard(a,c2);
	   p1.changeBoard(a,c2);
	   System.out.println("Game Board:");
	   System.out.println(" ");
	   p2.printBoard();
	   System.out.println(" ");
	   if(p2.checkWinner(c2)){
	       System.out.println("Player 2 you win!");
	       flag= true;
	       System.exit(0); 
	   }
	   if(p2.isaTie()){
	       System.out.println("It's a tie :(");
	       flag=true;
	       System.exit(0);
	   }
	 	    
	    }while(flag==false); 
     }
}
