#!/bin/bash

npm install

cd static
wget https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css
wget https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js
cd ..
echo "Instalation finished, you can start the UI with: 'npm start', go to localhost:8080 on browser."

