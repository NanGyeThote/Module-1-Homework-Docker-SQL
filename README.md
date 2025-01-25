# Module-1-Homework-Docker-SQL
Contains codes for solving the Module 1 Homework: Docker &amp; SQL

# Question 1. Understanding docker first run

### This is Docker File !
```bash
FROM python:3.12.8

RUN pip install pandas

ENTRYPOINT [ "bash" ]
```

### ------- Docker Command To test the PIP Version ----------------

- I run 
```bash
docker build -t test1:pandas .
```
- Then I run
```bash
docker run -it test:pandas
```
- I tried pip --version then I got the value of **24.3.1** in python **3.12.8**

------------------------------------------------------------------------------------------------------
