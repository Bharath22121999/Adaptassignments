package com.vunnam.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import com.vunnam.dao.EmpDao;
import com.vunnam.model.Employee;
import com.vunnam.service.PdfService;

@Controller
public class PdfController {
	@Autowired    
    EmpDao dao; 
	
	@RequestMapping("/pdf")
	public ModelAndView getPdf() {
		List<Employee> empList = (List<Employee>) dao.getAllEmployees();
		
		return new ModelAndView(new PdfService(), "empList", empList);
	}
}
