MONOVERSION=$1
ARCHITECTURE=$2
MONOOPENPETRADIR=/opt/mono-openpetra

if [ "$ARCHITECTURE" == "" ]
then
    echo "call: $0 <mono version> <architecture: i386 or amd64>"
    exit
fi

wget http://sourceforge.net/projects/openpetraorg/files/openpetraorg/mono-openpetra/debian-6.0/mono-openpetra-$MONOVERSION-src.tar/download

sudo rm -Rf $MONOOPENPETRADIR

tar xjf src/mono-$MONOVERSION.tar.bz2
unzip src/mod_mono-7051f21ba693536f84de43b6c9047eeb0698b8de.zip
unzip src/xsp-02c073d70cf48e0f5a203c9d1058dcaa3040c8f6.zip
tar xzf src/uncrustify-0.56.tar.gz
tar xzf src/nant-0.92-src.tar.gz

cd mono-$MONOVERSION
# apply any patches???
./configure --prefix=$MONOOPENPETRADIR
make
sudo make install
cd ..

# this is still needed for nant-0.92
sudo ln -s $MONOOPENPETRADIR/lib/mono/4.5/mcs.exe $MONOOPENPETRADIR/lib/mono/4.5/dmcs.exe

#needed for building nant
sudo ln -s $MONOOPENPETRADIR/lib/mono/4.5/mcs.exe $MONOOPENPETRADIR/lib/mono/2.0/gmcs.exe

# needed for nant generateSolution
sudo ln -s /usr/lib/libgdiplus.so $MONOOPENPETRADIR/lib/libgdiplus.so

export PKG_CONFIG_PATH=$MONOOPENPETRADIR/lib/pkgconfig
export PATH=$MONOOPENPETRADIR/bin:$PATH


cd xsp-02c073d70cf48e0f5a203c9d1058dcaa3040c8f6
./autogen.sh --prefix=$MONOOPENPETRADIR --disable-docs
make; 
sudo make install
cd ..

cd mod_mono-7051f21ba693536f84de43b6c9047eeb0698b8de
./autogen.sh --prefix=$MONOOPENPETRADIR --disable-docs
make
sudo make install
cd ..

# mono-openpetra should not depend on httpd, therefore copy the lib; mod_mono-openpetra creates the symbolic link in /usr/lib/httpd/modules
sudo cp /usr/lib/apache2/modules/mod_mono.so.0.0.0 $MONOOPENPETRADIR/lib/mod_mono.so

cd nant-0.92
sudo PATH=$MONOOPENPETRADIR/bin:$PATH PKG_CONFIG_PATH=$MONOOPENPETRADIR/lib/pkgconfig make install prefix=$MONOOPENPETRADIR
cd ..

cd uncrustify-0.56
./configure --prefix=$MONOOPENPETRADIR
make
sudo make install
cd ..

mkdir mono-openpetra-$MONOVERSION
cd mono-openpetra-$MONOVERSION
tar xzf ../src/debian.tar.gz
sed -i 's/Architecture: amd64/Architecture: $ARCHITECTURE/g' debian/control
sed -i 's/Architecture: all/Architecture: $ARCHITECTURE/g' debian/control
sed -i 's/Architecture: i386/Architecture: $ARCHITECTURE/g' debian/control


mkdir -p src/opt
cp -R $MONOOPENPETRADIR src/opt

fakeroot debian/rules binary

cd ..

