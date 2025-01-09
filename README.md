# Building a Startup Categorizer with Blog Using Django 5


#### 1. Starting a New Django Project

        new file:   .gitconfig
        new file:   .gitignore
        new file:   LICENSE
        new file:   README.md
        new file:   blog/__init__.py
        new file:   blog/admin.py
        new file:   blog/migrations/__init__.py
        new file:   blog/models.py
        new file:   blog/tests.py
        new file:   blog/views.py
        new file:   manage.py
        new file:   organizer/__init__.py
        new file:   organizer/admin.py
        new file:   organizer/migrations/__init__.py
        new file:   organizer/models.py
        new file:   organizer/tests.py
        new file:   organizer/views.py
        new file:   requirements.txt
        new file:   suorganizer/__init__.py
        new file:   suorganizer/settings.py
        new file:   suorganizer/urls.py
        new file:   suorganizer/wsgi.py

#### 2. Creating and integrating new apps

        deleted:    .gitconfig
        modified:   README.md
        modified:   suorganizer/settings.py


#### 3. Django Models and SQLite Database

        new file:   .gitconfig
        new file:   Chapter_03_Model_Managers_and_QuerySets.ipynb
        modified:   blog/admin.py
        new file:   blog/migrations/0001_initial.py
        modified:   blog/models.py
        modified:   organizer/admin.py
        new file:   organizer/migrations/0001_initial.py
        modified:   organizer/models.py
        modified:   suorganizer/settings.py

#### 4. Django Templates

        new file:   Chapter_04_Using_Templates_In_Python.ipynb
        new file:   blog/templates/blog/base_blog.html
        new file:   blog/templates/blog/post_detail.html
        new file:   blog/templates/blog/post_list.html
        modified:   organizer/admin.py
        new file:   organizer/templates/organizer/base_organizer.html
        new file:   organizer/templates/organizer/startup_detail.html
        new file:   organizer/templates/organizer/startup_list.html
        new file:   organizer/templates/organizer/tag_detail.html
        new file:   organizer/templates/organizer/tag_list.html
        modified:   organizer/views.py
        modified:   suorganizer/settings.py
        modified:   suorganizer/urls.py
        new file:   templates/base.html

#### 5. Django Views and Urls

        modified:   README.md
        new file:   blog/urls.py
        modified:   blog/views.py
        modified:   organizer/templates/organizer/startup_list.html
        new file:   organizer/urls.py
        modified:   organizer/views.py
        modified:   suorganizer/urls.py
        new file:   suorganizer/views.py

#### 6. Integrating Models,Templates,Views,and URL Configurations to Create Links between Webpages 

        new file:   Chapter_06_Reversing_URL_Patterns.ipynb
        modified:   README.md
        new file:   _db.sqlite3
        modified:   blog/models.py
        modified:   blog/templates/blog/post_detail.html
        modified:   blog/templates/blog/post_list.html
        modified:   blog/urls.py
        modified:   organizer/models.py
        modified:   organizer/templates/organizer/startup_detail.html
        modified:   organizer/templates/organizer/startup_list.html
        modified:   organizer/templates/organizer/tag_detail.html
        modified:   organizer/templates/organizer/tag_list.html
        modified:   organizer/urls.py
        modified:   suorganizer/urls.py
        modified:   templates/base.html

#### 7. Creating forms for user input

        new file:   Chapter_07_Forms_in_Python.ipynb
        new file:   Chapter_07_Model_Validation.ipynb
        modified:   README.md
        modified:   blog/admin.py
        new file:   blog/forms.py
        new file:   organizer/forms.py
        new file:   organizer/migrations/0002_alter_newslink_pub_date_alter_startup_founded_date.py