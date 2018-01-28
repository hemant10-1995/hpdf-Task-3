# Hasura-Product-development-Fellowship
# hpdf-Task-3/Hemant-Kumar
HPDF group Task-3 contains the Natural Language Analysis


follow this instruction to run this code on your local machine

1. Install python 3.6.3 on your machine from https://www.python.org/downloads/

2. Then go to the root folder of python in your mahine and copy path like below:
   for me it is look like  C:\Users\HEMANT-PC\AppData\Local\Programs\Python\Python36-32\Scripts(In windows system,Folder AppData remains hidden hence enable show hidden file)

3. Go to Control Panel>System>Advanced system settings>Advanced. Click on Environment variables>Path(system variables)>Edit>New>then paste the  path which is previously copied . for me which is " C:\Users\HEMANT-PC\AppData\Local\Programs\Python\Python36-32\Scripts" >then >Ok>Ok>Ok(three times OK)

4. Go to command prompt Now first we will install Virtual Environment. Type -> pip install virtualenv

5. The Environment is ready Now. We will go to any disk in which we want to create our project. 
  For ex.C:\Users\HEMANT-PC>mkdir myproject
         C:\Users\HEMANT-PC>cd myproject

6. C:\Users\HEMANT-PC\myproject>pip install virtualenv ,then type->pip install flask 
         i.e C:\Users\HEMANT-PC\myproject>pip install flask , now Installing setuptools,pip,wheel is done.

7. Go to  C:\Users\HEMANT-PC\myproject>cd flask\scripts  and type-> pip install flask, i.e Now our flask package is installed.
       i.ee: C:\Users\HEMANT-PC\myproject\flask\Scripts>pip install flask

8. Go to this directory \flask\scripts ,
    i.e C:\Users\HEMANT-PC\myproject>cd flask\Scripts 
     and type-> activate ,Flask is activated.
    i.e C:\Users\HEMANT-PC\myproject\flask\Scripts>activate 

9. Go to the folder where you have downloaded and saved your python file and navigate to that directoy :
  i.e  C:\Users\HEMANT-PC\myproject\flask\Scripts\hpdf-Task-3\watson> and Type-> pip install --upgrade watson-developer-cloud after that
  Type-> python run.py and your local server is activated now.
   * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 146-942-009
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

10.You can also use git clone method to clone your repository 
   i.e C:\Users\HEMANT-PC\myproject\flask\Scripts>git clone https://github.com/hemant10-1995/hpdf-Task-3.git
   then navigate the directory structure like this and run following below command
   (flask) C:\Users\HEMANT-PC\myproject\flask\Scripts\hpdf-Task-3\watson>python run.py
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 146-942-009
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

10. Go to your Favourite Browser and copy/type the link as shown in command prompt.(Not Necessarily localhost:5000 always)

Some sample Images are :
This page for input

![o1](https://user-images.githubusercontent.com/31190062/35481935-62beb876-0453-11e8-9b98-6505c17a921c.png)


This page having analyzed in JSON format:
![o2](https://user-images.githubusercontent.com/31190062/35481936-6330e22a-0453-11e8-84ba-84fafdf795a6.png)


Continue:
![o3](https://user-images.githubusercontent.com/31190062/35481937-63757ed0-0453-11e8-8976-8199d6ab61e0.png)

