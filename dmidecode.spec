Summary:	A tool for dumping a computer's DMI table contents
Summary(pl.UTF-8):	Narzędzie do zrzucania zawartości tabeli DMI komputera
Name:		dmidecode
Version:	3.6
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://download.savannah.gnu.org/releases/dmidecode/%{name}-%{version}.tar.xz
# Source0-md5:	e931a92708ac7a7396452dbc8be8decd
URL:		http://www.nongnu.org/dmidecode/
BuildRequires:	rpmbuild(macros) >= 1.673
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/dmidecode

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_sbindir}/biosdecode
%attr(755,root,root) %{_sbindir}/dmidecode
%attr(755,root,root) %{_sbindir}/ownership
%attr(755,root,root) %{_sbindir}/vpddecode
%{_mandir}/man8/biosdecode.8*
%{_mandir}/man8/dmidecode.8*
%{_mandir}/man8/ownership.8*
%{_mandir}/man8/vpddecode.8*
%{bash_compdir}/biosdecode
%{bash_compdir}/dmidecode
%{bash_compdir}/ownership
%{bash_compdir}/vpddecode
