Summary:	A small application that collects stock information from Yahoo!(c)
Name:		gnome-pm
Version:	0.8.2
Release:	1
License:	GPL
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Source0:	http://www.geocities.com/lordzephyroth/%{name}-%{version}.tar.gz
URL:		http://www.geocities.com/lordzephyroth/gnome-pm.html
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:	gnome-libs >= 1.0
BuildRequires:	libghttp >= 1.0
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
make CFLAGS="`gnome-config --cflags gtk gnome gnomeui` $RPM_OPT_FLAGS" LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/Applications}
install gnome-pm $RPM_BUILD_ROOT%{_bindir}
install gnome-pm.desktop $RPM_BUILD_ROOT%{_applnkdir}/Applications/gnome-pm.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-pm
%{_applnkdir}/Applications/gnome-pm.desktop
