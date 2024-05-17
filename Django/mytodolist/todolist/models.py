from django.db import models

class Todo(models.Model):
    # 할 일을 저장하는 필드. 최대 길이는 100자.
    todo = models.CharField(max_length=100)
    
    # 할 일의 내용을 저장하는 필드. 비어 있어도 됨.
    content = models.TextField(blank=True)
    
    # 할 일이 완료되었는지 여부를 저장하는 필드. 기본값은 False.
    completed = models.BooleanField(default=False)

    # 객체를 문자열로 표현할 때 사용할 내용. 여기서는 할 일의 내용으로 표시.
    def __str__(self):
        return self.todo