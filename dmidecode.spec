Summary:	A tool for dumping a computer's DMI table contents
Summary(pl.UTF-8):	Narzędzie do zrzucania zawartości tabeli DMI komputera
Name:		dmidecode
Version:	2.12
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://savannah.nongnu.org/download/dmidecode/%{name}-%{version}.tar.bz2
# Source0-md5:	a406f3cbb27736491698697beeddb781
URL:		http://www.nongnu.org/dmidecode/
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
użyteczne kawałki informacji takie jak numery seryjne i rewizja
BIOS-u.

%prep
%setup -q

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
%attr(755,root,root) %{_sbindir}/biosdecode
%attr(755,root,root) %{_sbindir}/dmidecode
%attr(755,root,root) %{_sbindir}/ownership
%attr(755,root,root) %{_sbindir}/vpddecode
%{_mandir}/man8/biosdecode.8*
%{_mandir}/man8/dmidecode.8*
%{_mandir}/man8/ownership.8*
%{_mandir}/man8/vpddecode.8*
