package com.pxw.spring.people;

public class Man {
    private String name;
    private int age;
    private Man man;


    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public Man() {
    }

    public Man getMan() {
        return man;
    }

    public void setMan(Man man) {
        this.man = man;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    
    public void test() {
        System.out.println("姓名：" + name + "\n年龄：" + age);
    }



}
