from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.session import Session
import repositories.session_repository as session_repository
import repositories.member_repository as member_repository

sessions_blueprint = Blueprint("sessions", __name__)

@sessions_blueprint.route("/sessions")
def sessions():
    sessions = session_repository.select_all()
    return render_template("/sessions/index.html", sessions=sessions)

@sessions_blueprint.route("/sessions/<id>")
def show(id):
    session = session_repository.select(id)
    members = session_repository.members(session)
    return render_template("/sessions/show.html", session=session, members=members)

@sessions_blueprint.route("/sessions/new")
def new_session():
    return render_template("sessions/new.html")

@sessions_blueprint.route("/sessions", methods=["POST"])
def add_session():
    name = request.form["name"]
    date = request.form["date"]
    time = request.form["time"]
    duration = request.form["duration"]
    capacity = request.form["capacity"]
    session = Session(name, date, time, duration, capacity, id)
    session_repository.save(session)
    return redirect("/sessions")

@sessions_blueprint.route("/sessions/<id>/edit")
def edit_session(id):
    session = session_repository.select(id)
    return render_template("/sessions/edit.html", session=session)

@sessions_blueprint.route("/sessions/<id>", methods=["POST"])
def update_session(id):
    name = request.form["name"]
    date = request.form["date"]
    time = request.form["time"]
    duration = request.form["duration"]
    capacity = request.form["capacity"]
    session = Session(name, date, time, duration, capacity, id)
    session_repository.update(session)
    return redirect("/sessions")

@sessions_blueprint.route("/sessions/<id>/delete", methods=["POST"])
def delete(id):
    session_repository.delete(id)
    return redirect("/sessions")
