from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    # 其他字段...

    def __str__(self):
        return self.username

class tb_user_chat(models.Model):
    chat_id = models.BigAutoField(primary_key=True)
    user_nickname = models.CharField(max_length=200, null=False, default="")
    chat_body = models.CharField(max_length=2000, null=False, default="")
    chat_time = models.IntegerField(null=False, default=0)
    db_time = models.IntegerField(null=False, default=0)
    delete_status = models.IntegerField(null=False, default=0)

    def __str__(self):
        return "[{chat_id=%d,user_nickname=%s,chat_body=%s,chat_time=%d,db_time=%d}]"\
               %(self.chat_id, self.user_nickname, self.chat_body, self.chat_time, self.db_time)