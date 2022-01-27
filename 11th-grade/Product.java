import java.text.DecimalFormat;

/**
 * @author Kesar Sampat
 * PD 6 APCSA 
 * Business Inventory - keeps track of the inventory for a store of your choice
 */
public class Product {
	
	private static long nextStockID = 1000;
	private long stockId;
	private String name;
	private String description; 
	private int numInStock;
	private double valueAtPurchase; 
	
	//constructor
	public Product(String n, String d, int num, double v) 
	
	{
		stockId = nextStockID; 
		nextStockID++; 
		name = n;
		description = d; 
		numInStock = num;
		valueAtPurchase = v;
			
	}

	public long getStockId()
	{
		return stockId;
	}

	public String getName() 
	{
		return name;
	}
	
	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public int getNumInStock()
	{
		return numInStock;
	}
	

	public double getValueAtPurchase() 
	{
		return valueAtPurchase;
	}
	

	public void setName(String name) 
	{
		this.name = name;
	}
	

	public void setNumInStock(int numInStock)
	{
		this.numInStock = numInStock;
	}
	
	/**
	 * Two products are equal when the product name and description are the same 
	 *
	 */
	public boolean equals(Object obj)
	{
		if ((name.equals(((Product) obj).getName()) && (description.equals(((Product) obj).getDescription())))) // same name and description
		{
			return true; 
		}
		
		return false;
			
	}
	
	
	public String toString() 
	{
		
		String s;
		s = "Name: " + getName() + "\n" + "Desc: " + getDescription() + "\n" +  "Num in Stock: " + getNumInStock() + "\n" + "Cost: " + getValueAtPurchase() + "\n" +  "ID Number: " + getStockId() + "\n"; 

		return s;
		
	}

}
