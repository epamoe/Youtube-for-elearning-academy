from py2neo import Graph
from .globals import main_graph

graph1 = Graph("neo4j+s://90de437f.databases.neo4j.io",auth=("neo4j","UJtiMLWQXyF-7PthUPwLq4vR5Ibj80gOcmdX68jqy6c"))

from py2neo_schemas.nodes import User, Video

# videos = Video.match(graph1)
# for vid in videos:
    # graph.push(vid)    
    # print(vid)


vid = Video (
    channel_name='Intellipaat', 
    description= """
    🔥Intellipaat Python course: https://intellipaat.com/python-for-data-science-training/\n🔥Intellipaat Programming courses: https://intellipaat.com/course-cat/programming/\nIn this video you will know how one can start coding and best programming languages to learn in 2020 for Job in Google, Microsoft, Infosys, TCS etc. Also you will know the top 5 programming languages to learn in 2020 for a rewarding career.\n#HowToStartCoding #ProgrammingForBeginners #LearnCoding #Python #Php #Java #Jbpm #Angular #C #c++ #Django #Linux #WebDevelopement\n00:00 - Introduction\n00:08 - How to start coding?\n01:37 - Why Learn Coding?\n04:54 - How to Start Coding?\n09:33 - Learn Basics of that language \n10:32 - Create a Basic Application\n12:11 
    - Which language and tools should you use?\n20:42 - How to Choose a Project?\n24:08 - Learning path: Coding\n28:12 - What Kind of Jobs 
    Can you Expect?\n📌 Do subscribe to Intellipaat channel & get regular updates on videos: https://www.youtube.com/user/intellipaaat?sub_confirmation=1\n\n💡 Know top 5 reasons to learn python: https://www.youtube.com/watch?v=TiFHCjJ8PQ8\n\n🔗 Watch complete Python tutorials here: https://www.youtube.com/watch?v=5GYeia8IRbg&list=PLVHgQku8Z935Qq0h3SZpSOwSrUMx1y3c9\n\n📕 Read complete Python tutorial here: https://intellipaat.com/blog/tutorial/python-tutorial/\n\n📕Read insightful blog on Python certification: https://intellipaat.com/blog/python-certification/\n\nAre you looking for something more? Enroll in our programming courses and become a certified Professional (https://intellipaat.com/all-courses/programming/). All the trainings are instructor led training provided by Intellipaat which is completely aligned with industry standards and certification bodies.\n\nIf you’ve enjoyed this how to start coding video, Like us and Subscribe to our channel for more similar informative videos and free tutorials. \nGot any questions about top programming languages? Ask us in the comment section below.\n----------------------------\nIntellipaat Edge\n \n1. 24*7 Life time Access & Support \n2. Flexible Class 
    Schedule\n3. Job Assistance\n4. Mentors with +14 yrs \n5. Industry Oriented Course ware\n6. Life time free Course Upgrade\n------------------------------\nFor more Information:\nPlease write us to sales@intellipaat.com, or call us at: +91- 7847955955  US : 1-800-216-8930(Toll Free)\n\nWebsite: https://intellipaat.com/all-courses/programming/\n\nFacebook: https://www.facebook.com/intellipaatonline\n\nLinkedIn: https://www.linkedin.com/company/intellipaat-software-solutions\n\nTelegram: https://t.me/Learn_with_Intellipaat\n\nInstagram: 
    https://www.instagram.com/intellipaat/\n\nTwitter: https://twitter.com/Intellipaat\n\nMeetup : https://www.meetup.com/Intellipaat/
    """, 
    published_at='2020-02-25T15:43:31Z',
    thumbnail='https://i.ytimg.com/vi/HIj8wU_rGIU/mqdefault.jpg', 
    title='How to Start Coding | Programming for Beginners | Learn Coding | Intellipaat', 
    video_id='HIj8wU_rGIU', 
    viewCount='5046988'
)
# graph.push(vid)
print(main_graph.exists(vid))

# users = User.match(graph)
# print(users)
# for user in users: 
#     print(user)