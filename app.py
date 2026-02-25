from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

#DB Config
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

@app.route("/")
def index():
    notices=Notice.query.order_by(Notice.issued_at.desc()).all()
    return render_template("index.html",notices=notices)

@app.route("/create",methods=["POST"])
def create_notice():
    title=request.form["title"]
    content=request.form["content"]

    new_notice=Notice(title=title,content=content)
    db.session.add(new_notice)
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/delete/<int:id>")
def delete_notice(id):
    notice=Notice.query.get_or_404(id)
    db.session.delete(notice)
    db.session.commit()

    return redirect(url_for("index"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)