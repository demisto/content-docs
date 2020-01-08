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
    echo "DEPLOY_PRIME_URL=${DEPLOY_PRIME_URL}"
    echo "DEPLOY_URL=${DEPLOY_URL}"
fi
if [[ -n "${NETLIFY}" && -n "${HEAD}" ]]; then
    CURRENT_BRANCH="${HEAD}"
else
    CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
fi

echo "==== current branch: ${CURRENT_BRANCH} ===="

CONTENT_GIT_URL="https://github.com/demisto/content.git"
CONTENT_BRANCH="${CURRENT_BRANCH}"
REQUIRE_BRANCH=false
if [ -n "${INCOMING_HOOK_BODY}" ]; then
    echo "INCOMING_HOOK_BODY=${INCOMING_HOOK_BODY}"
    INCOMING_HOOK_JSON=$(echo "${INCOMING_HOOK_BODY}" | python3 -c "import sys, urllib.parse as p; print(p.unquote(sys.stdin.read()));")
    hook_url=$(echo "${INCOMING_HOOK_JSON}" | jq -r .giturl)
    if [[ -n "${hook_url}" && "${hook_url}" != "null" ]]; then
        CONTENT_GIT_URL="${hook_url}"
    fi
    hook_branch=$(echo "${INCOMING_HOOK_JSON}" | jq -r .branch)
    if [[ -n "${hook_branch}" && "${hook_branch}" != "null" ]]; then
        CONTENT_BRANCH="${hook_branch}"
        REQUIRE_BRANCH=true
    fi    
fi

# Do a shallow clone to speed things up

if [ ! -d ${CONTENT_GIT_DIR} ]; then
    echo "Cloning content to dir: ${CONTENT_GIT_DIR} ..."
    git clone ${CONTENT_GIT_URL} ${CONTENT_GIT_DIR}
else
    echo "Content dir: ${CONTENT_GIT_DIR} exists. Skipped clone."
    if [ -z "${CONTENT_REPO_SKIP_PULL}"]; then
        echo "Doing pull..."
        (cd ${CONTENT_GIT_DIR}; git pull)
    fi
fi
cd ${CONTENT_GIT_DIR}
if [ ${CONTENT_BRANCH} != "master" ] && (git branch -a | grep "remotes/origin/${CONTENT_BRANCH}$"); then
    echo "found remote branch: '$CONTENT_BRANCH' will use it for generating docs"
    git checkout $CONTENT_BRANCH
else
    if [[ "${REQUIRE_BRANCH}" == "true" ]]; then
        echo "ERROR: couldn't find $CONTENT_BRANCH on remote. Aborting..."
        exit 2
    fi
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



