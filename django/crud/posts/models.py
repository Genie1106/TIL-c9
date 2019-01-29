from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	
	
# 1. Create
# post = Post(title="Hello", content="world!")
# post.save()

# 2. Read
# 2.1 All
# posts = Post.objects.all()
# 2.2 Get one
# post = Post.objectcs.get(pk=1) // django는 일반적으로 id 대신 pk를 사용
# 2.3 filter(WHERE)
# posts = Post.objects.filter(title="Hello").all()
# post = Post.objects.filter(title="Hello").first()
# 2.4 LIKE
# posts = Post.objects.filter(title__contains="He").all()
# 2.5 order_by
# posts = Post.objects.order_by('title').all() #오름차순
# posts = Post.objects.order_by('-title').all() #내림차순
# 2.6 limit & offset
# [offset:offset+limit]
# posts = Post.objects.all()[1:2]

# 3. Delete
# post = Post.objects.get(pk=2)
# post.delete()

# 4. Update
# post = Post.objects.get(pk=1)
# post.title = "hi"
# post.save()
