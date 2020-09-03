#swagger_py_codegen -s ./swagger/swagger.json -p server --ui --validate  --spec  ./
name="server"
sudo chown `whoami` /var/run/docker.sock

docker run -v `pwd`:/tmp swaggerapi/swagger-codegen-cli  generate -t /tmp/swagger/template/flaskConnexion -i /tmp/swagger/swagger.json -l python-flask -o /tmp/swagger/generated -Dservice
sudo chown -R `whoami` swagger/generated
#for file in `find swagger/generated -type f `
#do
#    sed -i "s/swagger_server/$name/g" $file
#done

#mv swagger/generated/swagger_server swagger/generated/server
