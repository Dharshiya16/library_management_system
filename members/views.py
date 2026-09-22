from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm

def member_list(request):

    search = request.GET.get('search', '')

    members = Member.objects.filter(
        name__icontains=search
    )

    return render(
        request,
        'members/member_list.html',
        {
            'members': members,
            'search': search
        }
    )


def member_add(request):

    if request.method == 'POST':
        form = MemberForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('member_list')

    else:
        form = MemberForm()

    return render(
        request,
        'members/member_form.html',
        {'form': form}
    )
def member_edit(request, id):

    member = Member.objects.get(id=id)

    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)

        if form.is_valid():
            form.save()
            return redirect('member_list')

    else:
        form = MemberForm(instance=member)

    return render(
        request,
        'members/member_form.html',
        {'form': form}
    )
def member_delete(request, id):

    member = Member.objects.get(id=id)
    member.delete()

    return redirect('member_list')
