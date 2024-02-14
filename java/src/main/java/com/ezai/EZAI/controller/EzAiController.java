package com.ezai.EZAI.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
public class EzAiController {
    @Autowired
    RestTemplate restTemplate;

    @RequestMapping("/test")
    public String testMethod() {
        return "Pass";
    }
}
