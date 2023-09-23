package com.example.sample.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloWebController {

    @GetMapping("/say-hello")
    public String index() {
        return "Greetings everyone, hello from Sweta";
    }
}
