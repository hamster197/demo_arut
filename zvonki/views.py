from datetime import timezone, datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from zvonki.forms import  zvn_form_edit, new_zvn_form
from zvonki.models import zvonok
from django.forms import modelformset_factory,  Textarea
from datetimepicker.widgets import DateTimePicker

##################
# index of zvonki
##################

@login_required
def zv_index_view(request):
    n1='CRM'
    tel_form = new_zvn_form()
    nzvnCount = zvonok.objects.filter(status_zvonka='Новый').count()
    allform1 = modelformset_factory(zvonok, fields=('tel', 'client_name', 'raion', 'subj', 'cena', 'status_zvonka',
                                                'prezvonit', 'coment', ),
                                        widgets={'prezvonit':  DateTimePicker(options={'format': '%Y-%m-%d %H:%M',
	                                            'language': 'ru-ru',}),
                                            'coment': Textarea(attrs={'rows': 80, 'cols': 20})},
                                        extra=0,
                                        )
    Fallform1 = modelformset_factory(zvonok, fields=('tel', 'client_name', 'raion', 'subj', 'cena', 'status_zvonka',
                                                    'prezvonit', 'coment',),
                                    widgets={'prezvonit': DateTimePicker(options={'format': '%Y-%m-%d %H:%M',
                                                                                  'language': 'ru-ru', }),
                                             'coment': Textarea(attrs={'rows': 80, 'cols': 20})},
                                    extra=1,
                                    )
    allform = allform1(queryset=zvonok.objects.filter(status_zvonka='Новый'))
    Fallform = Fallform1(queryset=zvonok.objects.none())
    perezv_call = zvonok.objects.filter(status_zvonka='Перезвонить',auth=request.user).order_by('-prezvonit')
    perezv_call_count = zvonok.objects.filter(status_zvonka='Перезвонить', auth=request.user).order_by('-prezvonit').count()
    nd_call = zvonok.objects.filter(status_zvonka='Недозвонился',auth=request.user).order_by('-date_sozd')
    nd_call_count = zvonok.objects.filter(status_zvonka='Недозвонился', auth=request.user).order_by('-date_sozd').count()
    work_call = zvonok.objects.filter(status_zvonka='В работе',auth=request.user).order_by('-date_sozd')
    work_call_count = zvonok.objects.filter(status_zvonka='В работе', auth=request.user).order_by('-date_sozd').count()
    arh_call = zvonok.objects.filter(status_zvonka='Архив',auth=request.user).order_by('-date_sozd')
    arh_call_count = zvonok.objects.filter(status_zvonka='Архив', auth=request.user).order_by('-date_sozd').count()
    all_call = zvonok.objects.filter(status_zvonka='В общем доступе',auth=request.user).order_by('-date_sozd')
    all_call_count = zvonok.objects.filter(status_zvonka='В общем доступе', auth=request.user).order_by('-date_sozd').count()
    n2='Все звонки:'+' Перезвонить:'+str(perezv_call_count)+'/ Недозвонился:'+str(nd_call_count)+'/ Недозвонился:'\
                                    +str(arh_call_count)+'/ В общем доступе:'+str(all_call_count);


    if request.POST:
        formset = allform1(request.POST, queryset=allform)
        if formset.is_valid():
            formset.save()

    return render(request,'zvonki/index.html',{'tn1':n1,'tn2':n2, 't_per_cl':perezv_call, 'tpcount':perezv_call_count,
                                               't_nd_cl':nd_call, 'tndcount':nd_call_count, 't_wk_cl':work_call, 'twcount':work_call_count,
                                             't_arh_cl':arh_call, 'tarhcount': arh_call_count,'t_all_cl':all_call, 'tallcount': all_call_count,
                                             'tAllForm':allform, 'tFAllForm':Fallform, 'tnzvncount':nzvnCount,'tTelForm':tel_form})




# New tel
#################
@login_required
def new_tel_save_view(request ):
    n1='CRM1'
    tel_form = new_zvn_form()
    if tel_form.is_valid():
        numb = tel_form.cleaned_data('tel')
        s = tel_form.save(commit=False)
        s.tel=numb
        #s = zvonok(tel=numb, auth=request.user, prezvonit=datetime.now())
        s.save()
    else:
        s = zvonok(tel='55', auth=request.user, prezvonit=datetime.now())
        s.save()
    nzvnCount = zvonok.objects.filter(status_zvonka='Новый').count()
    allform1 = modelformset_factory(zvonok, fields=('tel', 'client_name', 'raion', 'subj', 'cena', 'status_zvonka',
                                                'prezvonit', 'coment',),
                                        widgets={'prezvonit':  DateTimePicker(options={'format': '%Y-%m-%d %H:%M',
	                                            'language': 'ru-ru',}),
                                            'coment': Textarea(attrs={'rows': 80, 'cols': 20})},
                                        extra=0, )
    allform = allform1(queryset=zvonok.objects.filter(status_zvonka='Новый').order_by('-date_sozd'))
    perezv_call = zvonok.objects.filter(status_zvonka='Перезвонить',auth=request.user).order_by('-prezvonit')
    perezv_call_count = zvonok.objects.filter(status_zvonka='Перезвонить', auth=request.user).order_by('-prezvonit').count()
    nd_call = zvonok.objects.filter(status_zvonka='Недозвонился',auth=request.user).order_by('-date_sozd')
    nd_call_count = zvonok.objects.filter(status_zvonka='Недозвонился', auth=request.user).order_by('-date_sozd').count()
    work_call = zvonok.objects.filter(status_zvonka='В работе',auth=request.user).order_by('-date_sozd')
    work_call_count = zvonok.objects.filter(status_zvonka='В работе', auth=request.user).order_by('-date_sozd').count()
    arh_call = zvonok.objects.filter(status_zvonka='Архив',auth=request.user).order_by('-date_sozd')
    arh_call_count = zvonok.objects.filter(status_zvonka='Архив', auth=request.user).order_by('-date_sozd').count()
    all_call = zvonok.objects.filter(status_zvonka='В общем доступе',auth=request.user).order_by('-date_sozd')
    all_call_count = zvonok.objects.filter(status_zvonka='В общем доступе', auth=request.user).order_by('-date_sozd').count()
    n2='Все звонки:'+' Перезвонить:'+str(perezv_call_count)+'/ Недозвонился:'+str(nd_call_count)+'/ Недозвонился:'\
                                    +str(arh_call_count)+'/ В общем доступе:'+str(all_call_count);
    return render(request,'zvonki/index.html',{'tn1':n1,'tn2':n2, 't_per_cl':perezv_call, 'tpcount':perezv_call_count,
                                               't_nd_cl':nd_call, 'tndcount':nd_call_count, 't_wk_cl':work_call, 'twcount':work_call_count,
                                             't_arh_cl':arh_call, 'tarhcount': arh_call_count,'t_all_cl':all_call, 'tallcount': all_call_count,
                                             'tAllForm':allform, 'tnzvncount':nzvnCount,'tTelForm':tel_form})

@login_required
def pr_status_zvn_view(request, idd):
    zvn = get_object_or_404(zvonok , pk = idd)
    zvn.status_zvonka = 'Перезвонить'
    zvn.save()
    return redirect('zvn:index')

@login_required
def nd_status_zvn_view(request, idd):
    zvn = get_object_or_404(zvonok , pk = idd)
    zvn.status_zvonka = 'Недозвонился'
    zvn.save()
    return redirect('zvn:index')

@login_required
def work_status_zvn_view(request, idd):
    zvn = get_object_or_404(zvonok , pk = idd)
    zvn.status_zvonka = 'В работе'
    zvn.save()
    return redirect('zvn:index')

@login_required
def arh_status_zvn_view(request, idd):
    zvn = get_object_or_404(zvonok , pk = idd)
    zvn.status_zvonka = 'Архив'
    zvn.save()
    return redirect('zvn:index')

@login_required
def for_all_status_zvn_view(request, idd):
    zvn = get_object_or_404(zvonok , pk = idd)
    zvn.status_zvonka = 'В общем доступе'
    zvn.save()
    return redirect('zvn:index')

#################
# edit_zvonok
#################
@login_required
def edit_zvn_view(request, idd):
    n1='CRM'
    n2='информация о поступившем звонке';
    call = get_object_or_404(zvonok, pk=idd)
    if request.POST:
        form = zvn_form_edit(request.POST)
        if form.is_valid():
            call.coment = form.cleaned_data['coment']
            call.prezvonit = form.cleaned_data['date_pr_call']
            call.save()
    else:
        form = zvn_form_edit(initial={'coment': call.coment, 'date_pr_call': call.prezvonit})

    return render(request,'zvonki/edit.html',{'tn1':n1,'tn2':n2,'pCall':call, 'tForm':form})
#################