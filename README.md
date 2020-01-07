# Full-Featured Blogging Website | Python Django

This is a full-featured blog that was made using Python Django on a Model-View-Template architecture.

Features include:
- User creation, login, and authentication
- User profile pictures
- Ability to update username, user emails, and user profile pictures
- Creating, updating, and deleting blog posts
- Viewing blog posts made by specific users and self
- Use of Amazon S3 for image uploads for profile pictures

# To Run
To run this, you will have to have Python 3.7, Django and associated libraries installed.
1) Clone the repo to a local repo
2) Create your own AWS S3 Bucket 
3) Store your AWS Keys as OS environment variables in ./bash_profile
4) Set your AWS Keys to the keys pointed to by your OS environment variables
   AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
   AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
   AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
5) In the "edward_yuen_blog" directory, type "python3 manage.py runserver" to run
