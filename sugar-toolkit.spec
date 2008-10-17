%define commitid 2e6be9ea55
%define alphatag 20080822git%{commitid}

Summary: Sugar toolkit
Name: sugar-toolkit
Version: 0.82.11
Release: 1%{?dist}
#Release: 2.%{alphatag}%{?dist}
URL: http://wiki.laptop.org/go/Sugar
# git clone git://dev.laptop.org/sugar
# cd sugar
# git-checkout %{commitid}
#Source0: %{name}-%{version}-git%{commitid}.tar.bz2
Source0: http://dev.laptop.org/pub/sugar/sources/%{name}/%{name}-%{version}.tar.bz2
Source1: macros.sugar
License: LGPLv2
Group: System Environment/Libraries
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: pkgconfig
BuildRequires: pygtk2.0-devel
BuildRequires: gettext
BuildRequires: gtk2-devel
BuildRequires: perl-XML-Parser
BuildRequires: libsm6-devel
BuildRequires: libalsa2-devel

Requires: gnome-python-desktop
Requires: python-dbus
Requires: pygtk2.0
Requires: python-hippo-canvas
Requires: sugar-datastore
Requires: sugar-base
Requires: sugar-presence-service
Requires: python-simplejson
Requires: python-json
Requires: gettext

%description
Sugar is the core of the OLPC Human Interface. The toolkit provides
a set of widgets to build HIG compliant applications and interfaces
to interact with system services like presence and the datastore.

%prep
%setup -q

%build
%configure
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%find_lang %name
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/rpm/ 	 
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/rpm/macros.sugar

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING README

%{python_sitelib}/*
%{_sysconfdir}/rpm/macros.sugar

