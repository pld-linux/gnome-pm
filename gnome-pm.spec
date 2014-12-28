Summary:	A small application that collects stock information from Yahoo!(c)
Summary(pl.UTF-8):	Mała aplikacja zbierająca informacje o notowaniach z Yahoo!(c)
Name:		gnome-pm
Version:	0.9.3
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.one.net/pub/users/dobez/%{name}-%{version}.tar.gz
# Source0-md5:	a947488921af395e4ce3c9df0186977b
URL:		http://dobey.free.fr/gnome-pm/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gtk+-devel >= 1.2
BuildRequires:	gnome-libs >= 1.0
BuildRequires:	libghttp-devel >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
GnomePM is a small application that collects stock information from
Yahoo!(c) Finance, and presents it in a easy-to-read list. GnomePM is
designed to cut back on CPU, memory, and bandwidth usage by
eliminating the need for a Java enabled Web browser. Many more
features are planned for GnomePM in the future. Please note, however,
that Yahoo!(c) does not support this product.

%description -l pl.UTF-8
GnomePM to mała aplikacja zbierająca informacje o notowaniach z
serwisu Yahoo!(c) Finance i prezentująca je jako czytelną listę.
GnomePM został zaprojektowany by zmniejszyć użycie procesora, pamięci
i sieci poprzez wyeliminowanie potrzeby używania przeglądarki WWW z
obsługą Javy. Są planowane w przyszłości nowe możliwości. Uwaga:
Yahoo!(c) nie wspiera tego produktu.

%prep
%setup -q

%build
rm -f missing
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
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
