from django.db import models

class Question(models.Model):
    #문자열 필드 생성 
	question_text = models.CharField(max_length=200)
	
	#레코드 생성시 현재 시간 자동 저장 
	pub_time = models.DateTimeField('date publised')
	# 'date publised' : settings.py에 넣어둔 시간으로 동기화를 하겠다는 뜻 
	# 자동 문자열 필드 출력
	def __str__(self):
		return self.question_text
 
class Choice(models.Model):
    #EOM 관계를 정의해줘야함
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #on_delete : 데이터베이스의 기본 조건중 참조무결성이 있음. 
    choice_text = models.CharField(max_length=200)
    #숫자필드 생성 
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text