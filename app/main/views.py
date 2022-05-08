from flask import render_template
from .import main
from ..models import User, Upvote,Downvote,Comment 
from flask_login import login_required

@main.route('/')
def index():

    return render_template('index.html')
    
    
    
# @main.route('/movie/renew/new/int<:id>', methods = ['GET','POST'])
