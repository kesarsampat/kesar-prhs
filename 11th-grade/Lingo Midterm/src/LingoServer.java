import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;
import java.util.stream.IntStream;

public class LingoServer {
	private Lingo [] lingoArray; 
	private int numWords = 0; 
	
	/**
	 * Read in set of 5-letter words from a file & store them
	 * @param fileName
	 */
	public LingoServer(String fileName) {
		
		/*
		 * default number at 1024 as the middle ground between small and big file 
		 */
		Lingo [] lingoArrayTemp = new Lingo[1024]; 
	
		int i = 0; 
		
		//read in a file 
		try {
			Scanner inFile = new Scanner(new File(fileName));
			
			while(inFile.hasNextLine()) {
				String wordLine = inFile.nextLine(); 
				
				lingoArrayTemp[i] = new Lingo(wordLine); 
				
				if (i == lingoArrayTemp.length -1)
				{
					lingoArrayTemp = doubleArray(lingoArrayTemp);
				}
				
				i++; 				
				this.numWords++; 
			
			}
	
		}
		
		catch (FileNotFoundException ex) {
			System.out.println("File could not be located.");
		}
		
		this.lingoArray = lingoArrayTemp; 

	
	}
	
	/**
	 * Doubles the size of the original array when length of old array fills up 
	 * @param oldArray
	 * @return newArray - double the size 
	 */
	public Lingo [] doubleArray(Lingo [] oldArray)
	{
		//new length of array 
		int newLength = (oldArray.length) *2; //double it 
		
		//declare new array 
		Lingo [] newArray = new Lingo[newLength]; 
				
		//copy 
		System.arraycopy(oldArray, 0, newArray, 0, oldArray.length);
			
		return newArray; 
	
	}
	
	/**
	 * Checks to see if array has lingo objects still  
	 * @return true if any Lingo objects remain; false otherwise 
	 */
	public boolean hasLingo() {
		
		boolean has = false; 
		
		for (int i = 0; i < lingoArray.length; i++) {
			if (lingoArray[i] != null) {
				has = true; 
				break;
			}
		
		}

		return has; 
	}
	
	/**
	 * Obtain a lingo object (word) from array and store 
	 * @return random Lingo object from the array (with elimination) 
	 */
	public Lingo getLingo() {
		
		
		if (hasLingo() == false) { //no lingo objects are left 
			return null; 
		}
	
		Random rand = new Random(); //make random object 
		
		int lRand = 0;
		
		Lingo lObj = null; 
		
		while (lObj == null) { 
			lRand = rand.nextInt(0, lingoArray.length);
			lObj = lingoArray[lRand]; 
			//System.out.println(lRand);

		}
		
		lingoArray[lRand] = null; //using null to eliminate  
		numWords--; //reducing count every time word is eliminated
		
		return lObj;
		
		
	}
	
	/**
	 * Return a String containing some info
	 */
	public String toString() {
		String s = null;  
		s = "\nNumber of words: " + numWords + "\n" + "Capacity: " + lingoArray.length + "\n"; 
		
		return s; 
		
		
	}
	

}
