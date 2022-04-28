package com.pxw.spring.service;

import com.pxw.spring.dao.UserDao;

public class UserService {
    private UserDao userDao;

    public void setUserDao(UserDao userDao) {
        this.userDao = userDao;
    }

    public void add(){
        System.out.println("使用了add方法");
        userDao.update();
    }
}
