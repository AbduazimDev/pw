from django.shortcuts import render
from .models import About, Comment, ClientLogo, Education, Experince, Portfolio, Skills, Category, Service, Blog

def about(request):
    about = About.objects.all()
    comments = Comment.objects.all()
    clientlogo = ClientLogo.objects.all()
    education = Education.objects.all()
    experince = Experince.objects.all()
    skills = Skills.objects.all()
    categorys = Category.objects.all()
    projects = Portfolio.objects.all()
    service = Service.objects.all()
    blog = Blog.objects.all()
    return render(request, 'portfoliweb/index.html', {
        "about": about,
        "comments": comments,
        "clientlogo": clientlogo,
        "education": education,
        "experince": experince,
        "skills": skills,
        "categorys": categorys,
        "projects": projects,
        "service": service,
        "blog":blog,
 },)

def blog(request, pk):
    blog = Blog.objects.get(pk=pk)  
    return render(request, "portfoliweb/blog.html",{
        "blog":blog
    })
def project_detail(request, pk):
    project = Portfolio.objects.get(pk=pk)
    return render(request, "portfoliweb/project.html",{
        "project":project
    })

def test (request):
    return render(request, "portfoliweb/test.html")
