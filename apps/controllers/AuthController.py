from flask import Flask, render_template

def auth_login():
  return render_template("auth/auth_login.html")