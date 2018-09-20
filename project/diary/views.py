from django.shortcuts import render, redirect
from .forms import DayCreateForm

# Create your views here.
def index(request):
	return render(request, 'diary/day_list.html') #第二引数はどのページを見せるか


def add(request):
	#送信内容をもとにフォームを作る。POSTじゃなければ、空のフォーム
	form = DayCreateForm(request.POST or None)

	#method=POST、つまり送信ボタン押下時、入力内容が問題なければ
	if request.method == 'POST' and form.is_valid():
		form.save()
		return redirect('diary:index')

	#通常時のページのアクセスや、入力内容に誤りがあればまたページ表示
	context = {
		'form':form
	}
	return render(request, 'diary/day_form.html', context)