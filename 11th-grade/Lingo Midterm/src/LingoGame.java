import java.util.Arrays;
import java.util.Scanner;

//client program
/*TO DO 
 * test program with bb thing 
 * have user choose file 
 */
public class LingoGame {
	
	public static void main (String [] args) {
		
		//command line argument
		
		String wordsFile = "small5.txt"; // by default 
				
		if (args.length >= 1) 
		{
			wordsFile = args[0];
		}
		
		
		int numTries = 0; 
			
		
		LingoServer lServer = new LingoServer(wordsFile); 
				
		
		System.out.println("Welcome to Lingo!"); 
		
		System.out.println(lServer.toString()); 
		
		//ask for user input 
		Scanner input = new Scanner(System.in);
		
		boolean playAgain = true; 
		
	
		while (lServer.hasLingo())
		{  
			Lingo lWord = lServer.getLingo(); //getting word 
			System.out.println("The word starts with " + lWord.first()); 
			
			boolean goodGuess = true; 

			for (numTries = 0; numTries < 5; numTries++)
			{
			
				System.out.println("Guess the word (type 'QUIT' to stop game): ");
				
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
				
				goodGuess = true;
				
				
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
			
			System.out.println(lServer.toString()); 
			//System.out.println(Arrays.toString(lWord.guessWord(userGuess)));
		
		}
	
	}
		
}