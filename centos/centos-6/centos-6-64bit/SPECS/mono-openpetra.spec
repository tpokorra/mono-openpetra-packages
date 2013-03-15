%define name mono-openpetra
%define version 3.0.3
%define DATE    %(date +%%Y%%m%%d)
%define release 1
%define MonoPath /opt/mono-openpetra

Summary: Mono with fixes for OpenPetra
Name: %{name}
Version: %{version}
Release: %{release}
Packager: Timotheus Pokorra <timotheus.pokorra@solidcharity.com>
License: GPL
Group: OpenPetra Developers
Requires: pkgconfig
BuildRequires: gcc libtool bison gettext make bzip2 automake gcc-c++ patch httpd-devel
Source: mono-openpetra-%{version}.tar.gz
Source1: mono-%{version}.tar.bz2
Source2: xsp-02c073d70cf48e0f5a203c9d1058dcaa3040c8f6.zip
Source3: mod_mono-7051f21ba693536f84de43b6c9047eeb0698b8de.zip
Source4: nant-0.92-src.tar.gz
Patch0: crossdomainmarshaller-fix.patch

%description
Mono with fixes for OpenPetra.

%prep
[ -d $RPM_BUILD_ROOT ] && [ "/" != "$RPM_BUILD_ROOT" ] && rm -rf $RPM_BUILD_ROOT
%setup
%setup -T -D -a 1
%setup -T -D -a 2
%setup -T -D -a 3
%setup -T -D -a 4
%patch0 -p1

%build
# Configure and make source
BUILDDIR=`pwd`
cd $BUILDDIR/mono-%{version}
./configure --prefix=%{MonoPath}
make
sudo rm -Rf %{MonoPath}
sudo make install

#this was for bug https://bugzilla.xamarin.com/show_bug.cgi?id=3582
##sudo mv %{MonoPath}/lib/mono/4.0 %{MonoPath}/lib/mono/4.0old
#sudo rm -Rf %{MonoPath}/lib/mono/4.0
#sudo ln -s %{MonoPath}/lib/mono/4.5 %{MonoPath}/lib/mono/4.0
#sudo ln -s %{MonoPath}/lib/mono/4.5/mcs.exe %{MonoPath}/lib/mono/4.5/dmcs.exe

#needed for building nant
sudo ln -s %{MonoPath}/lib/mono/4.5/mcs.exe %{MonoPath}/lib/mono/2.0/gmcs.exe

export PKG_CONFIG_PATH=%{MonoPath}/lib/pkgconfig
export PATH=%{MonoPath}/bin:$PATH

cd $BUILDDIR/xsp-02c073d70cf48e0f5a203c9d1058dcaa3040c8f6
./autogen.sh --prefix=%{MonoPath} --disable-docs
make; 
sudo make install

cd $BUILDDIR/mod_mono-7051f21ba693536f84de43b6c9047eeb0698b8de
./autogen.sh --prefix=%{MonoPath} --disable-docs
make
sudo make install

cd $BUILDDIR/nant-0.92
sudo PATH=%{MonoPath}/bin:$PATH PKG_CONFIG_PATH=%{MonoPath}/lib/pkgconfig make install prefix=%{MonoPath}
sudo rm -Rf $BUILDDIR/nant-0.92

%install
# Install the files to the build root
install -d -m 755 $RPM_BUILD_ROOT%{MonoPath}

# Copy the files
cd %{MonoPath}
find * -follow -print | cpio -pLV -R root:users $RPM_BUILD_ROOT%{MonoPath}
rm -Rf $RPM_BUILD_ROOT%{MonoPath}/lib/mono/4.0
cd $RPM_BUILD_ROOT%{MonoPath}/lib/mono; ln -s 4.5 4.0

%clean
# Clean up after ourselves, but be careful in case someone sets a bad buildroot
[ -d $RPM_BUILD_ROOT ] && [ "/" != "$RPM_BUILD_ROOT" ] && rm -rf $RPM_BUILD_ROOT

%files
%{MonoPath}

%changelog
* Fri Jan 25 2013 Timotheus Pokorra <timotheus.pokorra@solidcharity.com>
- exclude mod_mono from this package
* Tue Jan 22 2013 Timotheus Pokorra <timotheus.pokorra@solidcharity.com>
- Upgrade from Mono 2.11.4 to Mono 3.0.3
* Fri Oct 19 2012 Timotheus Pokorra <timotheus.pokorra@solidcharity.com>
- First build
