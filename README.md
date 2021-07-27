# django-social-website 
### Testing 🔗 http://alimov8.pythonanywhere.com/
### 📚 Build powerful and reliable Python web application from scratch (Antonio Mele) 
#
 ### Getting Started
    • Setup Dev Environment
    • Playing with Django
 #
 ### 1. Authentication System 
  ##### ↪️ Commits:
    • Register 
    • Log in / Log out
    • Edit Profile, 
    • Change or Reset Password
  
  ##### ✏️ Topics:
    📌 Using the Django authentication framework
    📌 Creating user registration views
    📌 Extending the user model with a custom profile model
    📌 Adding social authentication with Python Social Auth
   
  ##### 📄 Summary:
  
    Implemented all the necessary views for users to register, log in, log out,
    edit their password, and reset their password. Built a model for custom user
    profiles and you created a custom authentication backend to let users log in to
    website using their email address. Also added social authentication to website
    so that users can use their existing Facebook, Twitter, or Google account to
    log in.
  #
  ### 2. Sharing Content on Website 
   ##### ↪️ Commits:
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
    
   ##### ✏️ Topics:
    📌 Creating many-to-many relationships
    📌 Customizing behavior for forms
    📌 Using jQuery with Django
    📌 Building a jQuery bookmarklet
    📌 Generating image thumbnails using easy-thumbnails
    📌 Implementing AJAX views and integrating them with jQuery
    📌 Creating custom decorators for views
    📌 Building AJAX pagination
    
   ##### 📄 Summary:
    Created models with many-to-many relationships and learned
    how to customize the behavior of forms. Used jQuery with Django to build
    a JavaScript bookmarklet to share images from other websites into website. 
    Covered the creation of image thumbnails using the easy-thumbnails
    library. Finally, Implemented AJAX views with jQuery and added AJAX
    pagination to the image list view.
    
    
   ### 3. Tracking User Actions
   ##### ↪️ Commits:
    Building a follow system
     • Creating many-to-many relationships with an intermediary model (Following system model)
     • Creating list and detail views for user profiles 
     • Building an AJAX view to follow users (Follow/Unfollow button client side views)
     
    Building a generic activity stream application
     • Using the contenttypes framework (to add target "X bookmarked Y" Generic Foregin Key)
     • Adding generic relations to your models
     • Avoiding duplicate actions in the activity stream (validation for activities)
     • Adding user actions to the activity stream 
     • Displaying the activity stream
     • Optimizing QuerySets that involve related objects
     • Using prefetch_related()
     
    Using signals for denormalizing counts. 
       (Denormalization is making data redundant in such a way that it optimizes read performance)
     • Working with signals (Signals can be used for updating denormalization data)
     • Application configuration classes
  
    Using Redis for storing item views
     • Installing Redis [https://github.com/microsoftarchive/redis/releases] [https://youtu.be/188Fy-oCw4w]
     • Using Redis with Python
     • Storing item views in Redis
     • Storing a ranking in Redis
     • Next steps with Redis

    
    
   ##### ✏️ Topics:
    📌 Building a follow system
    📌 Creating many-to-many relationships with an intermediary model
    📌 Creating an activity stream application
    📌 Adding generic relations to models
    📌 Optimizing QuerySets for related objects
    📌 Using signals for denormalizing counts
    📌 Storing item views in Redis
    
   ##### 📄 Summary:
    Built a follow system using many-to-many relationships with an
    intermediary model. Created an activity stream using generic relations and
    you optimized QuerySets to retrieve related objects. Then introduced
    Django signals, and created a signal receiver function to denormalize
    related object counts. Covered application configuration classes, which used
    to load your signal handlers. Also learned how to install and configure Redis
    in Django project. Finally, used Redis in project to store item views,
    and built an image ranking with Redis.

