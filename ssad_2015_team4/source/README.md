Source code of your project.

Hiring Portal is the main folder for all the source code.
mainportal is the project created in Django.
To run the app - 
1) cd ssad_2015_team4/source/Hiring\ Portal/mainportal
2) python manage.py runserver
Now the app is hosted on the local server.

First install the required packages. Refer to requirements.txt for further information.

The landing page is http://127.0.0.1:8000/static/static_files/landingpage.html
From here the navigation bars are self-explanatory.
Refer to testids.txt in the same folder for more information on test logins.


SOURCE CODE BREAK-UP:

1) The authentication is handled by the app named "authentication".
2) The CAS(Central Authentication Service) is handled by the app "django_cas_ng"
3) User roles are maintained by the app "userroles".
4) The Candidate's functionality and related are managed by the app"faculty_portal".
5) The IIIT employee functionalities are present in the folder "Academic".
6) In Academic, the app named "Staff" contains staff members views,controllers etc.
7) Similarly for Hiring Committee we have app named "HiringCommittee" (Inside Academic only).
8) For Regular Faculty members the app is named, "Faculty".
9) The folder static contains the necessary static files hosted on the server.

