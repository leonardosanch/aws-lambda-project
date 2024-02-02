FROM public.ecr.aws/sam/build-python3.9

COPY ./modules/users/requirements.txt ./modules/users/requirements.txt

RUN pip install -r ./modules/users/requirements.txt
