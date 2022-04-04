import java.io.FileNotFoundException;

/**
 * @author Kesar Sampat
 * APCSA PD 6 
 * Student DataBase Driver to run the program 
 *
 */
public class StudentDBDriver 
{

	public static void main(String[] args) throws FileNotFoundException 
	{
		String sf = "students.txt" ;
		String ef = "expressions.txt";
		
		StudentDataBase stDB = new StudentDataBase(sf, ef); //instantiates a studentdatabase
		
		stDB.display(); //show all students 


	}

}