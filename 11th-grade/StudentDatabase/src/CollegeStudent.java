/**
 * @author Kesar Sampat 
 * PD 6. APCSA 
 *
 */
public class CollegeStudent extends Student 
{
	private String dormitory;
	private String college;
	private String roomNumber;
	private String status;

	public CollegeStudent(String[] str) 
	{
		super(str);
		roomNumber = str[2];
		dormitory = str[3];
		college = str[4];
		status = str[5];
	}

	@Override
	public void setUserName(String uName) 
	{
		if (uName.length() == 6)
		{
			if (uName.substring(0,2) == "FR" || uName.substring(0,2) == "SO" || uName.substring(0,2) == "JU" || uName.substring(0,2) == "SE")
				userName = uName;
			
			else 
			{
				userName = null;
			}
			
		}
	}
	
	public String toString()
	{
		return super.toString() + "\nAddress: " + roomNumber + " " + dormitory + "\n" 
			+ college + "\nStatus: " + status + "\nUser Name: " + userName + "\n"; 
		
	}
	
	/**
	 * Sets status to freshman, sophomore, junior, or senior 
	 * @param str
	 */
	private void setStatus(String str)
	{
		if (str.substring(0,2) == "FR")
		{
			status = "freshman";
			
		}
		else if (str.substring(0,2) == "SO")
		{
			status = "sophomore";
			
		}
		else if (str.substring(0,2) == "JU")
		{
			status = "junior";
			
		}
		else if (str.substring(0,2) == "SE")
		{
			status = "senior";
			
		}
	
	}

}
