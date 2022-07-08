# from db_models import Page, Review, ReviewItem, Channel, db
# from werkzeug.exceptions import Forbidden, BadRequest, NotFound
# from scrapper import scrap_data, scrap_reviews, scrap_channel
# from models import ReviewModel,PageModel,YeldReviewModel,ChannelModel

# from sqlalchemy.orm import joinedload, selectinload
# from sqlalchemy import and_

# import requests

# class PageLib:

#     @staticmethod
#     def add_page(email,passwd,search_page):
#         scraper = scrap_data(email,passwd,search_page)
#         if 'login' in scraper:
#             raise NotFound('user not found')
#         if 'notfound' in scraper:
#             raise Forbidden('page not found')
#         if 'driver' in scraper:
#             raise NotFound('chrome driver failed')

#         page = Page(scraper['name'], scraper['likes'], scraper['followers'])
#         db.session.add(page)
#         db.session.commit()

#     @staticmethod
#     def update_page_status(page_id: int):
#         db_page_obj = Page.query.filter(Page.id == page_id).first()
#         if not db_page_obj:
#             raise NotFound("Page not found")
#         db_page_obj.approved = True
#         db.session.commit()

#     @staticmethod
#     def get_all_pages():
#         db_pages = db.session.query(Page).all()
#         if not db_pages:
#             #raise NotFound("No pages found")
#             return {}
#         pages = []
#         for db_page in db_pages:
#             page = PageModel(db_page.id, db_page.name, db_page.likes, db_page.followers, db_page.approved)
#             pages.append(page.to_dict())
#         return pages

#     @staticmethod
#     def search_page(page_name, above_likes):
#         db_pages = db.session.query(Page).filter(and_(Page.name == page_name, Page.likes >= above_likes)).all()
#         if not db_pages:
#             raise NotFound("No pages found")
#         pages = []
#         for db_page in db_pages:
#             page = PageModel(db_page.id, db_page.name, db_page.likes, db_page.followers, db_page.approved)
#             pages.append(page.to_dict())

#         return pages



# class ReviewLib:

#     @staticmethod
#     def add_reviews(yelp_link):
#         reviews_scraper = scrap_reviews(yelp_link)
#         reviews = reviews_scraper[1]
#         name = reviews_scraper[0][0]
#         phone = reviews_scraper[0][1]
#         yeld_review = Review(name, phone)
#         reviews_to_add =[]
#         for rev in reviews:
#             reviewer = rev[0]
#             comment = rev[1]
#             stars = rev[2]
#             reviewer_img = rev[3]
#             review = ReviewItem(reviewer, comment, stars, reviewer_img, yeld_review=yeld_review)
#             reviews_to_add.append(review)
#         db.session.add(yeld_review)
#         db.session.add_all(reviews_to_add)
#         db.session.commit()

#     @staticmethod
#     def update_yeld_reviews_status(yeld_review_id: int):
#         db_yeld_obj = Review.query.filter(Review.id == yeld_review_id).first()
#         if not db_yeld_obj:
#             raise NotFound("yeld review not found")
#         db_yeld_obj.approved = True
#         db.session.commit()

#     @staticmethod
#     def update_review_item_status(review_id: int):
#         db_review = ReviewItem.query.filter(ReviewItem.id == review_id).first()
#         if not db_review:
#             raise NotFound("review item not found")
#         db_review.approved = True
#         db.session.commit()

#     @staticmethod
#     def get_all_reviews():
#         db_yelds = db.session.query(Review). \
#             options(
#             joinedload(Review.reviews)).all()

#         if not db_yelds:
#             #raise NotFound("yeld reviews not found")
#             return {}
#         yelds = []
#         for db_yeld in db_yelds:
#             reviews = []
#             for db_review in db_yeld.reviews:
#                 review = ReviewModel(db_review.id, db_review.reviewer, db_review.comment, db_review.stars, db_review.reviewer_img, db_review.approved)
#                 reviews.append(review.to_dict())
#             yeld = YeldReviewModel(db_yeld.id, db_yeld.name,db_yeld.phone_number, db_yeld.approved, reviews)
#             yelds.append(yeld.to_dict())
#         return yelds
    
#     @staticmethod
#     def search_yeld(phone_number, timestamp, stars):
#         ####Review.created_at <= datetime.datetime.fromtimestamp(anchor_time)
#         db_yelds = db.session.query(Review).join(ReviewItem).filter(and_(Review.phone_number == phone_number, Review.created_at >= timestamp \
#                                             )).options(joinedload(Review.reviews)).all()

#         if not db_yelds:
#             #raise NotFound("No pages found")
#             return {}
#         yelds = []
#         for db_yeld in db_yelds:
#             reviews = []
#             for db_review in db_yeld.reviews:
#                 if db_review.stars >= stars:
#                     review = ReviewModel(db_review.id, db_review.reviewer, db_review.comment, db_review.stars, db_review.reviewer_img, db_review.approved)
#                     reviews.append(review.to_dict())
#             yeld = YeldReviewModel(db_yeld.id, db_yeld.name,db_yeld.phone_number, db_yeld.approved, reviews)
#             yelds.append(yeld.to_dict())

#         return yelds

# class ChannelLib:
#     @staticmethod
#     def add_channel(channel_link):
#         scraper = scrap_channel(channel_link)
#         if 'notfound' in scraper:
#             raise Forbidden('data not scrapped')

#         channel = Channel(scraper[0], scraper[1])
#         db.session.add(channel)
#         db.session.commit()

#     @staticmethod
#     def get_all_channels():
#         db_channels = db.session.query(Channel).all()
#         if not db_channels:
#             return {}
#         channels = []
#         for db_channel in db_channels:
#             channel = ChannelModel(db_channel.id, db_channel.name, db_channel.subscribers)
#             channels.append(channel.to_dict())
#         return channels


# channelLib = ChannelLib()
# reviewLib = ReviewLib()
# pageLib = PageLib()