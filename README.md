Testing the FCGF docker file with enabled ssh connection

how to run:

clone this repo:
  $ git clone REPO

Build image: 
  $ docker build --tag IMAGE_NAME:VERSION --file docker/Dockerfile .

Run the docker in the background:
  $ docker run -d -P --name CONTAINER_NAME IMAGE_NAME:VERSION
 
Check port:
  $ docker port CONTAINER_NAME 
  
  this gives out x.x.x.x:PORT
  
ssh to the root:
  $ ssh -p PORT root@x.x.x.x
  
set-up new password for root and for the non-root user named srs:
  $ passwd root
  $ passwd srs
  
  the ssh configurations are done.
  give only the password for the non-root user to others.

Connect to the non-root user:
  $ ssh -p PORT srs@x.x.x.x
  
  done using the ssh: type "exit"
  
when done using the container:
  $ docker container stop CONTAINER_NAME
  
Do not delete the IMAGE since this will delete all the ssh configuration.

Next step: apply the FastAPI
  
