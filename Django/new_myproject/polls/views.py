
# html 파일에 값들을 넘겨주기 위해서 추가 
from django.shortcuts import render, get_object_or_404
# html 구성을 위해 Question, Choice 테이블 추가 
from polls.models import Question, Choice
#리다이렉션을 위해 가져오는 것
from django.http import HttpResponseRedirect, HttpResponse
#기존에 있던 detail.html을 vote() 함수에 리다이렉션 해주기 위해 url 처리를 해줘야함 
from django.urls import reverse

#뷰함수 정의
#request 매개변수는 뷰 함수의 필수 인자 
def index(request):
    #질문을 정렬하여 5개만 뽑아오는 변수
    latest_question_list = Question.objects.order_by('-pub_time')
    context = {'latest_question_list': latest_question_list}
    # render 함수로 전달해주기 (사용자에게 전달)
    return render(request, 'polls/index.html', context)

#html에서 question_id로 form에 넘겨주기 위해 매개변수 지정 필요 
def detail(request, question_id):
    #get_object_or 404: 단축함수
    #첫번째 인자는 모델 클래스 
    #Question 모델 클래스로부터 pk = question_id 검색 조건에 맞는 객체를 조회 
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

#request는 필수 인자, detail() 뷰처럼 question_id 인자를 받음 
def vote(request, question_id):
    #에러처리 혹은 조건을 다시 재정의
    question = get_object_or_404(Question, pk=question_id)
    try:
        #question.choice_set.get 함수를 통해서 데이터를 가져옴
        #검색조건:  pk = request.POST['choice']
        #request.POST는 제출된 폼의 데이터를 담당하는 객체 
        #selected_choice = question.choice_set.get(pk=request.POST.get('choice'))
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # 키 에러가 나거나 조회시 조건에 맞는 데이터가 없으면 예외 처리 
    except (KeyError, Choice.DoesNotExist): 
        # 폼을 다시 보여줌 
        return render(request, 'polls/detail.html', {
            'question' : question, 
            'error_message' : "Error" 
        })
    # 둘 다 처리되지 않는 경우
    # except과 else 구문 엮어서 except 구문이 실행되지 않으면 아래 구문 실행
    # try 구문이 실행되면 무조건 실행되는 부분 
    else:
        # Choice 객체의 votes 속성 선택 카운트를 1 증가시킴
        selected_choice.votes +=1
        # 변경사항을 해당 Choice 테이블에 저장 
        selected_choice.save()
        # 결과 항목에 리다이렉션
        # args는 추가 인자가 오면 묶어서 함수 처리함 (arguments)
        # detail.html의 question.id를 넘겨받아 리다이렉션 
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))
    
def results(request, question_id):
    #에러처리 혹은 조건을 다시 재정의
    question = get_object_or_404(Question, pk=question_id)
    return (request, 'polls/results.html', {'question': question})