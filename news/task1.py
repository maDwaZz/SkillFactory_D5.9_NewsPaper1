# Итоговое задание D5.9

from django.contrib.auth.models import User
from news.models import *

# Создать двух пользователей (с помощью метода User.objects.create_user('username')).
user1 = User.objects.create_user('ShadowWarrior777')
user2 = User.objects.create_user('Dima1988')

# Создать два объекта модели Author, связанные с пользователями.
author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)

# Добавить 4 категории в модель Category.
category1 = Category.objects.create(news_category='Экономика')
category2 = Category.objects.create(news_category='Наука и техника')
category3 = Category.objects.create(news_category='Политика')
category4 = Category.objects.create(news_category='Развлечения')

# Добавить 2 статьи и 1 новость.
# Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
post1 = Post.objects.create(
    author=author1,
    title='Особенности использования Django ORM',
    text='Интересный, увлекательный и познавательный текст статьи'
    )
post1.categories.set([category2])
post1.save()

post2 = Post.objects.create(
    author=author2,
    title='Почему США не могут сбить китайские воздушные шары над Пентагоном',
    text='Провокативный, с особенно подчеркнутым личным мнением автора текст статьи'
    )
post2.categories.set=([category3])
post2.save()

post3 = Post.objects.create(
    author=author2,
    post_type='N',
    title='Замечены китайские воздушные шары в летном пространстве США',
    text='Новость, в которой автор старается сообщить факты, но все равно ненароком передает личное мнение'
    )
post3.categories.set=([category3])
post3.save()

# Создать как минимум 4 комментария к разным объектам модели Post
# (в каждом объекте должен быть как минимум один комментарий).
comment1 = Comment.objects.create(
    post=post1,
    user=user2,
    comment_text='Очень круто! Теперь лучше понимаю, как работает добавление статей на сайте.'
    )
comment2 = Comment.objects.create(
    post=post2,
    user=user2,
    comment_text='Какая отличная статья, автор явно разбирается в вопросе :D'
    )
comment3 = Comment.objects.create(
    post=post2,
    user=user1,
    comment_text='Сам себя не похвалишь - никто не похвалит :)'
    )
comment4 = Comment.objects.create(
    post=post3,
    user=user1,
    comment_text='Да хрень какая-то, не может такого быть...'
    )

# Применяя функции like() и dislike() к статьям/новостям и комментариям,
# скорректировать рейтинги этих объектов.
Post.like(post1)
Post.like(post2)
Post.like(post2)
Post.dislike(post3)
Post.like(post3)

Comment.like(comment1)
Comment.like(comment2)
Comment.like(comment2)
Comment.like(comment3)
Comment.dislike(comment4)

# Обновить рейтинги пользователей.
Author.update_rating(author1)
Author.update_rating(author2)

# Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
Author.objects.order_by('-user_rating').first().user.username
Author.objects.order_by('-user_rating').first().user_rating

# Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи,
# основываясь на лайках/дислайках к этой статье.
post_best = Post.objects.order_by('-post_rating').first()
post_best.creation_time
post_best.author.user.username
post_best.post_rating
post_best.title
post_best.preview()

# Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
Comment.objects.filter(post__id=2).values()





