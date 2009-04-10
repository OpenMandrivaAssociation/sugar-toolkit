# NOTE: Do not edit, file was generated by jhconvert

Name: sugar-toolkit
Version: 0.84.2
Release: %mkrel 2
Summary: Sugar toolkit
License: LGPLv2
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/glucose/sugar-toolkit/sugar-toolkit-0.84.2.tar.bz2

Patch: sugar-toolkit-0.84.2-sugar-610.patch
Patch1: sugar-toolkit-0.84.2-sugar-toolkit-de.patch
Patch2: sugar-toolkit-0.84.2-sugar-toolkit-es.patch

Requires: sugar-datastore >= 0.84.0
Requires: python-dbus  
Requires: python-hippo-canvas >= 0.3.0
Requires: gnome-python-desktop  
Requires: sugar-presence-service >= 0.84.0
Requires: python-gobject >= 2.14
Requires: python  
Requires: python-cjson  
Requires: sugar-base >= 0.84.0

BuildRequires: perl-XML-Parser  
BuildRequires: libalsa-devel  
BuildRequires: gettext  
BuildRequires: gtk+2-devel  
BuildRequires: intltool >= 0.33
BuildRequires: libsm-devel  
BuildRequires: python-gobject-devel >= 2.14
BuildRequires: pygtk2.0-devel  
BuildRequires: libpython-devel  
BuildRequires: x11-proto-devel  

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The toolkit provides a set of widgets to build HIG compliant applications
and interfaces to interact with system services like presence
and the datastore.

%prep
%setup -q -n sugar-toolkit-0.84.2
%patch -p1
%patch1 -p1
%patch2 -p1

# eliminate %%configure's "clever" behaviour
%define __libtoolize true

%build
%configure 
make 

%install
rm -rf %{buildroot}
make  \
	DESTDIR=%{buildroot} \
	install
%find_lang sugar-toolkit

%clean
rm -rf %{buildroot}

%files -f sugar-toolkit.lang
%defattr(-,root,root,-)
%{python_sitelib}/*
%doc AUTHORS COPYING README

