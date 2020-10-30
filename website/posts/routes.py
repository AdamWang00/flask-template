import os
from flask import (render_template, url_for, flash, current_app,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from website import db
from website.models import Post
from website.posts.forms import PostForm
from website.posts.utils import save_picture


posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        if form.picture.data:
            post = Post(title=form.title.data, content=form.content.data, image_file=save_picture(form.picture.data), author=current_user)
        else:
            post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created', 'success')
        return redirect(url_for('main.posts'))
    return render_template('create_post.html', title='New Post', form=form, legend="New Post")


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        if form.picture.data:
            if post.image_file != 'default.png':
                os.remove(os.path.join(current_app.root_path, 'static/post_pics', post.image_file))
            post.image_file = save_picture(form.picture.data)
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    if post.image_file != 'default.png':
        os.remove(os.path.join(current_app.root_path, 'static/post_pics', post.image_file))
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted', 'success')
    return redirect(url_for('main.posts'))
