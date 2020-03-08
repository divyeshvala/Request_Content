from django.shortcuts import render, redirect
from .models import Idea, Topic, Creator
from django.contrib import messages

from users.models import CreatorsFollowing, TopicsFollowing

def display_ideas(request):
    user = request.user
    my_ideas = []
    my_ideas = Idea.objects.filter(user_id=user.id)
    # all_ideas = Idea.objects.all()
    # find top 10 ideas. trending_ideas = ... 
    # then pass it to render.
    # for more efficiency - make separate table for trending ideas. keep track of number of likes
    # last idea in trending list. Now whenever user upvotes a particular idea, update the table.
    return render(request, 'display_ideas.html', {"user":user, "my_ideas":my_ideas })

def submit_idea(request):
    user = request.user
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        user = request.user

        if user.is_authenticated and user is not None and user.first_name !="":          
            # today = str(date.today())
            # time = str(datetime.now())
            Idea.objects.create(idea_title=title, idea_description=description, user_id=user.id, likes=0)
            messages.info(request, 'review submited')
        else:
            # ask user to login first
            messages.info(request, 'Please login first')

    return redirect('display_ideas_view_url')

def topics(request):
    user = request.user

    # adding new topic
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        user = request.user

        if user.is_authenticated and user is not None and user.first_name !="":          
            # today = str(date.today())
            # time = str(datetime.now())
            topic = Topic.objects.create(title=title, description=description, followers_count=0)
            TopicsFollowing.objects.create(username = user.username, topics_following_id = topic.id)
            messages.info(request, 'topic added')
        else:
            # ask user to login first
            messages.info(request, 'Please login first')

        return redirect('topics_view_url')

    user_topic_list = TopicsFollowing.objects.filter(username = user.username)
    following_topics_id_list = []
    for p in user_topic_list:
        following_topics_id_list.append(p.topics_following_id)

    following_topics_list = Topic.objects.filter(id__in = following_topics_id_list)
    first_four_topics = following_topics_list[:4]
    rest_of_the_topics = following_topics_list[4:]

    all_topics = Topic.objects.all()
    all_topics = [x for x in all_topics if x not in following_topics_list]
    all_topics1 = all_topics[:8]
    all_topics2 = all_topics[8:16]

    return render(request, "topics.html", {"first_four_topics":first_four_topics, "rest_of_the_topics":rest_of_the_topics, "all_topics1":all_topics1, "all_topics2":all_topics2 })

def creators(request):
    user = request.user

    # being a creator
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        user = request.user

        if user.is_authenticated and user is not None and user.first_name !="":          
            # today = str(date.today())
            # time = str(datetime.now())

            if CreatorsFollowing.objects.filter(username = user.username) :
                # you are already a creator.
                messages.info(request, 'you are already a creator')
            else :
                creator = Creator.objects.create(title=title, description=description, followers_count=0, rating=0)
                # you are following yourself :)
                CreatorsFollowing.objects.create(username = user.username, creator_following_id = creator.id)
                messages.info(request, 'Congrats you are creator now.')
        else:
            # ask user to login first
            messages.info(request, 'Please login first')

        return redirect('creators_view_url')

    user_creator_list = CreatorsFollowing.objects.filter(username = user.username)
    following_creators_id_list = []
    for p in user_creator_list:
        following_creators_id_list.append(p.creator_following_id)

    following_creators_list = Creator.objects.filter(id__in = following_creators_id_list)
    following_creators_list1 = following_creators_list[:4]
    following_creators_list2 = following_creators_list[4:]

    all_creators = Creator.objects.all()
    all_creators = [x for x in all_creators if x not in following_creators_list]
    all_creators1 = all_creators[:8]
    all_creators2 = all_creators[8:16]

    return render(request, "creators.html", {"following_creators_list1" : following_creators_list1, "following_creators_list2":following_creators_list2, "all_creators1":all_creators1, "all_creators2":all_creators2 })

# for requested content.



# videos