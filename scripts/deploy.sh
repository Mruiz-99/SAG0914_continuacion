#!/bin/sh

removeNoneImages() {
  echo "START TO REMOVE <NONE IMAGES>"
  docker images -f "dangling=true" -q | xargs docker rmi
  echo "END TO REMOVE <NONE IMAGES>"
}

echo "START DEPLOY"
cp $ENV_PROD_BACK_FILE .env.prod
ls -la
docker-compose down --rmi local
docker-compose --env-file=.env.prod up -d
removeNoneImages

echo "END DEPLOY"
