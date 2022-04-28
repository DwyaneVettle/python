package com.pxw.spring.people;

public class Person {
    private Man man;

    public void setMan(Man man) {
        this.man = man;
    }
    public void man(){
        man.test();
    }

    @Override
    public String toString() {
        return "Person{" +
                "man=" + man +
                '}';
    }
}
