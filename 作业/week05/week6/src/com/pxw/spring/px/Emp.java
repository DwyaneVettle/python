package com.pxw.spring.px;

public class Emp {
    private String EName;
    private String gender;
    //员工属于某一个部门，使用对象形式表示
    private Dept dept;

    public void setDept(Dept dept) {
        this.dept = dept;
    }

    public Dept getDept() {
        return dept;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public void setEName(String EName) {
        this.EName = EName;
    }
    public void add(){
        System.out.println(EName+":"+gender+":"+dept);
    }

}
