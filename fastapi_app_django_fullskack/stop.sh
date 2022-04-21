#!/bin/bash

if [ -e gunicorn.pid ]; then
    kill -TERM `cat gunicorn.pid`
fi
exit 0
