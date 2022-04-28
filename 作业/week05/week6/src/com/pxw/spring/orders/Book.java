package com.pxw.spring.orders;

public class Book {
    private String cname;
    private String caddr;

    public String getCname() {
        return cname;
    }

    public void setCname(String cname) {
        this.cname = cname;
    }

    public String getCaddr() {
        return caddr;
    }

    public void setCaddr(String caddr) {
        this.caddr = caddr;
    }

    public void test(){
        System.out.println(caddr+":"+cname);
    }
}
