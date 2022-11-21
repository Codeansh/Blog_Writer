# My Flask Blog

Create and upload posts , follow your favourite writers and manage your profile. 

## Run Locally ( On Linux )

####  Clone the project
> ```  https://github.com/Codeansh/My_Blog.git```

#### Create a virtual environment. ( if using linux then use)
> ``` python3 -m venv venv ```

#### Activate virtual environment
> ``` source venv/bin/activate ```


#### Run the script in terminal ( Docker should be installed )

> ``` docker build -t myblog  . ```<br>
> ``` docker run -it -d -p 8000:8000  myblog:latest```



#### Open your browser and type the url : http://localhost:8000/

##### It will redirect to login page like this 
