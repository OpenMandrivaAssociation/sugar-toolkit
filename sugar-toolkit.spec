# NOTE: Please do not edit this file, it was auto generated by jhconvert
#       See http://wiki.sugarlabs.org/go/Deployment_Team/jhconvert for details
%define _disable_ld_no_undefined 1

Name:		sugar-toolkit
Version:	0.98.1
Release:	1
Summary:	Sugar toolkit
License:	LGPLv2
Group:		Graphical desktop/Other
Url:		http://sugarlabs.org/

Source0:	http://download.sugarlabs.org/sources/sucrose/glucose/sugar-toolkit/sugar-toolkit-0.98.1.tar.bz2

Requires:	sugar-datastore >= 0.98.1
Requires:	python-dbus  
Requires:	python-hippo-canvas >= 0.3.0
Requires:	gnome-python-desktop  
Requires:	sugar-presence-service >= 0.98.1
Requires:	python-gobject >= 2.15
Requires:	python  
Requires:	python-cjson  
Requires:	python-dateutil  
Requires:	sugar-base >= 0.98.1

BuildRequires:	perl-XML-Parser  
BuildRequires:	pkgconfig(alsa)
BuildRequires:	gettext  
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	intltool >= 0.33
BuildRequires:	pkgconfig(sm)
BuildRequires:	python-gobject-devel >= 2.15
BuildRequires:	pygtk2.0-devel  
BuildRequires:	python-devel  
BuildRequires:	sugar-base >= 0.98.0
BuildRequires:	x11-proto-devel  

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
The toolkit provides a set of widgets to build HIG compliant applications
and interfaces to interact with system services like presence
and the datastore.

%prep
%setup -q -n sugar-toolkit-0.98.1


%build
%define __libtoolize true
%configure
%make

%install
%makeinstall_std
%find_lang sugar-toolkit

%files -f sugar-toolkit.lang
%{python_sitelib}/sugar/*
%doc AUTHORS COPYING README
