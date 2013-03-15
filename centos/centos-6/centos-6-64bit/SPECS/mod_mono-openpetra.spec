%define name mod_mono-openpetra
%define version 3.0.6
%define DATE    %(date +%%Y%%m%%d)
%define release 0
%define MonoPath /opt/mono-openpetra
%define ApacheModulesPath /usr/lib64/httpd/modules/
%define ApacheConfPath /etc/httpd/conf.d/

Summary: mod_Mono for OpenPetra
Name: %{name}
Version: %{version}
Release: %{release}
Packager: Timotheus Pokorra <timotheus.pokorra@solidcharity.com>
License: GPL
Group: OpenPetra Developers
Requires: httpd >= 2.2
Requires: pkgconfig
Requires: mono-openpetra >= %{version}
Source0: mod_mono-openpetra-%{version}.tar.gz

%description
mod_mono for OpenPetra.

%prep
[ -d $RPM_BUILD_ROOT ] && [ "/" != "$RPM_BUILD_ROOT" ] && rm -rf $RPM_BUILD_ROOT
%setup

%build
# Configure and make source

%install
# Install the files to the build root
install -d -m 755 $RPM_BUILD_ROOT%{ApacheModulesPath}
install -d -m 755 $RPM_BUILD_ROOT%{ApacheConfPath}
install -m 755 mod_mono.so $RPM_BUILD_ROOT%{ApacheModulesPath}
install -m 644 mod_mono.conf $RPM_BUILD_ROOT%{ApacheConfPath}

%clean
# Clean up after ourselves, but be careful in case someone sets a bad buildroot
[ -d $RPM_BUILD_ROOT ] && [ "/" != "$RPM_BUILD_ROOT" ] && rm -rf $RPM_BUILD_ROOT

%files
%{ApacheModulesPath}/mod_mono.so
%{ApacheConfPath}/mod_mono.conf

%changelog
* Fri Mar 15 2013 Timotheus Pokorra <timotheus.pokorra@solidcharity.com>
- upgrade to Mono 3.0.6
* Fri Jan 25 2013 Timotheus Pokorra <timotheus.pokorra@solidcharity.com>
- build for Mono 3.0
* Wed Nov 28 2012 Timotheus Pokorra <timotheus.pokorra@solidcharity.com>
- First build

