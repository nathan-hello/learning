#!/bin/bash
# http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail
IFS=$'\n\t'

BASE_URL="http://localhost:3000"


# -s = cURL doesn't show progress bar
# -o /dev/null = send output to null except...
# -w "%{http_code}" = ...for http_code 


index_get() {
  echo index_get $(curl \
  -s \
  -o /dev/null \
  -w "%{http_code}" \
  ${BASE_URL} \
  )
}


posts_get() {
  echo posts_get $(curl \
  -s \
  -o /dev/null \
  -w "%{http_code}" \
  ${BASE_URL}/posts \
  )
}

posts_post() {
  echo posts_post $(curl \
  -s \
  --header "Content-Type: application/json" \
  --request POST \
  --data '{"author":"steve","content":"minecraft tutorial", "title": "how to"}' \
  -o /dev/null \
  -w "%{http_code}" \
  ${BASE_URL}/posts \
  )
}


index_get
posts_get
posts_post