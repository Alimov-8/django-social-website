# django-social-website

 ### 1. Getting Started
    • Setup Dev Environment
    • Playing with Django
 #
 ### 2. Authentication System 
  ##### Commits:
    • Register 
    • Log in / Log out
    • Edit Profile, 
    • Change or Reset Password
  
  ##### Topics:
    • Using the Django authentication framework
    • Creating user registration views
    • Extending the user model with a custom profile model
    • Adding social authentication with Python Social Auth
   
  ##### Summary:
  
    Implemented all the necessary views for users to register, log in, log out,
    edit their password, and reset their password. Built a model for custom user
    profiles and you created a custom authentication backend to let users log in to
    website using their email address. Also added social authentication to website
    so that users can use their existing Facebook, Twitter, or Google account to
    log in.
  #
  ### 3. Sharing Content on Website 
   ##### Commits:
    Creating an image bookmarking website
    • Building the image model
    • Creating many-to-many relationships
    • Registering the image model in the administration site
    
    Posting content from other websites
    • Cleaning form fields
    • Overriding the save() method of a ModelForm
    • Building a bookmarklet with jQuery 
    
    Creating a detail view for images 
    Creating image thumbnails using easy-thumbnails 
    Adding AJAX actions with jQuery (Like button)
    Creating custom decorators for your views
    Adding AJAX pagination to your list views
    
   ##### Topics:
    • Creating many-to-many relationships
    • Customizing behavior for forms
    • Using jQuery with Django
    • Building a jQuery bookmarklet
    • Generating image thumbnails using easy-thumbnails
    • Implementing AJAX views and integrating them with jQuery
    • Creating custom decorators for views
    • Building AJAX pagination
    
   ##### Summary:
    Created models with many-to-many relationships and learned
    how to customize the behavior of forms. Used jQuery with Django to build
    a JavaScript bookmarklet to share images from other websites into website. 
    Covered the creation of image thumbnails using the easy-thumbnails
    library. Finally, Implemented AJAX views with jQuery and added AJAX
    pagination to the image list view.
    
    
   ### 4. Tracking User Actions
   ##### Commits:
    Building a follow system
    • Creating many-to-many relationships with an intermediary model
    • Creating list and detail views for user profiles
    • Building an AJAX view to follow users
    
    
   ##### Topics:
    • Building a follow system
    • Creating many-to-many relationships with an intermediary model
    • Creating an activity stream application
    • Adding generic relations to models
    • Optimizing QuerySets for related objects
    • Using signals for denormalizing counts
    • Storing item views in Redis
    
   ##### Summary:
    Built a follow system using many-to-many relationships with an
    intermediary model. Created an activity stream using generic relations and
    you optimized QuerySets to retrieve related objects. Then introduced
    Django signals, and created a signal receiver function to denormalize
    related object counts. Covered application configuration classes, which used
    to load your signal handlers. Also learned how to install and configure Redis
    in Django project. Finally, used Redis in project to store item views,
    and built an image ranking with Redis.

