FROM public.ecr.aws/lambda/python:3.10

# Install necessary packages
RUN yum -y install java-1.8.0-openjdk-devel gcc python3-devel

# Install konlpy
RUN pip3 install konlpy scikit-learn

# Copy function code
COPY lambda_function.py ${LAMBDA_TASK_ROOT}

# Overwrite the command by providing a different command directly in the template.
CMD ["lambda_function.lambda_handler"]
