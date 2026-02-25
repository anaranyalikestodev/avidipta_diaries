from flask import Blueprint,render_template,request,redirect,url_for,flash
from models.notice import db,Notice

notice_bp=Blueprint("notice_bp",__name__, template_folder="templates")

#Read Route
@notice_bp.route("/")
def index():
    notices=Notice.query.order_by(Notice.issued_at.desc()).all()
    return render_template("index.html",notices=notices)

#Create Route
@notice_bp.route("/create",methods=["GET","POST"])
def create_notice():
    if request.method=="POST":
        title=request.form["title"].strip()
        content=request.form["content"].strip()
        if not title or content:
            flash("Fields cannot be empty")
            return redirect(request.referrer)
      
        new_notice=Notice(title=title,content=content)
        db.session.add(new_notice)
        db.session.commit()
        return redirect(url_for("notices_bp.index",notice=None))

    return redirect(url_for("cu.html",notice=None))

#Edit Route
def edit_notices(id):
    notice=Notice.query.get(id)
    return render_template("edit.html",notice=notice)

#Update Route
@notice_bp.route("/update/<int:id>", methods=["POST"])
def update_notice(id):
    notice=Notice.query.get(id)
    notice.title=request.form["title"]
    notice.content=request.form["content"]
    db.session.commit()
    return redirect(url_for("notices_bp.index"))

#Delete Route
@notice_bp.route("/update/<int:id>",methods=["POST"])
def edit(id):
    notice=Notice.query.get_or_404(id)
    return render_template("CU.html")
@notice_bp.route("/delete/<int:id>")
def delete_notice(id):
    notice=Notice.query.get_or_404(id)
    db.session.delete(notice)
    db.session.commit()

    return redirect(url_for("index"))
