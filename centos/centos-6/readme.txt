yum -y install gcc libtool bison gettext make bzip2 automake gcc-c++ patch httpd-devel rpm-build
rpm -Uhv http://ftp.uni-kl.de/pub/linux/fedora-epel/6/i386/epel-release-6-8.noarch.rpm
yum -y install git-core

search on google for: rpm sqlite3 3.7 centos 6
at http://rpm.pbone.net/, you find:
ftp://ftp.pbone.net/mirror/ftp5.gwdg.de/pub/opensuse/repositories/Application:/Geo/CentOS_6/x86_64/sqlite-3.7.16-97.1.x86_64.rpm
and
ftp://ftp.pbone.net/mirror/ftp5.gwdg.de/pub/opensuse/repositories/Application:/Geo/CentOS_6/i686/sqlite-3.7.16-97.1.i686.rpm

wget, and rpm -Uhv sqlite*.rpm

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
./createsources 3.0.6
# need to modify the spec file, version and build number

rpmbuild -ba SPECS/mono-openpetra.spec
rpmbuild -ba SPECS/mod_mono-openpetra.spec

upload src and rpm packages to Sourceforge:
 sftp pokorra@frs.sourceforge.net
 cd /home/pfs/project/openpetraorg/openpetraorg/mono-openpetra/centos6
 put ...

useful git commands:
 git add .
 git diff HEAD
 git commit
 git push

