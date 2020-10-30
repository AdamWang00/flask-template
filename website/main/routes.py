from flask import flash, render_template, redirect, url_for, request, Blueprint
from website.main.forms import ContactForm
from website.main.utils import send_contact_email
from website.models import Post


main = Blueprint('main', __name__)


@main.route("/", methods=['GET'])
def home():
    return render_template('home.html', title='Home')


@main.route("/posts", methods=['GET'])
def posts():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=10)
    return render_template('posts.html', title='Posts', posts=posts)


@main.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        send_contact_email(form.name.data, form.email.data, form.message.data)
        flash('Your message has been sent. We will get back to you soon!', 'success')
        return redirect(url_for('main.contact'))
    return render_template('contact.html', title='Contact', form=form)
