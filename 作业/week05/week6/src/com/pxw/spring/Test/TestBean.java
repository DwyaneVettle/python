package com.pxw.spring.Test;

import com.pxw.spring.px.Emp;
import com.pxw.spring.orders.Book;
import com.pxw.spring.orders.Orders;
import com.pxw.spring.people.Person;
import com.pxw.spring.service.UserService;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;


public class TestBean {
    //构造方法
    @Test
    public void test(){
        ApplicationContext context = new ClassPathXmlApplicationContext("com/pxw/spring/resources/spring-01.xml");
        Orders orders = context.getBean("orders", Orders.class);
        orders.testOrd();
    }
    //p命名
    @Test
    public void test2(){
        ApplicationContext context = new ClassPathXmlApplicationContext("com/pxw/spring/resources/spring-01.xml");
        Book book = context.getBean("Book", Book.class);
        book.test();
    }
    //外部bean
    @Test
    public void test03(){
        ApplicationContext context = new ClassPathXmlApplicationContext("com/pxw/spring/resources/spring-01.xml");
        UserService userService = context.getBean("userService", UserService.class);
        userService.add();
    }
    //内部bean
    @Test
    public void test04(){
        ApplicationContext context = new ClassPathXmlApplicationContext("com/pxw/spring/resources/spring-01.xml");
        Person person = context.getBean("person", Person.class);
        person.man();
    }
    
    @Test
    public void test05(){
        ApplicationContext context = new ClassPathXmlApplicationContext("com/pxw/spring/resources/spring-02.xml");
        Emp emp = context.getBean("emp", Emp.class);
        emp.add();
    }

}
