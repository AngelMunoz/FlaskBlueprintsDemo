# Hello everyone!
This is a flask application using blueprints.
Blueprints are really good when one of the concerns is scalable apps.
each "blueprint" is what we could call a module, the application here is composed of two modules
`auth` and `admin` as the names suggest, auth is the module in charge of authentication and user session and allowing
where can users go or can not.

admin is a module that emulates a very simple administration website

the website is composed of a user who has a company and said company may have many subsidiaries, each subsidiary may have several employees.

while is not such a complex scenario, it shows you some concepts of the modern web development.

the application logic is a MVC workflow structure
where each module has its own controller and its own views, however the models work for the whole application.
each module will contain its own readme file explaining what is done there.

Have a nice day! oh by the way! this app is hosted in Heroku (thank you continuous deployment!)
which picks the files in github and serves them and updates as soon as the repository is updated.
