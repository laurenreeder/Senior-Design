from flask import Blueprint, redirect, url_for

from route_funcs import datasets

def register_routes(app):

    @app.route("/")
    def index():
        return redirect(url_for('datasets_new'))

    app.add_url_rule('/datasets/new', 'datasets_new', datasets.new, methods=['GET', 'POST'])
    app.add_url_rule('/datasets/<dataset_name>', 'datasets_view', datasets.view, methods=['GET'])
    app.add_url_rule('/datasets/run_learning', 'datasets_run', datasets.run_learning, methods=['POST'])
    app.add_url_rule('/datasets/check_learning', 'datasets_check', datasets.get_learning_result, methods=['GET'])


