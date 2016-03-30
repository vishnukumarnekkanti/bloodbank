#!/bin/bash
docker stop bloodbank
docker rm blooodbank
docker run -d --name=bloodbank -p 3306:3306 vishnukumarnekkanti/bloodbank:base

