API service for loading images into a database with subsequent processing using the Pillow library .

The service is ready to go, it remains only

**Clone the repository and go into it**  
git clone https://github.com/Tisot-studio/image_api.git  
cd image_api

**Create a virtual environment and run it, for example:**  
py -m venv testenv  
testenv\Scripts\activate

**Install all required packages:**  
pip install -r requirements.txt  

**Start server**  
py manage.py runserver  

**Now you can create requests through Postman! :)**  

**(GET) Get a list of all images**     
http://localhost:8000/api/images/  

**(GET) Get an image by its id**   
http://localhost:8000/api/images/1/  

**(POST) Upload image (file/url) to database**    
http://localhost:8000/api/images/  

**(POST) Resize a specific image (specify id). In the form, specify KEY: width and height VALUE: 500 and 600 (for example)**  
http://localhost:8000/api/images/1/resize/  

**(DELETE) Delete image (specify id)**    
http://localhost:8000/api/images/13/  
