# from flask import Flask, Response, request
# from email.policy import default
# from flask_migrate import Migrate
# from db_models import db, Page, Review
# import os
# from libfile import pageLib, reviewLib, channelLib

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db.init_app(app)
# migrate = Migrate(app, db)

# ####################################
# # the blueprint import should be here after flask app initialization
# from blueprint import blueprint_v1, app_ns, api_v1
# from resources import ResourceApp
# from flask_restx import fields, reqparse
# from werkzeug.exceptions import NotFound, Forbidden


# # register the blueprints
# app.register_blueprint(blueprint_v1)
# ###################################""
 
# ############## **MODELS** #######################
# reviews_page_post_model = app_ns.model('reviews_page_post_model', {
#     'yelp_link': fields.String(required=True, description='the link of reviews page', default='https://www.yelp.com/biz/lindell-chiropractic-mountain-view?osq=lindell+chiropractic')
# })

# facebook_page_post_model = app_ns.model('facebook_page_post_model', {
#     'email': fields.String(required=True, description='email of the facebook account', default='eltscrp@hotmail.com'),
#     'passwd': fields.String(required=True, description='password of the facebook account', default='54460380'),
#     'search_page': fields.String(required=True, description='the link of the facebook page', default='https://www.facebook.com/LindellChiropractic')
# })

# youtube_channel_post_model = app_ns.model('youtube_channel_post_model', {
#     'channel_link': fields.String(required=True, description='the link of the channel', default='https://www.youtube.com/user/tavarezorthodontics')
# })

# pages_list_parser = reqparse.RequestParser()
# pages_list_parser.add_argument(
#     'page_name', type=str, help='the anme of the page', required=True)
# pages_list_parser.add_argument(
#     'above_likes', type=int, help='the minimum number of likes , default=0', required=False)

# yelp_list_parser = reqparse.RequestParser()
# yelp_list_parser.add_argument(
#     'phone_number', type=int, help='the phone number of the yelp', required=True)
# yelp_list_parser.add_argument(
#     'stars', type=float, help='minimum number of stars, default=1', required=False, default = 1.0)
# yelp_list_parser.add_argument(
#     'timestamp', type=str, help='last time before scraping, default = current timestamp', required=False, default='2022-06-25 16:04:43.174608+00')
# ###################################
# ############## **VIEWS** #########################



# ####################### For Fcaebook ####################################""

# ## this endpoint for scrapping the facebook page 
# @app_ns.route('/facebook_page/add', doc={'example': 'app/facebook_page/add'})
# class ScrapFacebookPage(ResourceApp):

#     @app_ns.response(200, 'data added to database')
#     @app_ns.response(400, 'Wrong data format')
#     @app_ns.expect(facebook_page_post_model)
#     def post(self):
#         ## here we get data from scrapper and save it into database
#         email = api_v1.payload['email']
#         passwd = api_v1.payload['passwd']
#         search_page = api_v1.payload['search_page']
#         pageLib.add_page(email, passwd, search_page)
#         return Response(status=204)

# ## this endpoint is to approve a facebook page 
# @app_ns.route('/facebook_page/<int:page_id>', doc={'example': 'app/facebook_page/5'})
# class PageUpdateStatus(ResourceApp):

#     @app_ns.response(204, 'row approved')
#     @app_ns.response(400, 'Wrong data format')
#     @app_ns.response(403, 'Operation not permitted')
#     @app_ns.response(404, 'Resource not found')
#     def put(self, page_id: int):
#         pageLib.update_page_status(page_id)
#         return Response(status=204)

# ## return the facebook pages 
# @app_ns.route('/facebook_page', doc={'example': 'app/facebook_page'})
# class PagesDetails(ResourceApp):

#     @app_ns.response(200, 'pages details')
#     @app_ns.response(404, 'No pages found')
#     def get(self):
#         pages = pageLib.get_all_pages()
#         return {'pages': pages}


# ## search for a specfic page by name and likes 
# @app_ns.route('/facebook_page/search', doc={'example': 'app/facebook_page/search'})
# class PagesSearch(ResourceApp):

#     above_likes = 0
#     @app_ns.response(200, 'pages details')
#     @app_ns.response(404, 'No pages found')
#     @app_ns.expect(pages_list_parser)
#     def get(self):
#         args = request.args
#         page_name = args.get('page_name')
#         above_likes = max(int(args.get("above_likes", self.above_likes)), self.above_likes)
#         pages = pageLib.search_page(page_name, above_likes)
#         return {'pages': pages}


# ####################### For yelp ####################################""

# ## this endpoint for scrapping the yeld reviews 
# @app_ns.route('/reviews/add', doc={'example': 'app/reviews/add'})
# class ScrapReviews(ResourceApp):

#     @app_ns.response(204, 'data added to database')
#     @app_ns.response(400, 'Wrong data format')
#     @app_ns.expect(reviews_page_post_model)
#     def post(self):
#         ## here we get data from scrapper and save it into database
#         reviewLib.add_reviews(api_v1.payload['yelp_link'])
#         return Response(status=204)

# ## this endpoint is to approve a yeld reviews 
# @app_ns.route('/reviews/<int:yeld_review_id>', doc={'example': 'app/reviews/3'})
# class ReviewsUpdateStatus(ResourceApp):

#     @app_ns.response(204, 'row approved')
#     @app_ns.response(400, 'Wrong data format')
#     @app_ns.response(403, 'Operation not permitted')
#     @app_ns.response(404, 'Resource not found')
#     def put(self, yeld_review_id: int):
#         reviewLib.update_yeld_reviews_status(yeld_review_id)
#         return Response(status=204)

# ## this endpoint is to approve a review item 
# @app_ns.route('/reviews/item/<int:review_id>', doc={'example': 'app/reviews/item/3'})
# class ReviewsUpdateStatus(ResourceApp):

#     @app_ns.response(204, 'row approved')
#     @app_ns.response(400, 'Wrong data format')
#     @app_ns.response(403, 'Operation not permitted')
#     @app_ns.response(404, 'Resource not found')
#     def put(self, review_id: int):
#         reviewLib.update_review_item_status(review_id)
#         return Response(status=204)

# ## return the yeld reviews 
# @app_ns.route('/reviews', doc={'example': 'app/reviews'})
# class PagesDetails(ResourceApp):

#     @app_ns.response(200, 'yelp reviews details')
#     @app_ns.response(404, 'No yelp reviews found')
#     def get(self):
#         yeld_reviews = reviewLib.get_all_reviews()
#         return {'yelp_reviews': yeld_reviews}

# ## search for a specfic yeld reviews 
# @app_ns.route('/reviews/search', doc={'example': 'app/reviews/search'})
# class YeldSearch(ResourceApp):

#     stars = 0.0
#     @app_ns.response(200, 'yelp details')
#     @app_ns.response(404, 'No yelp found')
#     @app_ns.expect(yelp_list_parser)
#     def get(self):
#         args = request.args
#         phone_number = args.get('phone_number')
#         timestamp = args.get('timestamp')
#         stars = max(float(args.get("stars", self.stars)), self.stars)
#         yeld_reviews = reviewLib.search_yeld(phone_number, timestamp, stars)
#         return {'pages': yeld_reviews}


# ####################### For youtube channel ####################################""

# ## this endpoint for scrapping the youtube channel 
# @app_ns.route('/channel/add', doc={'example': 'app/channel/add'})
# class ScrapChannel(ResourceApp):

#     @app_ns.response(204, 'data added to database')
#     @app_ns.response(400, 'Wrong data format')
#     @app_ns.expect(youtube_channel_post_model)
#     def post(self):
#         ## here we get data from scrapper and save it into database
#         channelLib.add_channel(api_v1.payload['channel_link'])
#         return Response(status=204)

# ## return the youtube channels 
# @app_ns.route('/channel', doc={'example': 'app/channel'})
# class ChannelDetails(ResourceApp):

#     @app_ns.response(200, 'channel details')
#     @app_ns.response(404, 'No channels found')
#     def get(self):
#         channels = channelLib.get_all_channels()
#         return {'channels': channels}


from re import A
from flask import Flask, request, Response, jsonify
from flask_restx import Resource, Api, fields
from flask_migrate import Migrate

#from werkzeug.security import generate_password_hash,check_password_hash
## as a hash function we'll be  using argon
from argon2 import PasswordHasher
ph = PasswordHasher()
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import uuid
import jwt
import datetime
import os
from werkzeug.exceptions import NotFound, Forbidden

from db_models import Book, User
from models import UserModel, BookModel

from functools import wraps
app = Flask(__name__)

app.config['SECRET_KEY']='change-me'
app.config['SQLALCHEMY_DATABASE_URI']=os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
from db_models import db 
db.init_app(app)
migrate = Migrate(app, db)

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'x-access-tokens'
    }
}
api = Api(app, authorizations=authorizations)


user_post_model = api.model('user_post_model', {
    'name': fields.String(required=True, description='name of the user', default='user 1'),
    'email': fields.String(required=True, description='email of the user', default='user1@gmail.com'),
    'passwd': fields.String(required=True, description='password of the facebook account', default='54460380'),
})

login_post_model = api.model('login_post_model', {
    'email': fields.String(required=True, description='name of the user'),
    'passwd': fields.String(required=True, description='password of the facebook account', format='password'),
})

book_post_model = api.model('book_post_model', {
    'book_name': fields.String(required=True, description='name of the book'),
    'book_price': fields.Integer(required=True, description='price of the book'),
})


@api.route('/register', doc={'example': 'register'})
class UserManagemet(Resource):
    @api.response(200, 'user added')
    @api.response(400, 'Wrong data format')
    @api.expect(user_post_model)
    def post(self):
        ## here we get data from scrapper and save it into database
        name = api.payload['name']
        email = api.payload['email']
        ##hashed_password = generate_password_hash(api.payload['passwd'], method='sha256')
        
        hashed_password = ph.hash(api.payload['passwd'])

        new_user = User(public_id=str(uuid.uuid4()), name=name, email=email, hashed_password = hashed_password)

        db.session.add(new_user) 
        db.session.commit()   
        return Response(status=204)

def token_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):
       token = None
       if 'x-access-tokens' in request.headers:
           token = request.headers['x-access-tokens']
 
       if not token:
           return jsonify({'message': 'a valid token is missing'})
       try:
           data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
           current_user = User.query.filter_by(public_id=data['public_id']).first()
       except:
           return jsonify({'message': 'token is invalid'})
 
       return f(current_user, *args, **kwargs)
   return decorator 

@api.route('/login', doc={'example': 'login'})
class UserLogin(Resource):
    @api.response(200, 'user logged in')
    @api.response(400, 'Wrong data format')
    @api.expect(login_post_model)
    def post(self):
        ## here we get data from scrapper and save it into database
        email = api.payload['email']
        passwd = api.payload['passwd']
        ## email field in user table should be unique
        user = User.query.filter_by(email = email).first()
        if not user:
            raise NotFound('no user with this email')

        ## unhashed_password = check_password_hash(user.hashed_password, passwd)
        unhashed_password = ph.verify(user.hashed_password, passwd)

        if not unhashed_password:
            raise Forbidden('password incorrect')
        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow()+ datetime.timedelta(minutes=10)}, app.config['SECRET_KEY'])
        return jsonify({'token': token})
        
def get_current_user():
    token = request.headers['x-access-tokens']
    data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
    usr = User.query.filter_by(public_id=data['public_id']).first()
    return usr

import logging
@api.route('/books', doc={'example': 'books'})
class ListOwnBooks(Resource):
    @api.response(200, 'user books list')
    @api.response(404, 'No users found')
    @api.doc(security='apikey')
    @token_required
    def get(self, current_user):

        usr = get_current_user()
        db_books = Book.query.filter(Book.user_id == usr.id).all()
        
        if not db_books:
            raise NotFound("books not found")

        books = [BookModel(name = book.name, book_price = book.book_price).to_dict() for book in db_books]
        return {'books': books}


@api.route('/books/add', doc={'example': 'books/add'})
class AddOwnBook(Resource):
    @api.response(200, 'user book added')
    @api.response(404, 'No users found')
    @api.doc(security='apikey')
    @token_required
    @api.expect(book_post_model)
    def post(self, current_user):
        book_name = api.payload['book_name']
        book_price = api.payload['book_price']
        usr = get_current_user()
        new_book = Book(name = book_name, book_price = book_price, user_id = usr.id)
        
        db.session.add(new_book)
        db.session.commit()

        return Response(status=204)


@api.route('/books/favorite/<int:book_id>', doc={'example': 'books/favorite/2'})
class AddFavoriteBook(Resource):
    @api.response(200, 'book added to favorite')
    @api.response(404, 'No users found')
    @api.doc(security='apikey')
    @token_required
    def post(self, current_user, book_id:int):

        usr = get_current_user()
        favorite_book = Book.query.filter(Book.id == book_id).first()  
        if not favorite_book:
            raise NotFound("book not found")
        ## adding the book to the user favorite books   
        usr.favorite_books.append(favorite_book)   
        db.session.add(usr)
        db.session.commit()

        return Response(status=204)

@api.route('/books/favorite', doc={'example': 'books/favorite'})
class UserFavoriteBooks(Resource):
    @api.response(200, 'user favorite books list')
    @api.response(404, 'No users found')
    @api.doc(security='apikey')
    @token_required
    def get(self, current_user):

        usr = get_current_user()

        books = [BookModel(name = book.name, book_price = book.book_price).to_dict() for book in usr.favorite_books]
        return {'favorite books': books}

