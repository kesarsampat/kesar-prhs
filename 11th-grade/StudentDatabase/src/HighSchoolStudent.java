
public class HighSchoolStudent extends Student 
{
	private String streetAddress;
	private String city;
	private String state;
	private String zip;

	public HighSchoolStudent(String[] str)
	{
		super(str);
		streetAddress = str[2];
		city = str[3];
		state = str[4];
		zip = str[5];
		
				
	}
	
	public String toString()
	{
		return super.toString() + "\nAddress: \n" + streetAddress + "\n" + city + "," + state + "\n" + zip + "\nUser Name: " + userName + "\n"; 
		
	}
	
	@Override
	public void setUserName(String uName) 
	{
		
		if (userName.length() == 6)
		{
			if (Integer.parseInt(uName) != -1)
			userName = uName;
			
		}
		
		else
		{
			userName = null;
		}
	}

}
