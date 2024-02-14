package com.ezai.EZAI.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Getter;
import lombok.Setter;

@Setter
@Getter
@Entity(name = "User")
@Table(name = "users")
public class User {
    @Id
    private String email;
    private String firstName;
    private String lastName;
    private String info;

    public User() {
    }

    public User(String email, String firstName, String lastName, String info) {
        this.email = email;
        this.firstName = firstName;
        this.lastName = lastName;
        this.info = info;
    }

}
