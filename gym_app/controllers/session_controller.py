from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.session import Session

member_blueprint = Blueprint("sessions", __name__)