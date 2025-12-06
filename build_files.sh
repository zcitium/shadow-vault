pip install -r requirements.txt
mkdir -p staticfiles_build # Ensure directory exists
python3.9 manage.py collectstatic --noinput
# python3.9 manage.py migrate # Not needed for stateless app
