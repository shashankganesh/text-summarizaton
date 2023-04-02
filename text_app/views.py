from django.shortcuts import render,HttpResponse,redirect
from django.template import loader
from . import textsummarizer as ts
import os
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        txt = request.POST.get('text')
        print(txt)   
        if txt == "":
            # print("Empty") 
            # msg = "Please insert the text!"
            messages.error(request, 'Please insert the text!')
            return redirect('home')
        elif len(txt.split("."))<=2:
            msg="please insert more text to summarize!"
            messages.warning(request, 'Please insert more text to summarize!')
            return redirect('home')

        else:    
            summary=ts.generate_summary(str(txt))
            f= open("before.txt","w+")
            f.write(txt)
            f.close()
            f1=open("after.txt","w+")
            f1.write(summary)
            f1.close()
            file_name = "before.txt"
            file_name1 = "after.txt"
            # file_stats = os.stat(file_name)
            file1_size = os.path.getsize("before.txt")
            file1_size1 = os.path.getsize("after.txt")
            # file_stats1 = os.stat(file_name1)
            # nlen=(f'File Size in Bytes Before summarize is {file_stats.}')
            # olen=(f'File Size in Bytes After Summarize is {file_stats1.st_size}')
            # perc=(int(nlen)/int(olen))*100
            per1=(file1_size1/file1_size)*100
            per=(f'Summarised percentage is {per1}')
            file_size1=(f'File Size in Bytes After Summarize is {file1_size1}')
            file_size=(f'File Size in Bytes Before summarize is {file1_size}')
            return render(request,'text_app/home.html',{'summary': summary,'tlen': file_size,'slen': file_size1,'perc': per})
    
    else:
        return render(request,'text_app/home.html')
    # template = loader.get_template('home.html')
    # return HttpResponse(template.render())