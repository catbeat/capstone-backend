<!--
 * @Author: liziwei01
 * @Date: 2023-12-15 12:11:31
 * @LastEditors: liziwei01
 * @LastEditTime: 2023-12-15 12:23:06
 * @Description: file content
-->
# capstone-backend

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

## Description

Python Back-end application using Django for capstone project of Qian Wang, Ziwei Li, Zeyin Zhang in Johns Hopkins University

## Back-End Installation

First, create a database called capstone in MySQL
Second, create an environment of 3.8.18 and install dependencies
Third, create tables using

```bash
python3 ./manage.py migrate
```

## Front-End Installation

Refer to <https://github.com/liziwei01/capstone>

## Usage

if you need a http server

```bash
python3 manage.py runserver 0.0.0.0:8000
```

if you need a https server

```bash
python3 manage.py runsslserver --certificate in.crt --key in.key 0.0.0.0:8000
```

replace in.crt and 8000 to your crt file and your port
