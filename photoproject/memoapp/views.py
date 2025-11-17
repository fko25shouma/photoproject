from django.shortcuts import render, redirect
from .models import Memo

def memo_list(request):
    memos = Memo.objects.all().order_by('-created_at')
    return render(request, 'memo/memo_list.html', {'memos': memos})

def memo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        nickname = request.POST.get('nickname')

        Memo.objects.create(title=title, nickname=nickname)
        return redirect('memo_list')

    return render(request, 'memo/memo_create.html')
