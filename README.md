# UbuntuServer-GPIORaspberryPI4
Gestión remota de los GPIO de una Raspberry PI 4 a traves de comunicacion SSH desde un Ubuntu Server.

Cada uno de los archivos .sh y los .txt tanto en el Ubuntu Server y en la Raspberry se les debe otorgar permisos de accesos a traves del comando:

chmod -R 777 archivo.sh{txt}

Adicionalmente es necesario que exista comunicacion entre el Ubuntu Server y el microprocesador (Raspberry) a traves de SSH.
