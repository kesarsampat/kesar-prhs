import java.util.Arrays;

/**
 * @author Kesar Sampat 
 *
 */
public class Lingo {
	private String word; 
	
	/**
	 * Creates a new Lingo object from a 5 letter word 
	 * @param word
	 */
	public Lingo(String word) {
		this.word = word; 
		
		
	}
	
	/**
	 * @return first char of lingo word 
	 */
	public char first()	
	{
		char first = ' ';
		
		first = word.charAt(0);
		
		return first;
		
		
	}
	
	
	public int [] guessWord(String guess) 
	{
		//array - one location corresponding to each location in the Lingo word 
		int lingoArr [] = new int[5]; 
		
		//2 rule 
		for (int i = 0; i < lingoArr.length; i++) {

			//guess is less than 5 - extra chars = 0  
			if (i >= guess.length()) 
			{
				lingoArr[i] = 0;
				continue; 
				
			}
			
			//guess matches letter in same location
			if (guess.charAt(i) == (word.charAt(i))) {
				lingoArr[i] = 2; 
				
			}
			
		}
		
		
		//1 rule 
		for (int i = 0; i < lingoArr.length; i++)
		{		
			if (i >= guess.length())
			{
				lingoArr[i] = 0;
				continue;
				
			}
			
			if (lingoArr[i] == 2) {
				continue; //don't touch 
			}
			for (int j = 0; j < lingoArr.length; j++) 
			{
				
				if (word.charAt(j) == (guess.charAt(i))) {
					lingoArr[i] = 1 ;
					break;
				}
			}	
		}
		
		//0 rule 
		for (int i = 0; i < lingoArr.length; i++)
		{
			boolean found = false; 
			
			if (i >= guess.length())
			{
				lingoArr[i] = 0;
				continue; 
				
				
			}
			
			if (lingoArr[i] == 2 || lingoArr[i] == 1)
			{
				continue; //don't touch
			}

			for (int j = 0; j < lingoArr.length; j++) 
			{
				
				if (word.charAt(j) == (guess.charAt(i))) {
					found = true; 
				}
		
			}
			if (found == false) {
				lingoArr[i] = 0; 
			}
				
		}
		
		char [] charArray = new char[5]; 
		
		for (int i = 0; i < lingoArr.length; i++) {
			if (lingoArr[i] == 2)
			{
				charArray[i] =  Character.toUpperCase(guess.charAt(i)); 
				
			}
			
			else if ((lingoArr[i] == 1))
			{
				charArray[i] =  Character.toLowerCase(guess.charAt(i)); 

			}
			
			else {
					
					charArray[i] =  '-'; 

			}	
			
		}
		
		
		System.out.println(Arrays.toString(charArray));		
	
			
				
		return lingoArr; 
	}
	

	/**
	 *returns the Lingo word as a string 
	 */
	public String toString() 
	{
		String s = word; 
	
		
		return s; 
		
		
	}
	 

}
