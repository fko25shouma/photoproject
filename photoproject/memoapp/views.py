from django.shortcuts import render, redirect, get_object_or_404
from .models import Memo

def memo_list(request):
    memos = Memo.objects.all().order_by('-created_at')
    return render(request, 'memo/memo_list.html', {'memos': memos})

def memo_create(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        content12 = request.POST.get('content12')
        image = request.FILES.get('image')  

        Memo.objects.create(
            nickname=nickname,
            content12 =content12,
            image=image  
        )
        return redirect('memo_list')

    return render(request, 'memo/memo_create.html')


def memo_delete(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    memo.delete()
    return redirect('memo_list')
