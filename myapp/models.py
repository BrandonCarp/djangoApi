from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.textField()
    date_published = models.DateTImeField(auto_now_add=True)

    def __str__(self):
        return self.title

# class TodoItem(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField(default="")
#     completed = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title

# class UserItem(models.Model):
#     userName = models.CharField(max_length=25)
#     password = models.TextField(default="")

#     def set_password(self, raw_password):
#         # Hash the password before saving
#         self.password = make_password(raw_password)

#     def check_password(self, raw_password):
#         # Check if the raw password matches the hashed password
#         return check_password(raw_password, self.password)

#     def __str__(self):
#         return self.userName
    




