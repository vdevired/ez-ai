package com.ezai.EZAI.controller;

import com.ezai.EZAI.entity.User;
import com.ezai.EZAI.repository.UserRepo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import static org.springframework.web.bind.annotation.RequestMethod.GET;
import static org.springframework.web.bind.annotation.RequestMethod.POST;

@RestController
@RequestMapping("/user")
public class UserController {
    @Autowired
    RestTemplate restTemplate;

    private final UserRepo userRepo;

    public UserController(UserRepo userRepo) {
        this.userRepo = userRepo;
    }

    @RequestMapping(method = {GET}, path = "/retrieveAll")
    public ResponseEntity getAllUsers(){
        return ResponseEntity.ok(this.userRepo.findAll());
    }

    @RequestMapping(method = {GET}, path = "/retrieve")
    public ResponseEntity getByEmail(@RequestParam String email){
        return ResponseEntity.ok(this.userRepo.findByEmail(email));
    }

    @RequestMapping(method = {POST}, path = "/add", produces = MediaType.APPLICATION_JSON_VALUE)
    public void addUser(@RequestBody User user){
        userRepo.save(user);
    }
}
