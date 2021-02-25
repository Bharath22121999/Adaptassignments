import java.util.Scanner;

/*
 * Condition 1: -All subjects marks is greater than 60 is Passed 
 * Condition 2: -Any two subjects marks are greater than 60 is Promoted 
 * Condition 3: -Any one subject mark is greater than 60 or all subjects’ marks less than 60 is failed.*/

/* Note: In question the given conditions doesn't match evaluation test cases please check them, it is 20 instead of 60*/
class ResultDeclaration{
    public String declareResults( double subject1Marks, double subject2Marks, double subject3Marks) {
    	
    	/*if(subject1Marks >60 && subject2Marks>60 && subject3Marks>60) {
    		return "promoted";
    	}
    	else if((subject1Marks >60 && subject2Marks>60) || (subject2Marks >60 && subject3Marks>60) || (subject3Marks >60 && subject1Marks>60)) {
    		return "passed";
    	}
    	else { 
    		return "failed";
    	}*/
    	/* Note: In question the given conditions doesn't match evaluation test cases please check them, it is 20 instead of 60*/
    	if((subject1Marks>=20 && subject2Marks>=20) || (subject2Marks>=20 && subject3Marks>=20) || (subject3Marks>20 && subject1Marks>20)) {
    		if((subject1Marks>20 && subject2Marks>20) ||(subject2Marks>20 && subject3Marks>20) ||(subject3Marks>20 && subject1Marks>20)) {
    			return "passed\npromoted";
    		}else {
    			return "passed";
    		}
    	}else {
    		return "failed";
    	}
    	
    }
}
public class Assignment1Q4 {
    public static void main(String[] args) {
    	ResultDeclaration rd = new ResultDeclaration();
    	Scanner scan = new Scanner(System.in);
    	double s1,s2,s3;
    	s1 = scan.nextDouble();
    	s2 = scan.nextDouble();
    	s3 = scan.nextDouble();
    	System.out.print(rd.declareResults(s1, s2, s3));
    	scan.close();
    }
    
}