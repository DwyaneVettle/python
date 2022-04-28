package com.pxw.spring.dao;

public class UserDaoImpl implements UserDao{
    @Override
    public void update() {
        System.out.println("外部bean注入完成");
    }
}
