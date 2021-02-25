class SiCi {

    public double simpleInterest(double principalAmount,int time,double interestRate){
    	return principalAmount*time*interestRate/100;
    }
    public double compoundInterest(double principalAmount,int time,double interestRate){
    	
    	/*
    	 * a = p(1+r)^t
    	 * i = a-p*/
    	double amount = principalAmount*Math.pow(1+interestRate/100, time);
    	double intr = amount - principalAmount;
    	return intr;
    }
}
public class Assignment1Q3 {
    public static void main (String args[]) {
    	
    }
}