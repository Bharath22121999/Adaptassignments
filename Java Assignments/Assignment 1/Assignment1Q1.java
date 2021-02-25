import java.util.Scanner;

class ArmstrongOrNot {
    public boolean armstrongCheck(int num) {
    	int sum=0,backup = num;
    	while(num>0) {
    		int temp = num%10;
    		sum+=temp*temp*temp;
    		num = num/10;
    	};
    	if(sum == backup) {
    		return true;
    	}
		return false;
	}
}
public class Assignment1Q1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		int num = scan.nextInt();
		ArmstrongOrNot check = new ArmstrongOrNot();
		boolean res = check.armstrongCheck(num);
		System.out.println(res);
		scan.close();
	}

}
