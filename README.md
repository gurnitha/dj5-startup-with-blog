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

#### 8. DisplayingFormsinTemplates

        new file:   blog/templates/blog/post_confirm_delete.html
        new file:   blog/templates/blog/post_form.html
        new file:   blog/templates/blog/post_form_update.html
        modified:   organizer/migrations/0002_alter_newslink_pub_date_alter_startup_founded_date.py
        new file:   organizer/templates/organizer/newslink_confirm_delete.html
        new file:   organizer/templates/organizer/newslink_form.html
        new file:   organizer/templates/organizer/newslink_form_update.html
        new file:   organizer/templates/organizer/startup_confirm_delete.html
        new file:   organizer/templates/organizer/startup_form.html
        new file:   organizer/templates/organizer/startup_form_update.html
        new file:   organizer/templates/organizer/tag_confirm_delete.html
        new file:   organizer/templates/organizer/tag_form.html
        new file:   organizer/templates/organizer/tag_form_update.html

#### 9. Controlling Forms in Views

        modified:   blog/models.py
        modified:   blog/templates/blog/post_detail.html
        modified:   blog/templates/blog/post_list.html
        modified:   blog/urls.py
        modified:   blog/views.py
        modified:   organizer/admin.py
        modified:   organizer/migrations/0002_alter_newslink_pub_date_alter_startup_founded_date.py
        modified:   organizer/models.py
        modified:   organizer/templates/organizer/startup_detail.html
        modified:   organizer/templates/organizer/startup_list.html
        modified:   organizer/templates/organizer/tag_detail.html
        modified:   organizer/templates/organizer/tag_list.html
        modified:   organizer/urls.py
        new file:   organizer/utils.py
        modified:   organizer/views.py

        Note:

        Can do CRUD. :)

#### 10. Revisiting Migrations

        modified:   blog/admin.py
        new file:   blog/migrations/0002_post_data.py
        new file:   blog/migrations/0003_post_fields_startups_and_tags_optional.py
        modified:   blog/models.py
        modified:   organizer/admin.py
        new file:   organizer/migrations/0002_tag_data.py
        new file:   organizer/migrations/0003_startup_data.py
        new file:   organizer/migrations/0004_newslink_data.py
        new file:   organizer/migrations/0005_newslink_slug.py
        new file:   organizer/migrations/0006_newslink_unique_together_slug_startup.py
        new file:   organizer/migrations/0007_startup_tag_field_optional.py
        new file:   organizer/migrations/0008_alter_newslink_pub_date_alter_startup_founded_date.py
        modified:   organizer/models.py

        Note:

        CRUD + data

        :)

#### 11. Bending the Rules: The Contact Us Webpage

        modified:   blog/admin.py
        new file:   contact/__init__.py
        new file:   contact/forms.py
        new file:   contact/templates/contact/base_contact.html
        new file:   contact/templates/contact/contact_form.html
        new file:   contact/tests.py
        new file:   contact/urls.py
        new file:   contact/views.py
        modified:   organizer/migrations/0008_alter_newslink_pub_date_alter_startup_founded_date.py
        new file:   organizer/urls/__init__.py
        new file:   organizer/urls/newslink.py
        new file:   organizer/urls/startup.py
        new file:   organizer/urls/tag.py
        modified:   suorganizer/settings.py
        modified:   suorganizer/urls.py
        modified:   templates/base.html

        Note:

        Contact message display on terminal only ...

        :)

#### 14. Pagination: A Tool for Navigation

        new file:   Chapter_14_Pagination.ipynb
        modified:   blog/admin.py
        modified:   blog/templates/blog/post_list.html
        modified:   blog/urls.py
        modified:   blog/views.py
        modified:   contact/urls.py
        modified:   organizer/migrations/0008_alter_newslink_pub_date_alter_startup_founded_date.py
        modified:   organizer/models.py
        new file:   organizer/newslink.py
        new file:   organizer/startup.py
        new file:   organizer/tag.py
        modified:   organizer/templates/organizer/startup_list.html
        modified:   organizer/templates/organizer/tag_list.html
        modified:   organizer/urls/newslink.py
        modified:   organizer/urls/startup.py
        modified:   organizer/urls/tag.py
        modified:   organizer/views.py
        modified:   requirements.txt
        modified:   suorganizer/settings.py
        new file:   suorganizer/settings_ori.py
        modified:   suorganizer/urls.py

        :)

#### 15. Creating Webpages with Django Flatpages
        
        modified:   blog/urls.py
        modified:   blog/views.py
        new file:   core/__init__.py
        new file:   core/migrations/0001_sites_data.py
        new file:   core/migrations/0002_flatpages_data.py
        new file:   core/migrations/__init__.py
        modified:   organizer/admin.py
        modified:   organizer/migrations/0008_alter_newslink_pub_date_alter_startup_founded_date.py
        modified:   organizer/models.py
        modified:   organizer/views.py
        modified:   requirements.txt
        modified:   suorganizer/settings.py
        modified:   suorganizer/urls.py
        modified:   templates/base.html
        new file:   templates/flatpages/default.html

        :)