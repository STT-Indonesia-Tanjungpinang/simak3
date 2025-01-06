from flask import Flask, render_template

def frontend_index():
  return render_template("fronted/frontend_index.html")