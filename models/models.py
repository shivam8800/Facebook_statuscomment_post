from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    user_id = models.ForeignKey(User)
    status_text = models.CharField('Status_text', max_length=10000)

    def say_hello(self):
        return u'shivam - ' + self.status_text

    def __str__(self):
        return self.status_text

class Comment(models.Model):
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
    comments_text = models.CharField('Comment_text', max_length=10000)

    def __str__(self):
        return self.comments_text

class NestedComment(models.Model):
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    nested_comment_text =   models.CharField('nested_comment_text', max_length=1000)

    def __str__(self):
        return self.nested_comment_text

# def all_comments(main_id):
#     status = Status.objects.get(id=main_id)
#     all_comments = Comment.objects.all()
#     answer =all_comments.filter(status_id=main_id).comments_text
#     return answer

# def all_comments(main_id):
#     status = Status.objects.get(id=main_id)
#     ans = status.comment_set.all()
#     list1 = []
#     for i in ans:
#         # list1 = str(list1) + str(i) + " "
#         list1.append(str(i))
#     return list1


# list =[]
# all_status = Status.objects.all()
# dict ={}
# for i in all_status:
#     list1 =[]
#     dict['status'] = i.status_text
#     comments = i.comment_set.all()
#     for i in comments:
#         list1.append(str(i))
#     dict['comments'] = list1 
#     list.append(dict)
#     dict ={}        
# print list


