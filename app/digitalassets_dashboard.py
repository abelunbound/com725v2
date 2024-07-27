# app/digitalassets_dashboard.py
from flask import Flask, request, jsonify
from dash import Dash, html
import dash

# Create a Dash app
dash_app = Dash(__name__)

dash_app.layout = html.Div([
    html.H1("Hello Dash"),
    html.Div("Welcome to Dash on Vercel!")
])

# Create a Flask server
server = Flask(__name__)

@server.route("/")
def index():
    return dash_app.index()

@server.route("/_dash-component-suites/dash")
def dash_component_suites():
    return dash_app.server.send_static_file("dash_component_suites")

@server.route("/_dash-layout")
def dash_layout():
    return dash_app.index()

@server.route("/_dash-dependencies")
def dash_dependencies():
    return dash_app.index()

if __name__ == "__main__":
    server.run(debug=True, host="0.0.0.0", port=8000)
