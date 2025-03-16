FROM python:3.13.2
RUN useradd -m django_user
USER django_user
WORKDIR /app
COPY --chown=django_user . .
RUN pip install --upgrade pip
ENV PATH="/home/django_user/.local/bin:${PATH}"
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
