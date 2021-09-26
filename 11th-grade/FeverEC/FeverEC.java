import java.util.InputMismatchException;
import java.util.Scanner;

import javax.swing.JOptionPane;

/**
 * @author Kesar Sampat
 * Period 6
 * 
 *
 */
public class FeverEC {
	public static void main(String[] args)
	
	{
		String fever = ask("Do you have a fever?");
		System.out.println(fever);
		
		switch(fever) {
		
		case "YES":
			String coughing = ask("Do you have a cough?");
			
			if (coughing.equals("YES"))
				handleCough();
			
			else {
				String headache = ask("Do you have a headache?");
				
				if (headache.equals("YES"))
					handleHeadache();
				else {
					System.out.println("no headache");
					
				}
			}
			break;
			
		case "NO":
			showPossibleDiagnosis("Insufficeint information to list possiblites");
			break;
		
		default:
			System.out.println("Please enter yes or no.");
		}
	}
		
	//methods 
	
	public static String ask(String question) 
	
	{
		String answer = JOptionPane.showInputDialog(null, question);
		
		return answer.toUpperCase();
		
	
	}
	
	public static void showPossibleDiagnosis(String diag) 
	{
		JOptionPane.showMessageDialog(null, diag);

	}
	
	public static void handleCough()
	{
		System.out.println("Coughing");
		
	}
	
	public static void handleHeadache()
	{
		
		
	}
	
	public static void handleJoints()
	{
		
		
	}
	
	
	
	
	
	

}
