#!/usr/bin/env bash

# exit on errors
set -e

# Script will check out the Demisto content repo and then generate documentation based upon the checkout

SCRIPT_DIR=$(dirname ${BASH_SOURCE})
CURRENT_DIR=`pwd`
if [[ "${SCRIPT_DIR}" != /* ]]; then
    SCRIPT_DIR="${CURRENT_DIR}/${SCRIPT_DIR}"
fi
CONTENT_GIT_DIR=${SCRIPT_DIR}/.content
if [[ -n "${NETLIFY}" ]]; then
    echo "Netlify env data:"
    echo "BRANCH=${BRANCH}"
    echo "HEAD=${HEAD}"
    echo "COMMIT_REF=${COMMIT_REF}"
    echo "PULL_REQUEST=${PULL_REQUEST}"
    echo "REVIEW_ID=${REVIEW_ID}"
fi
if [[ -n "${NETLIFY}" && -n "${HEAD}" ]]; then
    DOCS_BRANCH="${HEAD}"
else
    DOCS_BRANCH=$(git rev-parse --abbrev-ref HEAD)
fi

echo "==== current branch: ${DOCS_BRANCH} ===="

# Do a shallow clone to speed things up

if [ ! -d ${CONTENT_GIT_DIR} ]; then
    echo "Cloning content to dir: ${CONTENT_GIT_DIR} ..."
    git clone https://github.com/demisto/content.git ${CONTENT_GIT_DIR}
else
    echo "Content dir: ${CONTENT_GIT_DIR} exists. Skipped clone."
    if [ -z "${CONTENT_REPO_SKIP_PULL}"]; then
        echo "Doing pull..."
        (cd ${CONTENT_GIT_DIR}; git pull)
    fi
fi
cd ${CONTENT_GIT_DIR}
if [ ${DOCS_BRANCH} != "master" ] && (git branch -a | grep "remotes/origin/${DOCS_BRANCH}$"); then
    echo "found remote branch: '$DOCS_BRANCH' will use it for generating docs"
    git checkout $DOCS_BRANCH
else
    echo "Using master to generate build"
    git checkout master
fi

cd ${SCRIPT_DIR}

TARGET_DIR=${SCRIPT_DIR}/../docs/reference
echo "Deleting and creating dir: ${TARGET_DIR}"
rm -rf ${TARGET_DIR}
mkdir ${TARGET_DIR}

echo "Copying CommonServerPython.py and demistomock.py"
cp ${CONTENT_GIT_DIR}/Scripts/CommonServerPython/CommonServerPython.py .
cp ${CONTENT_GIT_DIR}/Tests/demistomock/demistomock.py .

if [ -z "${NETLIFY}" ]; then
    echo "Not running in netlify. Using pipenv"
    echo "Installing pipenv..."
    pipenv install
    echo "Generating docs..."
    pipenv run ./gendocs.py -t "${TARGET_DIR}" -d "${CONTENT_GIT_DIR}"
else
    echo "Generating docs..."
    ./gendocs.py -t "${TARGET_DIR}" -d "${CONTENT_GIT_DIR}"
fi



