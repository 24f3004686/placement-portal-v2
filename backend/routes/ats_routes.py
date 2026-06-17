from flask import Blueprint, request, jsonify

ats_bp = Blueprint("ats", __name__)

@ats_bp.route("/analyze", methods=["POST"])
def analyze_resume():

    data = request.get_json()

    resume = data.get("resume", "").lower()

    skills = data.get("skills", "").lower().split(",")

    matched = []

    missing = []

    for skill in skills:

        skill = skill.strip()

        if skill in resume:

            matched.append(skill)

        else:

            missing.append(skill)

    total = len(skills)

    score = 0 if total == 0 else round(len(matched) / total * 100)

    return jsonify({

        "score": score,

        "matched": matched,

        "missing": missing

    })
