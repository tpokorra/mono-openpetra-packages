MONOVERSION=$1
if [ "$MONOVERSION" == "" ];
then
    echo "mono version is missing"
    exit
fi

cd SOURCES
mkdir mod_mono-openpetra-$MONOVERSION
cp mod_mono.conf mod_mono-openpetra-$MONOVERSION
tar czf mod_mono-openpetra-$MONOVERSION.tar.gz mod_mono-openpetra-$MONOVERSION
rm -Rf mod_mono-openpetra-$MONOVERSION
mkdir mono-openpetra-$MONOVERSION
tar czf mono-openpetra-$MONOVERSION.tar.gz mono-openpetra-$MONOVERSION
rm -Rf mono-openpetra-$MONOVERSION

wget http://download.mono-project.com/sources/mono/mono-$MONOVERSION.tar.bz2
