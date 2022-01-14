import java.util.Arrays;
import java.util.Scanner;

//client program
public class LingoGame {
	
	public static void main (String [] args) {
		
		//command line argument
		
		String wordsFile = "small5.txt"; // by default if nothing else entered in run config
				
		if (args.length >= 1) 
		{
			wordsFile = args[0];
		}
	
		int numTries = 0; 
		
		LingoServer lServer = new LingoServer(wordsFile); 
				
		//starting output in console 
		System.out.println("Welcome to Lingo!"); 
		
		System.out.println("\nThis is a word guessing game. Each word is 5 letters long. You have 5 tries to guess the word correctly. \nType 'QUIT' to stop the game at any time." );
		
		System.out.println(lServer.toString()); 
		
		//ask for user input 
		Scanner input = new Scanner(System.in);
		
		boolean playAgain = true; 
		
	
		while (lServer.hasLingo()) //while there are still objects in lingo array 
		{  
			Lingo lWord = lServer.getLingo(); //getting word 
			System.out.println("Guess the word! It starts with " + lWord.first()); 
			
			boolean goodGuess = true; //if guess is correct or not based off of 2s in the array 

			for (numTries = 0; numTries < 5; numTries++)
			{
			
				System.out.println("Your guess # " + (numTries+1) + ": ");
				
				String userGuess = input.nextLine();
							
				if (userGuess.equals("QUIT") || userGuess.equals("quit") )
				{
					playAgain = false; 
					break;
					
				}
								
				int [] status = lWord.guessWord(userGuess); 
				
				for (int i = 0; i < status.length; i++) 
				{
					
					if (status[i] != 2) 
					{
						goodGuess = false; 
						break;
						
					}
		
				}
				
				if (goodGuess == true)
				{
					System.out.println("\nNice job!\n"); 
					break; 
				}
				
				goodGuess = true; //word is 100% correct 
				
				
			}
			
			if (numTries == 5) {
				System.out.println("The word is " + lWord.toString()); 
				System.out.println("\nBetter luck next time...\n");
			}
			
			if (playAgain == false)
			{
				System.out.println("Thanks for playing!"); 
				break;
			}
			
			System.out.println(lServer.toString()); //printing out word after guessing
		
		}
	
	}
		
}