from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

feedback_list = []


@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        course = request.form.get("course")
        feedback = request.form.get("feedback")

        if name and email and course and feedback:
            feedback_data = {
                "name": name,
                "email": email,
                "course": course,
                "feedback": feedback,
                "submitted_at": datetime.now().strftime("%d-%m-%Y %I:%M %p")
            }

            feedback_list.append(feedback_data)
            message = "Feedback submitted successfully!"
        else:
            message = "Please fill all fields."

    return render_template(
        "index.html",
        feedback_list=feedback_list,
        message=message
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "application": "Student Feedback App",
        "version": "1.0.0"
    }), 200


@app.route("/api/feedback")
def get_feedback():
    return jsonify(feedback_list), 200


if __name__ == "__main__":
    app.run(host="192.168.1.23", port=5000)
