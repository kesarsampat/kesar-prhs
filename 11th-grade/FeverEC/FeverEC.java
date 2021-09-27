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
					String vomit = ask("Do you have vomit or diahreea?");

					if (vomit.equals("YES"))
						showPossibleDiagnosis("Possibilites include digestive tract infection.");
					else {
						handleJoints();
					}

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
		String shortOfBreath = ask("Are you short of breath or wheezing or coughing up phlegm?");

		if (shortOfBreath.equals("YES"))
			showPossibleDiagnosis("Possibilites include pneumonia or infections of airways");

		else {
			String hc = ask("Do you have a headahce?");

			if (hc.equals("YES"))
				showPossibleDiagnosis("Possibilites include viral infection");

			else {
				String bj = ask("Do you have aching bones or aching joints?");

				if (bj.equals("YES"))
					handleJoints();
				else {
					String rash = ask("Do you have a rash?");

					if (rash.equals("YES"))
						showPossibleDiagnosis("Insufficeint information to list possiblites");
					else {
						String st = ask("Do you have a sore throat?");

						if (st.equals("YES"))
							showPossibleDiagnosis("Possibilites include throat infection.");
						else {
							String backAndChills = ask("Do you have back pain just above the waist and chills and fever?");

							if (backAndChills.equals("YES"))
								showPossibleDiagnosis("Possibilites include kidney infection.");
							else {
								String urinating = ask("Do you have pain urinating or are you urinating more often?");

								if (urinating.equals("YES"))
									showPossibleDiagnosis("Possibilites include urinary tract infection.");
								else {
									String sun = ask("Have you spent the day in the sun or hot conditions?");
									if (sun.equals("YES"))
										showPossibleDiagnosis("Possibilites include sunstroke or heat exhaustion.");
									else {
										showPossibleDiagnosis("Insufficeint information to list possiblites");

									}
								}

							}
						}

					}

				}

			}

		}
	}

	public static void handleHeadache()
	{
		String pains = ask("Are you experiecning any of the following: pain when you are bending your head forward, nausea or vomiting, bright light hurting your eyes, drowsiness, or confusion?");

		if (pains.equals("YES"))
			showPossibleDiagnosis("Possibilites include meningitis.");
		//no else statement

	}

	public static void handleJoints()
	{
		showPossibleDiagnosis("Possibilities include viral infection.");

	}
}
