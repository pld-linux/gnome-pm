%define name		GnomePM
%define version		0.6.0
%define release		1
%define	prefix		/usr
%define sysconfdir 	/etc


Summary: A small application that collects stock information from Yahoo!(c).
Name: %{name}
Version: %{version}
Release: %{release}
Copyright: GPL
Group: Applications/Productivity
Source: http://tigris.sonicom.net/projects/gnome-pm-%{version}.tar.gz
URL: http://tigris.sonicom.net/projects/gnome-pm.html
BuildRoot: /var/tmp/%{name}-%{version}-root
Requires: gtk+ >= 1.2, gnome-core >= 1.0 libghttp >= 1.0, curl >= 5.10, netscape-navigator >= 4.5

%description
GnomePM is a small application that collects stock information from
Yahoo!(c) Finance, and presents it in a easy-to-read list. GnomePM is
designed to cut back on CPU, memory, and bandwidth usage by
eliminating the need for a Java enabled Web browser. Many more
features are planned for GnomePM in the future. Please note, however,
that Yahoo!(c) does not support this product.

%prep
%setup -q -n gnome-pm-%{version}

%build

make

%install

mkdir -p $RPM_BUILD_ROOT%{prefix}/bin/
mkdir -p $RPM_BUILD_ROOT%{prefix}/share/gnome/apps/Applications/
install -m 755 gnome-pm $RPM_BUILD_ROOT%{prefix}/bin/gnome-pm
install -m 644 gnome-pm.desktop $RPM_BUILD_ROOT%{prefix}/share/gnome/apps/Applications/gnome-pm.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{prefix}/bin/gnome-pm
%{prefix}/share/gnome/apps/Applications/gnome-pm.desktop

%changelog
* Wed Sep 1 1999 Tim Powers <timp@redhat.com>
- updated source to 0.6.0

* Thu Aug 26 1999 Tim Powers <timp@redhat.com>
- added libghttp >= 1.0 to Requires, as well as the others.

* Thu Aug 26 1999 Tim Powers <timp@redhat.com>
- first build for Powertools
