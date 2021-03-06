#!/usr/bin/env bash

# todo: maybe should've used fabric for deployment automation

source ./.env

function uwsgi_reload {
    ssh ${USER}@${REMOTE_HOST} -C "touch --no-dereference  ${UWSGI_RELOADER}"
}

function update_dependencies {
    ssh ${USER}@${REMOTE_HOST} -C "source ${VENV}/bin/activate;cd ${REMOTE_DIR};pip install -r requirements.txt"
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
    uwsgi_reload
else
    run_rsync
fi

