# Docker_Nao_Robot

Thanks to this project it will be possible to perfectly operate the [NAO-V5](http://doc.aldebaran.com/2-1/family/robots/dimensions_robot.html) robot from [Aldebaran], which, thanks to the Naoqi framework, can only execute commands in python2.7. This framework, deprecated in 2020 along with its python version, is not executable on new devices, even more so on devices using ARM architecture. Thanks to the creation of these two Docker containers and the development environment based on [SpecialK](https://gitlab.com/Tetsuo-tek/SpecialK.git)/[SkRobot](https://gitlab.com/Tetsuo-tek/SkRobot.git) we have managed not only to recreate a virtual Nao that perfectly integrates the SDK_naoqi_amd64 but also a development environment containing Python2.7 and pynaoqi. In the two folders naoqi_pySketch and naoqi_virtual, Docker files have been provided that emulate a Linux system with amd64 architecture. Simply build these two docker files to create a docker image that can be executed, giving life to two separate containers. Now step by step we will guide you in the creation of these two containers.

## Creation of the naoqi_virtual container

Go into the naoqi_virtual folder and execute the following command to create the image:

```bash
cd naoqi_virtual

docker buildx build --platform linux/arm64 -t nao .
```

Once the image is created, we must execute the command to create the container exposing port 9559 on which the Nao is listening, by running this command:

```bash
docker run -it --name virtual_nao -p 9559:9559 nao
```

Once this command is executed, our container will be started and our virtual Nao will be automatically executed.

## Creation of the naoqi_pySketch container

Go into the naoqi_pySketch folder and execute the following command to create the image:

```bash
docker buildx build --platform linux/arm64 -t pynaoqi .
```

Now we will proceed with the creation of the container enabling the work folder as a communication point between the host machine and the container with the command as shown below:

```bash
docker run -it --name naoqi_pySketch -v /absolute_path/work:/app pynaoqi
```

At this point, if you have followed the steps properly, everything will be ready, so we just wish you a lot of fun.
