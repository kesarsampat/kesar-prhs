import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

/**
 * @author Kesar Sampat 
 * PD 6 - APCSA 
 * 
 *
 */
public class InventoryDriver {
	public static void main(String [] args) throws FileNotFoundException
	{		
		Inventory inventory = new Inventory();
		
		//read in file 
 		Scanner inFile=new Scanner(new File("inventoryText.txt"));
 		
 		inFile.nextLine(); //skip first 2 lines 
 		inFile.nextLine();
 		
 		while(inFile.hasNext())
 		{
 			String fileLine = inFile.nextLine();
			String [] products = fileLine.split(","); //split with commas and into a string 
			Product p = new Product(products[0].trim(), products[1].trim(), Integer.parseInt(products[2].trim()), Double.parseDouble(products[3].trim())); 
			inventory.addProduct(p);
			
			//System.out.println(p.toString()); 
		
 		}
 		//System.out.println(inventory.toString()); 
 		
 		

 		inFile.close();
 		
 		//display a menu of choices for user to choose from 
 		
 	 		
 		System.out.println("Welcome to the Self-Care Inventory! \nPlease choose a number.");
 		
 		System.out.println("\n1. Display all Products in the inventory"); 
 		System.out.println("2. Display a single product "); 
 		System.out.println("3. Value of the current inventory"); 
 		System.out.println("4. Add a product to the inventory"); 
 		System.out.println("5. Add quantities to the inventory of a product"); 
 		System.out.println("6. Remove quantities from the inventory of a product"); 
 		System.out.println("7. Discontinue a Product"); 
 		System.out.println("8. Quit"); 
 		
 		boolean quit = false; 
 		
 		//ask for user input 
 		Scanner input = new Scanner(System.in); 
 		System.out.println("\nChoice Number: ");
 		String userChoice = input.nextLine();
 	 		 		
 		while (!quit)
 		{
 		
	 		switch(userChoice) 
	 		
	 		{
		 		case "1": //display all products in the inventory 
		 			System.out.println(inventory.toString());
		 			break; 
		 		
		 		case "2": //single product
		 		
		 			System.out.println("Choose to search by either stock number (1) or product name (2) ?");
		 	 		String uC2 = input.nextLine();
		 	 		
		 	 		int c2 = Integer.parseInt(uC2); 
		 	 		
		 	 		if (c2 == 1) 
		 	 		{
		 	 			System.out.println("\nEnter Stock Number: ");
		 	 			String uNum = input.nextLine();
		 	 			
		 	 			long uStockNum = Long.parseLong(uNum); //change type into Long 
		 	 			
		 	 			//displaying data
		 	 			System.out.println(inventory.findbyID(uStockNum).toString()); 
		 	 			
		 	 			
		 	 		}
		 	 		
		 	 		else if (c2 == 2) 
		 	 		{
		 	 			System.out.println("\nEnter Product Name: ");
		 	 			String uProductName = input.nextLine();
		 	 			
		 	 			//data display 
		 	 			System.out.println(inventory.findbyName(uProductName).toString()); 
		 	 			
		 	 			
		 	 		}
		 	 		
		 			break;
		 	 		
		 		case "3": //value of current inventory 
		 			System.out.println("Total Inventory Value: " + inventory.findInventoryValue()); 
		 			break;
		 		
		 		case "4": //add a product to the inventory 
		 					 			
		 			System.out.println("Product Name: "); 
		 			String uPName = input.nextLine();
		 			
		 			System.out.println("Product Description: "); 
		 			String uPDesc = input.nextLine();
		 			
		 			System.out.println("How many in stock? : "); 
		 			String uStockNum = input.nextLine();
		 			
		 			System.out.println("Product Cost: "); 
		 			String uPCost = input.nextLine();
		 			
		 			Product p = new Product(uPName, uPDesc, Integer.parseInt(uStockNum), Integer.parseInt(uPCost));
		 			inventory.addProduct(p);
		 			
		 			System.out.println(uPName + " has been succesfully added to inventory!"); 
		 			
		 			break;
		 		
		 		case "5": //add quantities to the inventory of a product 
		 	
		 			System.out.println("Would you like ID (1) or product name (2) to add quantities?: ");  
		 			String uC5 = input.nextLine();
		 		
		 	 		int c5 = Integer.parseInt(uC5); 
		 	 		
		 	 		if (c5 == 1) 
		 	 		{
		 	 			System.out.println("\nEnter Stock Number: ");
		 	 			String uNum5 = input.nextLine();
		 	 			long uStockNum5 = Long.parseLong(uNum5); //change type into Long 

		 	 			
		 	 			System.out.println("\nHow many would you like to add?: ");
		 	 			String num = input.nextLine();
		 	 			
		 	 				 	 			
		 	 			inventory.addToStock(uStockNum5, Integer.parseInt(num));
		 	 			
		 	 			Product pd = inventory.findbyID(uStockNum5); 
		 	 			
		 	 			System.out.println("The new quantity of " + pd.getName() + " is " + pd.getNumInStock()); 
		 	 		
		 	 		
		 	 		}
		 	 		
		 	 		else if (c5 == 2) 
		 	 		{
		 	 			System.out.println("\nEnter Product Name: ");
		 	 			String uNum5 = input.nextLine();

		 	 			Product pd = inventory.findbyName(uNum5);

		 	 			
		 	 			if (pd!= null)
		 	 			{
	
			 	 			System.out.println("\nHow many would you like to add?: ");
			 	 			String num = input.nextLine();
			 	 			
			 	 			long pdID = pd.getStockId();  

		
			 	 			inventory.addToStock(pdID, Integer.parseInt(num));
			 	 			
			 	 			Product pd2 = inventory.findbyID(pdID); 
			 	 			
			 	 			System.out.println("The new quantity of " + pd2.getName() + " is " + pd2.getNumInStock()); 
		 	 			}
		 	 		
		 	 		}
		 			break;
		 		case "6": //remove quantities to the inventory of a product 

		 			System.out.println("Would you like ID (1) or product name (2) to add quantities?: ");  
		 			String uC6 = input.nextLine();
		 		
		 	 		int c6 = Integer.parseInt(uC6); 
		 	 		
		 	 		if (c6 == 1) 
		 	 		{
		 	 			System.out.println("\nEnter Stock Number: ");
		 	 			String uNum6 = input.nextLine();
		 	 			long uStockNum6 = Long.parseLong(uNum6); //change type into Long 

		 	 			
		 	 			System.out.println("\nHow many would you like to remove?: ");
		 	 			String num = input.nextLine();
		 	 			
		 	 				 	 			
		 	 			inventory.removeFromStock(uStockNum6, Integer.parseInt(num));
		 	 			
		 	 			Product pd = inventory.findbyID(uStockNum6); 
		 	 			
		 	 			System.out.println("The new quantity of " + pd.getName() + " is " + pd.getNumInStock()); 
		 	 		
		 	 		
		 	 		}
		 	 		
		 	 		else if (c6 == 2) 
		 	 		{
		 	 			System.out.println("\nEnter Product Name: ");
		 	 			String uNum6 = input.nextLine();

		 	 			Product pd = inventory.findbyName(uNum6);

		 	 			
		 	 			if (pd!= null)
		 	 			{
	
			 	 			System.out.println("\nHow many would you like to remove?: ");
			 	 			String num = input.nextLine();
			 	 			
			 	 			long pdID = pd.getStockId();  

		
			 	 			inventory.removeFromStock(pdID, Integer.parseInt(num));
			 	 			
			 	 			Product pd2 = inventory.findbyID(pdID); 
			 	 			
			 	 			System.out.println("The new quantity of " + pd2.getName() + " is " + pd2.getNumInStock()); 
		 	 			}
		 	 		
		 	 		}
		 			break;
		
		 		case "7": //discontinue a product when given the id number
		 			System.out.println("Choose to search by either stock number (1) or product name (2) ?");
		 	 		String uC7 = input.nextLine();
		 	 		
		 	 		int c7 = Integer.parseInt(uC7); 
		 	 		
		 	 		if (c7 == 1) 
		 	 		{
		 	 			System.out.println("\nEnter Stock Number: ");
		 	 			String uNum7 = input.nextLine();
		 	 			
		 	 			long uStockNum7 = Long.parseLong(uNum7); //change type into Long 
		 	 			
		 	 			Product prod = inventory.findbyID(uStockNum7); 
		 	 			
		 	 			System.out.println("\nDo you really want to discontinue " + prod.getName() + "? (y/n)");
		 	 			String userCheck = input.nextLine();
		 	 			
		 	 			if (userCheck.equals("y") || userCheck.equals("Y"))
		 	 			{
		 	 				inventory.discontinueProduct(uStockNum7);
		 	 				System.out.println(prod.getName() + " was successfully deleted from the inventory."); 
		 	 				
		 	 			}
		 	 			
		 	 			else if ((userCheck.equals("n") || userCheck.equals("N")))
		 	 			{
		 	 				continue; 
		 	 				
		 	 			}
		 	 		
		 	 		}
		 	 		
		 	 		else if (c7 == 2) 
		 	 		{
		 	 			System.out.println("\nEnter Product Name: ");
		 	 			String prodName = input.nextLine();
		 	 			
		 	 			Product pd = inventory.findbyName(prodName); 
		 	 			if (pd!= null)
		 	 			{
		 	 		
			 	 			long pdID = pd.getStockId(); 
			 	 			
			 	 			System.out.println("\nDo you really want to discontinue " + prodName + "? (y/n)");
			 	 			String userCheck = input.nextLine();
			 	 			
			 	 			if (userCheck.equals("y") || userCheck.equals("Y"))
			 	 			{
			 	 				inventory.discontinueProduct(pdID);
			 	 				System.out.println(prodName + " was successfully deleted from the inventory."); 
			 	 				
			 	 			}
			 	 			
			 	 			else if ((userCheck.equals("n") || userCheck.equals("N")))
			 	 			{
			 	 				continue; 
			 	 				
			 	 			}
		 	 			}
		 	 		
		 	 		}
		 	 	
		 			break;
		 			
		 		case "8": 
		 			quit = true; 
		 			System.out.println("QUIT!");
		 			break;
		 		
		 			 
		 		default:
		 			break; 
		 			
		 			
		 		}
	 		
	 		if (!quit)
	 		{
	 			System.out.println("\nChoice Number: ");
	 	 		userChoice = input.nextLine();
	 		}
	 		
		 		
	 		
	 	}
	 
	}
}
