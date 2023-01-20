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
* [x] __Construct one or multiple docker files for your code__
* [x] __Build the docker files locally and make sure they work as intended__
* [ ] Write one or multiple configurations files for your experiments
* [ ] Used Hydra to load the configurations and manage your hyperparameters
* [ ] When you have something that works somewhat, remember at some point to to some profiling and see if
      you can optimize your code
* [x] __Use Weights & Biases to log training progress and other important metrics/artifacts in your code. Additionally,__
      __consider running a hyperparameter optimization sweep.__
* [ ] Use Pytorch-lightning (if applicable) to reduce the amount of boilerplate in your code

### Week 2

* [x] __Write unit tests related to the data part of your code__
* [x] __Write unit tests related to model construction and or model training__
* [x] __Calculate the coverage.__
* [x] __Get some continuous integration running on the github repository__
* [x] __Create a data storage in GCP Bucket for you data and preferable link this with your data version control setup__
* [x] __Create a trigger workflow for automatically building your docker images__
* [x] __Get your model training in GCP using either the Engine or Vertex AI__
* [x] __Create a FastAPI application that can do inference using your model__
* [ ] If applicable, consider deploying the model locally using torchserve
* [x] __Deploy your model in GCP using either Functions or Run as the backend__

### Week 3

* [ ] Check how robust your model is towards data drifting
* [x] Setup monitoring for the system telemetry of your deployed model
* [x] Setup monitoring for the performance of your deployed model
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

We chose to work with PyTorch Image Models for our classification task. The simplicity of the package made the setting up of the model incredibly simple. The library can easily be installed as timm using pip and it contains a wide range of different deep learning architectures with pretrained weights available. We have used resnet18 for this project and fine-tuned it on our own dataset.
The example training script for timm is very robust and lengthy, and while it is useful for setting up distributed training, the script was a bit overkill for us. Thus we wrote our own much simpler training script based on our pytorch knowledge.

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

For this project conda is used to manage the dependencies between all the packages installed. A common way to set up an environment like this would be to simply install a setup.py file. This is however not nessecary for this project since all packages can be installed using pip using no other command. For generating a exact copy of our environment one only have to install the requirement.txt given in the repository. After installing conda the exact commands to do this are the following:

conda create -n <venv name>
conda activate <venv name> 

Then navigate to folder with the requirements.txt 
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

The cookiecutter structure was used to organize our project. The structure did however not meet all of our requirements and did have a few features that was obsolete. Documentation and visualization were not a big part of this project so in the end "docs", "notebooks" and "reference" folders were not used. 
As mentioned the setup.py file was not used either due to the simplicity of the installation. 
We did not see the need to set up tox to have our pytests checked against multiple environments as we were working with fixed setups and the main goal was to have our final trained model in a container hosted on Cloud Run.
The project involved the use of cloud and docker. We made seperate dockerfiles for training and evaluating the model and for the final fastapi application, together with a yaml config file for building and pushing the docker in the cloud. 
Our dataset is stored both in a Cloud Storage Bucket, and on Google drive for both of which we have used dvc to manage. For this reason the github repository also includes dvc related config and info files.

### Question 6

> **Did you implement any rules for code quality and format? Additionally, explain with your own words why these**
> **concepts matters in larger projects.**
>
> Answer length: 50-100 words.
>
> Answer:

Workflows in github run the code through flake8 to test it for quality. Thus every time we commit code we are told what to correct to achieve higher quality code. We did however not use black to autoformat our code, since this sometimes leads to unwanted behaviour. The use of these tools may be much more important when working with many people since everyone have different coding style and with extensive codebase small formating issues can add up quickly and result in hardly readable code. In larger projects precommits are very helpfull, but are not needed in our small project. 

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

We have a code coverage of almost 50%, this could of course be improved but we have instead tested for the biggest and most important errors which is the most important. As mentioned in the lecture notes, there is no way to measure the quality of tests, but using the coverage packages we can atleast measure how much of the code have been covered by our tests. Therefore a 100% code coverage doesn't mean that the code is indestructible, even if the tests involve 100% of the code it doesn't necessarily mean that they wrap all edge-cases and functionality gaps as well. 

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

Yes each member in the team had their own branches for each bigger change that they were working on, which were only merged into the main branch if all tests run were complete and if the feature implemented worked as intended. This is very important such that a minor mistake from one member would not lead to errors for every other team member. This workflow ensures that a team member does not forget to test his feature properly before merging into it the main branch. The pull requests gave everyone a chance to review the changes before the final merge. In some cases we had to make modifications directly to main due to conflicts and git issues, but we tried to follow this principle as much as we could.

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

We have used dvc in out project to version controll the dataset. DVC was configured to store our data in Cloud Storage buckets and on Google Drive. This was a simple way to share the data and have it always up to date for everyone. We also integrated dvc into our Github Action workflows so that we can run checks directly against our data as well. Thus each time we commit changes to our branch the workflow gets the data using dvc from google cloud. A service account was setup in google cloud to have access to the data stored in the buckets.

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

![wandb](/reports/figures/wandb_ss.png)
![wandb](/reports/figures/wandb_ss_2.png)
![wandb](/reports/figures/wandb_ss_3.png)

As seen in the first image when have tracked the training loss which both inform us about if the model is converging in our experiments.
As seen in the second image we are also tracking batch size, epochs, learning rate, model architecture, optimizer, checkpoint ID, total trained epochs and the final training loss
As seen in the third image the predictin accuracy on the test set is displayed. 

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
- Gcloud bucket allow us to get access to our data in the cloud with our any authorization as long as we use the data is used within the same project.
- Gcloud Compute Engine to set up a virtual machine (VM) for doing training.
- Gcloud Triggers to trigger a docker image build each time code is pushed to main branch.
- GCloud build for building docker images.
- Gcloud Registry for storing images.
- Gcloud Run for running our model.

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

We used the compute engine to run our model training. It loads the docker container from the container registry were it was pushed from gcloud build where the container was build triggered by a push to github. The VM was configured to run the docker container on boot using the entrypoint defined in the dockerfile. 
We used instances placed in europe-central2-a with the following hardware: e2-medium, Intel Broadwell, 10 gb storage and we started the using a custom container: trainer_new:latest. Since our training task was not too big and since we wanted to ensure that we have enough credits for the whole course, we used a the compute engine with a CPU. 

### Question 19

> **Insert 1-2 images of your GCP bucket, such that we can see what data you have stored in it.**
> **You can take inspiration from [this figure](figures/bucket.png).**
>
> Answer:

![cloud bucket](/reports/figures/gcloud_bucket.png)
      
In our bucket we have stored several different files.
- model/ contains the .pth files created from training our model. This is loaded when using the fastAPI to evaluate a new image using the model
- processed/ contains the .pt files for the traning and testing of the model
- raw/ contains the raw image files as .jpg file

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

![cloud build](/reports/figures/cloud_build.png)

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

We did manage to deplay our model to the cloud. The goal was to input an image in the api and make google cloud run our model to make the prediction. For this we used google run to get the model from a docker file. The api implemented was the fastapi.  
Cloud run was configured to grab the latest image available in the conatiner registry, meaning that it will update once a new image is pushed to the registry. The fastapi container then grabs the newest model directly from the bucket and thus everything should be up to date as the latest version of everything.
      

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
The cost of this project was very minimal with the use of a VM with a CPU and a little dataset. The total cost landed at 1.15 dollars.
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

The user have 3 options to train or evaluate or code. 
      
1) Clone the github repository on your local computer. If the same dataset is used it can get pulled from a google bucket using dvc. This require some experience with python and make files to work. Also the environment has to be set up properly with our requirement file. 
      
2) The second option is to download the docker image such that one does not need the specific system requirements or worry about dependencies gone wrong. This is a very stable approach that ensure no dependencies problems, but the user still needs to have some knowledge about the code. One also still have to run the training locally, which is a problem when computer capasity is limited. As seen in the image the docker files are stored in the container registry in google cloud, and each time we push to the main branch a trigger ensures that a new docker image is build and pushed to the container registry such that the newest version is always reachable. For plotting the wandb is used. 
      
3) The third option is to do predictions using an api. The api is set up in the cloud such that one is able to run the model without worrying about any dependencies or having to look at the code. This is the most simple approach for the user, but takes some time to set up. The predictions is made in a vm using google run.

![diagram](/reports/figures/overviewv2.png)

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

The biggest challenge was figuring out how the cloud works, it has so many features and different ways to do the same things. The biggest challenge in the cloud was figuring out how the trainings script should get access to the dataset. There are several ways to train a docker image in the cloud and more ways to include the dataset. To make the api run on cloud was also very difficult. The authorization process between GitHub and the cloud also caused some trouble. Most of the remaining tasks was aldready done earlier in the exercises, why these did not cause very much trouble. In general the most challeging part was the frustration from waiting! Everytime a new version was pushed it took around 20 minutes before a new container was built, and then it could be tested. So it was debugging with 20 minute delays between each 'fix'... But once it worked, the satisfaction was enormous!
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

Gabriel (s174865) set up our GitHub with the cookiecutter structure. He also set up the DVC, cloud services and deployed our model in the cloud using fastAPI. Worked with the script for training the data and also setting up the training using the Cloud Engine.
      
Mads (s174855) set up the docker file and added configuration to the code. He also set up the DVC, cloud services, wrote a part of the report and deployed our model in the cloud using fastAPI. Creating the script for processing the raw data.
      
Cseke (s213734) helped with the Google cloud setup and deploying our model in the cloud using fastAPI, setting up DVC with Cloud Storage.
      
Tore (s183778) handled the GitHub workflow with CI tests, cache, DVC pull and google authorization to test data. And wrote a part of the report.
