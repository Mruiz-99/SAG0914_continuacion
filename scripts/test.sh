#!/bin/sh

echo "START TEST"

runFrontTest() {
  echo "|============== test front ==============|"
  cd ui
  yarn install
  ls -l
  yarn run test
}

runBackTest() {
  PROJECT_DIR=$(pwd)
  TEST_DIRS="api/UploaderService/upload api/NotificationService/email api/userservice api/inventario api/InterconnectivityService/RegistroCompraExterna api/InterconnectivityService/RecepcionProductosExternos"
  echo "|============== test back ==============|"
  echo $PROJECT_DIR
  cp $ENV_DEV_BACK_FILE ./.env

  for d in $TEST_DIRS
  do
    echo $d
    cd $d
    ls -l
    if [ -f requirements.dev.txt ]; then
      python -m pip install -r requirements.dev.txt
    elif [ -f requirements.txt ]; then
      python -m pip install -r requirements.txt
    else
     continue
    fi
    echo ">>> run test $d <<<"
    python -m pytest -v
    cd $PROJECT_DIR
  done
}

if [[ $1 == "front" ]]; then
  runFrontTest
elif [[ $1 == "back" ]]; then
  runBackTest
fi

echo "END TEST"
