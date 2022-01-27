import java.util.ArrayList;
import java.util.Arrays;

/**
 * @author Kesar Sampat 
 * PD 6 APCSA
 * Business Inventory
 */
public class Inventory {
	
	private ArrayList<Product> productList = new ArrayList<Product>();
	private Product product; 
	

	public Inventory()
	{
		product = new Product(null, null, 0, 0); 
		
	}
	
	/**
	 * adds a new product to the inventory 
	 * @param p
	 */
	public void addProduct(Product p)
	{
		productList.add(p); 
			
	}
	
	/**
	 * product name appends the word "discontinued" and the amount in stock is set to 0. 
	 * @param id
	 * @return
	 */
	

	
	public Product discontinueProduct(long id) 
	{
		Product p = findbyID(id); 
		
		if (p != null) 
		{
			p.setName(p.getName() + " discontinued"); 
			p.setNumInStock(0);
			
		}
		return p;
	
	}
	


	public Product findbyName(String n) 
	{
		Product p = null; 
		
		for (int i = 0; i < productList.size(); i++) 
		{
			if (n.equals(productList.get(i).getName())) 
			{
				p = productList.get(i);
			}
		
		}
		
		return p;
	
	}
	
	public Product findbyID(long id) 
	{
		Product p = null; 
		
		for (int i = 0; i < productList.size(); i++) 
		{
			if (id == productList.get(i).getStockId())
			{
				p = productList.get(i);
			}
		
		}
		
		return p;
	
	}
	
	/**
	 * Write the entire inventory to a file (when passed a PrintWriter object)
	 * @param Printwriter
	**/
	
	
	public void writeToFile(outFile Printwriter)  
	{ 
		//open file 
		
		//for loop - write each line to file 
		for (int i = 0; i < productList.size(); i++) 
		{
			String n = productList.get(i).getName(); 
			String desc = productList.get(i).getDescription(); 
			int stock = productList.get(i).getNumInStock(); 
			double val = productList.get(i).getValueAtPurchase(); 
			//write line to file 
		}
		
		//close file 

	}
	
	
	/**
	 * returns the monetary value of the entire inventory of products
	 * @return totalVal
	**/
	public double findInventoryValue() 
	{
		double totalVal = 0.0; 
		
		for (int i = 0; i <productList.size(); i++) 
		{
			double iStock = productList.get(i).getNumInStock(); 
			double iVal = productList.get(i).getValueAtPurchase(); 
			
			totalVal += (iStock*iVal); 
			
		}
		
		return totalVal; 
	
	}
	
	/**
	 * Add quantities to a specific product ID in the inventory
	 * @param id
	 * @param num
	 **/
	public void addToStock(long id, int num)
	{
		Product p = findbyID(id); 
		
		if (p != null) 
		{
			int curStock = p.getNumInStock(); 
			
			if (curStock != 0) //if not discontinued 
			{
				p.setNumInStock(curStock + num);
			}
		
		}
	
	}
	
	/**
	 * Removes quantities of a product with the given ID from the inventory
	 * @param id
	 * @param num
	**/
	public void removeFromStock(long id, int num)
	{
		Product p = findbyID(id); 
		
		if (p != null) 
		{
			int curStock = p.getNumInStock(); 
			
			if (curStock > num) //if not discontinued 
			{
				p.setNumInStock(curStock - num);
			}
		
		}
	
	}
	
	/**
	 * @param p
	 * @return true if the item is a duplicate of one already in the Inventory
	**/
	public boolean isDuplicate(Product p) 
	{
		boolean duplicate = false; 
		
		if (productList.indexOf(p) >= 0) 
		{
			duplicate = true; 
		}
	
		return duplicate;
	}
	
	
	/**
	 * Display inventory in a visually appealing, easy to read way
	 *
	 */
	public String toString()
	{
		String s = ""; 
		
		for (int i = 0; i < productList.size(); i++)
		{
			s = s+ productList.get(i).toString() + "\n";

		}
	
		return s; 

	}
}
