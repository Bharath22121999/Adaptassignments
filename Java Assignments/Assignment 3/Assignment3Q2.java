package a3assignments;

import java.util.HashSet;
import java.util.LinkedHashSet;

public class Assignment3Q2 {
    public static void main(String[] args) {
    	
    	//LinkedHashSet
    	System.out.println("LinkedHashSet------------\n");
    	LinkedHashSet<String> lh = new LinkedHashSet<String>();
    	lh.add("A");
    	lh.add("B");
    	LinkedHashSet<String> lhs = ordered(lh);
    	lhs.stream().forEach(i->System.out.println(i));
    	
    	///HashSet
    	System.out.println("\nHashSet------------------\n");
    	HashSet<String> hs = new HashSet<String>();
    	hs.add("Akil");
    	hs.add("Sachin");
    	HashSet<String> hs2 = unordered(hs);
    	hs2.stream().forEach(i->System.out.println(i));
    	
    }
    public static LinkedHashSet<String> ordered(LinkedHashSet<String> linkedHashSet){
    	linkedHashSet.add("C");
    	linkedHashSet.add("D");
		return linkedHashSet; 
    }
    public static HashSet<String> unordered(HashSet<String> hashSet){
    	hashSet.add("Munna Bhai");
    	hashSet.add("Gaithonde");
		return hashSet;
    }
}