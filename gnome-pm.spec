Summary:	A small application that collects stock information from Yahoo!(c)
Name:		gnome-pm
Version:	0.9.3
Release:	2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.one.net/pub/users/dobez/%{name}-%{version}.tar.gz
URL:		http://dobey.free.fr/gnome-pm/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:	gnome-libs >= 1.0
BuildRequires:	libghttp-devel >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
GnomePM is a small application that collects stock information from
Yahoo!(c) Finance, and presents it in a easy-to-read list. GnomePM is
designed to cut back on CPU, memory, and bandwidth usage by
eliminating the need for a Java enabled Web browser. Many more
features are planned for GnomePM in the future. Please note, however,
that Yahoo!(c) does not support this product.

%prep
%setup -q

%build
gettextize --copy --force
aclocal -I macros
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_applnkdir}/Network/Misc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-pm
%{_applnkdir}/Network/Misc/gnome-pm.desktop
