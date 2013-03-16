rpm -Uhv http://ftp.uni-kl.de/pub/linux/fedora-epel/5/i386/epel-release-5-4.noarch.rpm
yum install gcc libtool bison gettext make bzip2 automake gcc-c++ patch httpd-devel rpm-build openssh-clients mlocate git-core

there are a couple of problems building on CentOS 5, since some versions are quite old:
keep the automake and autoconf installed, but build newer versions and install them:

issues resolved:
configure.ac:20: error: possibly undefined macro: AC_PROG_MKDIR_P
Your sqlite3 version is old - please upgrade to at least v3.5.0!

wget http://ftp.gnu.org/gnu/autoconf/autoconf-latest.tar.gz
tar xzf autoconf-latest.tar.gz
cd autoconf-...
./configure --prefix=/usr
make
make install
cd ..

wget http://ftp.gnu.org/gnu/automake/automake-1.13.tar.gz
cd automake-1.13
./configure --prefix=/usr
make
make install
cd ..

wget http://ftp.gnu.org/gnu/libtool/libtool-2.4.2.tar.gz
cd libtool-2.4.2
./configure --prefix=/usr
make
make install
cd ..

wget http://www.sqlite.org/sqlite-autoconf-3071502.tar.gz
cd sqlite-autoconf-3071502
./configure --prefix=/usr
make
make install
cd ..

rpm -i mono-openpetra-*.src.rpm
rpmbuild -ba /usr/src/redhat/SPECS/mono-openpetra.spec
