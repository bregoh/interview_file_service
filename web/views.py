from datetime import datetime, timedelta
from django.utils import timezone
from django.shortcuts import render, redirect
from api.models import FileLinks, FilesManagement, UserAgent
from api.serializers import FileSerializer


# function to check if the date difference
# between the current time and the file create time
def checkLinkIsValid(oldDate):
    date_format_str = "%Y-%m-%d %H:%M:%S"
    current_datetime = timezone.make_naive(timezone.now(), timezone.utc).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    now = datetime.strptime(current_datetime, date_format_str)
    before = datetime.strptime(oldDate, date_format_str)
    diff = (now - before).total_seconds() / 3600

    if diff > 24:
        return False

    return True


def incrementDateByOneDay(date):
    formattedDate = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    increment = formattedDate + timedelta(days=1)
    return increment


def uploadPage(request):
    return render(request, "file.html")


def loginPage(request, file_id):
    context = dict()
    browser = request.user_agent.browser.family
    os = request.user_agent.os.family

    # get the current url
    file_url = request.path.strip("/")
    filemanager = FilesManagement.objects.filter(
        filelinks__link=file_url, filelinks__is_expired=False
    ).first()
    serializer = FileSerializer(filemanager)
    file_link = serializer.data["filelinks"][0]

    # redirect to 404 on invalid url
    if serializer.data.get("file_id") is None:
        return render(request, "404.html")

    # update the link visit count
    file_link_id = file_link["id"]
    link_visit = file_link["link_visit"] + 1

    # check if link has expired, if expired then update the link
    if not checkLinkIsValid(file_link["created"]):
        FileLinks.objects.filter(id=file_link_id).update(is_expired=True)

    # check if useragent exists
    useragent = UserAgent.objects.filter(
        os=os, browser=browser, link_id=file_link_id
    ).exists()

    # set the file info to context
    context["data"] = serializer.data
    context["url"] = file_url
    context["expiry_date"] = incrementDateByOneDay(serializer.data["created"])

    # check if user has already visited the file
    if useragent:
        FileLinks.objects.filter(id=file_link_id).update(link_visit=link_visit)
        return render(request, "file.html", context=context)

    # check if the method is a get to return
    if request.method == "GET":
        return render(request, "login.html")

    # check if password is correct
    password = request.POST.get("password")
    db_password = file_link["password"]
    if db_password != password:
        context["error"] = "invalid password"
        return render(request, "login.html", context=context)

    # render the file page
    FileLinks.objects.filter(id=file_link_id).update(link_visit=link_visit)
    UserAgent(os=os, browser=browser, link_id=file_link_id).save()
    return render(request, "file.html", context=context)


def indexPage(request):
    if request.user.is_anonymous:
        return redirect("/admin/login")

    context = dict()

    queryset = FilesManagement.objects.all()
    result = FileSerializer(queryset, many=True)

    context["data"] = result.data
    return render(request, "home.html", context=context)
