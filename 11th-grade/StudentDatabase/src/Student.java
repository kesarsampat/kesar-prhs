/**
 * @author Kesar Sampat
 * APCSA PD. 6
 * Student Database Project
 *
 */
public abstract class Student 
{
	private String firstName;
	private String lastName;
	private String ssn;
	protected String userName;
	private double gpa;
	private int creditsEarned;

	/**
	 * Extracts firstName, lastName, SSN from str 
	 * @param str
	 */
	public Student(String [] str)
	{
		firstName = str[0].split(" ")[0]; 
		lastName = str[0].split(" ")[1];
		ssn = str[1];
		
	}
	
	public String getLastName() 
	{
		return lastName;
	}

	public void setLastName(String lastName) 
	{
		this.lastName = lastName;
	}

	public String getUserName() 
	{
		return userName;
	}


	/**
	 * @return hyphenated SSN to the caller 
	 */
	public String getSSN()
	{
		return ssn;
		
	}
	
	/**
	 * Sets the total credits earned by a student
	 */
	public void setCreditsEarned(int credits)
	{
		
		creditsEarned = credits;
	}
	
	/**
	 * Sets the grade point average of a student
	 */
	public void setGPA(double gpa)
	{
		this.gpa = gpa;
		
	}
	
	/**
	Return -1 if the receiver’s last name is smaller than (lexicographically) other’s last name or
	the receiver’s last name is equal to other’s last name and the receiver’s first name
	is smaller than other’s first name.
	Return 0 if the receiver’s last name is equal to other’s last name and the receiver’s
	first name is equal to other’s first name.
	Return 1 the receiver’s last name is greater than other’s last name or
	the receiver’s last name is equal to other’s last name and the receiver’s first name
	is greater than other’s first name.
	**/
	public int compareTo(Object other)
	{
		int num = 0;
		if (lastName.length() <  ((Student) other).lastName.length() || lastName.length() == ((Student) other).lastName.length() && firstName.length() < ((Student) other).firstName.length())
		{
			num = -1;
		}
		
		else if (lastName.length() == ((Student) other).lastName.length() && firstName.length() == ((Student) other).firstName.length())
		{
			num = 0;
		}
		else if (lastName.length() >  ((Student) other).lastName.length() || lastName.length() == ((Student) other).lastName.length() && firstName.length() > ((Student) other).firstName.length() )
		{
			num = 1; 
		}
		
		return num; 
		
		
	}
	
	/**
	 * Returns a student’s information as shown below as a string.
		Name: Kent, Clark (last name first)
		SSN: 190-40-9211 (don’t forget to hyphenate)
		Credits Earned: 75
		GPA: 3.0
	 */
	public String toString()
	{
		String s = "";
		
		s+="Name: " + lastName + "," + firstName;
		s+="\nSSN: " + ssn;
		s+="\nCredits Earned: " + creditsEarned;
		s+="\nGPA: " + gpa;
		
		return s;
	
	}
	
	public abstract void setUserName(String uName);


}
