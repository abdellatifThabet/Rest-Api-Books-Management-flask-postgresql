from typing import Dict, List

class UserModel:

    def __init__(self, name, email):
        self.name = name
        self.likes = email

    def to_dict(self) -> Dict:
        return self.__dict__


class BookModel:

    def __init__(self, name, book_price):
        self.name = name
        self.book_price = book_price

    def to_dict(self) -> Dict:
        return self.__dict__


# class YeldReviewModel:

#     def __init__(self, id: int, name: str, phone_number: int, approved: bool, items: List[Dict] = []):
#         self.id = id
#         self.name = name
#         self.phone_number = phone_number
#         self.approved = approved
#         self.items = items

#     def to_dict(self) -> Dict:
#         return self.__dict__


# class ReviewModel:

#     def __init__(self, id: int, reviewer: str, comment: str, stars: float, reviewer_img: str, approved: bool):
#         self.id = id
#         self.reviewer = reviewer
#         self.comment = comment
#         self.stars = stars
#         self.reviewer_img = reviewer_img
#         self.approved = approved

#     def to_dict(self) -> Dict:
#         return self.__dict__


# class ChannelModel:

#     def __init__(self, id, name, subscribers):
#         self.id = id
#         self.name = name
#         self.subscribers = subscribers

#     def to_dict(self) -> Dict:
#         return self.__dict__