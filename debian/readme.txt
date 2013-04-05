this list of instructions works for both debian and ubuntu.
it is not an automated script, I follow the instructions manually at the moment.

prepare the server for build:

apt-get update
apt-get install dh-make gcc libtool bison pkg-config libglib2.0-dev gettext make bzip2 g++ libgdiplus unzip automake autoconf apache2-prefork-dev sudo

adduser timotheusp
visudo

su - timotheusp

wget http://sourceforge.net/projects/openpetraorg/files/openpetraorg/mono-openpetra/debian-6.0/mono-openpetra-3.0.6.src.tar/download  --output-document=mono-openpetra.src.tar
tar xf mono-openpetra.src.tar

mkdir tmp
cd tmp
tar xzf ../src/debian.tar.gz
# MANUALTODO update changelog
tar czf ../src/debian.tar.gz debian
cd ..

now run the script create-mono-openpetra-deb.sh as user timotheusp:
./create-mono-openpetra-deb.sh 3.0.6 i386
or
./create-mono-openpetra-deb.sh 3.0.6 amd64
