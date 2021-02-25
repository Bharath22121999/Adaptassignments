package a3assignments;

import java.util.ArrayList;
import java.util.List;
import java.util.ListIterator;

public class Assignment3Q3 {
	
	public static <T>List<T> traverseReverse(ArrayList<T> aList){
		
		List<T> rList = new ArrayList<>();
		ListIterator<T> iterator = aList.listIterator(aList.size());
		while(iterator.hasPrevious()) {
			rList.add(iterator.previous());
		}
		return rList;
	}	
	
	public static void main(String[] args) {
		ArrayList<String> list = new ArrayList<>();
		list.add("Hi");
		list.add("Hello");
		list.add("This");
		list.add("is");
		list.add("Vunnam");
		/*ListIterator<String> iterator = list.listIterator(list.size());
		while(iterator.hasPrevious()) {
			System.out.println(iterator.previous());
		}*/
		List<?> alist = traverseReverse(list);
		alist.stream().forEach(i->System.out.println(i));
	}
}
