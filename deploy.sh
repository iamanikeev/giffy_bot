#!/usr/bin/env bash

# todo: maybe should've used fabric for deployment automation

source ./.env

function uwsgi_reload {
    ssh ${USER}@${REMOTE_HOST} -C "touch --no-dereference  ${UWSGI_CONFIG}"
}

function collectstatic {
    ssh ${USER}@${REMOTE_HOST} -C "source ${VENV}/bin/activate;cd ${REMOTE_DIR};./manage.py collectstatic -v0 --noinput"
}

function run_rsync {
    rsync -uvrz \
      --delete \
      --exclude *__pycache__ \
      --exclude deploy.sh \
      --exclude _files/ \
      --exclude .env \
      --exclude .gitignore \
      ./* ${USER}@${REMOTE_HOST}:${REMOTE_DIR}
}

if [ ${SSH_KEY} ]; then
    run_rsync -e "ssh -i ${SSH_KEY}"
    uwsgi_reload -i ${SSH_KEY}
    collectstatic -i ${SSH_KEY}
else
    run_rsync
    uwsgi_reload
    collectstatic
fi

