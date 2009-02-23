# NOTE: Do not edit, file was generated by jhconvert

Name: sugar-toolkit
Version: 0.83.7
Release: %mkrel 1
Summary: Sugar toolkit
License: LGPLv2
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/glucose/sugar-toolkit/sugar-toolkit-0.83.7.tar.bz2

Requires: python-gobject >= 2.14
Requires: python-hippo-canvas >= 0.3.0
Requires: sugar-base >= 0.83.4
Requires: python-dbus  
Requires: sugar-datastore >= 0.83.3
Requires: python  
Requires: sugar-presence-service >= 0.83.3
Requires: gnome-python-desktop  
Requires: python-cjson  

BuildRequires: python-gobject-devel >= 2.14
BuildRequires: libsm-devel  
BuildRequires: intltool >= 0.33
BuildRequires: pygtk2.0-devel  
BuildRequires: libalsa-devel  
BuildRequires: libgtk+2-devel  
BuildRequires: libpython-devel  
BuildRequires: gettext  
BuildRequires: x11-proto-devel  
BuildRequires: perl-XML-Parser  

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The toolkit provides a set of widgets to build HIG compliant applications
and interfaces to interact with system services like presence
and the datastore.

%prep
%setup -q -n sugar-toolkit-0.83.7


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

