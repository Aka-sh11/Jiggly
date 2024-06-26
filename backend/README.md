# backend

 It is a simple REST API for a Jiggly Music App. It allows to play songs, manage albums, playlist and users. It is written in Python using Flask framework and SQLAlchemy ORM. It uses JWT for authentication and authorization. It also uses celery and redis for asynchronous tasks.


## Installation

1. Clone the repository and enter it

    ```
    git clone
    cd backend
    ```

2. Create virtual environment and activate it

    ```
    python -m venv myenv
    source myenv/bin/activate
   ```

4. Install dependencies

    ```
    pip install -r requirements.txt
    ```

5. Start redis server

    ```
    redis-server
    ```
    
6. Start MailHog

   ```
   ~/go/bin/MailHog
   ```
   
7. Start celery worker and beat

    ```
    celery -A main.celery_app worker --loglevel=info -B
    ```

8. Run the application

    ```
    python main.py
    ```
    
    It is advised to run a listener on smtp port 8025 to see the emails sent by the application. Otherwise you may face some errors.
