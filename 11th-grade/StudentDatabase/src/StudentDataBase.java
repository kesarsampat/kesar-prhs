import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

public class StudentDataBase 
{
	private ArrayList<Student> StudentRecords = new ArrayList<Student>();
	private Stack<Double> stack;
	
	//Initialize the studentFile and expressions.txt based on user input of the file names.
	 //Open the studentFile. For each line of input in the studentFile, create and
	 //initialize a new HighSchoolStudent or CollegeStudent (think of a creative way to know which to construct).
	 // Store this student into the ArrayList StudentRecords.
	 //
	 //Open the expressionFile. For each line of input in the expression file, grab the
	 //social security number, RPN (reverse polish notation) expression, and credits
	 //earned. Locate the student in StudentRecords with this SSN, update the creditsEarned
	 //and GPA fields.

	public StudentDataBase(String sf, String ef) throws FileNotFoundException
	{
		Scanner inFile = new Scanner(new File(sf));
				
		while(inFile.hasNextLine()) 
		{
			String [] lines = inFile.nextLine().split(",");
	
			//initializing a student object based off of ID field (college or hs)
			if (lines[5].substring(0,2).equals("FR") || lines[5].substring(0,2).equals("SO") || lines[5].substring(0,2).equals("JU") || lines[5].substring(0,2).equals("SE"))
			{
				
				CollegeStudent student = new CollegeStudent(lines); 
				
				StudentRecords.add(student); 


			}
			
			else 
			{
				HighSchoolStudent student = new HighSchoolStudent(lines); 
				//System.out.println(student); 
				StudentRecords.add(student); 

			}
		
		}
		
		
		//opening the expression file to calculate 
		
		
		Scanner file = new Scanner(new File(ef));
		
		
		while (file.hasNextLine())
		{
			String [] lines = file.nextLine().split(",");
		
			
			String ssn = lines[0].replace("-", "");
			String gpaRPN = lines[1];
			String creds = lines[2];
			
			
			int index = find(ssn);
			
						
			if (index >= 0) //legit index 
			{
				Student student = StudentRecords.get(index); //get student from student records using index  
				
				double gpa = evaluate(gpaRPN); //gpa calc
				int c = Integer.parseInt(creds); //parsing to int
				student.setCreditsEarned(c); //setting credits 
				student.setGPA(gpa); //setting gpa 
				
			}

		}
		
		inFile.close(); 
		file.close(); 
		
	
	}
	
	 

	 /**
	  * locates the student in the ArrayList StudentRecords and returns the index of where it is located. If it isn’t found, return -1.
	 * @param ssn
	 */
	public int find(String ssn)
	 {

		int index = -1; 
		
		for (Student s: StudentRecords)
		{
			if (ssn.equals(s.getSSN()))
			{
				
				index = StudentRecords.indexOf(s);
				break;
			}
				
			 
		}
		
		return index;  
		
		
	 }
	 
	 /**
	 * @param exp
	 * @return
	 */
	public double evaluate(String exp)
	{
		
		return 3.3;
			
			
	 //You will need a StringTokenizer to extract the operands and operators. Note that
	 //operands are separated from one another by either a blank space or an operator.
	 //If a token is an operand, push it as a Double onto the stack.
	 //If a token is an operator, pop off the (second operand), pop off the (first
	 //operand), compute (first operand) operator (second operand), push this value onto
	 //the stack. Continue until you run out of tokens, the final result is at the top of
	 //the stack. Example: 110. 5.+2.*103./ evaluates to approximately 2.23.
	 }
	 
	 /**
	 * Sort the students, display them one at a time at the console
	 */
	public void display ()
	 {
		
		for (Student s: StudentRecords) 
		{
			System.out.println(s.toString()); 
			
		}
	
	 }
	
		
	

}
