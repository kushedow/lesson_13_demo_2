from json import JSONDecodeError

from flask import Flask, jsonify, abort

from project.dao.candidates_dao import CandidatesDAO

from project.bp.error_handler import error_handler

app = Flask(__name__)

app.register_blueprint(error_handler)

app.config["DATA_SOURCE"] = "project/data/candidates.json"


@app.route('/')
def candidate_all_view():
    candidates_dao = CandidatesDAO(app.config["DATA_SOURCE"])
    cans = candidates_dao.get_all()
    return jsonify(cans)

@app.route('/can/<int:pk>/')
def candidate_single_view(pk):
    candidates_dao = CandidatesDAO(app.config["DATA_SOURCE"])
    can = candidates_dao.get_by_pk(pk)
    if can is None:
        return abort(418)
    return jsonify(can)


@app.delete("/can/<int:pk>/")
def candidate_single_delete(pk):
    candidates_dao = CandidatesDAO(app.config["DATA_SOURCE"])
    result = candidates_dao.delete_by_pk(pk)
    if result:
        return jsonify({"status": "deleted"}), 204
    else:
        return jsonify({"status": "failed"}), 404

