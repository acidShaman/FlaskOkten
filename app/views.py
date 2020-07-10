from app import app
from flask import render_template, redirect, url_for
from app import db


@app.route('/')
def main():
    return redirect(url_for('owners.show_owners'))
