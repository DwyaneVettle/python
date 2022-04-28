package com.pxw.spring.orders;

public class Orders {
    private String oname;
    private String oaddr;

    public Orders(String oname, String oaddr) {
        this.oname = oname;
        this.oaddr = oaddr;
    }
    public void testOrd(){
        System.out.println(oaddr+":"+oname);
    }
}
