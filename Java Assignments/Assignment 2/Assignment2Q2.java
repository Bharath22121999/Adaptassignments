package a2assignments;


/*
 * Write a program that describes the hierarchy of an organization. Here we need to write 3 classes 
 * Employee, Manager & Labour where Manager & Labour are the sub classes of the Employee. 
 * Manager has incentive & Labour has over time. Add the functionality 
 * to calculate total salary of all the employees. Use polymorphism i.e. method overriding.      
Description:-
 * Write a program to claculate the total salaries given to all the employees by an organization. 
 * In this organization there are employees category under which Manager and Labour are working 
 * where manager will recieve incentive and labourer will receive overtime benifits.*/

import java.util.ArrayList;

class Manager extends Assignment2Q2 {
	private int incentive = 5000;
    @Override
    public int getSalary(int salary) {
        //int incentive = 5000;
    	int mSalary = salary + incentive;
        
        return mSalary;
    }
}

class Labour extends Assignment2Q2 {
	private int overtime = 500;
    @Override
    public int getSalary(int salary) {
        //int overtime = 500;
        int lSalary = salary + overtime;
        return lSalary;
    }
}

public class Assignment2Q2 {
    int salary = 10000;
    public int getSalary(int salary){
    	this.salary = salary;
    	return salary;
    }
    public int totalEmployeesSalary(ArrayList<Integer> employeeSalaries){
    	int totalEmployeeSal = 0;
    	for(Integer i : employeeSalaries) {
    		totalEmployeeSal += i;
    	}
    	return totalEmployeeSal;
    }
    public static void main(String[] args) {
    	
    }
}