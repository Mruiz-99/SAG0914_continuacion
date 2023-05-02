#!/bin/sh

echo "START BUILD IMAGES"
cp $ENV_PROD_BACK_FILE .env
cp $ENV_PROD_BACK_FILE .env.prod
ls -la
docker-compose --env-file=.env build --no-cache
echo "END BUILD IMAGES"
