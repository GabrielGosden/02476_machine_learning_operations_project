---
layout: default
nav_exclude: true
---

# Exam template for 02476 Machine Learning Operations

This is the report template for the exam. Please only remove the text formatted as with three dashes in front and behind
like:

```--- question 1 fill here ---```

where you instead should add your answers. Any other changes may have unwanted consequences when your report is auto
generated in the end of the course. For questions where you are asked to include images, start by adding the image to
the `figures` subfolder (please only use `.png`, `.jpg` or `.jpeg`) and then add the following code in your answer:

```markdown
![my_image](figures/<image>.<extension>)
```

In addition to this markdown file, we also provide the `report.py` script that provides two utility functions:

Running:

```bash
python report.py html
```

will generate an `.html` page of your report. After deadline for answering this template, we will autoscrape
everything in this `reports` folder and then use this utility to generate an `.html` page that will be your serve
as your final handin.

Running

```bash
python report.py check
```

will check your answers in this template against the constrains listed for each question e.g. is your answer too
short, too long, have you included an image when asked to.

For both functions to work it is important that you do not rename anything. The script have two dependencies that can
be installed with `pip install click markdown`.

## Overall project checklist

The checklist is *exhaustic* which means that it includes everything that you could possible do on the project in
relation the curricilum in this course. Therefore, we do not expect at all that you have checked of all boxes at the
end of the project.

### Week 1

* [x] __Create a git repository__
* [x] __Make sure that all team members have write access to the github repository__
* [x] __Create a dedicated environment for your project to keep track of your packages__
* [x] __Create the initial file structure using cookiecutter__
* [x] __Fill out the `make_dataset.py` file such that it downloads whatever data you need__
* [x] __Add a model file and a training script and get that running__
* [x] __Remember to fill out the `requirements.txt` file with whatever dependencies that you are using__
* [ ] Remember to comply with good coding practices (`pep8`) while doing the project
* [ ] Do a bit of code typing and remember to document essential parts of your code
* [x] __Setup version control for your data or part of your data__
* [ ] __Construct one or multiple docker files for your code__
* [ ] __Build the docker files locally and make sure they work as intended__
* [ ] Write one or multiple configurations files for your experiments
* [ ] Used Hydra to load the configurations and manage your hyperparameters
* [ ] When you have something that works somewhat, remember at some point to to some profiling and see if
      you can optimize your code
* [ ] __Use Weights & Biases to log training progress and other important metrics/artifacts in your code. Additionally,__
      __consider running a hyperparameter optimization sweep.__
* [ ] Use Pytorch-lightning (if applicable) to reduce the amount of boilerplate in your code

### Week 2

* [ ] __Write unit tests related to the data part of your code__
* [ ] __Write unit tests related to model construction and or model training__
* [ ] __Calculate the coverage.__
* [ ] __Get some continuous integration running on the github repository__
* [ ] __Create a data storage in GCP Bucket for you data and preferable link this with your data version control setup__
* [ ] __Create a trigger workflow for automatically building your docker images__
* [ ] __Get your model training in GCP using either the Engine or Vertex AI__
* [ ] __Create a FastAPI application that can do inference using your model__
* [ ] If applicable, consider deploying the model locally using torchserve
* [ ] __Deploy your model in GCP using either Functions or Run as the backend__

### Week 3

* [ ] Check how robust your model is towards data drifting
* [ ] Setup monitoring for the system telemetry of your deployed model
* [ ] Setup monitoring for the performance of your deployed model
* [ ] If applicable, play around with distributed data loading
* [ ] If applicable, play around with distributed model training
* [ ] Play around with quantization, compilation and pruning for you trained models to increase inference speed

### Additional

* [ ] Revisit your initial project description. Did the project turn out as you wanted?
* [ ] Make sure all group members have a understanding about all parts of the project
* [ ] Uploaded all your code to github

## Group information

### Question 1
> **Enter the group number you signed up on <learn.inside.dtu.dk>**
>
> Answer:

We are group 'Awesome 33'. 

### Question 2
> **Enter the study number for each member in the group**
>
> Example:
>
> *sXXXXXX, sXXXXXX, sXXXXXX*
>
> Answer:

s174855, s174865, s183778, s213734


### Question 3
> **What framework did you choose to work with and did it help you complete the project?**
>
> Answer length: 100-200 words.
>
> Example:
> *We used the third-party framework ... in our project. We used functionality ... and functionality ... from the*
> *package to do ... and ... in our project*.
>
> Answer:

We chose to work with the PyTorch Image Models for doing a classification task. The simplicity of the package helped the project a lot since it can easily be installed as timm using pip. From timm we can load a wide range different deep learning architectures with pretraining. We have used resnet for this project, and fine-tuned a pre-training loaded from timm. 
A training script was not included in the installation of timm, but a clever training script using distributed training was a part of the PyTorch Image Models repository. For this project distributed training was not nessecary why we wrote our own training script using pytorch, which worked very well.

## Coding environment

> In the following section we are interested in learning more about you local development environment.

### Question 4

> **Explain how you managed dependencies in your project? Explain the process a new team member would have to go**
> **through to get an exact copy of your environment.**
>
> Answer length: 100-200 words
>
> Example:
> *We used ... for managing our dependencies. The list of dependencies was auto-generated using ... . To get a*
> *complete copy of our development enviroment, one would have to run the following commands*
>
> Answer:

For this project conda is used to manage the dependencies between all the packages installed. A common way to set up an environment like this would be to simply install the a setup.py file. This is however not nessecary for this project since all packages can be installed using pip using no other command. For generating a exact copy of our environment one only have to install the requirement.txt given in the repository. After installing conda the exact commands to do this are the following:

conda create -n <venv name>
conda activate <venv name> 

# navigate to folder with the requirements.txt 
pip install -r requirements.txt


### Question 5

> **We expect that you initialized your project using the cookiecutter template. Explain the overall structure of your**
> **code. Did you fill out every folder or only a subset?**
>
> Answer length: 100-200 words
>
> Example:
> *From the cookiecutter template we have filled out the ... , ... and ... folder. We have removed the ... folder*
> *because we did not use any ... in our project. We have added an ... folder that contains ... for running our*
> *experiments.*
> Answer:

The cookiecutter structure was used to organize our project. The structure did however not meet all of our requirements and did have a few features that was obsolete. Documentation and visualization where not a big part of this project why "docs", "notebooks" and "reference" folders where not used. 
As mentioned the setup.py file was not used either due to the simplicity of the installation. 
Instead of using the standard tox.ini file given we have chosen to run tests with pytests, which means we have added a new folder called "tests" for testing scripts that are run when typing "make tests". 
This project also involved the use of cloud and dockers why we have several dockerfiles for training and evaluating together with a yaml config file for building and pushing the docker in the cloud. 
Since our dataset was too big for github it is placed in a google cloud bucket and fetched using dvc when needed. Dvc require the .dvc folder and a .dvcignore file to work which also was added.

### Question 6

> **Did you implement any rules for code quality and format? Additionally, explain with your own words why these**
> **concepts matters in larger projects.**
>
> Answer length: 50-100 words.
>
> Answer:

Using the workflows in github the code is always run through flake8 to test it for quality. Thus every time we commit code we are told what to correct to make higher quality code. We did however not want to implement black to autoformat our code, since this sometimes leads to unwanted behaviour. An implementation of black may be much more important when working with many people since everyone have different coding style. For larger projects a precommit may also be very helpfull, but is not a big matter in our small project. 

## Version control

> In the following section we are interested in how version control was used in your project during development to
> corporate and increase the quality of your code.

### Question 7

> **How many tests did you implement and what are they testing in your code?**
>
> Answer length: 50-100 words.
>
> Example:
> *In total we have implemented X tests. Primarily we are testing ... and ... as these the most critical parts of our*
> *application but also ... .*
>
> Answer:

We used pytest to test our code using the test scripts found in the "tests" folder. We tested both the dataset, the training script and the final model. The dataset was tested for correct type and shape. The output of the final model was also tested for correct shape and type. We also ran some predictions of the model and gave a warning if the accuracy was less than 50%. 

### Question 8

> **What is the total code coverage (in percentage) of your code? If you code had an code coverage of 100% (or close**
> **to), would you still trust it to be error free? Explain you reasoning.**
>
> Answer length: 100-200 words.
>
> Example:
> *The total code coverage of code is X%, which includes all our source code. We are far from 100% coverage of our **
> *code and even if we were then...*
>
> Answer:

We have a code coverage of allmost 50%, this could be improved but we tested for the biggest and most important errors which is the most important. As mentioned in the lecture notes, there is no way to measure the quality of tests, but using the coverage packages we can atleast mensure how much of the code have been undergoing some kind of test. Therefore a 100% codecoverage doesn't mean that the code is indestructible, if the tests run are bad then a 100% coverage has no effect. 

### Question 9

> **Did you workflow include using branches and pull requests? If yes, explain how. If not, explain how branches and**
> **pull request can help improve version control.**
>
> Answer length: 100-200 words.
>
> Example:
> *We made use of both branches and PRs in our project. In our group, each member had an branch that they worked on in*
> *addition to the main branch. To merge code we ...*
>
> Answer:

Yes each member in the team has their own branch that are only merged into the main branch if all tests run are complete and if the feature implemented works perfectly. This is very important such that a minor mistake from one member would not lead to errors for every other team member. Thw workflow also ensure that a team member does not forget to test his feature properly before merging into it the main branch. The pull requst gives everyone a change to follow the changed before the final merge.

### Question 10

> **Did you use DVC for managing data in your project? If yes, then how did it improve your project to have version**
> **control of your data. If no, explain a case where it would be beneficial to have version control of your data.**
>
> Answer length: 100-200 words.
>
> Example:
> *We did make use of DVC in the following way: ... . In the end it helped us in ... for controlling ... part of our*
> *pipeline*
>
> Answer:

We have used dvc for our project to get the data from google cloud. This is a simple way for others to get the same data as we have used without any problems. This is also required if tests should be run on the dataset in the workflow before pushing. Thus each time we commit changes to our branch the workflow gets the data using dvc from google cloud. A service account was setup in google cloud to get a authorization key for github to access the data.

### Question 11

> **Discuss you continues integration setup. What kind of CI are you running (unittesting, linting, etc.)? Do you test**
> **multiple operating systems, python version etc. Do you make use of caching? Feel free to insert a link to one of**
> **your github actions workflow.**
>
> Answer length: 200-300 words.
>
> Example:
> *We have organized our CI into 3 separate files: one for doing ..., one for running ... testing and one for running*
> *... . In particular for our ..., we used ... .An example of a triggered workflow can be seen here: <weblink>*
>
> Answer:

Continues integration is very important to keep every part of the code up to date and catch potential errors. We have implemented a GitHub workflow that takes care of a wide range of problems and runs several tests on the code, data and code quality. This involves unit testing with pytest and linting with flake8, but we did not want to use black for autocorrecting code syntax. For running the tests, DVC pulls the data from a Google cloud bucket, which also required the workflow to get access to google cloud.
We did only test the code using python 3.9 and Ubuntu 2204, since we all have the same setup, but if more people involved the more systems should be included.
We also took advantage of the caching feature in our workflow due to all the dependencies that are installed each time a commit is made. This reduces the testing time significantly. The workflow can be found in our GitHub repository.
We did not want to build the docker image in GitHub since this the image is large, and it takes a long time to build. We prefer to build it in the cloud. The same goes for implementing the training of the model in the workflow. This does not make sense in our case.

## Running code and tracking experiments

> In the following section we are interested in learning more about the experimental setup for running your code and
> especially the reproducibility of your experiments.

### Question 12

> **How did you configure experiments? Did you make use of config files? Explain with coding examples of how you would**
> **run a experiment.**
>
> Answer length: 50-100 words.
>
> Example:
> *We used a simple argparser, that worked in the following way: python my_script.py --lr 1e-3 --batch_size 25*
>
> Answer:

To configure the experiments the argparser was utilized in the following way: python train_model.py --learning_rate 1e-3 --batch_size 64 --epochs 5 --model_arch resnet18 --optimizer_select Adam

The values provided in the example above represent the default values of the training script. For usabillity help messages are also provided for each argument suxh as the help for --model_arch: "Model architecture available form TIMM". 

The predict_model.py script also utilizes argparser however only with model_checkpoint and --batch_size, where the model checkpoint is the file name of the model checkpoint the predictions should be based on. 

### Question 13

> **Reproducibility of experiments are important. Related to the last question, how did you secure that no information**
> **is lost when running experiments and that your experiments are reproducible?**
>
> Answer length: 100-200 words.
>
> Example:
> *We made use of config files. Whenever an experiment is run the following happens: ... . To reproduce an experiment*
> *one would have to do ...*
>
> Answer:

To provide a clear overview of what experiments have been run and thus which configs have been used, it was selected to log key parameters of the training using Weights and Biases. Parameters saved include: Epochs, batchsize, learningrate, model architecture, optimizer, trainLoss and finally the CheckpointID. 

Weights and Biases further saves project data such as OS, python version, link to Git repository and the Git state. This means that the code used for the run is traced on Git and can be found. 

To reproduce an experiment one would have to have access to the Git and further the parameters of the run through Weights and Biases. Using the correct version of the script together with the OS & python version should make it possible to simply add the parameters to the run. All of this together provides the foundation for reproduceability.

### Question 14

> **Upload 1 to 3 screenshots that show the experiments that you have done in W&B (or another experiment tracking**
> **service of your choice). This may include loss graphs, logged images, hyperparameter sweeps etc. You can take**
> **inspiration from [this figure](figures/wandb.png). Explain what metrics you are tracking and why they are**
> **important.**
>
> Answer length: 200-300 words + 1 to 3 screenshots.
>
> Example:
> *As seen in the first image when have tracked ... and ... which both inform us about ... in our experiments.*
> *As seen in the second image we are also tracking ... and ...*
>
> Answer:

![container registry](/reports/figures/GCP_bucket.png)
![container registry](/reports/figures/GCP_bucket.png)
![container registry](/reports/figures/GCP_bucket.png)

### Question 15

> **Docker is an important tool for creating containerized applications. Explain how you used docker in your**
> **experiments? Include how you would run your docker images and include a link to one of your docker files.**
>
> Answer length: 100-200 words.
>
> Example:
> *For our project we developed several images: one for training, inference and deployment. For example to run the*
> *training docker image: `docker run trainer:latest lr=1e-3 batch_size=64`. Link to docker file: <weblink>*
>
> Answer:

Docker was used to implemented to ensure good reproducibility and easy training in the cloud. Google cloud has a great way of building docker and handling docker images. Docker images can however become quite large, why we have individual images for different tasks like training and predicting to minimize the amount of packages needed to install. Docker images are created using cloud build in google cloud on trigger when a push is made to the main branch. The operation requires a cloud.yml file that tells us to build and push the docker image, the building of the docker image is specified by the docker file. When an image is successfully built, it can be found under container registry in the cloud ready for training. Training can happen both in the cloud or locally, if we want to run it locally we need to fetch the docker image from the cloud and into docker. When the image can be found by docker (docker images) it can be run using the following command "docker run --name <name> <repository>:<tag>"
The link to one of our docker files can be found in our GitHub https://github.com/GabrielGosden/02476_machine_learning_operations_project/blob/main/trainer.dockerfile

### Question 16

> **When running into bugs while trying to run your experiments, how did you perform debugging? Additionally, did you**
> **try to profile your code or do you think it is already perfect?**
>
> Answer length: 100-200 words.
>
> Example:
> *Debugging method was dependent on group member. Some just used ... and others used ... . We did a single profiling*
> *run of our main code at some point that showed ...*
>
> Answer:

Debugging is subjective and thus the preferred method varied from group member to group member. In general the first step is always to look at the error messages of the run which often provides enough information for a quick fix such as "x package not installed" which is then easily fixed by pip install x. 

In more complex error settings the print function is often utilized as this first of all can show if the code reaches the print statement of if it crashes before this e.g. "Now I'm here!". Once the problem is narrowed down to maybe a single function call the print function can be used to show the input(s) to the function, both in terms of value but also type and dimensions.

We in NO WAY consider out code to be perfect, but rather accept that it is working and thus fulfills the purpose of the scope of this project. We have not profiled our code as the dataset used is only around 500 images, meaning that 5 epochs of training took minutes even on CPU. We did therefore not see a need for optimizing the code using profiling and instead focused on the cloud integration. 

## Working in the cloud

> In the following section we would like to know more about your experience when developing in the cloud.

### Question 17

> **List all the GCP services that you made use of in your project and shortly explain what each service does?**
>
> Answer length: 50-200 words.
>
> Example:
> *We used the following two services: Engine and Bucket. Engine is used for... and Bucket is used for...*
>
> Answer:
We have used buckets for cloud storage. This allows us to get access to our data in the cloud with our any authorization as long as we use the data is used within the same project.
Compute engine to set up a virtual machine (VM) for doing actual computations.
Triggers to trigger a docker image build each time code is pushed to main branch.
Cloud build for build images, and cloud registry for storing images.
vm instance for training??

### Question 18

> **The backbone of GCP is the Compute engine. Explained how you made use of this service and what type of VMs**
> **you used?**
>
> Answer length: 100-200 words.
>
> Example:
> *We used the compute engine to run our ... . We used instances with the following hardware: ... and we started the*
> *using a custom container: ...*
>
> Answer:

The compute engine ran most of our script, it builds the docker image and trains our algorithm. This means that we don't have to wait for the jobs to complete before we can use our own computer, since the cloud can handle several jobs at the same time.
Since our training task was not too big and since we wanted to ensure that we have enough credits for the whole course, we used a VM with a CPU. It has a storage of10 GB which was enough for our project.


### Question 19

> **Insert 1-2 images of your GCP bucket, such that we can see what data you have stored in it.**
> **You can take inspiration from [this figure](figures/bucket.png).**
>
> Answer:

![container registry](/reports/figures/GCP_bucket.png)
      
--- question 19 fill here ---

### Question 20

> **Upload one image of your GCP container registry, such that we can see the different images that you have stored.**
> **You can take inspiration from [this figure](figures/registry.png).**
>
> Answer:
![container registry](/reports/figures/container_registry1.png)


### Question 21

> **Upload one image of your GCP cloud build history, so we can see the history of the images that have been build in**
> **your project. You can take inspiration from [this figure](figures/build.png).**
>
> Answer:

![container registry](/reports/figures/cloud_build.png)

### Question 22

> **Did you manage to deploy your model, either in locally or cloud? If not, describe why. If yes, describe how and**
> **preferably how you invoke your deployed service?**
>
> Answer length: 100-200 words.
>
> Example:
> *For deployment we wrapped our model into application using ... . We first tried locally serving the model, which*
> *worked. Afterwards we deployed it in the cloud, using ... . To invoke the service an user would call*
> *`curl -X POST -F "file=@file.json"<weburl>`*
>
> Answer:

did we manage to deploy or model

### Question 23

> **Did you manage to implement monitoring of your deployed model? If yes, explain how it works. If not, explain how**
> **monitoring would help the longevity of your application.**
>
> Answer length: 100-200 words.
>
> Example:
> *We did not manage to implement monitoring. We would like to have monitoring implemented such that over time we could*
> *measure ... and ... that would inform us about this ... behaviour of our application.*
>
> Answer:

Monitoring is a big and important topic. Especially, data drifting should be monitored closely. We did not do this for our project, but it would have been a nice feature, since new hot dogs come up every day that may not be in the dataset. This ensures that we will get notified if our application gets outdated, and thus keep its relevance for a longer time.
System monitoring should be used when the number of requests on an application is high, since we do not expect a lot of people using this application (because people in general know what they are eating), we have left system monitoring out.

### Question 24

> **How many credits did you end up using during the project and what service was most expensive?**
>
> Answer length: 25-100 words.
>
> Example:
> *Group member 1 used ..., Group member 2 used ..., in total ... credits was spend during development. The service*
> *costing the most was ... due to ...*
>
> Answer:
The cost of this project was very minimal with the use of a VM with a CPU. The total cost landed at ...
The most expensive service was the VM, but even that was very cheap.

## Overall discussion of project

> In the following section we would like you to think about the general structure of your project.

### Question 25

> **Include a figure that describes the overall architecture of your system and what services that you make use of.**
> **You can take inspiration from [this figure](figures/overview.png). Additionally in your own words, explain the**
> **overall steps in figure.**
>
> Answer length: 200-400 words
>
> Example:
>
> *The starting point of the diagram is our local setup, where we integrated ... and ... and ... into our code.*
> *Whenever we commit code and puch to github, it auto triggers ... and ... . From there the diagram shows ...*
>
> Answer:

--- question 25 fill here ---

### Question 26

> **Discuss the overall struggles of the project. Where did you spend most time and what did you do to overcome these**
> **challenges?**
>
> Answer length: 200-400 words.
>
> Example:
> *The biggest challenges in the project was using ... tool to do ... . The reason for this was ...*
>
> Answer:

A project like this always causes struggles, most of the time goes with investigating problems instead of actually coding.
The biggest challenge was figuring out how the cloud works, it has so many features and different ways to do the same things. In biggest challenge in the cloud was figuring out how the trainings script should get access to the dataset. There are several ways to train a docker image in the cloud and more ways to include the dataset. The authorization process between GitHub and the cloud also caused some trouble. Most of the remaining tasks was aldready done earlier in the exercises, why these did not cause very much trouble.
We mostly used Google to figure out how to solve these problems, but the Slack channel also had a few answers to our questions. The course is also very well documented why we started reading the lecture text before moving on to other services.

### Question 27

> **State the individual contributions of each team member. This is required information from DTU, because we need to**
> **make sure all members contributed actively to the project**
>
> Answer length: 50-200 words.
>
> Example:
> *Student sXXXXXX was in charge of developing of setting up the initial cookie cutter project and developing of the*
> *docker containers for training our applications.*
> *Student sXXXXXX was in charge of training our models in the cloud and deploying them afterwards.*
> *All members contributed to code by...*
>
> Answer:

Gabriel (s..) set up our GitHub with the cookiecutter structure. He also set up the DVC and cloud services
Mads (s...) set up the docker file and added configuration to the code. He also set up the DVC and cloud services and wrote a part of the report.
Cseke (s...) helped with the Google cloud setup and deployed our model in the cloud using fastAPI
Tore (s183778) handled the GitHub workflow with CI tests, cache, DVC pull and google authorization to test data. And wrote a part of the report.
