# First

sam deploy --guided --profile user_test


# DEPLOY
sam build --use-container


sam deploy --profile user_test --config-env develop

# Docker:


#1- aws ecr-public get-login-password --region us-east-1 --profile user_test | docker login --username AWS --password-stdin public.ecr.aws


#2- docker build -t dependencies-project .



aws ecr-public get-login-password --region us-east-1 --profile user_test | docker login --username AWS --password $(aws ecr-public get-login-password --region us-east-1 --profile user_test) public.ecr.aws

#3- docker tag dependencies-project:latest public.ecr.aws/f0a7l5k8/dependencies_docker

#4- docker push public.ecr.aws/f0a7l5k8/dependencies_docker

#Ejecutar en local:

sam local start-api --invoke-image public.ecr.aws/f0a7l5k8/dependencies_docker





Comandos de envío para dependencies_docker

Asegúrese de tener instalada la versión más reciente de AWS CLI y Docker. Para obtener más información, consulte Empezar a utilizar Amazon ECR .
Siga los siguientes pasos a fin de autenticar y enviar una imagen a su repositorio. Para obtener métodos de autenticación de registro adicionales, incluido el ayudante de credenciales de Amazon ECR, consulte Autenticación del registro .
Recupere un token de autenticación y autentique su cliente de Docker en el registro.
Utilice AWS CLI:

aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/f0a7l5k8
Nota: Si recibe un error al utilizar AWS CLI, asegúrese de tener instaladas las últimas versiones de AWS CLI y Docker.
Cree una imagen de Docker con el siguiente comando. Para obtener información sobre cómo crear un archivo de Docker desde cero, consulte las instrucciones aquí . Puede omitir este paso si ya se creó la imagen:

docker build -t dependencies_docker .
Cuando se complete la creación, etiquete la imagen para poder enviarla a este repositorio:

docker tag dependencies_docker:latest public.ecr.aws/f0a7l5k8/dependencies_docker:latest
Ejecute el siguiente comando para enviar esta imagen al repositorio de AWS recién creado:

docker push public.ecr.aws/f0a7l5k8/dependencies_docker:latest


https://gallery.ecr.aws/sam/build-python3.9  








https://github.com/Rojas-Andres/aws-lambda-python-cloudformation/blob/master/modules/users/lib_users/database.py



create table usuarios(id serial, nombre varchar(250), apellido varchar(250), ciudad varchar(250));
