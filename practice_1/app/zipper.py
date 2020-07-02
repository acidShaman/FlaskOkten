from posts import posts
from users import users


def zipper():
    zipped = []
    for usr in users:
        id = usr.get('id')
        posts_of_user = []
        for pst in posts:
            if pst.get('userId') == id:
                posts_of_user.append(pst)
        zipped.append({id: [usr, posts_of_user]})
    return zipped
