Summary:	A tool for dumping a computer's DMI table contents
Summary(pl.UTF-8):	Narzędzie do zrzucania zawartości tabeli DMI komputera
Name:		dmidecode
Version:	2.10
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://savannah.nongnu.org/download/dmidecode/%{name}-%{version}.tar.bz2
# Source0-md5:	3c9c4d55a40b78600f3b43bfa64616f9
URL:		http://www.nongnu.org/dmidecode/
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dmidecode is a tool for dumping a computer's DMI (some say SMBIOS)
table contents in a human-readable format. This table contains a
description of the system's hardware components, as well as other
useful pieces of information such as serial numbers and BIOS revision.

%description -l pl.UTF-8
Dmidecode jest narzędziem do zrzucania zawartości DMI (niektórzy mówią
na to SMBIOS) komputera w formacie odczytywalnym przez człowieka.
Tabela ta zawiera opis sprzętowych komponentów systemu, a także
użyteczne kawałki informacji takie jak numery seryjne i rewizja BIOSu.

%prep
%setup -q

# GNU make no longer ignores != assignment
sed '/PROGRAMS !=/d' -i Makefile

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags} -Wall -W -pedantic" \
	LDFLAGS="%{rpmcflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/dmidecode

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
