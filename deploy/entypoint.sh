#!/bin/sh
gunicorn --reload \
    --access-logfile access.log \
    --error-logfile error.log \
    --workers=1 --bind=0.0.0.0:$PORT app:app