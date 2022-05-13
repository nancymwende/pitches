from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from ..models import User,Post,Comment,Upvote,Downvote 
from flask_login import current_user, login_required
from .forms import UpdateProfile,CommentForm,PostForm
from .. import db,photos

@main.route('/')
def index():
    posts= Post.query.all()


    '''
    View root page function that returns the index page and its data
    '''

    return render_template('index.html',posts= posts)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user=user)


#update profile
@main.route('/user/<uname>/update', methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
        
    form = UpdateProfile()
        
    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template("profile/profile.html",form  =form)
    
# update pic section    
@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))
    

    
#pitches   
@main.route('/new_pitches', methods=['GET', 'POST'])
@login_required
def new_pitches():
    form = PostForm() 
    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        content = form.content.data
        new_post = Post(title=title,category=category, content=content)
        new_post.save_post()
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('main.index'))

        
    return render_template('/pitches.html',form=form)
    
#comments    
@main.route('/comment', methods=['GET', 'POST'])    
@login_required
def post_details(id):
    comments = Comment.query.filter_by(post_id=id).all()
    posts = Post.query.get(id)
    if posts is None:
        abort(404)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(
            comment=form.comment.data,
            post_id=id,
            user_id=current_user.id
        )
        db.session.add(comment)
        db.session.commit()
        form.comment.data = ''
        flash('Your comment has been posted successfully!')
    return render_template('comments.html', post=posts, comment=comments, comment_form=form)\
    

    
@main.route('/like/<int:id>',methods = ['POST','GET'])
@login_required
def like(id):
    get_posts = Upvote.get_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for posts in get_posts:
        to_str = f'{posts}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_vote = Upvote(post_id=id)
    new_vote.save()
    return redirect(url_for('main.index',id=id))
    

@main.route('/dislike/<int:id>',methods = ['POST','GET'])
@login_required
def dislike(id):
    get_posts = Downvote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for posts in get_posts:
        to_str = f'{posts}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_vote = Downvote(post_id=id)
    new_vote.save()
    return redirect(url_for('main.index',id=id))

    
    
    
    
    
