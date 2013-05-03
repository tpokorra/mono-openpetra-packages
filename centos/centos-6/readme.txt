yum -y install gcc libtool bison gettext make bzip2 automake gcc-c++ patch httpd-devel rpm-build
rpm -Uhv http://ftp.uni-kl.de/pub/linux/fedora-epel/6/i386/epel-release-6-8.noarch.rpm
yum -y install git-core

adduser timotheusp
passwd timotheusp
visudo
 timotheusp ALL=(ALL)       ALL

as user timotheusp:
git config --global user.email "timotheus.pokorra@solidcharity.com"
git config --global user.name "Timotheus Pokorra"
eval $(ssh-agent -s)
ssh-add
git clone git@github.com:tpokorra/mono-openpetra-packages.git

ln -s mono-openpetra-packages/centos/centos-6 rpmbuild
wget http://sourceforge.net/projects/openpetraorg/files/openpetraorg/mono-openpetra/centos-6/mod_mono-openpetra-3.0.6-1.src.rpm/download
wget http://sourceforge.net/projects/openpetraorg/files/openpetraorg/mono-openpetra/centos-6/mono-openpetra-3.0.6-0.src.rpm/download
rpm -i *.src.rpm

cd rpmbuild
./createrelease 3.0.6
# need to modify the spec file, version and build number

rpmbuild -ba SPECS/mono-openpetra.spec
rpmbuild -ba SPECS/mod_mono-openpetra.spec

upload src and rpm packages to Sourceforge

useful git commands:
 git add .
 git diff HEAD
 git commit
 git push

